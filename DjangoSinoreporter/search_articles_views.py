def get_documents(searched_phrase, collection_name, index_name, user=None, limit=100, additional_query_params=None):
    mongo_db = os.environ.get('DB_HOST')
    client = pymongo.MongoClient(mongo_db)
    mydb = client.chinaNewsInt
    mycol = mydb[collection_name]
    pipeline = [
        {
            '$search': {
                'index': index_name,
                'text': {
                    'query': searched_phrase,
                    'path': {
                        'wildcard': '*'
                    }
                }
            }
        },
        {'$limit': limit}
    ]

    if user and collection_name == 'news_article':
        pipeline.append({'$lookup':
                         {
                             'from': 'news_article_bookmarks',
                             'localField': 'id',
                             'foreignField': 'article_id',
                             'as': 'news_article_bookmarks'
                         }
                         })
    if additional_query_params:
        pipeline.insert(1, additional_query_params)
    search_result = mycol.aggregate(pipeline)
    data = list(search_result)
    if user and collection_name == 'news_article':
        for datum in data:
            if any(bookmark['user_id'] == user.id for bookmark in datum['news_article_bookmarks']):
                datum['is_bookmarked'] = True
    return data
