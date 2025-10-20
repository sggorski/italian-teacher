let nouns = [];
let verbs = [];
let adjectives = [];

let parameters = {};
let flag = false

function displayCurrentDictionary(dict) {
    const liveOutput = document.getElementById('liveOutput');
    liveOutput.innerHTML = '';

    if (Object.keys(dict).length === 0) {
        const p = document.createElement('p');
        p.textContent = "Here you will be able to see your current sentence's parameters";
        liveOutput.appendChild(p);
        return;
    }
    for (const [key, value] of Object.entries(dict)) {
        const p = document.createElement('p');
        p.textContent = `${key} → ${value}`;
        liveOutput.appendChild(p);
    }
}

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
displayCurrentDictionary(parameters);

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

    displayCurrentDictionary(parameters);
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
    displayCurrentDictionary(parameters);
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
    displayCurrentDictionary(parameters);
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
    displayCurrentDictionary(parameters);
    document.querySelector('.stage5SF').hidden = true;
    if(article === "none") document.querySelector('.stage6SF').hidden = false;
    else if(article === "definite") document.querySelector('.stage7SF').hidden = false;
    else document.querySelector('.stage8SF').hidden = false;

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
    displayCurrentDictionary(parameters);
    document.querySelector('.stage6SF').hidden = true;
    if(demonstrative === "none") document.querySelector('.stage7SF').hidden = false;
    else document.querySelector('.stage8SF').hidden = false;
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
    displayCurrentDictionary(parameters);
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
    displayCurrentDictionary(parameters);
    document.querySelector('.stage8SF').hidden = true;
    if(!flag) uploadVerbs().then(r => document.querySelector('.stage3').hidden = false);
    else{
            console.log("Collected data: ", parameters)
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
        displayCurrentDictionary(parameters);
        document.querySelector('.stage2P').hidden = true;
        if(!flag) uploadVerbs().then(r => document.querySelector('.stage3').hidden = false);
        else{
            console.log("Collected data: ", parameters)
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
    //flag = true;
    displayCurrentDictionary(parameters);
    document.querySelector('.stage3V1').hidden = false
});

const sentenceTypeForm = document.getElementById('sentenceTypeForm');
sentenceTypeForm.addEventListener('submit', (event) => {
    event.preventDefault();
    parameters.sentence_type = document.querySelector('input[name="sentenceType"]:checked').value
    console.log('Selected sentence type:', parameters.sentence_type);
    displayCurrentDictionary(parameters);
    document.querySelector('.stage3V1').hidden = true;
    document.querySelector('.stage3V2').hidden = false;
});

const tenseForm = document.getElementById('tenseForm');
const moodTypeForm = document.getElementById('moodTypeForm');

tenseForm.addEventListener('submit', (event) => {
    event.preventDefault();
    parameters.tense_type = document.querySelector('input[name="tenseType"]:checked').value
    console.log('Selected tense type:', parameters.tense_type);
    displayCurrentDictionary(parameters);

    while (moodTypeForm.children.length > 2) {
        moodTypeForm.removeChild(moodTypeForm.children[2]);
    }

    //creating label for subjunctive
    let subjunctiveLabel = document.createElement('label')
    const subjunctiveInput = document.createElement('input');
    subjunctiveInput.type = 'radio';
    subjunctiveInput.name = 'moodType';
    subjunctiveInput.value = 'subjunctive';
    subjunctiveInput.required = true;
    subjunctiveLabel.appendChild(subjunctiveInput)
    subjunctiveLabel.appendChild(document.createTextNode('Subjunctive'));

    //creating label for imperative
    let imperativeLabel = document.createElement('label')
    const imperativeInput = document.createElement('input');
    imperativeInput.type = 'radio';
    imperativeInput.name = 'moodType';
    imperativeInput.value = 'imperative';
    imperativeInput.required = true;
    imperativeLabel.appendChild(imperativeInput)
    imperativeLabel.appendChild(document.createTextNode('Imperative'))



    if(parameters.tense_type === "present" && parameters.subject_person_code.startsWith('1')){
        console.log("heere")
        moodTypeForm.appendChild(subjunctiveLabel);
        moodTypeForm.appendChild(document.createElement('br'));
    }
    else if(parameters.tense_type === "present"){
        moodTypeForm.appendChild(subjunctiveLabel);
        moodTypeForm.appendChild(document.createElement('br'));
        moodTypeForm.appendChild(imperativeLabel);
        moodTypeForm.appendChild(document.createElement('br'));
    }
    else if(parameters.tense_type === "past"){
        moodTypeForm.appendChild(subjunctiveLabel);
        moodTypeForm.appendChild(document.createElement('br'));
    }

    const button = document.createElement('button');
    button.type = 'submit';
    button.textContent = 'Confirm';
    moodTypeForm.appendChild(button)

    moodTypeForm.addEventListener('submit', (event) => {
        event.preventDefault();
        parameters.mood_type = document.querySelector('input[name="moodType"]:checked').value
        console.log('Selected mood type:', parameters.mood_type);
        displayCurrentDictionary(parameters);
        flag=true;
        document.querySelector('.stage3V3').hidden = true;
        document.querySelector('.stage1').hidden = false;
    });

    document.querySelector('.stage3V2').hidden = true;
    document.querySelector('.stage3V3').hidden = false;
});

const finalResultDiv = document.getElementById('finalResult');
const practiceBtn = document.getElementById('practiceAgainBtn');
practiceBtn.addEventListener('click', () => {
    finalResultDiv.textContent = '';
    parameters = {};
    displayCurrentDictionary(parameters)
    flag = false;
    document.querySelector('.stageFinal').hidden = true
    document.querySelector('.stage1').hidden = false

});