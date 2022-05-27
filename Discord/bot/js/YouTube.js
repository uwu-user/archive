
// $ npm install simple-youtube-api
const YouTube = require("simple-youtube-api");

// YouTube Api (v3)
const youtube = new YouTube("api here");

client.on("ready", () => {
	
  // YouTube channel URL
  let chURL = "https://youtube.com/channel/UCZ5XnGb-3t7jCkXdawN2tkA";
 //  Do not use https://youtube.com/c/discord
 
  let namech = "Category id here";
  let subscriberch = "Channel 1 id here ";
  let viewsch = "Channel 2 id here";
  let videosch = " Channel 3 id here";
  
  // Updata Time
  let time = 10000; // 10000 = 10s~

  let Name;
  let sub;
  let view;
  let videos;
  
  setInterval(() => {
    youtube.getChannel(chURL).then(c => {
      Name = c.title;
      let name = client.channels.cache.get(namech);
      name.setName(`『 ${Name} 』`);
    });
  }, time);
  setInterval(() => {
    youtube.getChannel(chURL, { part: "statistics" }).then(c => {
      sub = c.subscriberCount;
      view = c.viewCount;
      videos = c.videoCount;
      let Sub = client.channels.cache.get(subscriberch);
      let View = client.channels.cache.get(viewsch);
      let Videos = client.channels.cache.get(videosch);
      Sub.setName(`『 Subscriber 』〘 ${sub} 〙`);
      View.setName(`『 Views 』〘 ${view} 〙`);
      Videos.setName(`『 Videos 』〘 ${videos} 〙`);
    });
  }, time);
});