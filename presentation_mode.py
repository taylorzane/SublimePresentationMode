import sublime
import sublime_plugin

DEBUG = False

# TODO: Expand this list
settings = [
  'color_scheme',
  'font_face',
  'font_size',
  'theme'
]

class PresentationModeCommand(sublime_plugin.ApplicationCommand):
  def run(self):
    presentation_settings = sublime.load_settings("PresentationMode.sublime-settings")
    s = sublime.load_settings("Preferences.sublime-settings")

    if presentation_settings.get("in_presentation_mode"):
      return

    for setting in settings:
      presentation_settings.set("bak_" + setting, s.get(setting))

      if presentation_settings.has(setting):
        if DEBUG:
          print("====")
          print(setting)
          print(presentation_settings.get(setting))
          print(presentation_settings.get("bak_" + setting))
          print("====")
        s.set(setting, presentation_settings.get(setting))

    presentation_settings.set("in_presentation_mode", True)

    sublime.save_settings("PresentationMode.sublime-settings")
    sublime.save_settings("Preferences.sublime-settings")

class RevertPresentationModeCommand(sublime_plugin.ApplicationCommand):
  def run(self):
    presentation_settings = sublime.load_settings("PresentationMode.sublime-settings")
    s = sublime.load_settings("Preferences.sublime-settings")

    if not presentation_settings.get("in_presentation_mode"):
      return

    for setting in settings:
      if DEBUG:
        print("====")
        print(setting)
        print(presentation_settings.get(setting))
        print(presentation_settings.get("bak_" + setting))
        print("====")
      if presentation_settings.has("bak_" + setting):
        s.set(setting, presentation_settings.get("bak_" + setting))

    presentation_settings.set("in_presentation_mode", False)

    sublime.save_settings("PresentationMode.sublime-settings")
    sublime.save_settings("Preferences.sublime-settings")


class SaveCurrentCommand(sublime_plugin.ApplicationCommand):
  def run(self):
    presentation_settings = sublime.load_settings("PresentationMode.sublime-settings")
    s = sublime.load_settings("Preferences.sublime-settings")

    for setting in settings:
      if DEBUG:
        print("====")
        print(setting)
        print(presentation_settings.get(setting))
        print(s.get(setting))
        print("====")
      presentation_settings.set(setting, s.get(setting))

    sublime.save_settings("PresentationMode.sublime-settings")
    sublime.save_settings("Preferences.sublime-settings")
