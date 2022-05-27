
let = MessageButton } = require("discord.js");

client.on("messageCreate", async message => {
  if (message.content.startsWith("r")) {
    let button = new MessageButton()
      .setStyle(1)
      .setLabel("*")
      .setCustomId("Rainbow");

    await message.channel
      .send({
        content: "** **",
        components: [
          {
            type: 1,
            components: [button]
          }
        ]
      })
      .then(m => {
        const collector = m.createMessageComponentCollector({
          type: "BUTTON",
          time: 10000 // 10s
        });

        collector.on("collect", async button => {
          if (button.customId == "Rainbow") {
            let button = new MessageButton()
              .setStyle(Math.floor(Math.random() * 4) + 1);
              .setLabel("*")
              .setCustomId("Rainbow");

            await m.edit({
              content: "** **",
              components: [
                {
                  type: 1,
                  components: [button]
                }
              ]
            });
          }
        });
      });
  }
});