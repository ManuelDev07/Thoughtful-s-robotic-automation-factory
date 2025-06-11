<h1>Thoughtful-s-robotic-automation-factory</h1>
Interview coding exercise

<h2>Rules</h2>
<div>
    <p>Sort the packages using the following criteria:</p>
    <ul>
        <li>A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.</li>
	<li>A package is **heavy** when its mass is greater or equal to 20 kg.</li>
    </ul><br>
    <p>You must dispatch the packages in the following stacks:</p>
    <ul>
        <li><strong>STANDARD:</strong> standard packages (those that are not bulky or heavy) can be handled normally. </li>
	<li><strong>SPECIAL:</strong> packages that are either heavy or bulky can't be handled automatically. </li>
	<li><strong>REJECTED:</strong> packages that are **both** heavy and bulky are rejected. </li>
    </ul>


<strong>Implementing sort() function as sort(width, height, length, mass) without using ternary operators</strong>

**How to run:**
It is only a .py file to be executed through the terminal (powershell, cmd) and calling the function with various values specified in the function parameters.
