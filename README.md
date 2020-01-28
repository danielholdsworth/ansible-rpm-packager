# ansible-rpm-packager
Ansible Play that creates RPM Packages from URL.

<h2>Dependencies</h2>
<ol>
  <li>Ansible</li>
  <li>`rpmbuild` module</li>
  <li>An RPM building environment</li>
  <li>A `unix` machine </li>
</ol>

<h2>How to use</h2>

`python rpm.py`

```
Which package would you like to RPM?
Plugin Name? (In xxx-xxx-xxx format): 404-to-301
Download URL?: https://downloads.wordpress.org/plugin/404-to-301.3.0.5.zip
```
