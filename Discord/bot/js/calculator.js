
#d.js v13

const { Discord, Client, Intents, Collection } = require("discord.js");
const { MessageEmbed, MessageButton, MessageSelectMenu, MessageActionRow } = require("discord.js");
const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES]
});

//-------------------------------------------------------------
// login ?
//-------------------------------------------------------------

client.login(" You bot TOKEN ").catch(function(error) {
  console.log(error.message);
});

//-------------------------------------------------------------
// calculator.js
//-------------------------------------------------------------

const math = require("mathjs");

client.on("messageCreate", message => {
	try {
  if (message.content.startsWith("$calculator")) {

    let button = new Array([], [], [], []);
    let row = [];
    let text = [
    
    // #1
      "(",
      ")",
      "+",
      "/",
      "CE",

    // #2
      "7",
      "8",
      "9",
      "^",
      "*",

   // #3
      "4",
      "5",
      "6",
      "0",
      ".",

   // #4
      "1",
      "2",
      "3",
      "-",
      "="
    ];

    let current = 0;

    for (let i = 0; i < text.length; i++) {
      if (button[current].length === 5) current++;
      button[current].push(createButton(text[i]));
      if (i === text.length - 1) {
        for (let btn of button) row.push(addRow(btn));
      }
    }

    let Menu = new MessageSelectMenu({
      placeholder: "Settings",
      customId: "Menu",
      options: [
        {
          label: "Test1",
          value: "test1",
          description: "test 1"
        },
        {
          label: "Test2",
          value: "test2",
          description: "test 1"
        }
      ]
    });

    var textmsg = "0";

    const Embed = new MessageEmbed()
         .setDescription(textmsg)
         .setTimestamp();

    message.channel
      .send({
        embeds: [Embed],
        components: row, [
          {
            type: 1,
            components: [Menu]
          }
        ]
      })
      .then(msg => {
        let isWrong = false;
        let time = 180000;
        let value = "";

        function createCollector(val, result = false) {
          const filter = button =>
            button.user.id === message.author.id &&
            button.customId === "cal" + val;
          let collect = msg.createMessageComponentCollector({
            filter,
            componentType: "BUTTON",
            time: time
          });

          collect.on("collect", async x => {
            if (x.user.id !== message.author.id) return;

            x.deferUpdate();

            if (result === "new") value = "0";
            else if (isWrong) {
              value = val;
              isWrong = false;
            } else if (value === "0") value = val;
            else if (result) {
              isWrong = true;
              value = mathEval(value);
            } else value += val;
            if (value.includes("CE")) return (value = "0");

            textmsg = value;

            const Embed = new MessageEmbed()
              .setDescription(textmsg)
              .setTimestamp();

            msg.edit({
              embeds: [Embed],
              components: row, [
          {
            type: 1,
            components: [Menu]
          }
                 ]
            });
          });
        }

        for (let txt of text) {
          let result;
          if (txt === "CE") result = "new";
          else if (txt === "=") result = true;
          else result = false;
          createCollector(txt, result);
        }
        setTimeout(() => {
          textmsg = "Your Time for using the calculator ran out (3 minutes)";

          const Embed = new MessageEmbed()
            .setDescription(textmsg)
            .setTimestamp();

          msg.edit({
            embeds: [Embed],
            components: []
          });
        }, time);
      });

    function addRow(btns) {
      let row1 = new MessageActionRow();
      for (let btn of btns) {
        row1.addComponents(btn);
      }
      return row1;
    }

    function createButton(label, style = "SECONDARY") {
      if (label === "CE") style = "DANGER";
      else if (label === ".") style = "PRIMARY";
      else if (label === "=") style = "SUCCESS";
      else if (isNaN(label)) style = "PRIMARY";

      const btn = new MessageButton()
        .setLabel(label)
        .setStyle(style)
        .setCustomId("cal" + label);
      return btn;
    }

    function mathEval(input) {
      try {
        let res = `${input} = ${math.evaluate(input)}`;
        return res;
      } catch {
        return "Wrong Input";
      }
    }
  } catch (error) {
  	message.channel.send({ content: error.message });
   }
});