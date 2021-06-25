<h1>Forgot your password?</h1>
<p>Enter your e-mail address to obtain a new password.</p>

<form action="." method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Send me instructions!">
</form>