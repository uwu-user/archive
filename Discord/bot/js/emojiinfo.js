const Discord = require("discord.js");
const moment = require("moment");
moment.locale("pt-BR");

module.exports.run = async (client, message, args) => {
        let emoji = message.guild.emojis.find(emoji => emoji.name === `${args.join(" ")}`)
        let animado;
            if (emoji.animated === true) animado = "yes"
            if (emoji.animated === false) animado = "no"
        let gerenciadotwitch;
            if (emoji.managed === true) gerenciadotwitch = "yes"
            if (emoji.managed === false) gerenciadotwitch = "no"
        const embed = new Discord.RichEmbed()
        .setTitle(`emoji: ${emoji.name}`)
        .setColor("#FF0000")
        .setThumbnail(emoji.url)
        .addField("guild:", emoji.guild.name)
        .addField("Animado:", animado)
        .addField("Criado em:", moment(emoji.createdAt).format("LLLL"))
        .addField("ID:", emoji.id)
        .addField("Gerenciado pela Twitch:", gerenciadotwitch)
        message.channel.send(embed);
}