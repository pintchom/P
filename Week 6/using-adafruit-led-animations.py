import board, neopixel, time
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, \
    CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.sequence import AnimationSequence

colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE, WHITE, BLACK]

pixels_num_of_lights = 10
pixels = neopixel.NeoPixel(board.NEOPIXEL, pixels_num_of_lights, brightness=0.5)
strip_num_of_lights = 30
strip = neopixel.NeoPixel(board.A1, strip_num_of_lights, brightness=0.5)
pixels.fill(BLACK)
strip.fill(BLACK)

blink = Blink(pixels, speed=0.5, color=JADE)
blink_strip = Blink(strip, speed=0.5, color=AMBER)
colorcycle = ColorCycle(pixels, speed=0.1, colors=colors)
colorcycle_strip = ColorCycle(strip, speed=0.1, colors=colors)
chase = Chase(pixels, speed=0.1, color=WHITE, size=3, spacing=6)
chase_strip = Chase(strip, speed=0.1, color=WHITE, size=1, spacing=1)
comet = Comet(pixels, speed=0.1, color=RED, tail_length=10, bounce=True)
comet_strip = Comet(strip, speed=0.05, color=RED, tail_length=int(strip_num_of_lights/4), bounce=True)
pulse = Pulse(pixels, speed=0.05, color=AMBER, period=2)
pulse_strip = Pulse(strip, speed=0.05, color=BLUE, period=2)
sparkle = Sparkle(pixels, speed=0.05, color=PURPLE)
sparkle_strip = Sparkle(strip, speed=0.05, color=PURPLE)
sparklepulse = SparklePulse(pixels, speed=0.05, period=5, color=BLUE)
sparklepulse_strip = SparklePulse(strip, speed=0.05, period=5, color=BLUE)
rainbow = Rainbow(pixels, speed=0.05, period=2)
rainbow_strip = Rainbow(strip, speed=0.05, period=2)
rainbowchase = RainbowChase(pixels, speed=0.05, size=5, spacing=0, step=8)
rainbowchase_strip = RainbowChase(strip, speed=0.05, size=5, spacing=0, step=8)

animations = AnimationSequence(
    blink,
    colorcycle,
    chase,
    comet,
    pulse,
    sparkle,
    sparklepulse,
    rainbow,
    rainbowchase,
    advance_interval=5, auto_clear=True
)
animations_strip = AnimationSequence(
    blink_strip,
    colorcycle_strip,
    chase_strip,
    comet_strip,
    pulse_strip,
    sparkle_strip,
    sparklepulse_strip,
    rainbow_strip,
    rainbowchase_strip,
    advance_interval=5, auto_clear=True
)

print("Animation running")
while True:
    # blink.animate()
    # blink_strip.animate()
    # colorcycle.animate()
    # colorcycle_strip.animate()
    # chase.animate()
    # chase_strip.animate()
    # comet.animate()
    # comet_strip.animate()
    # pulse.animate()
    # pulse_strip.animate()
    # sparkle.animate()
    # sparkle_strip.animate()
    # sparklepulse.animate()
    # sparklepulse_strip.animate()
    # rainbow.animate()
    # rainbow_strip.animate()
    # rainbowchase.animate()
    # rainbowchase_strip.animate()
    animations.animate()
    animations_strip.animate()
