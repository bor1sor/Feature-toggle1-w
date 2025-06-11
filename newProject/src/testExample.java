import io.restassured.RestAssured;

public class testExample {
    public static void main(String[] args) {
        RestAssured.given()
                .when().get("https://jsonplaceholder.typicode.com/posts/1")
                .then().assertThat().statusCode(200);
    }
}