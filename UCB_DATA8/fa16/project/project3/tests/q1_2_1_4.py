test = {
  'name': '2.1.4',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(close_songs.labels) >= {'Genre', 'Artist', 'Title', 'like', 'love'}
          True
          >>> close_songs.num_rows == 7
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> close_songs.column('Title').item(1) == 'Big Red Rocket Of Love'
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': r"""
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
