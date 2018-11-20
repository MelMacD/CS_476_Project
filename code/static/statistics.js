$(document).ready(function() {
    $("#statsTable").DataTable();
    
    // need to figure out rankings and update the right table rows with their ranking
    // would need to count the number of commenters and reactions for each and compare them
    // then need to compare values and assign rankings
    // store as json, then iterate through and set ranking and display accordingly
    let values = {};
    $("tr").each( function( ) {
        alert($(this).find(".commenters").text());
    });
});
