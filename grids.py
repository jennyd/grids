#!/usr/bin/python

import sys, pygame
from optparse import OptionParser

parser = OptionParser(conflict_handler="resolve")
parser.add_option("-b", "--bar", type="int", default=20, dest="bar_width",
                  help="width of bars, in pixels [default=%default]")
parser.add_option("-g", "--gap", type="int", default=100, dest="gap_width",
                  help="width of gap between bars, in pixels [default=%default]")
parser.add_option("-t", "--time", type="float", default=2, dest="seconds_between_bars",
                  help="time between appearance of new bars, in seconds [default=%default]")
parser.add_option("-w", "--window-width", type="int", default=640, dest="width",
                  help="width of window, in pixels [default=%default]")
parser.add_option("-h", "--window-height", type="int", default=480, dest="height",
                  help="height of window, in pixels [default=%default]")
parser.add_option("-f", "--fullscreen", action="store_true", default=False, dest="fullscreen",
                  help="make window fullscreen (ESC to exit) [default=%default]")
(options, args) = parser.parse_args()

black = 0, 0, 0
green = 0, 255, 0

pygame.init()

window_size = width, height = options.width, options.height
flags = 0
fullscreen = options.fullscreen
if fullscreen:
    window_size = 0, 0
    flags = (pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
screen = pygame.display.set_mode(window_size, flags)
if fullscreen:
    window_size = width, height = screen.get_width(), screen.get_height()
    pygame.mouse.set_visible(False)

gap_width = options.gap_width
bar_width = options.bar_width
combined_width = gap_width + bar_width
seconds_between_bars = options.seconds_between_bars
ms_between_bars = 1000 * seconds_between_bars

x = -bar_width

start_t = pygame.time.get_ticks()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
    screen.fill(black)
    current_t = pygame.time.get_ticks()
    proportion_along = (current_t % ms_between_bars) / float(ms_between_bars)
    x = proportion_along * combined_width - bar_width
    start_x = x
    while start_x < width:
        r = pygame.Rect(start_x, 0, bar_width, height)
        screen.fill(green, r)
        start_x += combined_width
    pygame.display.flip()

