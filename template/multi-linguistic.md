<!-- Chinese Version -->
<div class="zh post-container">
    {% capture about_zh %}{% include posts/directory/zh.md %}{% endcapture %}
    {{ about_zh | markdownify }}
</div>

<!-- English Version -->
<div class="en post-container">
    {% capture about_en %}{% include posts/directory/en.md %}{% endcapture %}
    {{ about_en | markdownify }}
</div>