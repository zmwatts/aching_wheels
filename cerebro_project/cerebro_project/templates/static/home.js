// import querystring from "querystring";
// let query = querystring.stringify({});


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

new Vue({
    el: '#app1',
    delimiters: ["[[","]]"],
    data: {
        message: 'Hello!'
    }
});