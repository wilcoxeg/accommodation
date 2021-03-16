var shuffleSequence = seq("intro",  "instructions", sepWith("sep", seq( "practice", rshuffle(startsWith("target"), startsWith("catch")), "outro")));


var defaults = [
    "Separator", {
        hideProgressBar: false,
        transfer: 1000,
        normalMessage: "Please wait for the next question.",
        errorMessage: "Wrong. Please wait for the next question."
    },
    "DashedSentence", {
        mode: "self-paced reading"
    },
    "AcceptabilityJudgment", {
        as: ["1", "2", "3", "4", "5", "6", "7"],
        presentAsScale: true,
        instructions: "Use number keys or click boxes to answer.",
        leftComment: "(Bad)", rightComment: "(Good)"
    },
    "Question", {
        hasCorrect: true
    },
    "Message", {
        hideProgressBar: true,
        transfer: "keypress"
    },
    "Form", {
        hideProgressBar: true,
        continueOnReturn: true,
        saveReactionTime: true,
        checkedValue: "yes"
    },
    "RangeForm", {
        hideProgressBar: true,
    }
];

var slider_style = "-webkit-appearance: none; width:150px; background:#d3d3d3; height: 4px;outline: none;";

var construct_dialog = function(context, minus_trigger, plus_trigger) {
    var context = "<p style='font-size:20px;'> <b>" + context + "</b></p><br>";
    var m_t = "<div class='slidecontainer'> <span style='font-size:20px;'> &emsp; &emsp;" + minus_trigger + " </span> &emsp; <span style='float:right;'> least acceptable <input style=' "+slider_style+"' type='range' min='1' max='100' class='slider' name='minus_trigger' id='minus_trigger'> most acceptable </span> </div> <br><br>";    
    var p_t = "<div class='slidecontainer'> <span style='font-size:20px;'> &emsp; &emsp;" + plus_trigger + " </span> &emsp; <span style='float:right;'> least acceptable <input style=' "+slider_style+"' type='range' min='1' max='100' class='slider' name='plus_trigger' id='plus_trigger'> most acceptable</span> </div> <br>";
    
    var rand = Math.random();
    if(rand < 0.5) {
        return [context, m_t, p_t].join("");
    } else {
        return [context, p_t, m_t].join("");
    };
    
};

var items = [

    ["sep", "Separator", { }],
    
    ["intro", "Form", { html: { include: "example_intro.html" } } ],
    ["instructions", "Form", { html: { include: "instructions.html" } } ],
    ["outro", "Form", { continueMessage: "Click here to end the survey", html: { include: "example_outro.html" } } ],
    
    ["practice", "Form", {html: construct_dialog("What did Sandra and Charlotte do last weekend?", "They went to the movies.", "She went to the movies." )}],
    ["practice", "Form", {html: construct_dialog("What did Henry do on vacation?", "He went to the beach.", "He visited his parent's house in the country." )}],
    ["practice", "Form", {html: construct_dialog("Where did Rosie put the plants?", "She put them in the box with the books.", "She put it in the box with the books." )}],
    
    ["catch", "Form", {html: construct_dialog("My father bought a new TV recently.", "We think he spent too much money on it.", "We think she spent too much money on it." )}],
["catch", "Form", {html: construct_dialog("The local priest asked for donations for a food bank.", "My family gave him lots of money.", "My family gave her lots of money." )}],
["catch", "Form", {html: construct_dialog("Two years ago, our uncle moved to a different city.", "We miss him very badly.", "We miss her very badly." )}],
["catch", "Form", {html: construct_dialog("Last week, my brother found $20 on the sidewalk.", "I said I think he should donate it to charity.", "I said I thought she should donate it to charity." )}],
["catch", "Form", {html: construct_dialog("Yesterday, a nun visited our school.", "We heard her speak in our class on world religion.", "We heard him speak in our class on world religion." )}],
["catch", "Form", {html: construct_dialog("Last year, my aunt visited us from Canada.", "She brought a big jar of maple syrup.", "He brought a big jar of maple syrup." )}],
["catch", "Form", {html: construct_dialog("My mother bought a new car recently.", "We think she got it for a good price.", "We think he got it for a good price." )}],
["catch", "Form", {html: construct_dialog("Three years ago, my sister started college.", "This year, she is going to graduate early.", "This year, he is going to graduate early." )}],


   
];


