import java.io.*;
import java.net.*;

public class c {

   public static String getHTML(String https://www.googleapis.com/youtube/v3/channels?part=UCJ6td3C9QlPO9O_J5dF4ZzA&key=AIzaSyDIbJw0VKn8HpY0_eoj7rmbVwVZULAB9yU) throws Exception {
      StringBuilder result = new StringBuilder();
      URL url = new URL(urlToRead);
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setRequestMethod("GET");
      BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
      String line;
      while ((line = rd.readLine()) != null) {
         result.append(line);
      }
      rd.close();
      return result.toString();
   }

   public static void main(String[] args) throws Exception
   {
     System.out.println(getHTML(args[0]));
   }
}