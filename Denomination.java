import java.util.Scanner;
class Denomination{



    public static void main(String[] args) {
        System.out.println("\t\t\t\t\t\t** MONEY DENOMIATION **");
        Scanner scanner=new Scanner(System.in);
        long tt=0,fh=0,th=0,h=0,f=0,t=0,ten=0,two=0,five=0,one=0,mon=0,a;
        boolean turn=false;
        System.out.println("1.METHOD\n(IT WORKS BY ENTERING A CASH BY ONE BY ONE) \n2.METHOD \n(THIS METHOD WORKING UNDER A BULK ENTERIES)\n3.QUIT");
         a=scanner.nextInt();

       
        if(a==1) 
        {
        turn=true;
        while(turn==true)
        {
            System.out.println("\n\n");
            System.out.println("\n\n1.2000rs 2.500rss 3.200rs 4.100rs 5.50rs 6.20rs 7.10rs 8.5rs 9.2rs 10.rs");
             System.out.println("\n\nENTER YOUR OPTIION:\t\t\t\t\t\t\t\t\t\t\t\t\t11.EXIT");
             int money=scanner.nextInt();
            switch (money) {
                case 1:
                    tt+=2000;
                    break;

                case 2:
                    fh+=500;
                    break;
                
                case 3:
                    th+=200;
                    break;
                case 4:
                    h+=100;
                    break;
                case 5:
                    f+=50;
                    break;
                case 6:
                    t+=20;
                    break;
                case 7:
                    ten+=10;
                    break;
                case 8:
                    five+=5;
                    break;
                case 9:
                    two+=2;
                    break;
                case 10:
                    one+=1;
                    break;
                case 11:
                    turn=false;
                    break;
                default:
                    System.out.println("ENTER A VALID DENOMINATION");
                    break;
            }
            System.out.println("result");
            System.out.println("\n");
            System.out.printf("1.2000 x %d = %d\n",Math.abs(tt/2000),tt);
            System.out.printf("2.500  x %d = %d\n",Math.abs(fh/500),fh);
            System.out.printf("3.200  x %d = %d\n",Math.abs(th/200),th);
            System.out.printf("4.100  x %d = %d\n",Math.abs(h/100),h);
            System.out.printf("5.50   x %d = %d\n",Math.abs(f/50),f);
            System.out.printf("6.20   x %d = %d\n",Math.abs(t/1),t);
            System.out.printf("7.10   x %d = %d\n",Math.abs(ten/10),ten);
            System.out.printf("8.5    x %d = %d\n",Math.abs(five/5),five);
            System.out.printf("9.2    x %d = %d\n",Math.abs(two/2),two);
            System.out.printf("10.1   x %d = %d\n",Math.abs(one/1),one);
            System.out.printf("\nTOTAL AMOUNT == %d",tt+fh+th+h+f+t+ten+five+two+one);

        }}
        else if(a==2){
            turn=true;
            while(turn==true)
            {
                System.out.println("\n\n");
                 System.out.println("\n\n1.2000rs 2.500rss 3.200rs 4.100rs 5.50rs 6.20rs 7.10rs 8.5rs 9.2rs 10.rs");
                 System.out.println("ENTER YOUR OPTION:");
               int money=scanner.nextInt();
                switch (money) {
                    case 1:
                        System.out.println("No. of 2000rs Notes:");
                        mon=scanner.nextInt();
                        tt=2000*mon+tt;
                        break;
    
                    case 2:
                        System.out.println("No. of 500rs Notes:");
                        mon=scanner.nextInt();
                        fh=500*mon+fh;
                        break;
                    
                    case 3:
                    System.out.println("No. of 200rs Notes:");
                     mon=scanner.nextInt();
                    th=200*mon+th;
                    break;
                    case 4:
                    System.out.println("No. of 100rs Notes:");
                    mon=scanner.nextInt();
                    h=100*mon+h;
                    break;
                    case 5:
                    System.out.println("No. of 50rs Notes:");
                    mon=scanner.nextInt();
                    f=50*mon+f;
                    break;
                    case 6:
                    System.out.println("No. of 20rs Notes:");
                    mon=scanner.nextInt();
                    t=20*mon+t;
                    break;
                    case 7:
                    System.out.println("No. of 10rs Notes:");
                    mon=scanner.nextInt();
                    ten=10*mon+ten;
                    break;
                    case 8:
                    System.out.println("No. of 5rs Notes:");
                    mon=scanner.nextInt();
                    five=5*mon+five;
                    break;
                    case 9:
                    System.out.println("No. of 2rs Notes:");
                    mon=scanner.nextInt();
                    two=2*mon+two;
                    break;
                    case 10:
                    System.out.println("No. of 1rs Notes:");
                    mon=scanner.nextInt();
                    one=1*mon+one;
                    break;
                    case 11:
                        turn=false;
                        break;
                    default:
                        System.out.println("ENTER A VALID DENOMINATION");
                        break;
                }
                System.out.println("result");
                System.out.println("\n");
                System.out.printf("1.2000 x %d = %d\n",Math.abs(tt/2000),tt);
                System.out.printf("2.500  x %d = %d\n",Math.abs(fh/500),fh);
                System.out.printf("3.200  x %d = %d\n",Math.abs(th/200),th);
                System.out.printf("4.100  x %d = %d\n",Math.abs(h/100),h);
                System.out.printf("5.50   x %d = %d\n",Math.abs(f/50),f);
                System.out.printf("6.20   x %d = %d\n",Math.abs(t/1),t);
                System.out.printf("7.10   x %d = %d\n",Math.abs(ten/10),ten);
                System.out.printf("8.5    x %d = %d\n",Math.abs(five/5),five);
                System.out.printf("9.2    x %d = %d\n",Math.abs(two/2),two);
                System.out.printf("10.1   x %d = %d\n",Math.abs(one/1),one);
                System.out.printf("\nTOTAL AMOUNT == %d",tt+fh+th+h+f+t+ten+five+two+one);
    
            }
        }
        else {

        System.out.println("\n\n\nTHANKS FOR CHOOSING US");
        }
    }
}