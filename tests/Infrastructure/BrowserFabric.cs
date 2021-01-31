using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Firefox;

namespace Jane.Tests.Infrastructure
{
	public static class BrowserFabric
	{
		public static IWebDriver CreateDriver(string browser, ChromeOptions options = null)
		{
			switch (browser)
			{
				case "Chrome":
					return new ChromeDriver();
				case "Firefox":
					return new FirefoxDriver();
				default: return new ChromeDriver();
			}
		}
	}
}
