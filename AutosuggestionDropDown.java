import java.time.Duration;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class AutosuggestionDropDown {

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
		System.setProperty("webdriver.gecko.driver", "D:\\GeckoDriver\\geckodriver.exe");

		//Browser Set up
		FirefoxDriver driver = new FirefoxDriver();
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
		driver.get("https://dramacool.cy/");
		driver.findElement(By.xpath("//input[@id='search-key']")).sendKeys("Loyalty");
		Thread.sleep(3000);
		List<WebElement> autosuggestions = driver.findElements(By.xpath("//li[@class='ui-menu-item']"));
		for(int i = 0; i<autosuggestions.size();i++) {
			System.out.println(autosuggestions.get(i).getText());
		}
		Thread.sleep(3000);
		for(int i = 0; i<autosuggestions.size();i++) {
			if((autosuggestions).get(i).getText().equalsIgnoreCase("Heart of Loyalty (2021)")) {
				autosuggestions.get(i).click();
			}
		}
		Thread.sleep(3000);
		driver.close();
	}

}
