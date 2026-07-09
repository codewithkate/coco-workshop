SELECT
usage_time,
  REQUEST_ID,
  TOKENS as total_tokens,
  TOKEN_CREDITS,
  OBJECT_KEYS(TOKENS_GRANULAR)[0]::string AS model_name,
  COALESCE(TOKENS_GRANULAR:"claude-opus-4-6":"cache_read_input",0) as cache_read_input,
  COALESCE(TOKENS_GRANULAR:"claude-opus-4-6":"cache_write_input",0) as cache_write_input,
  COALESCE(TOKENS_GRANULAR:"claude-opus-4-6":"input",0) as input_tokens,
  COALESCE(TOKENS_GRANULAR:"claude-opus-4-6":"output",0) as output_tokens,
  ((5 * input_tokens) + (25 * output_tokens) + (0.5 * cache_read_input) + (6.25 * cache_write_input))/1000000 as cost_in_us_dollars

FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_CODE_DESKTOP_USAGE_HISTORY as D
WHERE OBJECT_KEYS(TOKENS_GRANULAR)[0]::string = 'claude-opus-4-6'
AND USER_NAME = CURRENT_USER()
AND usage_time::date = CURRENT_DATE()
ORDER BY usage_time ASC;