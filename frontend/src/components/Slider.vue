<template>
    <div class="relative slide rounded-lg">
        <div v-if="imgs.length>1" class="carousel-indicators absolute bottom-0 flex h-24 w-full justify-center items-center">
            <ol class="z-50 flex w-4/12 justify-center">
                <li v-for="(img, key, i) in images" :key="`li-${i}`" @click="toggle(i)" :class="{'active':active === i}" class="carousel-indicator md:w-4 md:h-4 bg-gray-500 rounded-full cursor-pointer mx-2">
                </li>
            </ol>
        </div>
        <div class="carousel-inner relative overflow-hidden w-full rounded-lg">
            <div v-for="(img, key, i) in images" :id="`slide-${i}`" :key="`img-${i}`" :class="`${active === i ? 'active' : 'left-full'}`"
                class="carousel-item inset-0 relative w-full transform transition-all duration-500 ease-in-out">
                <div v-if="key!=='default'" class="absolute p-4 flex justify-center w-full top-0 left-0 text-sm text-gray-500 dark:text-gray-400">{{ key }}</div>
                <img class="block w-full rounded-lg" :src="img" alt="First slide" />
            </div>
        </div>
        <div v-if="imgs.length>1" class="absolute top-0 left-0 h-full flex items-center justify-center">
            <button class="px-4 h-full" @click="prev"><IconChevron style="transform: rotate(180deg)"/></button>
        </div>
        <div v-if="imgs.length>1" class="absolute top-0 right-0 h-full flex items-center justify-center">
            <button class="px-4 h-full" @click="next"><IconChevron/></button>
        </div>
    </div>
</template>
<script>

import IconChevron from './icons/IconChevron.vue'

export default {
    components:{
        IconChevron
    },
    data() {
        return {
            active: 0
        }
    },
    props: {
        images: {
            default: () => {},
            type: Object
        }
    },
    methods:{
        toggle(i){
            this.active = i
        },
        prev(){
            this.active--
            this.active = this.active<0?this.imgs.length-1:this.active
        },
        next(){
            this.active++
            this.active = this.active>this.imgs.length-1?0:this.active
        },
    },
    computed:{
        imgs: function (){
            return Object.entries(this.images)
        }
    }
}
</script>
<style scoped>
.left-full {
    left: -100%;
}

.carousel-item {
    float: left;
    position: relative;
    display: block;
    width: 100%;
    margin-right: -100%;
    backface-visibility: hidden;
}

.carousel-item.active {
    left: 0;
}
.carousel-indicator.active{
    background-color: white !important;
}
</style>