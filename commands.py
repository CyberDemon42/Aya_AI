def fn():
    return {
        'увеличить громкость':'amixer set Master 5%+',
        'уменьшить громкость':'amixer set Master 5%-',
        'выключить звук':'amixer set Master mute',
        'включить звук':'amixer set Master unmute',
        'запусти гугл': 'flatpak run com.google.Chrome',
        'запусти терминал': 'neofetch',
        'запусти телеграм': 'flatpak run org.telegram.desktop',
        'запусти вс код':'flatpak run com.vscodium.codium',
        'инфо':'inxi'
    }

def allfn():
    return ['увеличить громкость', 'уменьшить громкость', 'выключить звук', 
            'включить звук', 'запусти гугл', 'запусти терминал', 'запусти телеграм']