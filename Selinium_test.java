package com.ProjCert;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;

public class Main {

    public static void main(String[] args) {
        // initialise the webdriver
        WebDriver driver =new HtmlUnitDriver();
        //browse to the required URL
        driver.get("http://localhost");
        //select the About Us link and click it
        WebElement el =driver.findElement(By.linkText("About Us"));
        el.click();
        // Get the text by the tag name "body". content of About Page
       // WebElement s = driver.findElement(By.tagName("body")); // for php website with bugs
        WebElement s = driver.findElement(By.tagName("article"));
        s.getText();
        //Print the text in the body of the About Us Page and quit
        System.out.println( s.getText());
        driver.quit();



    }
}
