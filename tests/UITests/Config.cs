using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Configuration.Json;

namespace UITests
{
    public static class Config
    {
        private static IConfigurationRoot configuration;
        private static object sync = new object();

		private static IConfigurationRoot Instance
		{
			get
			{
				if (configuration == null)
				{
					lock (sync)
					{
						if (configuration == null)
							configuration = new ConfigurationBuilder()
								.AddJsonFile("appconfig.json")
								.Build();
					}
				}
				return configuration;
			}
		}

		public static string WebUrl => Instance["appSettings:webURL"];
		public static string Browser => Instance["browserSettings:browser"];
	}
}