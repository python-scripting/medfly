<!-- =========================================================================================
    File Name: TheFooter.vue
    Description: Footer component
    Component Name: TheFooter
   
========================================================================================== -->


<template functional>
    <footer class="the-footer flex-wrap justify-between" :class="classes">
        <p>
          <span>COPYRIGHT &copy;</span>
          <span>2021 </span>
          <a href="http://namselas.com" target="_blank" rel="nofollow">Namselas Consulting Pvt Ltd</a>
          <span class="hidden sm:inline-block">, All rights Reserved</span>
        </p>
       <!--  <span class="md:flex hidden items-center">
            <span>Hand-crafted & Made with</span>
            <feather-icon icon="HeartIcon" svgClasses="stroke-current text-danger w-6 h-6" class="ml-2" />
        </span> -->
    </footer>
</template>

<script>
export default {
    name: "the-footer",
    props: {
        classes: {
            type: String,
        }
    }
}
</script>
