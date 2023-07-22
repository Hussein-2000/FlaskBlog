<!-- <script>
    // Get radio inputs
    var usernameradio = document.getElementById("Username")
    var emailradio = document.getElementById("email")
    
    var usernameContent = document.getElementById("usernameContent")
    var emailContent = document.getElementById("emailContent")


    usernameradio.addEventListener("change", function() {
        if (usernameradio.checked) {
            usernameContent.style.display = "block";
            emailContent.style.display = "none";
        }
    });

    emailradio.addEventListener("change", function() {
        if (emailradio.checked) {
            emailContent.style.display = "block";
            usernameContent.style.display = "none";
        }
    });
    
</script>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    // Show/hide input fields based on selected search option
    $('input[name="SearchOptions"]').change(function() {
        var selectedOption = $(this).val();
        if (selectedOption === 'Username') {
            $('#usernameContent').show();
            $('#emailContent').hide();
        } else if (selectedOption === 'email') {
            $('#usernameContent').hide();
            $('#emailContent').show();
        }
    });
</script> -->

   <!-- <div class="form-row form-group col-md-6">
        How to search your account?
        <!-- <div>
            <input type="radio" id="Username" name="SearchOptions" value="Username">
            <label for="Username">Username</label>
        </div>
        <div>
            <input type="radio" name="SearchOptions" id="email" value="email">
            <label for="email">email</label>
        </div> -->
        
    <!-- </div> --> -->
     <div id="usernameContent" style="display: none;" class="form-row form-group col-md-6">
        {{ form.username.label(class="Label") }}
            {% if form.username.errors %}
            {{ form.username(class="form-control is-invalid") }}
            <div class="invalid-feedback">
                {% for error in form.username.errors %}
                <span> {{ error }}</span>
                {% endfor%}
            </div>
            {% else%}
            {{ form.username(class="form-control") }}
            {% endif%}

    </div>