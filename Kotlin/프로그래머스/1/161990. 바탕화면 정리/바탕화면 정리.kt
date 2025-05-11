class Solution {
    fun solution(wallpaper: Array<String>): IntArray {
        var answer: IntArray = intArrayOf()
        
        
        var lux = wallpaper.size
        var luy = wallpaper[0].length
        var rdx = 0
        var rdy = 0
        
        for (i in 0..(wallpaper.size-1)) {
            
            if (wallpaper[i].contains('#')) {
                val indy = wallpaper[i].indexOf('#')
                val indy2 = wallpaper[i].lastIndexOf('#')+1
                val indx = i
                
                if (indy < luy) luy = indy
                if (indx < lux) lux = indx
                if (indy2 > rdy) rdy = indy2
                if (indx+1 > rdx) rdx = indx+1
            }
        }
        
        answer = intArrayOf(lux, luy, rdx, rdy)
        return answer
    }
}