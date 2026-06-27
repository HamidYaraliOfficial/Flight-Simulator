import sys, math, time, random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# ═══════════════════════════════════════════════════════════════
#  THEMES
# ═══════════════════════════════════════════════════════════════
THEMES = {
    "dark": {
        "bg": "#0a0a1a", "bg2": "#0f0f2e", "bg3": "#1a1a3e",
        "card": "#1e1e4a", "card2": "#252560",
        "acc": "#00d4ff", "acc2": "#7b2fff",
        "text": "#e8e8ff", "text2": "#a0a0cc",
        "border": "#3a3a7a", "danger": "#ff4444",
        "success": "#44ff88", "warn": "#ffaa00",
        "sky_top": "#000510", "sky_mid": "#001030", "sky_bot": "#002060",
        "ground": "#1a3a1a", "ground2": "#0f2a0f",
    },
    "light": {
        "bg": "#e8f0ff", "bg2": "#d0e0ff", "bg3": "#c0d0f0",
        "card": "#ffffff", "card2": "#f0f4ff",
        "acc": "#0066cc", "acc2": "#6600cc",
        "text": "#111133", "text2": "#334466",
        "border": "#99aacc", "danger": "#cc2200",
        "success": "#006633", "warn": "#cc7700",
        "sky_top": "#87ceeb", "sky_mid": "#b0d8f0", "sky_bot": "#d8eeff",
        "ground": "#4a7a3a", "ground2": "#3a6a2a",
    },
}

# ═══════════════════════════════════════════════════════════════
#  TRANSLATIONS
# ═══════════════════════════════════════════════════════════════
TR = {
    "en": {
        "title": "Flight Simulator", "play": "FLY NOW", "settings": "Settings",
        "quit": "Quit", "back": "Back", "theme": "Theme", "lang": "Language",
        "dark": "Dark", "light": "Light", "choose_plane": "Choose Aircraft",
        "choose_map": "Choose Map", "choose_weather": "Weather",
        "start_flight": "Start Flight", "altitude": "ALT", "speed": "SPD",
        "heading": "HDG", "vspeed": "V/S", "throttle": "THR", "fuel": "FUEL",
        "pause": "PAUSE", "resume": "Resume", "restart": "Restart",
        "main_menu": "Main Menu", "paused": "PAUSED", "game_over": "CRASHED",
        "landed": "LANDED!", "score": "Score", "time": "Time",
        "controls": "Controls: WASD/Arrows = Pitch/Roll | Q/E = Yaw | Z/X = Throttle",
        "fps": "FPS", "wind": "WIND", "stall": "STALL WARNING",
        "overspeed": "OVERSPEED", "low_fuel": "LOW FUEL",
        "clouds": "Clouds", "turbulence": "Turbulence",
        "p1": "F-16 Falcon", "p2": "Boeing 747", "p3": "Cessna 172", "p4": "Concorde",
        "m1": "Clear Sky", "m2": "Stormy", "m3": "Mountain", "m4": "Ocean",
        "w1": "Clear", "w2": "Cloudy", "w3": "Storm", "w4": "Fog",
    },
    "fa": {
        "title": "شبیه‌ساز پرواز", "play": "پرواز کن", "settings": "تنظیمات",
        "quit": "خروج", "back": "برگشت", "theme": "تم", "lang": "زبان",
        "dark": "تاریک", "light": "روشن", "choose_plane": "انتخاب هواپیما",
        "choose_map": "انتخاب نقشه", "choose_weather": "آب‌وهوا",
        "start_flight": "شروع پرواز", "altitude": "ارتفاع", "speed": "سرعت",
        "heading": "جهت", "vspeed": "سرعت عمودی", "throttle": "گاز", "fuel": "سوخت",
        "pause": "توقف", "resume": "ادامه", "restart": "شروع مجدد",
        "main_menu": "منوی اصلی", "paused": "متوقف", "game_over": "سقوط!",
        "landed": "فرود موفق!", "score": "امتیاز", "time": "زمان",
        "controls": "کنترل: WASD = پیچ/رول | Q/E = یاو | Z/X = گاز",
        "fps": "FPS", "wind": "باد", "stall": "خطر استال", "overspeed": "سرعت زیاد",
        "low_fuel": "سوخت کم", "clouds": "ابر", "turbulence": "تلاطم",
        "p1": "اف-16 فالکون", "p2": "بوئینگ 747", "p3": "سسنا 172", "p4": "کنکورد",
        "m1": "آسمان صاف", "m2": "طوفانی", "m3": "کوهستان", "m4": "اقیانوس",
        "w1": "صاف", "w2": "ابری", "w3": "طوفان", "w4": "مه",
    },
    "zh": {
        "title": "飞行模拟器", "play": "立即飞行", "settings": "设置",
        "quit": "退出", "back": "返回", "theme": "主题", "lang": "语言",
        "dark": "暗色", "light": "亮色", "choose_plane": "选择飞机",
        "choose_map": "选择地图", "choose_weather": "天气",
        "start_flight": "开始飞行", "altitude": "高度", "speed": "速度",
        "heading": "航向", "vspeed": "垂直速度", "throttle": "油门", "fuel": "燃油",
        "pause": "暂停", "resume": "继续", "restart": "重新开始",
        "main_menu": "主菜单", "paused": "已暂停", "game_over": "坠机!",
        "landed": "成功着陆!", "score": "分数", "time": "时间",
        "controls": "控制: WASD=俯仰/滚转 | Q/E=偏航 | Z/X=油门",
        "fps": "帧率", "wind": "风", "stall": "失速警告", "overspeed": "超速",
        "low_fuel": "燃油不足", "clouds": "云", "turbulence": "颠簸",
        "p1": "F-16战隼", "p2": "波音747", "p3": "塞斯纳172", "p4": "协和式",
        "m1": "晴空", "m2": "暴风雨", "m3": "山地", "m4": "海洋",
        "w1": "晴朗", "w2": "多云", "w3": "风暴", "w4": "雾",
    },
}

PLANES = {
    "f16":    {"icon": "✈", "key": "p1", "speed": 9, "accel": 0.7, "turn": 3.5, "fuel_rate": 0.8, "color": "#4488ff"},
    "b747":   {"icon": "🛫", "key": "p2", "speed": 5, "accel": 0.3, "turn": 1.5, "fuel_rate": 0.4, "color": "#ffffff"},
    "c172":   {"icon": "🛩", "key": "p3", "speed": 3, "accel": 0.5, "turn": 2.5, "fuel_rate": 0.2, "color": "#ffcc44"},
    "concorde": {"icon": "✈", "key": "p4", "speed": 12, "accel": 0.6, "turn": 2.0, "fuel_rate": 1.2, "color": "#cccccc"},
}

MAPS = {
    "clear":    {"key": "m1", "icon": "☀️", "turbulence": 0.1, "vis": 1.0},
    "stormy":   {"key": "m2", "icon": "⛈️", "turbulence": 0.8, "vis": 0.5},
    "mountain": {"key": "m3", "icon": "🏔️", "turbulence": 0.3, "vis": 0.9},
    "ocean":    {"key": "m4", "icon": "🌊", "turbulence": 0.2, "vis": 0.95},
}

WEATHERS = {
    "clear":  {"key": "w1", "icon": "☀️", "wind": 0.1, "vis": 1.0},
    "cloudy": {"key": "w2", "icon": "⛅", "wind": 0.3, "vis": 0.7},
    "storm":  {"key": "w3", "icon": "⛈️", "wind": 0.9, "vis": 0.3},
    "fog":    {"key": "w4", "icon": "🌫️", "wind": 0.1, "vis": 0.2},
}

# ═══════════════════════════════════════════════════════════════
#  FLIGHT PHYSICS
# ═══════════════════════════════════════════════════════════════
class FlightPhysics:
    def __init__(self, plane_data, map_data, weather_data):
        p = plane_data
        self.max_speed    = p["speed"] * 80
        self.accel_factor = p["accel"]
        self.turn_rate    = p["turn"]
        self.fuel_rate    = p["fuel_rate"]
        self.turbulence   = map_data["turbulence"] + weather_data["wind"] * 0.5
        self.wind_x       = (random.random() - 0.5) * weather_data["wind"] * 20
        self.wind_z       = (random.random() - 0.5) * weather_data["wind"] * 20
        self.vis          = min(map_data["vis"], weather_data["vis"])

        self.x   = 0.0;   self.y   = 500.0;  self.z   = 0.0
        self.vx  = 0.0;   self.vy  = 0.0;    self.vz  = 80.0
        self.pitch = 0.0; self.roll  = 0.0;  self.yaw = 0.0
        self.throttle = 0.5
        self.speed    = 80.0
        self.fuel     = 100.0
        self.score    = 0
        self.elapsed  = 0.0
        self.alive    = True
        self.landed   = False
        self.stall    = False
        self.overspeed= False

        self._pitch_input = 0.0
        self._roll_input  = 0.0
        self._yaw_input   = 0.0

    def set_input(self, pitch, roll, yaw, thr_delta):
        self._pitch_input = pitch
        self._roll_input  = roll
        self._yaw_input   = yaw
        self.throttle = max(0.0, min(1.0, self.throttle + thr_delta * 0.02))

    def update(self, dt):
        if not self.alive or self.landed:
            return
        self.elapsed += dt
        tr = self.turn_rate * dt * 60

        # Turbulence
        turb = self.turbulence
        self._pitch_input += (random.random() - 0.5) * turb * 0.4
        self._roll_input  += (random.random() - 0.5) * turb * 0.4

        self.pitch = max(-85, min(85, self.pitch + self._pitch_input * tr * 1.2))
        self.roll  = max(-80, min(80, self.roll  + self._roll_input  * tr))
        self.yaw   = (self.yaw + self._yaw_input * tr * 0.8) % 360

        # Heading from yaw
        yaw_r   = math.radians(self.yaw)
        pitch_r = math.radians(self.pitch)
        roll_r  = math.radians(self.roll)

        # Lift & thrust
        self.speed = max(0, min(self.max_speed,
            self.speed + (self.throttle * self.accel_factor * 60 - 15) * dt))
        lift = self.speed * 0.012 * math.cos(pitch_r)
        gravity = 9.8

        self.stall     = self.speed < 40
        self.overspeed = self.speed > self.max_speed * 0.95

        if self.stall:
            lift *= 0.1
            gravity *= 1.5

        # Velocity
        forward_x =  math.sin(yaw_r) * math.cos(pitch_r)
        forward_y =  math.sin(pitch_r)
        forward_z =  math.cos(yaw_r) * math.cos(pitch_r)

        self.vx = forward_x * self.speed + self.wind_x
        self.vy = forward_y * self.speed + (lift - gravity) * dt * 8
        self.vz = forward_z * self.speed + self.wind_z

        self.x += self.vx * dt
        self.y += self.vy * dt
        self.z += self.vz * dt

        # Fuel
        self.fuel = max(0.0, self.fuel - self.fuel_rate * self.throttle * dt * 0.5)
        if self.fuel <= 0:
            self.throttle = 0

        # Ground collision
        if self.y <= 0:
            if self.speed < 60 and abs(self.pitch) < 10:
                self.landed = True
                self.score += 1000
            else:
                self.alive = False
            self.y = 0

        # Score
        self.score += int(self.speed * dt * 0.1)

# ═══════════════════════════════════════════════════════════════
#  3-D RENDERER  (pseudo-3D cockpit view)
# ═══════════════════════════════════════════════════════════════
class FlightRenderer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.physics: FlightPhysics | None = None
        self.theme = "dark"
        self._clouds   = [self._rand_cloud() for _ in range(40)]
        self._stars    = [(random.random(), random.random()) for _ in range(200)]
        self._mountains= [self._rand_mountain() for _ in range(18)]
        self._buildings= [self._rand_building() for _ in range(30)]
        self._t = 0.0

    def _rand_cloud(self):
        return {"x": random.uniform(-8000, 8000),
                "y": random.uniform(300, 2500),
                "z": random.uniform(200, 6000),
                "r": random.uniform(150, 500),
                "op": random.uniform(0.4, 0.9)}

    def _rand_mountain(self):
        return {"x": random.uniform(-5000, 5000),
                "h": random.uniform(400, 1800),
                "z": random.uniform(1000, 8000),
                "w": random.uniform(600, 2000)}

    def _rand_building(self):
        return {"x": random.uniform(-2000, 2000),
                "h": random.uniform(50, 400),
                "z": random.uniform(200, 3000),
                "w": random.uniform(40, 120)}

    def set_physics(self, ph):
        self.physics = ph

    def set_theme(self, t):
        self.theme = t
        self.update()

    def tick(self, t):
        self._t = t
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        W, H = self.width(), self.height()
        th = THEMES[self.theme]

        if self.physics:
            self._draw_world(p, W, H, th)
            self._draw_cockpit(p, W, H, th)
        else:
            p.fillRect(0, 0, W, H, QColor(th["bg"]))

        p.end()

    def _horizon_y(self, W, H):
        ph = self.physics
        pitch_offset = ph.pitch / 90.0 * H * 0.6
        return H * 0.45 + pitch_offset

    def _draw_world(self, p, W, H, th):
        ph = self.physics
        hy = self._horizon_y(W, H)
        vis = 1.0

        # ── Sky gradient ──
        sky_grad = QLinearGradient(0, 0, 0, max(hy, 1))
        alt_fac = min(1.0, ph.y / 8000.0)
        if self.theme == "dark":
            sky_grad.setColorAt(0, QColor(0, 2, 20))
            sky_grad.setColorAt(0.5, QColor(0, int(10 + 40 * alt_fac), int(60 + 60 * alt_fac)))
            sky_grad.setColorAt(1, QColor(int(20 * (1-alt_fac)), int(60 * (1-alt_fac)), int(120 * (1-alt_fac))))
        else:
            sky_grad.setColorAt(0, QColor(20, 80, 180))
            sky_grad.setColorAt(0.6, QColor(100, 170, 240))
            sky_grad.setColorAt(1, QColor(180, 220, 255))
        p.fillRect(0, 0, W, int(hy) + 2, QBrush(sky_grad))

        # ── Stars (night/dark) ──
        if self.theme == "dark" and ph.y > 500:
            p.setPen(QColor(255, 255, 255, int(min(180, ph.y / 20))))
            for sx, sy in self._stars:
                p.drawPoint(int(sx * W), int(sy * hy * 0.9))

        # ── Sun / Moon ──
        self._draw_sun(p, W, H, hy, th)

        # ── Mountains ──
        self._draw_mountains(p, W, H, hy, th, ph)

        # ── Ground ──
        if hy < H:
            gnd_grad = QLinearGradient(0, hy, 0, H)
            if self.theme == "dark":
                gnd_grad.setColorAt(0, QColor(15, 50, 15))
                gnd_grad.setColorAt(0.3, QColor(10, 35, 10))
                gnd_grad.setColorAt(1, QColor(5, 20, 5))
            else:
                gnd_grad.setColorAt(0, QColor(80, 160, 60))
                gnd_grad.setColorAt(0.3, QColor(60, 130, 40))
                gnd_grad.setColorAt(1, QColor(40, 100, 25))
            p.fillRect(0, int(hy), W, H - int(hy), QBrush(gnd_grad))

            # Grid lines on ground
            self._draw_ground_grid(p, W, H, hy, th, ph)

        # ── Buildings ──
        self._draw_buildings(p, W, H, hy, th, ph)

        # ── Clouds ──
        self._draw_clouds(p, W, H, hy, th, ph)

        # ── Roll indicator (horizon tilt) ──
        self._draw_roll_overlay(p, W, H, th, ph)

    def _draw_sun(self, p, W, H, hy, th):
        t = self._t * 0.01
        sx = int(W * (0.5 + 0.3 * math.sin(t)))
        sy = int(hy * 0.3)
        if self.theme == "dark":
            # Moon
            p.setBrush(QColor(220, 220, 240, 200))
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(sx - 18, sy - 18, 36, 36)
            p.setBrush(QColor(10, 10, 30, 180))
            p.drawEllipse(sx - 10, sy - 20, 32, 32)
        else:
            # Sun glow
            for r, a in [(60, 30), (45, 60), (30, 120), (18, 255)]:
                c = QColor(255, 240, 100, a)
                p.setBrush(c); p.setPen(Qt.PenStyle.NoPen)
                p.drawEllipse(sx - r, sy - r, r * 2, r * 2)

    def _draw_mountains(self, p, W, H, hy, th, ph):
        p.setPen(Qt.PenStyle.NoPen)
        for m in self._mountains:
            rel_z = m["z"] - ph.z * 0.001
            if rel_z < 100: continue
            scale = 600.0 / rel_z
            cx = int(W/2 + (m["x"] - ph.x * 0.01) * scale)
            mh = int(m["h"] * scale * 0.8)
            mw = int(m["w"] * scale)
            if cx + mw < 0 or cx - mw > W: continue
            base_y = int(hy)
            tip_y  = base_y - mh
            if tip_y >= H: continue

            fog = max(0, min(200, int(rel_z / 40)))
            if self.theme == "dark":
                rc, gc, bc = 40, 60, 50
            else:
                rc, gc, bc = 100, 130, 110

            poly = QPolygon([
                QPoint(cx - mw, base_y),
                QPoint(cx, tip_y),
                QPoint(cx + mw, base_y),
            ])
            p.setBrush(QColor(rc, gc, bc, 255 - fog))
            p.drawPolygon(poly)

            # Snow cap
            if m["h"] > 800:
                snow_h = int(mh * 0.25)
                sp = QPolygon([
                    QPoint(cx - int(mw * 0.25), tip_y + snow_h),
                    QPoint(cx, tip_y),
                    QPoint(cx + int(mw * 0.25), tip_y + snow_h),
                ])
                p.setBrush(QColor(240, 245, 255, 200))
                p.drawPolygon(sp)

    def _draw_ground_grid(self, p, W, H, hy, th, ph):
        pen = QPen(QColor(0, 180, 0, 60) if self.theme == "dark" else QColor(0, 100, 0, 40))
        pen.setWidth(1)
        p.setPen(pen)
        # Perspective grid
        vp_x = W // 2
        vp_y = int(hy)
        step = 80
        for i in range(1, 16):
            y = vp_y + i * step
            if y > H: break
            fac = i / 15.0
            x0 = int(vp_x - fac * W * 0.9)
            x1 = int(vp_x + fac * W * 0.9)
            p.drawLine(x0, y, x1, y)
        for col in range(-8, 9):
            p.drawLine(vp_x, vp_y, vp_x + col * W // 8, H)

    def _draw_buildings(self, p, W, H, hy, th, ph):
        p.setPen(Qt.PenStyle.NoPen)
        for b in self._buildings:
            rel_z = b["z"] - ph.z * 0.001
            if rel_z < 50 or rel_z > 3000: continue
            scale = 400.0 / rel_z
            cx = int(W/2 + (b["x"] - ph.x * 0.01) * scale)
            bh = int(b["h"] * scale)
            bw = int(b["w"] * scale)
            if bw < 2: continue
            base_y = int(hy)
            top_y  = base_y - bh
            if cx + bw < 0 or cx - bw > W: continue

            fog = max(0, min(220, int(rel_z / 12)))
            if self.theme == "dark":
                p.setBrush(QColor(30, 30, 60, 255 - fog))
                p.drawRect(cx - bw//2, top_y, bw, bh)
                # Windows
                if bw > 6 and bh > 8:
                    p.setBrush(QColor(255, 240, 100, max(0, 160 - fog)))
                    ws = max(2, bw // 4)
                    for wy in range(top_y + 3, base_y - 3, max(4, bh//6)):
                        for wx in range(cx - bw//2 + 2, cx + bw//2 - 2, ws + 2):
                            if random.random() < 0.6:
                                p.drawRect(wx, wy, max(1, ws-1), max(1, ws-1))
            else:
                p.setBrush(QColor(160, 160, 200, 255 - fog))
                p.drawRect(cx - bw//2, top_y, bw, bh)
                p.setBrush(QColor(100, 180, 220, max(0, 120 - fog)))
                if bw > 4:
                    ws = max(2, bw // 4)
                    for wy in range(top_y + 2, base_y - 2, max(4, bh//5)):
                        for wx in range(cx - bw//2 + 2, cx + bw//2 - 2, ws + 2):
                            p.drawRect(wx, wy, max(1, ws-1), max(1, ws-1))

    def _draw_clouds(self, p, W, H, hy, th, ph):
        for c in self._clouds:
            rel_z = c["z"] - ph.z * 0.001
            if rel_z < 100 or rel_z > 8000: continue
            scale = 800.0 / rel_z
            cx = int(W/2 + (c["x"] - ph.x * 0.005) * scale)
            cy_world = c["y"] - ph.y
            cy = int(hy - cy_world * scale * 0.5)
            cr = int(c["r"] * scale)
            if cr < 4 or cy > H or cy < -cr: continue
            if cx + cr < 0 or cx - cr > W: continue

            alpha = int(c["op"] * 200)
            fog   = max(0, min(160, int(rel_z / 40)))
            alpha = max(0, alpha - fog)
            col   = QColor(240, 245, 255, alpha) if self.theme == "light" else QColor(180, 190, 210, alpha)
            p.setBrush(col)
            p.setPen(Qt.PenStyle.NoPen)
            for ox, oy, rs in [(0,0,1.0),(-cr//2, cr//5, 0.7),(cr//2, cr//5, 0.7),(0,-cr//3, 0.6)]:
                r2 = int(cr * rs)
                p.drawEllipse(cx + ox - r2, cy + oy - r2, r2*2, r2*2)

    def _draw_roll_overlay(self, p, W, H, th, ph):
        """Tilts the artificial horizon line according to roll"""
        cx, cy = W//2, H//2
        roll_r = math.radians(ph.roll)
        L = min(W, H) // 3
        dx = int(math.cos(roll_r) * L)
        dy = int(math.sin(roll_r) * L)
        pen = QPen(QColor(0, 255, 100, 120), 2, Qt.PenStyle.DashLine)
        p.setPen(pen)
        p.drawLine(cx - dx, cy - dy, cx + dx, cy + dy)

    def _draw_cockpit(self, p, W, H, th):
        """Draw cockpit frame overlay"""
        ph = self.physics
        # Vignette
        grad = QRadialGradient(W/2, H/2, max(W, H)*0.7)
        grad.setColorAt(0.6, QColor(0, 0, 0, 0))
        grad.setColorAt(1.0, QColor(0, 0, 0, 160))
        p.fillRect(0, 0, W, H, QBrush(grad))

        # Cockpit border
        fw = int(W * 0.06)
        fh = int(H * 0.08)
        pen = QPen(QColor(40, 40, 40, 220), 3)
        p.setPen(pen)
        p.setBrush(QColor(20, 20, 20, 200))
        # Top bar
        p.drawRect(0, 0, W, fh)
        # Bottom bar
        p.drawRect(0, H - fh, W, fh)
        # Left pillar
        p.drawRect(0, 0, fw, H)
        # Right pillar
        p.drawRect(W - fw, 0, fw, H)

        # Nose indicator
        pen2 = QPen(QColor(0, 255, 120, 180), 2)
        p.setPen(pen2)
        p.setBrush(Qt.BrushStyle.NoBrush)
        mid_x, mid_y = W//2, H//2
        p.drawLine(mid_x - 40, mid_y, mid_x - 10, mid_y)
        p.drawLine(mid_x + 10, mid_y, mid_x + 40, mid_y)
        p.drawLine(mid_x, mid_y - 15, mid_x, mid_y - 5)
        p.drawEllipse(mid_x - 4, mid_y - 4, 8, 8)

        # Stall / overspeed warning flash
        if ph.stall and int(self._t * 4) % 2 == 0:
            p.fillRect(0, 0, W, H, QColor(255, 50, 0, 60))
        if ph.overspeed and int(self._t * 4) % 2 == 0:
            p.fillRect(0, 0, W, H, QColor(255, 200, 0, 40))


# ═══════════════════════════════════════════════════════════════
#  HUD WIDGET
# ═══════════════════════════════════════════════════════════════
class HUDWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.physics: FlightPhysics | None = None
        self.theme = "dark"
        self.lang  = "en"
        self._fps  = 0.0
        self._fps_buf = []
        self._last_t  = time.time()
        self.setStyleSheet("background: transparent;")

    def set_physics(self, ph): self.physics = ph
    def set_theme(self, t):    self.theme = t; self.update()
    def set_lang(self, l):     self.lang  = l; self.update()

    def tick(self):
        now = time.time()
        dt  = now - self._last_t
        self._last_t = now
        if dt > 0:
            self._fps_buf.append(1.0/dt)
            if len(self._fps_buf) > 30: self._fps_buf.pop(0)
            self._fps = sum(self._fps_buf)/len(self._fps_buf)
        self.update()

    def paintEvent(self, e):
        if not self.physics: return
        p   = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        W, H = self.width(), self.height()
        ph  = self.physics
        th  = THEMES[self.theme]
        tr  = TR[self.lang]
        acc = QColor(th["acc"])
        txt = QColor(th["text"])

        # ── PFD (Primary Flight Display) top-left ──
        self._draw_pfd(p, W, H, ph, th, tr, acc, txt)
        # ── Engine / fuel top-right ──
        self._draw_engine_panel(p, W, H, ph, th, tr, acc, txt)
        # ── Compass bottom-center ──
        self._draw_compass(p, W, H, ph, th, tr, acc, txt)
        # ── Warnings ──
        self._draw_warnings(p, W, H, ph, th, tr)
        # ── FPS ──
        p.setFont(QFont("Consolas", 9))
        p.setPen(QColor(100, 255, 100, 140))
        p.drawText(W - 80, H - 10, f"{tr['fps']}: {self._fps:.0f}")
        p.end()

    def _gauge_rect(self, x, y, w, h):
        return QRect(x, y, w, h)

    def _draw_pfd(self, p, W, H, ph, th, tr, acc, txt):
        scale = min(W, H) / 800
        px, py = int(10 * scale + 40), int(10 * scale + 40)
        bw, bh = int(180 * scale), int(220 * scale)

        # Background panel
        panel = QRect(px, py, bw, bh)
        p.setBrush(QColor(0, 0, 0, 160))
        p.setPen(QPen(acc, 1))
        p.drawRoundedRect(panel, 8, 8)

        font_s = max(8, int(11 * scale))
        font_v = max(9, int(13 * scale))
        p.setFont(QFont("Consolas", font_s))

        items = [
            (tr["altitude"], f"{ph.y:.0f} m"),
            (tr["speed"],    f"{ph.speed:.0f} km/h"),
            (tr["vspeed"],   f"{ph.vy:+.1f} m/s"),
            (tr["heading"],  f"{ph.yaw:.0f}°"),
            (tr["pitch"],    f"{ph.pitch:.1f}°") if "pitch" in tr else ("Pitch", f"{ph.pitch:.1f}°"),
            (tr["roll"],     f"{ph.roll:.1f}°") if "roll" in tr else ("Roll", f"{ph.roll:.1f}°"),
            (tr["throttle"], f"{ph.throttle*100:.0f}%"),
        ]
        # fall back if keys missing
        items = [
            (tr.get("altitude","ALT"),  f"{ph.y:.0f} m"),
            (tr.get("speed","SPD"),     f"{ph.speed:.0f} km/h"),
            (tr.get("vspeed","V/S"),    f"{ph.vy:+.1f} m/s"),
            (tr.get("heading","HDG"),   f"{ph.yaw:.0f}°"),
            ("Pitch",                   f"{ph.pitch:.1f}°"),
            ("Roll",                    f"{ph.roll:.1f}°"),
            (tr.get("throttle","THR"),  f"{ph.throttle*100:.0f}%"),
        ]

        row_h = bh // (len(items) + 1)
        for i, (label, val) in enumerate(items):
            y_pos = py + row_h * (i + 1) - row_h // 2
            p.setPen(QColor(th["text2"]))
            p.drawText(px + 8, y_pos, label)
            # Color value by criticality
            if label in (tr.get("vspeed","V/S"),) and ph.vy < -15:
                vc = QColor(255, 80, 80)
            elif label == tr.get("throttle","THR") and ph.throttle < 0.1:
                vc = QColor(255, 160, 0)
            else:
                vc = acc
            p.setPen(vc)
            p.setFont(QFont("Consolas", font_v, QFont.Weight.Bold))
            p.drawText(px + bw - int(85 * scale), y_pos, val)
            p.setFont(QFont("Consolas", font_s))

        # Throttle bar
        bar_y = py + bh - int(18 * scale)
        bar_w = int((bw - 16) * ph.throttle)
        p.setBrush(QColor(0, 200, 100, 180))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRoundedRect(px + 8, bar_y, bar_w, int(10 * scale), 3, 3)
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.setPen(QPen(acc, 1))
        p.drawRoundedRect(px + 8, bar_y, bw - 16, int(10 * scale), 3, 3)

    def _draw_engine_panel(self, p, W, H, ph, th, tr, acc, txt):
        scale = min(W, H) / 800
        bw, bh = int(140 * scale), int(80 * scale)
        px = W - bw - int(50 * scale)
        py = int(50 * scale)

        p.setBrush(QColor(0, 0, 0, 160))
        p.setPen(QPen(acc, 1))
        p.drawRoundedRect(px, py, bw, bh, 8, 8)

        # Fuel gauge
        fuel_label = tr.get("fuel", "FUEL")
        p.setFont(QFont("Consolas", max(8, int(10 * scale))))
        p.setPen(QColor(th["text2"]))
        p.drawText(px + 8, py + int(20 * scale), fuel_label)

        fw = int((bw - 16) * ph.fuel / 100.0)
        fc = QColor(255, 80, 80) if ph.fuel < 20 else QColor(255, 200, 0) if ph.fuel < 50 else QColor(0, 220, 100)
        p.setBrush(fc)
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRoundedRect(px + 8, py + int(28 * scale), fw, int(12 * scale), 3, 3)
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.setPen(QPen(acc, 1))
        p.drawRoundedRect(px + 8, py + int(28 * scale), bw - 16, int(12 * scale), 3, 3)

        p.setPen(fc)
        p.setFont(QFont("Consolas", max(9, int(11 * scale)), QFont.Weight.Bold))
        p.drawText(px + 8, py + int(58 * scale), f"{ph.fuel:.0f}%")

        # Score & time
        score_y = py + bh + int(10 * scale)
        p.setBrush(QColor(0, 0, 0, 140))
        p.setPen(QPen(acc, 1))
        p.drawRoundedRect(px, score_y, bw, int(55 * scale), 6, 6)
        p.setFont(QFont("Consolas", max(8, int(10 * scale))))
        p.setPen(txt)
        p.drawText(px + 8, score_y + int(18 * scale), f"{tr.get('score','Score')}: {ph.score}")
        p.drawText(px + 8, score_y + int(36 * scale), f"{tr.get('time','Time')}: {ph.elapsed:.0f}s")

    def _draw_compass(self, p, W, H, ph, th, tr, acc, txt):
        scale = min(W, H) / 800
        cr    = int(50 * scale)
        cx    = W // 2
        cy    = H - cr - int(30 * scale)

        p.setBrush(QColor(0, 0, 0, 160))
        p.setPen(QPen(acc, 2))
        p.drawEllipse(cx - cr, cy - cr, cr * 2, cr * 2)

        # Compass ticks
        p.setFont(QFont("Consolas", max(7, int(8 * scale))))
        for deg, lbl in [(0,"N"),(90,"E"),(180,"S"),(270,"W")]:
            angle_r = math.radians(deg - ph.yaw - 90)
            tx = cx + int(math.cos(angle_r) * cr * 0.75)
            ty = cy + int(math.sin(angle_r) * cr * 0.75)
            p.setPen(QColor(255, 220, 100) if lbl == "N" else txt)
            p.drawText(tx - 5, ty + 5, lbl)

        # Heading arrow
        ha = math.radians(-90)
        p.setPen(QPen(QColor(0, 255, 120), 2))
        p.drawLine(cx, cy,
                   cx + int(math.cos(ha) * cr * 0.85),
                   cy + int(math.sin(ha) * cr * 0.85))

        # Heading value
        p.setFont(QFont("Consolas", max(8, int(10 * scale)), QFont.Weight.Bold))
        p.setPen(acc)
        p.drawText(cx - 18, cy + cr + int(14 * scale), f"{ph.yaw:.0f}°")

    def _draw_warnings(self, p, W, H, ph, th, tr):
        warnings = []
        if ph.stall:     warnings.append((tr.get("stall","STALL"), "#ff4444"))
        if ph.overspeed: warnings.append((tr.get("overspeed","OVERSPEED"), "#ffaa00"))
        if ph.fuel < 20: warnings.append((tr.get("low_fuel","LOW FUEL"), "#ff8800"))

        scale = min(W, H) / 800
        for i, (msg, color) in enumerate(warnings):
            if int(time.time() * 3) % 2 == 0:
                p.setFont(QFont("Consolas", max(12, int(16 * scale)), QFont.Weight.Bold))
                p.setPen(QColor(color))
                fm   = p.fontMetrics()
                tw   = fm.horizontalAdvance(msg)
                p.drawText(W//2 - tw//2, H//2 - int(40 * scale) + i * int(30 * scale), msg)


# ═══════════════════════════════════════════════════════════════
#  GAME PAGE
# ═══════════════════════════════════════════════════════════════
class GamePage(QWidget):
    sig_back = pyqtSignal()

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang  = lang
        self._physics: FlightPhysics | None = None
        self._paused  = False
        self._keys    = set()
        self._timer   = QTimer(self)
        self._timer.setInterval(16)
        self._timer.timeout.connect(self._tick)
        self._t = 0
        self._build()

    def _build(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Renderer (background)
        self._renderer = FlightRenderer(self)
        self._renderer.set_theme(self.theme)
        layout.addWidget(self._renderer, 1)

        # HUD (overlay)
        self._hud = HUDWidget(self._renderer)
        self._hud.set_theme(self.theme)
        self._hud.set_lang(self.lang)
        self._hud.setGeometry(self._renderer.rect())

        # Pause overlay
        self._pause_overlay = self._build_pause_overlay()
        self._pause_overlay.hide()

        # Game over overlay
        self._over_overlay = self._build_over_overlay()
        self._over_overlay.hide()

        # Controls hint
        tr = TR[self.lang]
        hint = QLabel(tr.get("controls", "WASD/Arrows=Pitch/Roll Q/E=Yaw Z/X=Throttle"), self)
        hint.setStyleSheet(f"color: {THEMES[self.theme]['text2']}; font-size: 10px; background: transparent;")
        hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(hint)

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def _build_pause_overlay(self):
        ov = QWidget(self)
        ov.setStyleSheet("background: rgba(0,0,0,160);")
        vl = QVBoxLayout(ov)
        vl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tr = TR[self.lang]
        th = THEMES[self.theme]

        lbl = QLabel(tr.get("paused","PAUSED"))
        lbl.setStyleSheet(f"color: {th['acc']}; font-size: 36px; font-weight: bold; background: transparent;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vl.addWidget(lbl)
        vl.addSpacing(20)

        for key, slot in [("resume", self._resume), ("restart", self._restart), ("main_menu", self._go_menu)]:
            btn = QPushButton(tr.get(key, key.replace("_"," ").title()))
            btn.setFixedSize(200, 50)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {th['card']}; color: {th['text']};
                    border: 2px solid {th['acc']}; border-radius: 10px;
                    font-size: 15px; font-weight: bold;
                }}
                QPushButton:hover {{ background: {th['acc']}; color: #000; }}
            """)
            btn.clicked.connect(slot)
            vl.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
            vl.addSpacing(8)

        return ov

    def _build_over_overlay(self):
        ov = QWidget(self)
        ov.setStyleSheet("background: rgba(0,0,0,180);")
        vl = QVBoxLayout(ov)
        vl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tr = TR[self.lang]
        th = THEMES[self.theme]

        self._over_label = QLabel("CRASHED")
        self._over_label.setStyleSheet(f"color: {th['danger']}; font-size: 40px; font-weight: bold; background: transparent;")
        self._over_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vl.addWidget(self._over_label)

        self._over_score = QLabel("")
        self._over_score.setStyleSheet(f"color: {th['acc']}; font-size: 20px; background: transparent;")
        self._over_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vl.addWidget(self._over_score)
        vl.addSpacing(20)

        for key, slot in [("restart", self._restart), ("main_menu", self._go_menu)]:
            btn = QPushButton(tr.get(key, key.replace("_"," ").title()))
            btn.setFixedSize(200, 50)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {th['card']}; color: {th['text']};
                    border: 2px solid {th['acc']}; border-radius: 10px;
                    font-size: 15px; font-weight: bold;
                }}
                QPushButton:hover {{ background: {th['acc']}; color: #000; }}
            """)
            btn.clicked.connect(slot)
            vl.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
            vl.addSpacing(8)

        return ov

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self._hud.setGeometry(self._renderer.rect())
        self._pause_overlay.setGeometry(self.rect())
        self._over_overlay.setGeometry(self.rect())

    def start_flight(self, plane_id, map_id, weather_id):
        plane   = PLANES[plane_id]
        mapp    = MAPS[map_id]
        weather = WEATHERS[weather_id]
        self._physics = FlightPhysics(plane, mapp, weather)
        self._renderer.set_physics(self._physics)
        self._hud.set_physics(self._physics)
        self._paused = False
        self._pause_overlay.hide()
        self._over_overlay.hide()
        self._t = 0
        self._keys.clear()
        self.setFocus()
        self._timer.start()

    def _tick(self):
        if self._paused or not self._physics: return
        dt = 0.016
        self._t += dt

        # Key input
        pitch = roll = yaw = thr = 0.0
        if Qt.Key.Key_W in self._keys or Qt.Key.Key_Up    in self._keys: pitch = -1.0
        if Qt.Key.Key_S in self._keys or Qt.Key.Key_Down  in self._keys: pitch =  1.0
        if Qt.Key.Key_A in self._keys or Qt.Key.Key_Left  in self._keys: roll  = -1.0
        if Qt.Key.Key_D in self._keys or Qt.Key.Key_Right in self._keys: roll  =  1.0
        if Qt.Key.Key_Q in self._keys: yaw  = -1.0
        if Qt.Key.Key_E in self._keys: yaw  =  1.0
        if Qt.Key.Key_Z in self._keys: thr  =  1.0
        if Qt.Key.Key_X in self._keys: thr  = -1.0

        self._physics.set_input(pitch, roll, yaw, thr)
        self._physics.update(dt)
        self._renderer.tick(self._t)
        self._hud.tick()

        if not self._physics.alive:
            self._timer.stop()
            tr = TR[self.lang]
            self._over_label.setText(tr.get("game_over","CRASHED"))
            self._over_score.setText(f"{tr.get('score','Score')}: {self._physics.score}   {tr.get('time','Time')}: {self._physics.elapsed:.0f}s")
            self._over_overlay.show()

        if self._physics.landed:
            self._timer.stop()
            tr = TR[self.lang]
            self._over_label.setText(tr.get("landed","LANDED!"))
            self._over_score.setText(f"{tr.get('score','Score')}: {self._physics.score}   {tr.get('time','Time')}: {self._physics.elapsed:.0f}s")
            self._over_overlay.show()

    def keyPressEvent(self, e):
        self._keys.add(e.key())
        if e.key() == Qt.Key.Key_Escape:
            if self._physics and self._physics.alive and not self._physics.landed:
                self._toggle_pause()

    def keyReleaseEvent(self, e):
        self._keys.discard(e.key())

    def _toggle_pause(self):
        self._paused = not self._paused
        self._pause_overlay.setVisible(self._paused)

    def _resume(self):
        self._paused = False
        self._pause_overlay.hide()
        self.setFocus()
        if not self._timer.isActive():
            self._timer.start()

    def _restart(self):
        self._over_overlay.hide()
        self._pause_overlay.hide()
        if self._physics:
            self.start_flight(
                self._cur_plane, self._cur_map, self._cur_weather
            )

    def _go_menu(self):
        self._timer.stop()
        self._pause_overlay.hide()
        self._over_overlay.hide()
        self.sig_back.emit()

    def set_current_config(self, plane_id, map_id, weather_id):
        self._cur_plane   = plane_id
        self._cur_map     = map_id
        self._cur_weather = weather_id

    def set_theme(self, t):
        self.theme = t
        self._renderer.set_theme(t)
        self._hud.set_theme(t)

    def set_lang(self, l):
        self.lang = l
        self._hud.set_lang(l)


# ═══════════════════════════════════════════════════════════════
#  SELECT PAGE
# ═══════════════════════════════════════════════════════════════
class SelectPage(QWidget):
    sig_start = pyqtSignal(str, str, str)
    sig_back  = pyqtSignal()

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang  = lang
        self._sel_plane   = "f16"
        self._sel_map     = "clear"
        self._sel_weather = "clear"
        self._build()

    def _build(self):
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(20, 20, 20, 20)
        self._refresh()

    def _refresh(self):
        tr = TR[self.lang]
        th = THEMES[self.theme]

        # Clear
        while self._main_layout.count():
            item = self._main_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()

        self.setStyleSheet(f"background: {th['bg']}; color: {th['text']};")

        # Title
        title = QLabel(tr["title"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {th['acc']}; font-size: 28px; font-weight: bold;")
        self._main_layout.addWidget(title)
        self._main_layout.addSpacing(10)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background: transparent; border: none;")
        inner = QWidget()
        inner.setStyleSheet("background: transparent;")
        vl    = QVBoxLayout(inner)
        vl.setSpacing(12)

        # ── Plane selection ──
        vl.addWidget(self._section_label(tr["choose_plane"], th))
        plane_row = self._make_selection_row(
            PLANES, "key", self._sel_plane,
            lambda pid: self._select("plane", pid), th, tr
        )
        vl.addLayout(plane_row)

        # ── Map selection ──
        vl.addWidget(self._section_label(tr["choose_map"], th))
        map_row = self._make_selection_row(
            MAPS, "key", self._sel_map,
            lambda mid: self._select("map", mid), th, tr
        )
        vl.addLayout(map_row)

        # ── Weather selection ──
        vl.addWidget(self._section_label(tr["choose_weather"], th))
        wx_row = self._make_selection_row(
            WEATHERS, "key", self._sel_weather,
            lambda wid: self._select("weather", wid), th, tr
        )
        vl.addLayout(wx_row)

        scroll.setWidget(inner)
        self._main_layout.addWidget(scroll, 1)
        self._main_layout.addSpacing(10)

        # Buttons row
        btn_row = QHBoxLayout()
        back_btn = QPushButton(tr["back"])
        start_btn = QPushButton(tr["start_flight"])
        for btn, color in [(back_btn, th["border"]), (start_btn, th["acc"])]:
            btn.setFixedHeight(48)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {th['card']}; color: {th['text']};
                    border: 2px solid {color}; border-radius: 10px;
                    font-size: 15px; font-weight: bold; padding: 0 20px;
                }}
                QPushButton:hover {{ background: {color}; color: #000; }}
            """)
        back_btn.clicked.connect(self.sig_back.emit)
        start_btn.clicked.connect(self._on_start)
        btn_row.addWidget(back_btn)
        btn_row.addStretch()
        btn_row.addWidget(start_btn)
        self._main_layout.addLayout(btn_row)

    def _section_label(self, text, th):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"color: {th['text2']}; font-size: 14px; font-weight: bold; background: transparent;")
        return lbl

    def _make_selection_row(self, data_dict, key_field, sel_id, callback, th, tr):
        row = QHBoxLayout()
        row.setSpacing(10)
        for item_id, info in data_dict.items():
            label_key = info.get(key_field, item_id)
            label_txt = tr.get(label_key, item_id)
            icon_txt  = info.get("icon", "")
            is_sel    = item_id == sel_id
            btn = QPushButton(f"{icon_txt}\n{label_txt}")
            btn.setFixedSize(110, 70)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {'rgba(0,212,255,0.18)' if is_sel else th['card']};
                    color: {th['text'] if not is_sel else th['acc']};
                    border: {'2px solid '+th['acc'] if is_sel else '1px solid '+th['border']};
                    border-radius: 10px; font-size: 12px; font-weight: bold;
                }}
                QPushButton:hover {{ background: {th['card2']}; border: 2px solid {th['acc']}; }}
            """)
            _id = item_id
            btn.clicked.connect(lambda _, i=_id: callback(i))
            row.addWidget(btn)
        row.addStretch()
        return row

    def _select(self, kind, val):
        if kind == "plane":   self._sel_plane   = val
        if kind == "map":     self._sel_map     = val
        if kind == "weather": self._sel_weather = val
        self._refresh()

    def _on_start(self):
        self.sig_start.emit(self._sel_plane, self._sel_map, self._sel_weather)

    def set_theme(self, t): self.theme = t; self._refresh()
    def set_lang(self, l):  self.lang  = l; self._refresh()


# ═══════════════════════════════════════════════════════════════
#  SETTINGS PAGE
# ═══════════════════════════════════════════════════════════════
class SettingsPage(QWidget):
    sig_back         = pyqtSignal()
    sig_theme_change = pyqtSignal(str)
    sig_lang_change  = pyqtSignal(str)

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang  = lang
        self._build()

    def _build(self):
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._refresh()

    def _refresh(self):
        tr = TR[self.lang]
        th = THEMES[self.theme]

        while self._main_layout.count():
            item = self._main_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()

        self.setStyleSheet(f"background: {th['bg']}; color: {th['text']};")

        title = QLabel(tr["settings"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {th['acc']}; font-size: 28px; font-weight: bold;")
        self._main_layout.addWidget(title)
        self._main_layout.addSpacing(20)

        card = QWidget()
        card.setStyleSheet(f"background: {th['card']}; border-radius: 14px;")
        card.setFixedWidth(360)
        cl = QVBoxLayout(card)
        cl.setSpacing(14)
        cl.setContentsMargins(24, 24, 24, 24)

        # Theme
        cl.addWidget(self._row_label(tr["theme"], th))
        th_row = QHBoxLayout()
        for tid, tname in [("dark", tr["dark"]), ("light", tr["light"])]:
            btn = QPushButton(tname)
            btn.setFixedHeight(40)
            is_sel = tid == self.theme
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {'rgba(0,212,255,0.25)' if is_sel else th['card2']};
                    color: {th['acc'] if is_sel else th['text']};
                    border: {'2px solid '+th['acc'] if is_sel else '1px solid '+th['border']};
                    border-radius: 8px; font-size: 13px; font-weight: bold;
                }}
                QPushButton:hover {{ background: {th['card2']}; border: 2px solid {th['acc']}; }}
            """)
            _t = tid
            btn.clicked.connect(lambda _, t=_t: self._change_theme(t))
            th_row.addWidget(btn)
        cl.addLayout(th_row)
        cl.addSpacing(8)

        # Language
        cl.addWidget(self._row_label(tr["lang"], th))
        lang_row = QHBoxLayout()
        for lid, lname in [("en","English"), ("fa","فارسی"), ("zh","中文")]:
            btn = QPushButton(lname)
            btn.setFixedHeight(40)
            is_sel = lid == self.lang
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {'rgba(0,212,255,0.25)' if is_sel else th['card2']};
                    color: {th['acc'] if is_sel else th['text']};
                    border: {'2px solid '+th['acc'] if is_sel else '1px solid '+th['border']};
                    border-radius: 8px; font-size: 13px; font-weight: bold;
                }}
                QPushButton:hover {{ background: {th['card2']}; border: 2px solid {th['acc']}; }}
            """)
            _l = lid
            btn.clicked.connect(lambda _, l=_l: self._change_lang(l))
            lang_row.addWidget(btn)
        cl.addLayout(lang_row)

        self._main_layout.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)
        self._main_layout.addSpacing(24)

        back_btn = QPushButton(tr["back"])
        back_btn.setFixedSize(160, 46)
        back_btn.setStyleSheet(f"""
            QPushButton {{
                background: {th['card']}; color: {th['text']};
                border: 2px solid {th['border']}; border-radius: 10px;
                font-size: 14px; font-weight: bold;
            }}
            QPushButton:hover {{ background: {th['border']}; }}
        """)
        back_btn.clicked.connect(self.sig_back.emit)
        self._main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def _row_label(self, text, th):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"color: {th['text2']}; font-size: 13px; background: transparent;")
        return lbl

    def _change_theme(self, t): self.theme = t; self.sig_theme_change.emit(t); self._refresh()
    def _change_lang(self, l):  self.lang  = l; self.sig_lang_change.emit(l);  self._refresh()

    def set_theme(self, t): self.theme = t; self._refresh()
    def set_lang(self, l):  self.lang  = l; self._refresh()


# ═══════════════════════════════════════════════════════════════
#  MENU PAGE
# ═══════════════════════════════════════════════════════════════
class MenuPage(QWidget):
    sig_play     = pyqtSignal()
    sig_settings = pyqtSignal()
    sig_quit     = pyqtSignal()

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang  = lang
        self._anim_t  = 0.0
        self._anim_timer = QTimer(self)
        self._anim_timer.timeout.connect(self._animate)
        self._anim_timer.start(40)
        self._build()

    def _build(self):
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._refresh()

    def _animate(self):
        self._anim_t += 0.04
        self.update()

    def _refresh(self):
        tr = TR[self.lang]
        th = THEMES[self.theme]

        while self._main_layout.count():
            item = self._main_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()

        self.setStyleSheet(f"background: {th['bg']}; color: {th['text']};")

        self._main_layout.addStretch(2)

        # Icon + title
        icon_lbl = QLabel("✈")
        icon_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_lbl.setStyleSheet(f"font-size: 72px; background: transparent;")
        self._main_layout.addWidget(icon_lbl)

        title = QLabel(tr["title"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"""
            color: {th['acc']};
            font-size: 40px; font-weight: 900;
            letter-spacing: 3px;
            background: transparent;
        """)
        self._main_layout.addWidget(title)

        sub = QLabel("PyQt6 Flight Simulator")
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub.setStyleSheet(f"color: {th['text2']}; font-size: 14px; background: transparent;")
        self._main_layout.addWidget(sub)
        self._main_layout.addSpacing(36)

        # Buttons
        for key, slot, primary in [
            ("play",     self.sig_play.emit,     True),
            ("settings", self.sig_settings.emit, False),
            ("quit",     self.sig_quit.emit,      False),
        ]:
            btn = QPushButton(tr[key])
            btn.setFixedSize(240, 54)
            if primary:
                btn.setStyleSheet(f"""
                    QPushButton {{
                        background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                            stop:0 {th['acc']}, stop:1 {th['acc2']});
                        color: #000; border-radius: 14px;
                        font-size: 18px; font-weight: 900; letter-spacing: 2px;
                        border: none;
                    }}
                    QPushButton:hover {{ opacity: 0.85; }}
                    QPushButton:pressed {{ padding-top: 2px; }}
                """)
            else:
                btn.setStyleSheet(f"""
                    QPushButton {{
                        background: {th['card']}; color: {th['text']};
                        border: 2px solid {th['border']}; border-radius: 12px;
                        font-size: 15px; font-weight: bold;
                    }}
                    QPushButton:hover {{ border-color: {th['acc']}; color: {th['acc']}; }}
                """)
            btn.clicked.connect(slot)
            self._main_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
            self._main_layout.addSpacing(8)

        self._main_layout.addStretch(3)

        # Version
        ver = QLabel("v1.0  |  PyQt6")
        ver.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ver.setStyleSheet(f"color: {th['text2']}; font-size: 10px; background: transparent;")
        self._main_layout.addWidget(ver)
        self._main_layout.addSpacing(8)

    def paintEvent(self, e):
        super().paintEvent(e)
        p  = QPainter(self)
        W, H = self.width(), self.height()
        th = THEMES[self.theme]
        t  = self._anim_t
        # Animated particles
        p.setPen(Qt.PenStyle.NoPen)
        random.seed(42)
        for i in range(30):
            x  = (random.random() * W + math.sin(t * 0.7 + i) * 60) % W
            y  = (random.random() * H - t * 18 * (0.3 + random.random() * 0.7)) % H
            r  = random.randint(1, 3)
            a  = int(40 + random.random() * 80)
            c  = QColor(th["acc"])
            c.setAlpha(a)
            p.setBrush(c)
            p.drawEllipse(int(x), int(y), r*2, r*2)
        p.end()

    def set_theme(self, t): self.theme = t; self._refresh()
    def set_lang(self, l):  self.lang  = l; self._refresh()


# ═══════════════════════════════════════════════════════════════
#  MAIN WINDOW
# ═══════════════════════════════════════════════════════════════
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme = "dark"
        self.lang  = "en"
        self.setWindowTitle(TR[self.lang]["title"])
        self.setMinimumSize(800, 600)
        self.resize(1200, 750)
        self._build()

    def _build(self):
        self._stack = QStackedWidget()
        self.setCentralWidget(self._stack)

        self._menu_pg     = MenuPage(self.theme, self.lang)
        self._select_pg   = SelectPage(self.theme, self.lang)
        self._settings_pg = SettingsPage(self.theme, self.lang)
        self._game_pg     = GamePage(self.theme, self.lang)

        self._stack.addWidget(self._menu_pg)      # 0
        self._stack.addWidget(self._select_pg)    # 1
        self._stack.addWidget(self._settings_pg)  # 2
        self._stack.addWidget(self._game_pg)      # 3

        # Signals
        self._menu_pg.sig_play.connect(lambda: self._stack.setCurrentIndex(1))
        self._menu_pg.sig_settings.connect(lambda: self._stack.setCurrentIndex(2))
        self._menu_pg.sig_quit.connect(self.close)

        self._select_pg.sig_back.connect(lambda: self._stack.setCurrentIndex(0))
        self._select_pg.sig_start.connect(self._start_game)

        self._settings_pg.sig_back.connect(lambda: self._stack.setCurrentIndex(0))
        self._settings_pg.sig_theme_change.connect(self._apply_theme)
        self._settings_pg.sig_lang_change.connect(self._apply_lang)

        self._game_pg.sig_back.connect(lambda: self._stack.setCurrentIndex(0))

        self._stack.setCurrentIndex(0)

    def _start_game(self, plane_id, map_id, weather_id):
        self._game_pg.set_current_config(plane_id, map_id, weather_id)
        self._game_pg.start_flight(plane_id, map_id, weather_id)
        self._stack.setCurrentIndex(3)
        self._game_pg.setFocus()

    def _apply_theme(self, t):
        self.theme = t
        for pg in [self._menu_pg, self._select_pg, self._settings_pg, self._game_pg]:
            pg.set_theme(t)

    def _apply_lang(self, l):
        self.lang = l
        self.setWindowTitle(TR[l]["title"])
        for pg in [self._menu_pg, self._select_pg, self._settings_pg, self._game_pg]:
            pg.set_lang(l)


# ═══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Flight Simulator")
    app.setStyle("Fusion")
    font = QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    app.setFont(font)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
