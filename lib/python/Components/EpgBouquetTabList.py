from Components.Label import Label


class EpgBouquetTabList(Label):
	"""Optional horizontal strip of bouquet names for Grid EPG skins
	that define a 'guidebouquetlist' widget. Shows the current bouquet
	bracketed, followed by the bouquets after it. Inert (no-op) if the
	active skin doesn't define the widget, so this is safe to enable
	unconditionally in EPGSelectionGrid without requiring every skin
	to be updated.
	"""

	def __init__(self):
		Label.__init__(self, "")
		self.tabNames = []

	def setBouquets(self, names, currentIndex):
		self.tabNames = names
		self._render(currentIndex)

	def setSelected(self, index):
		self._render(index)

	def _render(self, currentIndex):
		if not self.tabNames:
			self.setText("")
			return
		ordered = self.tabNames[currentIndex:] + self.tabNames[:currentIndex]
		parts = []
		for i, name in enumerate(ordered):
			parts.append("[ %s ]" % name if i == 0 else name)
		self.setText("   |   ".join(parts))
