from useragents_me_scraper import useragents as ua


def test_process_ua():
    test_ua_json = '[{"ua":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36","pct":36.47},{"ua":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36","pct":24.17},{"ua":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/109.0.0.0 Safari\/537.36","pct":5.47}]'
    test_processed_ua = ua._process_ua(test_ua_json)
    test_content = test_ua_json
    test_start_date, test_end_date = ua.utils.get_week_timeframe()

    assert(ua.utils.convert_str_to_date(test_processed_ua['start_date']) == test_start_date and
           ua.utils.convert_str_to_date(test_processed_ua['end_date']) == test_end_date and
           test_processed_ua['content'] == test_content)
