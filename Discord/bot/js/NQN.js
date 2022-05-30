//-------------------------------------------------------------
// NQN
//-------------------------------------------------------------

const { WebhookClient } = require("discord.js");

client.on("messageCreate", async message => {
  if (
    message.author.bot ||
    message.channel.type == "dm" ||
    !message.channel.guild
  )
    return;
  let a = webhookcontent(message.content, ":", ":");
  let msg = message.content;
  if (!a.length) return;

  a.forEach(m => {
    let emoji = client.emojis.catch.find(x => x.name === m);
    var b = `:${m}:`;
    var c = new RegExp(b, "g");

    if (
      emoji &&
      !msg.split(" ").find(x => x === emoji.toString()) &&
      !msg.includes(`<a${b}${emoji.id}>`)
    )
      msg = msg.replace(c, emoji.toString());
  });

  if (msg === message.content) return;

  message.delete();
  message.channel
    .createWebhook(
      message.member.nickname
        ? message.member.nickname
        : message.author.username,
      message.author.avatarURL()
    )
    .then(wb => {
      const user = new WebhookClient(wb.id, wb.token);
      user.send(msg);
      user.delete();
    });
});

function webhookcontent(q, w, e) {
  var r = [];
  var t = w.length;
  var y = e.length;
  var u = 0;
  var o = 0;
  var p = 0;
  var u = (o = p = 0);

  while (false !== (o = strpos(q, w, u))) {
    o += t;
    p = strpos(q, e, o);
    if (false === p) {
      break;
    }
    r.push(q.substr(o, p - o));
    u = p + y;
  }

  return r;
}

function strpos(v, j, k) {
  var i = (v + "").indexOf(j, k || 0);
  return i === -1 ? false : i;
}
