// /*
// code adapted from 2016 FA INFO 290 TA project assignment
// */
//
// $(document).ready(function() {
//   $('select').material_select();
// });
//
// $('.dropdown-button').dropdown({
//     inDuration: 300,
//     outDuration: 225,
//     constrain_width: false, // Does not change width of dropdown to that of the activator
//     hover: true, // Activate on hover
//     gutter: 0, // Spacing from edge
//     belowOrigin: false, // Displays dropdown below the button
//     alignment: 'left' // Displays dropdown with edge aligned to the left of button
//   }
// );

<script type="text/javascript" src="https://platform.linkedin.com/in.js">
    api_key: 86faisvke7rqht
    authorize: true
    onLoad: onLinkedInLoad
</script>

<script type="text/javascript">

    // Setup an event listener to make an API call once auth is complete
    function onLinkedInLoad() {
        IN.Event.on(IN, "auth", getProfileData);
    }

    // Handle the successful return from the API call
    function onSuccess(data) {
        console.log(data);
    }

    // Handle an error response from the API call
    function onError(error) {
        console.log(error);
    }

    // Use the API call wrapper to request the member's basic profile data
    function getProfileData() {
        IN.API.Raw("/people/~").result(onSuccess).error(onError);
    }

</script>
