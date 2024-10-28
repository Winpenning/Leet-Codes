using System;
using System.IO;
public class Program{
    public static void Main(){
        int value = RomanToInt("LVIII");
        System.Console.WriteLine(value);
    }

    public static int RomanToInt(string romanNumber){
         Dictionary<char, int> relation = new Dictionary<char, int>
        {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };
        int result = 0;
        int previous = 0;
        
        for(int i = romanNumber.Length-1; i >= 0; i--){

            int current = relation[romanNumber[i]];

            if(current < previous)
                result -= current;
            else
                result += current;
            
            previous = current;
        }
        return result;
    }
}