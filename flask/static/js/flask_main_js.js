$(document).ready(function () {
    // Initial setup
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('.prediction-details').hide();
    $('.resources-section').hide();

    // Resources with Indian agencies
    const resources = [
        { name: "World Health Organization - Cardiovascular Diseases", link: "https://www.who.int/health-topics/cardiovascular-diseases", description: "Global insights and prevention strategies." },
        { name: "Indian Heart Association", link: "https://indianheartassociation.org", description: "Heart health resources and education specific to India." },
        { name: "All India Institute of Medical Sciences (AIIMS) - Cardiology", link: "https://www.aiims.edu", description: "Comprehensive medical information and expert resources on heart diseases." },
        { name: "National Heart Institute (NHI) - India", link: "https://www.nationalheartinstitute.com", description: "Specialized cardiovascular care and resources in India." }
    ];

    // Function to display resources
    function displayResources() {
        const resourcesList = $('#resources-list');
        resourcesList.empty();  // Clear any existing items
        resources.forEach(resource => {
            resourcesList.append(
                `<li>
                    <a href="${resource.link}" target="_blank">${resource.name}</a> - ${resource.description}
                </li>`
            );
        });
        $('.resources-section').show();
    }

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
    
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation and progress text
        $(this).hide();
        $('.loader').show();
        let progressText = ['Analyzing ECG image...', 'Processing data...', 'Generating result...'];
        let index = 0;
        $('#result').fadeIn(400).text(progressText[index]);

        let interval = setInterval(() => {
            index = (index + 1) % progressText.length;
            $('#result').fadeOut(200, function() {
                $(this).text(progressText[index]).fadeIn(200);
            });
        }, 1500);

        // Make prediction by calling API /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Stop progress text loop
                clearInterval(interval);

                // Hide loader, show the result with animation
                $('.loader').hide();
                $('#result').fadeOut(300, function () {
                    $(this).text('Result: ' + data.condition_type).fadeIn(600);
                });

                // Display prediction details
                if (data.condition_type && data.description && data.symptoms && data.risk_factors && data.lifestyle_advice) {
                    $('#condition-type').text(data.condition_type);
                    $('#condition-description').text(data.description);
                    $('#condition-symptoms').text(data.symptoms);
                    $('#condition-risk-factors').text(data.risk_factors);
                    $('#condition-lifestyle').text(data.lifestyle_advice);

                    $('.prediction-details').show();

                    // Display resources for further support
                    displayResources();
                } else {
                    $('#result').text('Error: Prediction data incomplete');
                }
            },
            error: function () {
                clearInterval(interval);
                $('#result').text('Error: Unable to predict');
                $('.loader').hide();
                $('#btn-predict').show();
            }
        });
    });
});
