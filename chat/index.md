---
layout: wide
title: "Chat"
subtitle: "Ask questions, get help, and muse about Harvest"
---

<div id=hipchat-client></div>

<script src="{{ site.baseurl }}js/hipchat.js"></script>
<script>
    HipChat({
        el: '#hipchat-client',
        url: 'https://www.hipchat.com/gkfNOKOPG',
        timezone: 'EST'
    });
</script>