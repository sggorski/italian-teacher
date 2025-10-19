let nouns = [];
let verbs = [];
let adjectives = [];

let parameters = {
};

let flag = false

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

async function uploadVerbs(){
    verbs.forEach(verb => {
            let verbSelect = document.getElementById("verbSelect")
            const option = document.createElement('option');
            option.value = verb;
            option.textContent = verb;
            verbSelect.appendChild(option);
    });
}


async function constructSentence(data) {
    try {
        const response = await fetch('/api/construct_sentence', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) throw new Error('Network error');
        const result = await response.json();
        console.log('Constructed sentence:', result.sentence);
        return result.sentence;
    } catch (error) {
        console.error('Error while constructing sentence:', error);
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
    if(!flag){
        parameters.subject_isPerson = selected === 'person';
        console.log('Subject isPerson:',  parameters.subject_isPerson);
    }
    else{
        parameters.object_isPerson = selected === 'person';
        console.log('Object isPerson:',  parameters.object_isPerson);
    }

    document.querySelector('.stage1').hidden = true;
    if((parameters.subject_isPerson && !flag) || (parameters.object_isPerson && flag)){
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
    if(!flag){
        parameters.subject_noun = nounSelect.value;
        console.log('Selected noun:',  parameters.subject_noun);
    }
    else{
        parameters.object_noun = nounSelect.value;
        console.log('Selected noun:',  parameters.object_noun);
    }
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
    if(!flag){
        parameters.subject_adjective = adjectiveSelect.value;
        console.log('Selected adjective:', parameters.subject_adjective);
    }else{
       parameters.object_adjective = adjectiveSelect.value;
       console.log('Selected adjective:', parameters.object_adjective);
    }
    document.querySelector('.stage4SFA').hidden = true
    document.querySelector('.stage5SF').hidden = false
});

// picking an article: Definite or Indefinite
const articleForm = document.getElementById('articleForm');
articleForm.addEventListener('submit', (event) => {
    event.preventDefault();
    let article = document.querySelector('input[name="articleType"]:checked').value;
    if(!flag){
        parameters.subject_article = article
        console.log('Selected article type:', parameters.subject_article);
    }
    else{
        parameters.object_article = article
        console.log('Selected article type:', parameters.object_article);
    }

    document.querySelector('.stage5SF').hidden = true;
    document.querySelector('.stage6SF').hidden = false;
});


// picking an demonstrative: Far or Near
const demonstrativeForm = document.getElementById('demonstrativeForm');
demonstrativeForm.addEventListener('submit', (event) => {
    event.preventDefault();
    let demonstrative = document.querySelector('input[name="demonstrativeType"]:checked').value;
    if(!flag){
        parameters.subject_demonstrative = demonstrative
        console.log('Selected demonstrative type:', parameters.subject_demonstrative);
    }
    else{
        parameters.object_demonstrative = demonstrative
        console.log('Selected demonstrative type:', parameters.object_demonstrative);
    }

    document.querySelector('.stage6SF').hidden = true;
    document.querySelector('.stage7SF').hidden = false;
});


// picking a possessive
const possessiveForm = document.getElementById('possessiveForm');
possessiveForm.addEventListener('submit', (event) => {
    event.preventDefault();
    let possessive = document.querySelector('input[name="possessiveType"]:checked').value;
    if(!flag){
        parameters.subject_possessive = possessive;
        console.log('Selected possessive type:', parameters.subject_possessive);
    }else{
        parameters.object_possessive = possessive;
        console.log('Selected possessive type:', parameters.object_possessive);
    }

    document.querySelector('.stage7SF').hidden = true;
    document.querySelector('.stage8SF').hidden = false;
});

// picking a number singular or plural
const numberForm = document.getElementById('numberForm');
numberForm.addEventListener('submit', (event) => {
    event.preventDefault();
    let number = document.querySelector('input[name="numberType"]:checked').value;
    if(!flag){
        parameters.subject_number = number;
        console.log('Selected number type:', parameters.subject_number);
    }else{
        parameters.object_number = number;
        console.log('Selected number type:', parameters.object_number);
    }

    document.querySelector('.stage8SF').hidden = true;
    uploadVerbs().then(r => document.querySelector('.stage3').hidden = false);
});

//handling table for picking the right person
const buttons = document.querySelectorAll('button[data-code]');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        if(!flag){
            parameters.subject_person_code = button.getAttribute('data-code');
            console.log('Selected code:', parameters.subject_person_code);
        }else{
            parameters.object_person_code = button.getAttribute('data-code');
            console.log('Selected code:', parameters.object_person_code);
        }
        document.querySelector('.stage2P').hidden = true;
        if(!flag) uploadVerbs().then(r => document.querySelector('.stage3').hidden = false);
        else{
            console.log("Collected data: ", parameters)
            flag = false;
            parameters = {}
            document.querySelector('.stageLoad').hidden = false
            let result = constructSentence(parameters);
            result.then(r => {
                document.querySelector('.stageLoad').hidden = true
                const outputDiv = document.getElementById('finalResult');
                outputDiv.textContent = r;
                document.querySelector('.stageFinal').hidden = false
            })
        }
    });
});

//picking verb
const verbSelect = document.getElementById('verbSelect');
const verbForm = document.getElementById('verbForm');
verbForm.addEventListener('submit', (event) => {
    event.preventDefault();
    parameters.verb = verbSelect.value;
    console.log('Selected verb:', parameters.verb);
    document.querySelector('.stage3').hidden = true
    flag = true;
    document.querySelector('.stage1').hidden = false
});