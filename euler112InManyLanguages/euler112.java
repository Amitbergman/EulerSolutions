package euler112InManyLanguages;

class euler112{

    public static boolean isIncreasing(int number){
        if (number < 10){
            return true;
        }
        while (number > 0){
            if (number < 10){
                return true;
            }
            if (number %10  < (number /10)%10){
                return false;
            }
            number = number / 10;
        }
        return true;
    }

    public static boolean isDecreasing(int number){
        if (number < 10){
            return true;
        }
        while (number > 0){
            if (number < 10){
                return true;
            }
            if (number %10  > (number /10)%10){
                return false;
            }
            number = number / 10;
        }
        return true;
    }

    private static boolean isBouncing(int number){
        return (!isDecreasing(number)&&!isIncreasing(number));
    }
    public static void main(String args[]){

        int counter = 0;
        for (int i = 0; i < 1000; i++) {
            if (isBouncing(i)){
                counter++;
            }
        }
        System.out.println(counter);

        double percentage = 0;
        double general = 0;
        double bouncy = 0;
        int toCheck = 1;
        double goal = 0.99;
        while (percentage < goal){
            if (isBouncing(toCheck)){
                bouncy +=1;
            }
            
            toCheck +=1;
            general +=1;
            percentage = bouncy / general;

        }
        System.out.println("Answer to euler 112 is: " +  general);

    }
}