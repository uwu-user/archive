let count = 0;
let timeout;

client.on("message", message => {
	try {
	if (message.author.bot) return;
  const oke = client.emojis.cache.get("ok_emoji_id");
  const error = client.emojis.cache.get("error_emoji_id");
  
  if (message.channel.id === "channel_id") {
    if (Number(message.content) === count + 1) {
      count++;
      message.react(oke);
      if (timeout) client.clearTimeout(timeout);
    } else if (message.author.id !== client.user.id) {
      if (isNaN(message.content)) return;
      let Embed = new MessageEmbed().setTitle("error");
      let msg = `**${message.author.tag} RUINED IT AT ${count}!! Next number is 1. Wrong number.**`;
      message.channel.send({ content: msg, embeds: [Embed]
      });
      message.react(error);
      count = 0;
      if (timeout) client.clearTimeout(timeout);
    }
  }
  } catch (error) {
  	message.channel.send({ content: error.message })
  }
});
