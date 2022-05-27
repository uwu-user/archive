const { MessageButton } = require('discord.js');

client.on("message",async message => {
   	if (message.content.startsWith("ttt")) {
   	
        let User = message.mentions.members.first()
        if(!User) return message.channel.send("Ping a user ;-;!");
        
        if (User.id === message.member.id) return message.channel.send({ content: "No" });

        let acceptEmbed = new MessageEmbed()
        .setTitle(`Waiting for ${User.user.tag} to accept!`)
    
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

      message.channel.send({
        embeds: [acceptEmbed],
        components: [accept, decline]
         }).then(m => {
    	
        let filter = (button) => button.user.id == User.id
        
        const collector = m.createMessageComponentCollector({ type: 'BUTTON', time: 30000, filter: filter })
        
        collector.on('collect', async (button) => {
            if (button.customId == 'declinet') {
                button.deferUpdate()
                return collector.stop('decline')
      
          } else if (button.customId == 'accept') {
                button.deferUpdate()
                collector.stop()
                let fighters = [message.member.id, User.id].sort(() => (Math.random() > .5) ? 1 : -1)
    
                let msg = "✨";
                let buttonO = "⭕";
                let buttonX = "❌";

         let buttonMap = {
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
        }
        
                const xoemb = new MessageEmbed()
                    .setTitle('TicTacToe')
                    .setDescription(`**How to Play ?**\n*Wait for your turn.. If its your turn, Click one of the buttons from the table to draw your emoji at there.*`)
                    .setTimestamp()
                    
                let infomsg = await message.channel.send({ embeds: [xoemb] }).then(ms => {
                    setTimeout(() => ms.delete(), 10000)
                })

                let msg = await message.channel.send({ content: `Waiting for Input | <@!${buttonMap.userid}>, Your Emoji: ${buttonO}` })
            
              tictactoe(msg);

                async function tictactoe(m) {
                
       	buttonMap.userid = fighters[buttonMap.user]
            let butronwon = { buttonO: false, buttonX: false }
            if (buttonMap.button1.label == buttonO && buttonMap.button4.label == buttonO && buttonMap.button7.label == buttonO) buttonwon[buttonO] = true
            if (buttonMap.button2.label == buttonO && buttonMap.button5.label == buttonO && buttonMap.button8.label == buttonO) buttonwon[buttonO] = true
            if (buttonMap.button3.label == buttonO && buttonMap.button6.label == buttonO && buttonMap.button9.label == buttonO) buttonwon[buttonO] = true
            if (buttonMap.button1.label == buttonO && buttonMap.button5.label == buttonO && buttonMap.button9.label == buttonO) buttonwon[buttonO] = true
            if (buttonMap.button3.label == buttonO && buttonMap.button5.label == buttonO && buttonMap.button7.label == buttonO) buttonwon[buttonO] = true
            if (buttonMap.button1.label == buttonO && buttonMap.button2.label == buttonO && buttonMap.button3.label == buttonO) buttonwon[buttonO] = true
            if (buttonMap.button4.label == buttonO && buttonMap.button5.label == buttonO && buttonMap.button6.label == buttonO) buttonwon[buttonO] = true
            if (buttonMap.button7.label == buttonO && buttonMap.button8.label == buttonO && buttonMap.button9.label == buttonO) buttonwon[buttonO] = true
            if (buttonwon[buttonO] !== false) return m.edit({ content: `**${buttonO} Winer**`, components: [] })
            if (buttonMap.button1.label == buttonX && buttonMap.button4.label == buttonX && buttonMap.button7.label == buttonX) buttonwon[buttonX] = true
            if (buttonMap.button2.label == buttonX && buttonMap.button5.label == buttonX && buttonMap.button8.label == buttonX) buttonwon[buttonX] = true
            if (buttonMap.button3.label == buttonX && buttonMap.button6.label == buttonX && buttonMap.button9.label == buttonX) buttonwon[buttonX] = true
            if (buttonMap.button1.label == buttonX && buttonMap.button5.label == buttonX && buttonMap.button9.label == buttonX) buttonwon[buttonX] = true
            if (buttonMap.button3.label == buttonX && buttonMap.button5.label == buttonX && buttonMap.button7.label == buttonX) buttonwon[buttonX] = true
            if (buttonMap.button1.label == buttonX && buttonMap.button2.label == buttonX && buttonMap.button3.label == buttonX) buttonwon[buttonX] = true
            if (buttonMap.button4.label == buttonX && buttonMap.button5.label == buttonX && buttonMap.button6.label == buttonX) buttonwon[buttonX] = true
            if (buttonMap.button7.label == buttonX && buttonMap.button8.label == buttonX && buttonMap.button9.label == buttonX) buttonwon[buttonX] = true
            if (buttonwon[buttonX] !== false) return m.edit({ content :`**${buttonX} Winer**`, components: [] })
            
             let button1 = new MessageButton({
                style: buttonMap.button1.style,
                label: buttonMap.button1.label,
                custom_id: "button1",
                disabled: buttonMap.button1.disabled
                });
            let button2 = new MessageButton({
                style: buttonMap.button2.style,
                label: buttonMap.button2.label,
                custom_id: "button2",
                disabled: buttonMap.button2.disabled
                });
            let button3 = new MessageButton({
                style: buttonMap.button3.style,
                label: buttonMap.button3.label,
                custom_id: "button3",
                disabled(buttonMap.button3.disabled
                });
            let button4 = new MessageButton({
                style: buttonMap.button4.style,
                label: buttonMap.button4.label,
                custom_id: "button4",
                disabled: buttonMap.button4.disabled,
                });
            let button5 = new MessageButton({
                style: buttonMap.button5.style,
                label: buttonMap.button5.label,
                custom_id: "button5",
                disabled: buttonMap.button5.disabled
                });
            let button6 = new MessageButton({
                style: buttonMap.button6.style,
                label: buttonMap.button6.label,
                custom_id: "button6",
                disabled: buttonMap.button6.disabled
                });
            let button7 = new MessageButton({
                style: buttonMap.button7.style,
                label: buttonMap.button7.label,
                custom_id: "button7",
                disabled: buttonMap.button7.disabled
                });
            let button8 = new MessageButton({
                style: buttonMap.button8.style,
                label: buttonMap.button8.label,
                custom_id: "button8",
                disabled: buttonMap.button8.disabled
                });
            let button9 = new MessageButton({
                style: buttonMap.button9.style,
                label: buttonMap.button9.label,
                custom_id: "button9",
                disabled: buttonMap.button9.disabled
                });
                
            let Menu = new MessageSelectMenu({
                placeholder: "Go!",
                maxValues: 1,
                minValues: 1,
                customId: "Menu0",
                options: [{
                label: "Replay",
                value: "game1",
                description: "replay the game =3",
                 },{
                label: "Exit",
                value: "game2",
                description: "exit the game and delete msg =3",
                 }],
                 disabled: true
            });
     
        m.edit({content: `**TicTacToe** | <@!${buttonMap.userid}>'s turn (${buttonMap.user == 0 ? buttonO : buttonX})`, 
            components: [{
              type: 1,
              components: [Menu]
              },{
              type: 1,
              components: [button1, button2, button3]
              },{
              type: 1,
              components: [button4, button5, button6]
              },{
              type: 1,
              components: [button7, button8, button9]
                            }] 
                       });
                    
                    const filter = (button) => button.user.id === buttonMap.userid;
                    
                    const collector = m.createMessageComponentCollector({ filter, componentType: 'BUTTON', max: 1, time: 30000 });

                    collector.on('collect', b => {

                        if (b.user.id !== buttonMap.userid) return b.reply({ content: 'Wait for your chance.', ephemeral: true })

                        if (buttonMap.user == 0) {
                            buttonMap.user = 1
                            buttonMap[b.customId] = {
                                style: 2,
                                emoji: buttonO,
                                disabled: true
                            }
                        } else {
                            buttonMap.user = 0
                            buttonMap[b.customId] = {
                                style: 2,
                                emoji: buttonX,
                                disabled: true
                            }
                        }
                        
                        b.deferUpdate()
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
                                .reduce((res, key) => (res[key] = obj[key], res), {});
                        let Brgs = objectFilter(map(buttonMap, (_, fruit) => fruit.emoji == msg), num => num == true);
                        if (Object.keys(Brgs).length == 0) return m.edit({ content: 'It\'s a tie!' })
                        tictactoe(m)
                    });
                    collector.on('end', collected => {
                        if (collected.size == 0) m.edit({ content: `<@!${buttonMap.userid}> didn\'t react in time! (30s)`, components: [] })
                    });
                }

            }
        })

        collector.on('end', (collected, reason) => {
            if (reason == 'time') {
                let embed = new MessageEmbed()
                    .setTitle('Challenge Not Accepted in Time')
                    .setDescription('Ran out of time!\nTime limit: 30s')
                m.edit({
                    embeds: [embed],
                    components: []
                })
            }
            if (reason == 'decline') {
                let embed = new Discord.MessageEmbed()
                    .setTitle("Game Declined!")
                    .setDescription(`${User.user.tag} has declined your game!`)
                m.edit({
                    embeds: [embed],
                    components: []
                })
            }
        })
    })
}