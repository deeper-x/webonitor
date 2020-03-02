from watchdog.events import LoggingEventHandler, PatternMatchingEventHandler
from watchdog.observers import Observer
import logging
from configuration import WATCHED_FILEXT


class Listen:
    """
    Manage directory listening
    """
    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M%S')

        self._event_handler = PatternMatchingEventHandler(patterns=WATCHED_FILEXT,
                                                          ignore_patterns='',
                                                          ignore_directories=True,
                                                          case_sensitive=False,
                                                         )

        self._observer = Observer()

    def __on_created(self, event) -> str:
        return logging.info(f'Created {event.src_path}')

    def __on_deleted(self, event) -> str:
        return logging.info(f'Deleted {event.src_path}')

    def __on_modified(self, event) -> str:
        return logging.info(f'Modified {event.src_path}')

    def __on_moved(self, event) -> str:
        return logging.info(f'Moved {event.src_path}')

    def observe(self, path: str, event: str) -> bool:
        """
        Watch directory content, responding on change
        :param path:str directory path to inspect
        :param event:str passed event [add, del, mod, cut]
        :return: None
        :raises: KeyboardInterrupt, on user interruption
        """
        logging.info(f'Listening for {event} event...')

        if event == 'add':
            self._event_handler.on_created = self.__on_created
        elif event == 'del':
            self._event_handler.on_deleted = self.__on_deleted
        elif event == 'mod':
            logging.warning(f'File {event} has no actions - NOOP')
        #    self._event_handler.on_modified = self.__on_modified
        elif event == 'cut':
            self._event_handler.on_moved = self.__on_moved
        else:
            logging.error(f'File {event} event is unhandled...')
            return False

        self._observer.schedule(self._event_handler, path, recursive=True)
        self._observer.start()

        try:
            self._observer.join()
            return True

        except KeyboardInterrupt:
            self._observer.stop()
            return False

