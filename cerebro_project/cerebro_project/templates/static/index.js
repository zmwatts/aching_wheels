axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

let app = new Vue({
    el: '#app',
    delimiters: ["[[","]]"],
    data: {
        mapdiv: "",
        message: 'Hello!',
        id: 0,
        person: {},
        newCommentText: "",
        newCommentusername: "",
        comments: [],
    },
    mounted: 
       function (){
           let url = window.location.pathname;
           this.id = url.substring(url.lastIndexOf('/') + 1);
        axios.get(`http://127.0.0.1:8000/apis/v1/${this.id}/`)
        .then((response) => {
            console.log(response.data)
            app.person = response.data
            console.log("anystring")
        })
        .then(()=>{
        let maps = document.getElementById("viewdiv")
            app.mapdiv =  `<iframe
            width="700em"
            height="600em"
            frameborder="0" style="border:0"
            src="https://www.google.com/maps/embed/v1/view?key=${token}&center=${app.person.last_seen_latitude},${app.person.last_seen_longitude}&zoom=18&maptype=satellite" 
            allowfullscreen>
            </iframe>`
        }),
    },
    methods:
        addNewComment: function () {
            this.comments.push({
                id: this.nextCommentId++,
                username: this.newCommentusername,
                comment: this.newCommentText
            })
            this.newCommentText = "",
            this.newCommentusername = "",
        }

})