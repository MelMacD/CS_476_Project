$(document).ready(function() {
    $("#statsTable").DataTable();
    
    // need to figure out rankings and update the right table rows with their ranking
    // would need to count the number of commenters and reactions for each and compare them
    // then need to compare values and assign rankings
    // store as json, then iterate through and set ranking and display accordingly
    let values = {};
    $(".dataRow").each( function( ) {
        values[$(this).attr("id")] = parseInt($(this).find("td.commenters").text()) +
            parseInt($(this).find("td.reactions").text());
    });
    console.log(values);
});
