package org.example;

import com.thoughtworks.gauge.Step;
import io.appium.java_client.MobileElement;
import io.appium.java_client.TouchAction;
import io.appium.java_client.touch.offset.PointOption;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.touch.TouchActions;

public class StepImplementation extends BaseTest{

    @Step("<time> saniye bekle")
    public void waitTime(int time) throws InterruptedException {
        Thread.sleep(1000* time);
    }
    @Step("<Key> İd'li elemente tıkla")
    public void clickElementByid(String Key){
        appiumDriver.findElement(By.id(Key)).click();
        System.out.println(Key+"Elenitine tıklandı");
    }
    @Step("<Key> İd'li elemente <keywordc> değerini yaz")
    public void SendkeyElementByid(String Key,String keywordc){
        appiumDriver.findElement(By.id(Key)).sendKeys(keywordc);
        System.out.println(Key+"Elenitine tıklandı");

    }
    @Step("<Key> xpath'li elemente tıkla")
    public void clickElementByxpath(String Key){
        appiumDriver.findElement(By.xpath(Key)).click();
        System.out.println(Key+"Elenitine tıklandı");
    }
    @Step("<Key> xpath'li elemente <keywordc> değerini yaz")
    public void SendkeyElementByxpath(String Key,String keywordc){
        appiumDriver.findElement(By.xpath(Key)).sendKeys(keywordc);
        System.out.println(Key+"Elenitine tıklandı");

    }
    @Step("<Key> css'li elemente tıkla")
    public void clickElementByCss(String Key){
        appiumDriver.findElement(By.cssSelector(Key)).click();
        System.out.println(Key+"Elenitine tıklandı");
    }
    @Step("<Key> css'li elemente <keywordc> değerini yaz")
    public void SendkeyElementBycss(String Key,String keywordc){
        appiumDriver.findElement(By.cssSelector(Key)).sendKeys(keywordc);
        System.out.println(Key+"Elenitine tıklandı");

    }
    @Step("x =<Key> y=<Key> Scroll Yap")
    public void ScrollBy(int x,int y){
        TouchActions action = new TouchActions(appiumDriver);
        action.longPress((WebElement) PointOption.point(x,y+250)).move(x,y);
        action.release();
        action.perform();
    }
    @Step("<time> yapılır")
    public void print(String text) throws InterruptedException {
        System.out.println(text);
    }
}
