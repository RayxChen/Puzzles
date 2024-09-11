class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        // from target go backwards to start
        while (tx >= sx && ty >= sy){
            if ((tx == sx && (ty - sy) % tx == 0) || (ty == sy && (tx - sx) % ty == 0)){
                return true;
            }
            if (tx > ty){
                tx %= ty;
            }
            else {
                ty %= tx;
            }

        }
        return false;

    }
};