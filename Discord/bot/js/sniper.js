
client.snipes = new Map();

client.on("messageDelete", function(message, channel) {
  client.snipes.set(message.channel.id, {
    content: message.content,
    author: message.author,
    image: message.attachments.first()
      ? message.attachments.first().proxyURL
      : null
  });
});

client.on("message", message => {
  if (message.content.startsWith(prefix_ + "sniper")) {
    let msg = client.snipes.get(message.channel.id);
    if (!msg) return message.channel.send({ content: "**nothing =/**"});
    const sniperEmbed = new MessageEmbed()
      .setAuthor(msg.author.tag, msg.author.avatarURL)
      .setDescription(msg.content)
      .setImage(msg.image);
    message.channel.send({ embed: sniperEmbed});
  }
});