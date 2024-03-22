// script.js

document.addEventListener("DOMContentLoaded", function() {
    const showMoreButton = document.getElementById("show-more");
    const bookRows = document.querySelectorAll(".book-row");
    let visibleRowCount = 10;

    showMoreButton.addEventListener("click", function() {
        for (let i = visibleRowCount; i < visibleRowCount + 10; i++) {
            if (bookRows[i]) {
                bookRows[i].style.display = "block";
            }
        }
        visibleRowCount += 10;

        // Hide the "Show More" button when all rows are displayed
        if (visibleRowCount >= bookRows.length) {
            showMoreButton.style.display = "none";
        }
    });
});
