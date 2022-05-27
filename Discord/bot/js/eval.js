
client.on("messageCreate", message => {
  const args = message.content.split(" ").slice(1);
  const code = args.join(" ");

  function clean(text) {
    if (typeof text === "string")
      return text
        .replace(/`/g, "`" + String.fromCharCode(8203))
        .replace(/@/g, "@" + String.fromCharCode(8203));
    else return text;
  }

  if (message.content.startsWith("d.js!eval")) {
    try {
      let evaled;
      if (!args[0]) return message.channel.send({ content: "Erorr404" });
      let N = ["token", "secret", "destroy", "process.env"];
      if (N.some(word => message.content.toLowerCase().includes(word))) {
        evaled = "This information cannot be displayed";
      } else {
        evaled = eval(code);
      }

      if (typeof evaled !== "string")
        evaled = require("util").inspect(evaled, { depth: 0 });

      let cc = clean(evaled);
      if (cc.length >= 2050) cc = cc.substr(0, 2040);
      const Embed = {
        color: 0x12ff00,
        title: "Eval Command",
        description:
          "```py\n" +
          code +
          "```\n" +
          "```py\n" +
          `${new Date() - message.createdTimestamp}ms` +
          "```\n" +
          "```py\n" +
          typeof evaled +
          "```" +
          "\n\n```py\n" +
          cc +
          "```",
        timestamp: new Date()
      };
      message.channel.send({ embeds: [Embed] });
    } catch (error) {
      let cc_err = clean(error);
      if (cc_err.length >= 2050) cc_err = cc_err.substr(0, 2040);
      const Embed = {
        color: 0xff0c00,
        title: "Error",
        description: "```py\n" + code + "```" + "\n\n```py\n" + cc_err + "```",
        timestamp: new Date()
      };
      message.channel.send({ embeds: [Embed] });
    }
  }
});
