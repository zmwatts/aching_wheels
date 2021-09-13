axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

let app = new Vue({
    el: '#app',
    delimiters: ["[[","]]"],
    data: {
        message: 'Hello!',
        id: 0,
        person: {},
    },
    mounted: 
       function (){
           let url = window.location.pathname;
           this.id = url.substring(url.lastIndexOf('/') + 1);
        axios.get(`http://127.0.0.1:8000/apis/v1/${this.id}/`)
        .then((response) => {
            console.log(response.data)
            app.person = response.data
        })
        this.source=`https://www.google.com/maps/embed/v1/place?key=${token}&q=Space+Needle,Seattle+WA`
        let maps = document.getElementById("mapsdiv")
        maps.innerHTML =  `<iframe
        width="450"
        height="250"
        frameborder="0" style="border:0"
        src="https://www.google.com/maps/embed/v1/MAP_MODE?key=${token}&PARAMETERS" allowfullscreen>
      </iframe>`
      `https://www.google.com/maps/embed/v1/streetview
  ?key=${token}
  &location=${response.data.last_seen_latitude},${response.data.last_seen_longitude}
  &heading=210
  &pitch=10
  &fov=35`

},

})