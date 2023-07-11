# Movies to Markdown

This is a simple Python application written, with a little help from GitHub CoPilot :muscle::smile:, to extract some information about movies and write it out as markdown files.

The use case for this was generating sample data to be used with OpenAI models. The data needed to be something new that the AI hadn't been trained on, so extracting some information about recently released movies seemed to be a simple source of data.

Instructions for getting started with the TMDB API can be found here - https://developer.themoviedb.org/docs

You'll need to create an account and then register for API access.

In the last section of the code where the markdown files are generated, you can optionally remove the last two lines of code:

```python
f'## Reviews\n\n' \
f'{"".join(reviews)}' \
```

The reviews typically generate a lot of information. The review data was used when a bulkier document is needed.