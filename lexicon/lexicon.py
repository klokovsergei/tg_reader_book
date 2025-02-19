LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': '<b>Привет, читатель!</b> 📖\n\n'
          'Этот бот поможет тебе удобно читать роман '
          'Ивана Гончарова "Обломов". Просто загружай книгу и '
          'получай её небольшими порциями, идеально подходящими '
          'для чтения без скролла.\n\n'
          'Чтобы увидеть список доступных команд, введи /help.',
    '/help': '<b>Добро пожаловать в бот-читалку!</b> 📚\n\n'
         'Вот список доступных команд:\n\n'
         '📖 <b>/beginning</b> — начать чтение с первой страницы\n'
         '➡️ <b>/continue</b> — продолжить с того места, где остановился\n'
         '🔖 <b>/bookmarks</b> — открыть список сохранённых закладок\n'
         'ℹ️ <b>/help</b> — справка по работе бота\n\n'
         'Чтобы сохранить закладку, просто нажми на кнопку с номером страницы.\n\n'
         '<b>Приятного чтения!</b> 😊',
    '/bookmarks': '<b>Ваши закладки:</b>\n\nЗдесь сохраняются страницы, '
              'на которых вы остановились. Выберите нужную, чтобы '
              'продолжить чтение! 📚',
    'edit_bookmarks': '<b>Управление закладками</b>\n\nВы можете удалить '
                  'ненужные. 📖',
    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'no_bookmarks': '📖 У вас пока нет закладок.\n\nЧтобы добавить страницу в '
                'закладки, просто нажмите на её номер во время чтения.\n\n'
                '▶️ /continue — продолжить чтение',
    'cancel_text': '/continue - продолжить чтение'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/beginning': '📚 В начало книги',
    '/continue': '📖 Продолжить чтение',
    '/bookmarks': '🔖 Мои закладки',
    '/help': '❓ Помощь и команды'
}