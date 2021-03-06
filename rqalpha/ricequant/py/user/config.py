{'base': {'accounts': {'STOCK': 100000.0},
          'benchmark': '000300.XSHG',
          'data_bundle_path': '/home/user_325121/.rqalpha-plus/bundle',
          'end_date': datetime.date(2017, 6, 1),
          'frequency': '1d',
          'margin_multiplier': 1,
          'persist': False,
          'persist_mode': PERSIST_MODE.REAL_TIME,
          'resume_mode': False,
          'run_type': RUN_TYPE.BACKTEST,
          'source_code': None,
          'start_date': datetime.date(2016, 1, 1),
          'strategy_file': 'strategy.py'},
 'extra': {'context_vars': None,
           'dividend_reinvestment': False,
           'enable_profiler': False,
           'force_run_init_when_pt_resume': False,
           'is_hold': False,
           'locale': 'zh_Hans_CN',
           'log_level': 'verbose',
           'user_log_disabled': False,
           'user_system_log_disabled': False},
 'mod': {'indicator': {'enabled': True, 'lib': 'rqalpha_mod_indicator'},
         'ricequant_data': {'enabled': True,
                            'lib': 'rqalpha_mod_ricequant_data',
                            'night_trading': False,
                            'priority': 101,
                            'rqdata_client_addr': 'q-rqdatad',
                            'rqdata_client_password': 'research',
                            'rqdata_client_port': 16003,
                            'rqdata_client_retry_cnt': 30,
                            'rqdata_client_username': 'research'},
         'sys_accounts': {'enabled': True},
         'sys_analyser': {'enabled': True, 'plot': True},
         'sys_funcat': {'enabled': False},
         'sys_progress': {'enabled': True},
         'sys_risk': {'enabled': True},
         'sys_simulation': {'enabled': True},
         'sys_stock_realtime': {'enabled': False}},
 'validator': {'cash_return_by_stock_delisted': False, 'close_amount': True},
 'version': '0.1.6',
 'whitelist': ['base', 'extra', 'validator', 'mod']}