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
    mounted: function (){
           let url = window.location.pathname;
           this.id = url.substring(url.lastIndexOf('/') + 1);
            axios.get(`http://127.0.0.1:8000/apis/v1/${app.id}/`)
        .then((response) => {
            console.log(response.data)
            app.person = response.data
            console.log("anystring")
        })
        .then(()=>{
        // let maps = document.getElementById("viewdiv")
            app.mapdiv =  `<iframe
            width="700em"
            height="600em"
            frameborder="0" style="border:0"
            src="https://www.google.com/maps/embed/v1/view?key=${token}&center=${app.person.last_seen_latitude},${app.person.last_seen_longitude}&zoom=18&maptype=satellite" 
            allowfullscreen>
            </iframe>`
        });
    },
});

let comment = new Vue({
    el: '#comments',
    data: {
        comments: [],
        newCommentText: "",
        newCommentusername: "",
        id: 0,
    },
    mounted: function(){
        let url = window.location.pathname;
        this.id = url.substring(url.lastIndexOf('/') + 1);
    },
    methods: {
    addNewComment: function (user) {
        this.comments.push({
            id: this.nextCommentId++,
            username: this.newCommentusername,
            comment: this.newCommentText
        })
        console.log(user)
    // axios.post("http://127.0.0.1:8000/apis/v1/comment/",
    // {
    //     content:app.newCommentText,
    //     username:
    //     missing_person: id
    // }
    // )
        this.newCommentText = "",
        this.newCommentusername = ""
      }
    }
})