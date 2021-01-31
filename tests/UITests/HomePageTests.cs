using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using UITests.PagoObjectModel;

namespace UITests
{
    public class Tests
    {
        private PageManager pageManager;

        [SetUp]
        public void Setup()
        {
            pageManager = new PageManager();
        }

        [Test]
        public void AllItemsAreDisplayed()
        {
            //Act
            pageManager.HomePage.NavigteTo();

            //Assert
            Assert.That(pageManager.HomePage.HomeLinkData.Equals(HomePage.HomeLinkHeaderText));
            Assert.That(pageManager.HomePage.SearchPlaceholder.Equals(HomePage.SearchPlaceholderText));
            Assert.That(pageManager.HomePage.EmptyListMessageText.Equals(HomePage.EmptyListText));
            Assert.That(pageManager.HomePage.Settings.Displayed);
            Assert.That(pageManager.HomePage.CurrentPageText.Equals(HomePage.DefaultPageNumber));
            Assert.That(pageManager.HomePage.PaginatorGoToFirstButton.Displayed);
            Assert.That(pageManager.HomePage.PaginatorGoToPreviousButton.Displayed);
            Assert.That(pageManager.HomePage.PaginatorGoToNextButton.Displayed);
            Assert.That(pageManager.HomePage.PaginatorGoToLastButton.Displayed);
        }

        [Test]
        public void PaginationButtonsAreDisabled()
        {
            //Act
            pageManager.HomePage.NavigteTo();

            //Assert
            Assert.That(pageManager.HomePage.GetDisabledButton(HomePage.PaginatorGoToFirst).Displayed);
            Assert.That(pageManager.HomePage.GetDisabledButton(HomePage.PaginatorGoToPrevious).Displayed);
            Assert.That(pageManager.HomePage.GetDisabledButton(HomePage.PaginatorGoToNext).Displayed);
            Assert.That(pageManager.HomePage.GetDisabledButton(HomePage.PaginatorGoToLast).Displayed);
        }

        [TearDown]
        public void TearDown()
        {
            pageManager.Clean();
        }
    }
}