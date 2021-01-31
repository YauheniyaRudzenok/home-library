using System;
using OpenQA.Selenium;

namespace UITests.PagoObjectModel
{
    public class HomePage : BasePage
    {
        public const string HomeLinkHeaderText = "Home Library";
        public const string SearchPlaceholderText = "Search...";
        public const string EmptyListText = "No records found";
        public const int DefaultPageNumber = 1;

        private const string HomeLinkSelector = "div.branding > a";
        private const string SearchFieldSelector = "div.search > input";
        private const string SettingIconSelector = "i.pi";
        private const string EmptyListMessageSelector = "div[class*=emptymessage]";

        public const string PaginatorGoToFirst = "span[class*=step-backward]";
        public const string PaginatorGoToPrevious = "span[class*=caret-left]";
        private const string PaginatorCurrentPage = "a[class*=active]";
        public const string PaginatorGoToNext = "span[class*=caret-right]";
        public const string PaginatorGoToLast = "span[class*=step-forward]";
        public const string Disabledstatus = "a.ui-state-disabled";

        public HomePage(IWebDriver driver): base(driver)
        {}

        protected override string PageURL => Config.WebUrl;

        public IWebElement HomeLink => Driver.FindElement(By.CssSelector(HomeLinkSelector));
        public IWebElement SearchField => Driver.FindElement(By.CssSelector(SearchFieldSelector));
        public IWebElement Settings => Driver.FindElement(By.CssSelector(SettingIconSelector));
        public IWebElement EmptyListMessage => Driver.FindElement(By.CssSelector(EmptyListMessageSelector));
        public IWebElement PaginatorGoToFirstButton => Driver.FindElement(By.CssSelector(PaginatorGoToFirst));
        public IWebElement PaginatorGoToPreviousButton => Driver.FindElement(By.CssSelector(PaginatorGoToPrevious));
        public IWebElement CurrentPage => Driver.FindElement(By.CssSelector(PaginatorCurrentPage));
        public IWebElement PaginatorGoToNextButton => Driver.FindElement(By.CssSelector(PaginatorGoToNext));
        public IWebElement PaginatorGoToLastButton => Driver.FindElement(By.CssSelector(PaginatorGoToLast));
        public IWebElement GetDisabledButton(string button) => Driver.FindElement(By.CssSelector(Disabledstatus + " > " + button));

        public string HomeLinkData => HomeLink.Text;
        public string SearchPlaceholder => SearchField.GetAttribute("placeholder");
        public string EmptyListMessageText => EmptyListMessage.Text;
        public int CurrentPageText => int.Parse(CurrentPage.Text);
    }
}
