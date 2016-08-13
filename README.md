# revamp.tech
This is a the repository for [the RevAmp Technologies' website](revamp.tech).
It is based on the (python based) [Pelican](getpelican.com) framework which is used for creating static sites.
This is an adaptation of the adaptation (made by Frank Valcarcel) to the "Twenty" theme by [html5up](html5up.net).

The template uses [skel.js](http://skeljs.org/) to handle responsiveness.
For skel to work right css has to be available at the `{{ SITEURL }}/css/` path.
At the moment the files are in the theme directory (of the output directory, after the site have been compiled by Pelican) so they have to be moved to the appropriate folders for the site to work as intended.
