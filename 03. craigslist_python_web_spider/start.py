# Each city in specific category for postings with keyword
import requests
from bs4 import BeautifulSoup as soup

r = requests.get("https://www.craigslist.org/about/sites")
content = soup(r.content, "html.parser")

linksArray = []
pathArray = [
    "d/computer-gigs/search/cpg",
    "d/creative-gigs/search/crg",
    "d/art-media-design/search/med",
    "d/internet-engineering/search/eng",
    "d/software-qa-dba-etc/search/sof",
    "d/systems-networking/search/sad",
    "d/web-html-info-design/search/web"
]


loop = True
for country in content.find_all("div", attrs={'class': "colmask"}):
    if loop:
        for states_box in country.find_all("div"):
            # for state in country.find_all("h4"):
            #     print("-------------------------------------\n\n\n")
            #     print(state.text + "\n")
            #     print(state.next_sibling)

            for area in states_box.find_all("ul"):
                for location in area.find_all("a"):
                    linksArray.append(location.get("href"))

    loop = False

# keywords are not cap sensitive. lower case w in "web" will also look for upper case "Web" and vice versa.
keywords = ["web", "Cloud", "Desktop","Mobile","Tablet","Server","Router","Switch","Embedded","Software","Hardware","Engineer","Architect","Scientist","Programmer","Developer","Branding","Graphics","UI","UX","Designer","IoT","Wearable","Technologies","Technologies","Scalable",
"Databases", "Data","Datacenter","computing","Networking","Innovation","Creativity","Social","Media","SEO","ASO","SEM","SMM","Object-Oriented","Procedural","Functional","Programming", "design", "designer", "website", "portfolio", "logo", "poster", "flyer", "ecommerce",




# Object-Oriented, Procedural / Functional and Creative Programming
"Python", "PHP", "Ruby", "Go", "Perl", "ASP.NET", "Native C", "Swift", "Java", "JSP", "J2EE", "ObjectiveC", "JavaScript", "Lisp", "Haskell", "Lua", "Clojure","Scala", "Kotlin", "Elixir", "Scheme", "Tcl/Tk", "R statistical processing language", "Mathematica", "ActionScript", "Powershell", "Bash", "Zsh", "Fish", "Ksh", "Tcsh",

# Web Application Frameworks
"Application", "Frameworks","Django", "Flask", "Pyramid", "Laravel", "Phalcon", "Symfony", "Yii", "CodeIgniter", "CakePHP", "Zend", "Kohana", "Lithium", "Aura", "Fat-Free", "PHP-MVC", "FuelPHP", "Slim", "Ruby on Rails", "SharePoint", "ASP.NET MVC", "Windows Communication Foundation (WCF)", "DotNetNuke", "Hibernate", "Spring", "JSF", "Struts", "Google Web Toolkit", "Play", "Wicket", "Grails", "Vaadin", "Flex",

# JavaScript / ECMAScript Libraries, Frameworks, Compilers, Transpilers
"JavaScript", "Libraries","Compilers","Transpilers","AngularJS", "Node.js", "React", "Redux", "Flux", "Relay", "MobX", "React native", "VueJS", "Ember", "Ratchet", "Crossfilter", "CanJS", "DoneJS", "StealJS", "DocumentJS", "jQuery", "Underscore", "Backbone", "Mustache", "Handlebars", "Bootstrap", "Kendo", "dc.js", "RequireJS", "Prototype", "script.aculo.us", "MooTools", "ExtJS", "Qooxdoo","Yahoo", "MochiKit", "Midori", "The Dojo Toolkit", "Babel", "TypeScript", "CoffeeScript", "ClojureScript", "Elm",

# Node.js frameworks
"Express", "hapi", "flatiron", "locomotive", "total.js", "koa.js", "TWEE.IO", "diet.js", "Flicker.js", "Nodal", "CompoundJS", "geddy", "Sails.js", "Adonis", "RhapsodyJS", "Strapi", "ThinkJS", "Trails", "Catberry.js", "AllcountJS", "Derby", "Feathers", "SocketStream", "MEAN.js", "MEAN.io", "Meteor", "Meatier", "Mojito", "Seeds.js", "SANE", "COKE", "Sleekjs", "Danf", "Catberry", "Nuke.js", "We.js", "seneca.js", "Keystone.js", "Horizon", "Restocat", "actionHero.js", "Frisby", "restling", "restify", "restmvc", "percolator", "LoopBack", "Fortune.js", "facet", "Raddish", "Restberry", "Gugamarket", "Connect", "Kraken", "ewdGateway2", "Wintersmith", "docpad", "Blacksmith", "romulus", "Petrify", "Tower.js", "Impress", "Rendr", "Backnode", "Sequelize", "Cylon.js", "Virgilio.js", "SHPS",

# Database Programming, Scalability, Performance and Optimization
"MongoDB", "Couchbase", "Cassandra", "Hadoop", "MapReduce", "BigTable", "MySQL", "MariaDB", "PostgreSQL", "GIS", "MS SQL", "ADO.NET", "LINQ", "SQLite", "Oracle", "SQL", "PL/SQL", "MS Access",

# User Interfaces (UI/UX)
"CSS3", "SASS", "SCSS", "LESS", "AJAX", "JSON", "HTML5", "Custom Fonts", "Google Fonts", "Adobe Typekit", "Blade", "Smarty", "Twig", "Volt", "Slim", "Haml", "jQuery UI", "jQuery Mobile", "GWT","Photoshop", "Illustrator", "Flash Professional", "Flash Builder", "Flash Catalyst", "Fireworks", "Device Central",

# Mobile & Tablet Application Development
"Apple iOS", "iPhone", "iPod touch", "iPad", "Android", "Windows Phone", "Amazon Fire Phone/Tablet", "Microsoft Surface", "Kindle Fire", "Google", "Microsoft", "Amazon related phones/tablets",

# Mobile Application Frameworks
"Cocoa Touch", "Googles Android SDK", "Android Development Tools", "jQuery Mobile", "PhoneGap", "Xamarin", "Kony", "Cordova", "Ionic", "Sencha Touch", "Kendo UI Mobile", "Dojo Mobile", "Appcelerator", "Titanium",

# Data Visualizations
"Kibana", "Grafana", "Graphite", "Datadog", "Elk", "Splunk", "D3.js", "Highcharts", "dc.js", "Flot", "Plotly", "DataHero", "Chart.js", "Tableau", "Raw", "Dygraphs", "ZingChart", "InstantAtlas", "Timeline", "Exhibit", "Modest Maps", "Leaflet", "WolframAlpha", "Visual.ly", "Visualize Free", "Better World Flux", "FusionCharts", "jqPlot", "JavaScript InfoVis Toolkit", "Qlikview", "Datawrapper", "The Google Visualization API", "Springy.js", "Polymaps.js", "Dimple", "Sigma.js", "Raphael.js", "gRaphael", "Ember Charts",

# Unit Testing & Automated Testing
"Test-Driven Development", "Behaviour-Driven Development", "Functional Tests", "Acceptance Tests", "Unit Testing", "Integration Testing", "System Testing", "Performance Testing", "Security Testing", "Usability Testing", "Compatibility Testing", "PyUnit", "Cucumber", "jbehaves", "PHPUnit", "Codeception", "Behat", "PHPSpec", "SimpleTest", "Storyplayer", "Peridot", "Atoum", "Kahlan", "Selenium",

# Software Testing and Automation for Web Applications and Browsers
"Appium", "QMetry Automation Studio", "PhantomJS", "HtmlUnit", "CasperJS", "NightmareJS", "SlimerJS", "Jasmine", "Karma", "Mocha", "Chai",

# Distributed Search Engines
"Apache Solr", "ElasticSearch", "Lucene", "Sphinx", "Xapian", "Indri", "Zettair", "OpenSearchServer",

# Application Architecture
"Microservices", "SOA", "Monolithic", "API", "REST", "MVC", "MVVM", "MVP", "Flux",

# Build Scripts, Build Automation Tools & Package Managers
"Gulp", "Grunt", "NPM", "Bower", "Browserify", "Webpack", "Brunch", "Composer", "Maven", "Ant", "Gradle", "Buildr", "Gant", "Ivy", "Make", "Rake",

# Data Pipelines, Messaging and Streaming
"Apache Kafka", "RabbitMQ", "Kinesis", "Apache Spark", "ActiveMQ", "Apollo", "Kestrel", "JMS", "SQS",

# WebRTC
"WebRTC standards", "OpenTok", "TokBox", "Xirsys", "Kandy", "Wowza", "OpenWebRTC", "Kurento", "EasyRTC", "Licode", "Otalk", "PeerJS",

# Continuous Integration, Continuous Delivery/Deployment
"Jenkins", "Travis", "Bamboo", "CircleCI", "CIsimple", "Hudson", "Shippable", "SolanoCI", "Wercker", "GitLab CI", "Buddy", "Semaphore", "Solano Labs", "AppVeyor", "Assertible", "Shippable", "Nevercode", "GoCD", "PHPCI", "Distelli", "FinalBuilder", "Buildkite", "CruiseControl", "Integrity", "QuickBuild", "UrbanCode", "Gump", "Strider", "Buildbot", "BuildMaster", "Continuum", "Visual Studio Team Services", "Continua CI", "Cabie", "Meister", "Vexor", "Drone.io", "Buildout", "easyCIS", "Flosum", "XL Deploy", "Codefresh", "MidVision Rapid Deploy", "Cake", "Magnum CI", "Buddybuild", "Phabricator", "Spinnaker", "Bitrise", "OctopusDeploy", "Codeship", "TeamCity",

# Software Development and Delivery Methodologies
"Agile", "Scrum", "Sprint", "Waterfall", "Lean", "Kanban",

# Bug Tracking, Issue Tracking, and Project Management
"Jira", "Rally", "Trello", "Slack", "Discord", "HipChat", "Basecamp", "Pivotal", "Asana", "VersionOne", "Team Foundation Server", "HPE Agile Manager", "Evernote",

# In-memory Storage and Caching System
"Memcached", "Redis", "Varnish Cache", "Amazon Elasticache", "Ehcache", "Oracle Coherence", 

# Web Servers
"Nginx", "Apache Http Server", "ATS", "Squid", "HAProxy", "Apache Tomcat", "IIS", "Unix", "Linux", "Windows", "MAMP",

# Hardware Programming
"Arduino", "Raspberry Pi", "BeagleBone Black", "Intel Galileo", "pcDuino", "Uruk", "Goldilocks", "ExtraCore", "SparkCore", "DigiSpark", "Parallela Micro ServerBoard", "Giant Gecko", "Nanode Winode", "Launch Pad", "Discovery",

# Mail Servers
"Postfix", "Sendmail", "Qmail", "Zimbra", "Microsoft Exchange", "Exim", "Dovecot", "Courier", "Cyrus",

# Communication Technologies
"Twilio", "Nexmo", "Plivo", "Google Voice", "Tropo", "VOIP", "Amazon SNS", "Asterisk", "Global SMS", "Global MMS", "OpenVBX",

# Monitoring Systems
"Nagios", "Spiceworks", "OpenNMS", "Ganglia", "Collectd", "Sensu", "Zenoss", "Cricket", "Icinga", "Zabbix", "Cacti", "Splunk",

# Monitoring Tools
"JConsole", "VisualVM",

# Virtualization & Containers
"KVM", "XenServer", "VMware", "Hyper-V", "OCP", "OpenStack", "LXC", "LXD", "LXCFS", "Docker", "CloudStack", "OpenShift",

# Configuration Management
"Chef", "Puppet", "Salt", "Ansible", "CFEngine", "Vagrant",

# Cloud Operating System, Cloud Infrastructure, Building and Managing Cloud Computing Platforms
"Amazon Web Services", "Rackspace Cloud", "Google App Engine", "Microsoft Azure", "Heroku", "Linode", "Digital Ocean", "OpenStack", "VMware", "Kubernetes", "Mesos", "Marathon", "Yarn", "Spark",

# Amazon Web Services (AWS)
"EC2", "S3", "Elastic MapReduce", "CloudFront", "SimpleDB", "RDS", "SQS", "SNS", "CloudWatch", "VPC", "ELB", "EBS", "AWS Import/Export", "Lightsail", "Elastic Beanstalk", "EC2 Container Registry", "Lambda", "EC2 Container Service", "Batch", "Auto Scaling", "Glacier", "Snowball Edge", "Storage Gateway", "Snonmobile", "Elastic File System", "Snowball", "Aurora", "DynamoDB Accelerator", "Databasse Migration Service", "Elasticache", "Redshift",

# Game Programming
"Unity", "Unreal Engine", "CryEngine",


# Building Programming Languages
"Assembly", "C", "Compiler", "Lexer", "Parser", "Scanner", "Tokenizer", "Interpreter", "Abstract Syntax Tree", "Valgrind", "Decompiler", "gdb", "strace", "ltrace", "apport", "Perf", "GNU Make", "CMake", "bsd make", "nmake", "Antlr", "Lex", "Flex", "Yacc", "Bison", "Boost Spirit", "JavaCC", "Accent", "Elk", "json-lexer",

# Markup Languages
"D/X/HTML", "XML", "XSL", "XSLT", "Web Services", "WSDL", "SOAP", "REST", "RSS", "W3C Standards",

# Network Administration
"Systems Architect", "TCP/IP", "Cisco IOS", "LAN", "WAN", "VLAN", "BGP", "OSPF", "ARP", "RIP", "DNS", "IPv4", "IPv6", "Asterisk", "Rack systems", "Resolving Software and Hardware issues", "Large Scale Deployment", "Thin Client", "ISP", "VOIP", "Surveillance", "Wireless Networks", "Firewalls", "Routers", "Switches", "Network Planning", "Network Security", "OpenVPN",

# Operating Systems
"Windows", "Linux","Debian", "Ubuntu", "Fedora", "Mint Linux", "CentOS", "Red Hat Enterprise Linux", "openSUSE", "SUSE Linux Enterprise", "Mageia", "Mandriva", "Arch Linux", "Unix", "FreeBSD", "Mac", "iOS", "Android", "Windows Phone",

# Content Delivery Network (CDN)
"Akamai", "MaxCDN", "Amazon CloudFront", "CloudFlare", "Rackspace Cloud Files", "CacheFly", "WPPronto", "SoftLayer", "CDN77", "Incapsula", "jsDelivr",

# Browser Rendering Engines
"Webkit", "Safari", "Chrome", "Blackberry", "Palm", "Presto", "Opera", "Opera Mobile", "Gecko", "Firefox", "Firefox Mobile", "Trident", "Internet Explorer", "IE Mobile",

# Integrated Development Environments (IDE)
"NetBeans", "Xcode", "Eclipse", "SpringSource Tool Suites", "Visual Studio", "Zend Studio", "PhpStorm",

# Text Editors
"Sublime Text", "Notepad++", "Atom", "Emacs", "Vim", "Nano", "Vi",

# Version Control Systems
"Git", "Github", "Gitlab", "Gitolite", "Gitorious", "Bitbucket", "Subversion", "Mercurial", "Concurrent Versions System", "Bazaar", "LibreSource", "Monotone",

# Content Management Systems (CMS)
"Wordpress", "Joomla", "Drupal", "Squarepsace", "Frog CMS", "SilverStripe", "Mambo", "TYPOlight", "Concrete5", "MODX",

# Customer Relationship Management (CRM) Software
"Salesforce", "Highrise", "SugarCRM", "Capsule", "NetSuite", "Etelos", "Zoho", "Entellium",

# Ecommerce Shopping Carts
"Shopify", "Volusion", "Virtuemart", "TomatoCart", "Prestashop", "OpenCart", "Magento", "ZenCart", "osCommerce", "StoreSprite", "Cube Cart", "Ubercart",

# Payment Gateways & Processors
"Stripe", "Square", "Braintree", "Authorize.net", "Paypal", "Venmo", "Chase Paymentech", "Google Wallet", "WePay", "Amazon Payments", "Dwolla", "2CheckOut", "ACH Payments", "Bitcoin", "Litecoin", "Feathercoin", "Dogecoin", "Peercoin", "Namecoin", "Ethereum", "Ripple", "NXT", "First Data",

# Search Engine Optimization (SEO)
"Alexa", "Backlink", "Domain Popularity", "Domain Stat", "Google Page Rank", "Adwords Keyword","Google Banned", "Keyword Density","Keyword Difficulty", "Keyword Suggestion", "Deep Link Ratio", "Link Popularity", "Outbound Links", "Title & Meta Tags", "Sitemap", "Directory Submission", "URL Rewriting", "Search Engine Position", "Serps Tracker", "Robots.txt", "Google Analytics",

# Social Media Marketing
"Facebook", "Twitter", "Pinterest", "Google+", "LinkedIn", "YouTube", "Bebo", "Hi5", "Orkut", "Share This", "Add this", "HootSuit", "Vertical Response", "Sprout Social", "Sendible", "Postlings",

# Online Marketing
"SEO", "Email Marketing", "Email Newsletters", "Email Subscriptions", "Marketing Ads", "Blogs", "Content Marketing", "Forums", "Web 2.0", "RegEx Keywords", "Links", "SEO", "SES", "SEM", "SERP", "DMOZ",

# Press Releases
"PRNewswire", "PRWeb", "BusinessWire", "MarketWire", "Techcrunch", "Mashable", "Wired", "Engadget",

# Ad Networks, Ad Exchange and Affiliate Marketing
"Google Adsense", "Media.net", "BuySellAds", "Conversant", "Adblade", "Clicksor", "Chitika", "Infolinks", "Kontera", "Amazon Associates", "CJ Affiliate by Conversant","Rakuten LinkShare", "AdMob", "Flurry", "TapJoy", "Millenial Media", "AirPush", "iAd", "Outbrain", "YouTube Partner Program", "Google DFP Video", "Videology", "PulsePoint", "Tribal Fusion", "Vibrant Media", "LiveIntent", 

]

i = 0
for link in linksArray:
    for path in pathArray:
        search = requests.get(link + path)
        s_content = soup(search.content, "html.parser")
        for post in s_content.find_all("a", attrs={'class': "result-title"}):
            for keyword in keywords:
                if keyword in post.text:
                    print(post.text)
                    print(post.get('href'))
                    print('\n')
                    break

i = i + 1