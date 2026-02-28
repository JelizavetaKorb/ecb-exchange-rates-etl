ECB Exchange Rate ETL
This is a small Python script that fetches the latest Euro foreign exchange reference rates from the European Central Bank and compares them to long-term historical averages. It then saves the results as a simple Markdown table.

What it does
Each time you run it the script downloads two datasets from the ECB: today's rates and the full historical dataset going back decades. It focuses on four currencies: USD, SEK, GBP, and JPY. Then calculates the historical average for each, and puts everything side by side in a table. This way you can quickly see whether today’s rate is above or below the long-term average.

The output is saved as exchange_rates.md in the project root.
