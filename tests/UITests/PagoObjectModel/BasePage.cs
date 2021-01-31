using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;

namespace UITests
{
    public abstract class BasePage
    {
        protected BasePage(IWebDriver driver)
        {
            Driver = driver;
        }

        public IWebDriver Driver { get; protected set; }
        protected virtual string PageURL { get; }
        protected virtual string PageTitle => "HomeLibrary";


        public void NavigteTo()
        {
            Driver.Navigate().GoToUrl(PageURL);
            EnsurePageIsLoaded();
        }

        public void EnsurePageIsLoaded(bool onlyCheckStartWith = true)
        {
            bool urlIsCorrect = !onlyCheckStartWith ?
                Driver.Url.StartsWith(PageURL):
                Driver.Url == PageURL;

            bool pageIsLoaded = urlIsCorrect && (Driver.Title == PageTitle);
            if (!pageIsLoaded)
            {
                throw new Exception($"Failed to load the page. Page {Driver.Url} with title {Driver.Title} is not loaded");
            }
        }

        public string JavaScriptExecutor(string script)
        {
            IJavaScriptExecutor javaScriptExecutor = (IJavaScriptExecutor)Driver;
            return javaScriptExecutor.ExecuteScript(script)?.ToString();
        }

        public void WaitByCss(string item = null)
        {
            var script = "return document.readyState";
            WebDriverWait wait = new WebDriverWait(Driver, timeout: TimeSpan.FromSeconds(30));
            wait.Until(condition => JavaScriptExecutor(script).Equals("complete"));
            if (item != null)
                wait.Until(SeleniumExtras.WaitHelpers.ExpectedConditions.ElementIsVisible(By.CssSelector(item)));
        }
    }
}
