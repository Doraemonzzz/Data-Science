test = {
  'name': 'Question 3.1.3',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> genre_and_distances.num_columns
          2
          >>> genre_and_distances.num_rows == train_lyrics.num_rows
          True
          >>> np.allclose(genre_and_distances.column('Distance'), sorted(fast_distances(test_20.row(0), train_20)))
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
