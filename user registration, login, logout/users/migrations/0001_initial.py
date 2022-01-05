{%extends "blog/base.html" %}
{%  load crispy_forms_tags %}
{%block content%}
    <div class="content-section">
        <form method="POST">
            {%csrf_token%}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Login</legend>
                {{form|crispy}}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Login</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Don't have an account? <a class ="ml-2" href="{% url 'register' %}">Sign Up Now</a>
            </small>
        </div>
    </div>
{%endblock%}
