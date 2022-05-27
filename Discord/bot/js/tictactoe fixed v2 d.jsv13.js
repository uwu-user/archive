
const {
  MessageEmbed,
  MessageButton,
  MessageSelectMenu
} = require("discord.js");

client.on("messageCreate", async message => {
  if (message.content.startsWith("ttt")) {
    try {
      let User = message.mentions.members.first();
      if (!User) return message.channel.send("Ping a user ;-;!");

      if (User.id === message.member.id) return message.channel.send({ content: "No" });

      let acceptEmbed = new MessageEmbed().setTitle(
        `Waiting for ${User.tag} to accept!`
      );

      let accept = new MessageButton({
        style: 3,
        label: "Accept",
        customId: "accept",
        disabled: false
      });

      let decline = new MessageButton({
        style: 4,
        label: "Decline",
        customId: "declinet",
        disabled: false
      });
      message.delete();
      message.channel
        .send({
          content: `**<@${message.author.id}> Vs <@${User.id}>**`,
          embeds: [acceptEmbed],
          components: [
            {
              type: 1,
              components: [accept, decline]
            }
          ]
        })
        .then(m => {
          let filter = button => button.user.id == User.id;

          const collector = m.createMessageComponentCollector({
            type: "BUTTON",
            time: 30000,
            filter: filter
          });

          collector.on("collect", async button => {
            if (button.customId == "declinet") {
              button.deferUpdate();
              return collector.stop("decline");
            } else if (button.customId == "accept") {
              button.deferUpdate();
              collector.stop();

              if (button.user.id !== User.id)
                return message.reply({
                  content: "Wait for your chance."
                });

              let fighters = [message.member.id, User.id].sort(() =>
                Math.random() > 0.5 ? 1 : -1
              );

              let msg = "✨";
              let buttonO = "⭕";
              let buttonX = "❌";

              let buttonMap = {
                GameOver: false,
                user: 0,
                button1: {
                  style: 1,
                  label: msg,
                  disabled: false
                },
                button2: {
                  style: 1,
                  label: msg,
                  disabled: false
                },
                button3: {
                  style: 1,
                  label: msg,
                  disabled: false
                },
                button4: {
                  style: 1,
                  label: msg,
                  disabled: false
                },
                button5: {
                  style: 1,
                  label: msg,
                  disabled: false
                },
                button6: {
                  style: 1,
                  label: msg,
                  disabled: false
                },
                button7: {
                  style: 1,
                  label: msg,
                  disabled: false
                },
                button8: {
                  style: 1,
                  label: msg,
                  disabled: false
                },
                button9: {
                  style: 1,
                  label: msg,
                  disabled: false
                }
              };

              const Embed = new MessageEmbed()
                .setTitle("TicTacToe")
                .setDescription(
                  `**How to Play ?**\n*Wait for your turn.. If its your turn, Click one of the buttons from the table to draw your emoji at there.*`
                )
                .setTimestamp();

              let infomsg = await message.channel
                .send({ embeds: [Embed] })
                .then(ms => {
                  setTimeout(() => ms.delete(), 5000);
                });

              let mc = await message.channel.send({
                content: "×.×?"
              });

              tictactoe(mc);
              m.delete();
              async function tictactoe(mc) {
                buttonMap.userid = fighters[buttonMap.user];
                let buttonwon = { buttonO: false, buttonX: false };
                if (
                  buttonMap.button1.label == buttonO &&
                  buttonMap.button4.label == buttonO &&
                  buttonMap.button7.label == buttonO
                )
                  buttonwon[buttonO] = true;
                if (
                  buttonMap.button2.label == buttonO &&
                  buttonMap.button5.label == buttonO &&
                  buttonMap.button8.label == buttonO
                )
                  buttonwon[buttonO] = true;
                if (
                  buttonMap.button3.label == buttonO &&
                  buttonMap.button6.label == buttonO &&
                  buttonMap.button9.label == buttonO
                )
                  buttonwon[buttonO] = true;
                if (
                  buttonMap.button1.label == buttonO &&
                  buttonMap.button5.label == buttonO &&
                  buttonMap.button9.label == buttonO
                )
                  buttonwon[buttonO] = true;
                if (
                  buttonMap.button3.label == buttonO &&
                  buttonMap.button5.label == buttonO &&
                  buttonMap.button7.label == buttonO
                )
                  buttonwon[buttonO] = true;
                if (
                  buttonMap.button1.label == buttonO &&
                  buttonMap.button2.label == buttonO &&
                  buttonMap.button3.label == buttonO
                )
                  buttonwon[buttonO] = true;
                if (
                  buttonMap.button4.label == buttonO &&
                  buttonMap.button5.label == buttonO &&
                  buttonMap.button6.label == buttonO
                )
                  buttonwon[buttonO] = true;
                if (
                  buttonMap.button7.label == buttonO &&
                  buttonMap.button8.label == buttonO &&
                  buttonMap.button9.label == buttonO
                )
                  buttonwon[buttonO] = true;
                if (!buttonwon[buttonO] === false) {
                  buttonMap.GameOver = false;
                  buttonMap.button1.disabled = true;
                  buttonMap.button2.disabled = true;
                  buttonMap.button3.disabled = true;
                  buttonMap.button4.disabled = true;
                  buttonMap.button5.disabled = true;
                  buttonMap.button6.disabled = true;
                  buttonMap.button7.disabled = true;
                  buttonMap.button8.disabled = true;
                  buttonMap.button9.disabled = true;
                  message.channel.send({
                    content: `**${buttonO} | Winer**`,
                    components: []
                  });
                }
                if (
                  buttonMap.button1.label == buttonX &&
                  buttonMap.button4.label == buttonX &&
                  buttonMap.button7.label == buttonX
                )
                  buttonwon[buttonX] = true;
                if (
                  buttonMap.button2.label == buttonX &&
                  buttonMap.button5.label == buttonX &&
                  buttonMap.button8.label == buttonX
                )
                  buttonwon[buttonX] = true;
                if (
                  buttonMap.button3.label == buttonX &&
                  buttonMap.button6.label == buttonX &&
                  buttonMap.button9.label == buttonX
                )
                  buttonwon[buttonX] = true;
                if (
                  buttonMap.button1.label == buttonX &&
                  buttonMap.button5.label == buttonX &&
                  buttonMap.button9.label == buttonX
                )
                  buttonwon[buttonX] = true;
                if (
                  buttonMap.button3.label == buttonX &&
                  buttonMap.button5.label == buttonX &&
                  buttonMap.button7.label == buttonX
                )
                  buttonwon[buttonX] = true;
                if (
                  buttonMap.button1.label == buttonX &&
                  buttonMap.button2.label == buttonX &&
                  buttonMap.button3.label == buttonX
                )
                  buttonwon[buttonX] = true;
                if (
                  buttonMap.button4.label == buttonX &&
                  buttonMap.button5.label == buttonX &&
                  buttonMap.button6.label == buttonX
                )
                  buttonwon[buttonX] = true;
                if (
                  buttonMap.button7.label == buttonX &&
                  buttonMap.button8.label == buttonX &&
                  buttonMap.button9.label == buttonX
                )
                  buttonwon[buttonX] = true;
                if (!buttonwon[buttonX] === false) {
                  buttonMap.GameOver = true;
                  buttonMap.button1.disabled = true;
                  buttonMap.button2.disabled = true;
                  buttonMap.button3.disabled = true;
                  buttonMap.button4.disabled = true;
                  buttonMap.button5.disabled = true;
                  buttonMap.button6.disabled = true;
                  buttonMap.button7.disabled = true;
                  buttonMap.button8.disabled = true;
                  buttonMap.button9.disabled = true;
                  message.channel.send({
                    content: `**${buttonX} | Winer**`,
                    components: []
                  });
                }
                let button1 = new MessageButton({
                  style: buttonMap.button1.style,
                  label: buttonMap.button1.label,
                  customId: "button1",
                  disabled: buttonMap.button1.disabled
                });
                let button2 = new MessageButton({
                  style: buttonMap.button2.style,
                  label: buttonMap.button2.label,
                  customId: "button2",
                  disabled: buttonMap.button2.disabled
                });
                let button3 = new MessageButton({
                  style: buttonMap.button3.style,
                  label: buttonMap.button3.label,
                  customId: "button3",
                  disabled: buttonMap.button3.disabled
                });
                let button4 = new MessageButton({
                  style: buttonMap.button4.style,
                  label: buttonMap.button4.label,
                  customId: "button4",
                  disabled: buttonMap.button4.disabled
                });
                let button5 = new MessageButton({
                  style: buttonMap.button5.style,
                  label: buttonMap.button5.label,
                  customId: "button5",
                  disabled: buttonMap.button5.disabled
                });
                let button6 = new MessageButton({
                  style: buttonMap.button6.style,
                  label: buttonMap.button6.label,
                  customId: "button6",
                  disabled: buttonMap.button6.disabled
                });
                let button7 = new MessageButton({
                  style: buttonMap.button7.style,
                  label: buttonMap.button7.label,
                  customId: "button7",
                  disabled: buttonMap.button7.disabled
                });
                let button8 = new MessageButton({
                  style: buttonMap.button8.style,
                  label: buttonMap.button8.label,
                  customId: "button8",
                  disabled: buttonMap.button8.disabled
                });
                let button9 = new MessageButton({
                  style: buttonMap.button9.style,
                  label: buttonMap.button9.label,
                  customId: "button9",
                  disabled: buttonMap.button9.disabled
                });
                if (buttonMap.GameOver === false) {
                  mc.edit({
                    content: `**TicTacToe** | <@!${buttonMap.userid}>'s turn (${
                      buttonMap.user == 0 ? buttonO : buttonX
                    })`,
                    components: [
                      {
                        type: 1,
                        components: [button1, button2, button3]
                      },
                      {
                        type: 1,
                        components: [button4, button5, button6]
                      },
                      {
                        type: 1,
                        components: [button7, button8, button9]
                      }
                    ]
                  });
                } else if (buttonMap.GameOver === true) {
                  mc.edit({
                    content: "Game Over",
                    components: [
                      {
                        type: 1,
                        components: [button1, button2, button3]
                      },
                      {
                        type: 1,
                        components: [button4, button5, button6]
                      },
                      {
                        type: 1,
                        components: [button7, button8, button9]
                      }
                    ]
                  });
                }

                const filter0 = button => button.user.id === buttonMap.userid;
                const collector0 = mc.createMessageComponentCollector({
                  type: "BUTTON",
                  time: 60000,
                  filter: filter0,
                  max: 1
                });

                collector0.on("collect", b => {
                  if (buttonMap.GameOver === true) {
                    b.deferUpdate();
                    return collector0.stop();
                  }
                  if (b.user.id !== buttonMap.userid)
                    return b.channel.send({
                      content: "Wait for your chance."
                    });

                  if (buttonMap.GameOver === false) {
                    if (buttonMap.user === 0) {
                      buttonMap.user = 1;
                      buttonMap[b.customId] = {
                        style: 2,
                        label: buttonO,
                        disabled: true
                      };
                    } else if (buttonMap.user === 1) {
                      buttonMap.user = 0;
                      buttonMap[b.customId] = {
                        style: 2,
                        label: buttonX,
                        disabled: true
                      };
                    }
                  } else if (buttonMap.GameOver === false) return;

                  b.deferUpdate();
                  const map = (obj, fun) =>
                    Object.entries(obj).reduce(
                      (prev, [key, value]) => ({
                        ...prev,
                        [key]: fun(key, value)
                      }),
                      {}
                    );

                  const objectFilter = (obj, predicate) =>
                    Object.keys(obj)
                      .filter(key => predicate(obj[key]))
                      .reduce((res, key) => ((res[key] = obj[key]), res), {});
                  let Brgs = objectFilter(
                    map(buttonMap, (_, fruit) => fruit.label == msg),
                    num => num == true
                  );
                  if (Object.keys(Brgs).length == 0) {
                    let embed = new MessageEmbed()
                      .setTitle("Game Declined!")
                      .setDescription("It's a tie!");
                    message.channel.send({
                      embeds: [embed],
                      components: []
                    });
                  }
                  tictactoe(mc);
                });

                collector0.on("end", (collected, reason) => {
                  if (reason == "time") {
                    if (buttonMap.GameOver === false) {
                      let embed = new MessageEmbed()
                        .setTitle("Challenge Time Over")
                        .setDescription("Ran out of time!\nTime limit: 1m");
                      mc.edit({
                        content: null,
                        embeds: [embed],
                        components: []
                      });
                    }
                  } else return;
                });
              }
            }
          });

          collector.on("end", (collected, reason) => {
            if (reason == "time") {
              let embed = new MessageEmbed()
                .setTitle("Challenge Not Accepted in Time")
                .setDescription("Ran out of time!\nTime limit: 1m");
              m.edit({
                content: null,
                embeds: [embed],
                components: []
              });
            }
            if (reason == "decline") {
              message.delete();
              let embed = new MessageEmbed()
                .setTitle("Game Declined!")
                .setDescription(`${User.user.tag} has declined your game!`);
              m.edit({
                content: null,
                embeds: [embed],
                components: []
              });
            }
          });
        });
    } catch (error) {
      message.channel.send(error.message || "Error");
    }
  }
});
