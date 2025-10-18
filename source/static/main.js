let nouns = [];
let verbs = [];
let adjectives = [];
let isPerson = null; // boolean variable
let noun = ""
let adjective = ""

async function fetchData() {
    try {
        const response = await fetch('/api/get_data');
        if (!response.ok) throw new Error('Network error');
        const data = await response.json();
        nouns = data.nouns;
        verbs = data.verbs;
        adjectives = data.adjectives;
        console.log('Fetched data:', nouns, verbs, adjectives);
    } catch (error) {
        console.error('Error while fetching data:', error);
    }
}

//hiding all elements
const stages = document.querySelectorAll('[class^="stage"]');
stages.forEach(stage => {
    if (!stage.classList.contains('stage1')) {
        stage.hidden = true
    }
});

fetchData();

//picking subject
const subjectForm = document.getElementById('subjectForm');
const nounSelect = document.getElementById('nounSelect');

subjectForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const selected = document.querySelector('input[name="subjectType"]:checked').value;
    isPerson = selected === 'person';
    console.log('isPerson:', isPerson);

    document.querySelector('.stage1').hidden = true;
    if(isPerson){
        document.querySelector('.stage2P').hidden = false;
    }
    else{
        nouns.forEach(noun => {
            const option = document.createElement('option');
            option.value = noun;
            option.textContent = noun;
            nounSelect.appendChild(option);
        });
        document.querySelector('.stage2SF').hidden = false
    }
});

//picking noun
const nounForm = document.getElementById('nounForm');
nounForm.addEventListener('submit', (event) => {
    event.preventDefault();
    noun = nounSelect.value;
    console.log('Selected noun:', noun);
    document.querySelector('.stage2SF').hidden = true
    document.querySelector('.stage3SF').hidden = false
});

// checking if user want an adjective
const adjectiveForm = document.getElementById('adjectiveForm');
const wantsAdjective = document.getElementById('adjectiveCheckbox');
const adjectiveSelect = document.getElementById('adjectiveSelect');

adjectiveForm.addEventListener('submit', (event) => {
    event.preventDefault();
    console.log('Wants adjective:', wantsAdjective.checked);
    document.querySelector('.stage3SF').hidden = true;
    if(wantsAdjective.checked){
        adjectives.forEach(adj => {
            const option = document.createElement('option');
            option.value = adj;
            option.textContent = adj;
            adjectiveSelect.appendChild(option);
        });
        document.querySelector('.stage4SFA').hidden = false;
    }
    else{
        document.querySelector('.stage5SF').hidden = false;
    }
});

//picking adjective
const adjectivePickForm = document.getElementById('adjectivePickForm');
adjectivePickForm.addEventListener('submit', (event) => {
    event.preventDefault();
    adjective = adjectiveSelect.value;
    console.log('Selected adjective:', adjective);
    document.querySelector('.stage4SFA').hidden = true
    document.querySelector('.stage5SF').hidden = false
});