# LittleLemon-Web-Application

<h2> Capstone project (back-end)</h2>
<h4>The capstone project is based on a scenario involving the Little Lemon restaurant. In particular, the owners of Little Lemon want to extend the book a table functionality on the Little Lemon website</h4>

<h3>Api list:</h3>
This also includes djoser auth/ endpoints provided by the djoser library.

<ul>
  <h4><ins>My API endpoints:</ins></h4>
  <li>restaurant/menu-items/ POST GET </li>
  <li>restaurant/menu-items/<int:pk> GET PUT PATCH DELETE</li>
  <h4>Bookings view api: requires authentication</h4>
  <li>restaurant/booking/ POST GET</li>
  <li>restaurant/booking/<int:pk> GET PUT PATCH DELETE</li>
  <h4><ins>Djoser API endpoints</ins></h4>
  <li>auth/users/ POST for registration (signing up) GET requires authentication when requested by admin token returns all users and when by regular user returns user info </li>
  <li>auth/users/{userId}/ GET DELETE PUT PATCH when used by admin can be used on any user ID and when used by user it can be used with users own id only and acts like users/me/ </li>
  <li>auth/users/me/ requires authentication GET PUT PATCH DELETE</li>
  <li>auth/token/login/ POST takes username and password and returns token</li>
  <li>auth/token/logout/ takes token and expires token</li>
</ul>
<footer>Thank you again for your time please notice that I use appending slashes (=endpoint/)</footer>
