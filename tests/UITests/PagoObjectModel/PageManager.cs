using Jane.Tests.Infrastructure;
using OpenQA.Selenium;

namespace UITests.PagoObjectModel
{
    public class PageManager
    {
        private readonly IWebDriver driver;
        private HomePage _homePage;

        public PageManager()
        {
            driver = BrowserFabric.CreateDriver(Config.Browser);
        }

        public HomePage HomePage => _homePage ??= new HomePage(driver);

        public void Clean()
        {
            _homePage = null;
            driver?.Dispose();
        }
    }
}
