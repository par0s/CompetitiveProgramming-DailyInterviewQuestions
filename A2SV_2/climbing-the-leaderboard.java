import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'climbingLeaderboard' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY ranked
     *  2. INTEGER_ARRAY player
     */

    public static List<Integer> climbingLeaderboard(List<Integer> ranked, List<Integer> player) {
    // Write your code here
        int n = ranked.size();      
        
        //use set to populate ranks array with unique values to binary search on unique values
        HashSet<Integer> visited = new HashSet<>();
        int[][] ranks = new int[n][2];        
        int ind = 0;
        
        for(int i = 0; i < n; i++){
            //check if it has not been assigned a rank
            if(!visited.contains(ranked.get(i))){                   
                    visited.add(ranked.get(i));
                    ranks[ind][0] = ranked.get(i);
                    ranks[ind][1] = ind + 1;
                    ind += 1;
                }            
            }
        
        int p = player.size();
        ArrayList<Integer> res = new ArrayList<Integer>();
        for(int i = 0; i < p; i++){   
            //we don't have to add the number to the rank array because since the player array is sorted the currenct(less) score won't affect the rank of the next(bigger) score.                     
            res.add(binarySearch(ranks,player.get(i),ind));
        }                      
        return res;
    }
    
    public static int binarySearch(int[][] ranks,int current,int h){
        //h is the higher limit because the ranks array can have trailing zeroes at the end which are not populated or that represent the non unique values
        int low = 0;
        int high = h - 1;
        int n = ranks.length;
        
        while(low <= high){
            int mid = low + (high - low) / 2;
            int midVal = ranks[mid][0];            
            if(midVal == current){
                return ranks[mid][1];
            }
 
            if(midVal < current){
                if(mid - 1 >= 0 && ranks[mid - 1][0] > current){
                    return ranks[mid][1];
                }                
                high = mid - 1;                               
            }
            else{                
                low = mid + 1; 
            }
        }        
        
        //if low is greater than h, it means it is lower than all scores
        if(low >= h){
            return h + 1;
        }
        //if high is -1 it means it is greater than all scores
        if(high <= -1){
            return 1;
        }        
        return -1;
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int rankedCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> ranked = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int playerCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> player = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        List<Integer> result = Result.climbingLeaderboard(ranked, player);

        bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
