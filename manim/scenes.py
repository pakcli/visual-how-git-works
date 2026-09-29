from manim import *

# Konfigurasi Layar Kotak 1:1 HD (1080x1080)
config.pixel_width = 1080
config.pixel_height = 1080
config.frame_width = 8.0
config.frame_height = 8.0
config.background_color = "#181825"

# ==============================================================================
# LEVEL 1: PAGAR RUMAH (1:1 HD Square Animation)
# ==============================================================================
class PagarGitSquareScene(Scene):
    def construct(self):
        # Header Top
        badge = RoundedRectangle(corner_radius=0.15, width=7.2, height=0.7, fill_color="#313244", fill_opacity=0.9, stroke_color="#89b4fa")
        badge.to_edge(UP, buff=0.3)
        badge_txt = Text("LEVEL 1: ANALOGI PAGAR RUMAH", font_size=18, color="#89b4fa", weight=BOLD).move_to(badge)
        self.play(FadeIn(badge), Write(badge_txt), run_time=0.8)

        # Garis Pembatas Split View
        divider = DashedLine(LEFT * 3.6, RIGHT * 3.6, color="#45475a").shift(UP * 0.1)
        sub_metafora = Text("METAFORA NYATA", font_size=12, color="#a6adc8").next_to(divider, UP, buff=0.15).to_edge(LEFT, buff=0.6)
        sub_git = Text("STRUKTUR GIT DAG", font_size=12, color="#a6e3a1").next_to(divider, DOWN, buff=0.15).to_edge(LEFT, buff=0.6)
        self.play(Create(divider), Write(sub_metafora), Write(sub_git), run_time=0.6)

        # Step Indicator Box
        step_box = RoundedRectangle(corner_radius=0.1, width=7.0, height=0.55, fill_color="#1e1e2e", fill_opacity=0.9, stroke_color="#b4befe")
        step_box.shift(UP * 2.8)
        step_lbl = Text("Step 1: Rangka Besi (v0.1.0-alpha)", font_size=14, color=WHITE).move_to(step_box)

        # -------------------------------------------------------------
        # STEP 1: Rangka Besi (v0.1.0-alpha)
        # -------------------------------------------------------------
        pagar = VGroup(*[
            Rectangle(width=0.45, height=1.7, fill_opacity=1, fill_color="#45475a", stroke_color="#6c7086", stroke_width=2).shift(LEFT * 2.4 + RIGHT * i * 0.95 + UP * 1.35)
            for i in range(5)
        ])
        
        # Git Graph Nodes
        c1 = Circle(radius=0.32, color="#6c7086", fill_opacity=1, fill_color="#313244").shift(LEFT * 2.5 + DOWN * 1.8)
        c1_lbl = Text("C1", font_size=13, color=WHITE).move_to(c1)
        c1_tag = Text("v0.1.0-alpha", font_size=11, color="#fab387").next_to(c1, DOWN, buff=0.15)
        head_ptr = Arrow(DOWN * 0.6, DOWN * 0.1, color="#f38ba8", buff=0).next_to(c1, UP, buff=0.1)
        head_lbl = Text("HEAD -> develop", font_size=11, color="#f38ba8").next_to(head_ptr, UP, buff=0.1)

        self.play(FadeIn(step_box), Write(step_lbl), Create(pagar), GrowFromCenter(c1), Write(c1_lbl), Write(c1_tag), GrowArrow(head_ptr), Write(head_lbl))
        self.wait(1.5)

        # -------------------------------------------------------------
        # STEP 2: Cat Dasar Anti Karat (v0.2.0-beta)
        # -------------------------------------------------------------
        step2_lbl = Text("Step 2: Cat Dasar Abu-abu (v0.2.0-beta)", font_size=14, color=WHITE).move_to(step_box)
        c2 = Circle(radius=0.32, color="#89b4fa", fill_opacity=1, fill_color="#1e1e2e").shift(LEFT * 0.8 + DOWN * 1.8)
        c2_lbl = Text("C2", font_size=13, color=WHITE).move_to(c2)
        c2_tag = Text("v0.2.0-beta", font_size=11, color="#89b4fa").next_to(c2, DOWN, buff=0.15)
        a1_2 = Arrow(c1.get_right(), c2.get_left(), buff=0.1, color="#6c7086")

        self.play(
            Transform(step_lbl, step2_lbl),
            pagar.animate.set_fill("#7f8c8d").set_stroke("#95a5a6"),
            GrowArrow(a1_2), GrowFromCenter(c2), Write(c2_lbl), Write(c2_tag),
            head_ptr.animate.next_to(c2, UP, buff=0.1),
            head_lbl.animate.next_to(head_ptr, UP, buff=0.1)
        )
        self.wait(1.5)

        # -------------------------------------------------------------
        # STEP 3: Cabang Eksperimen (Kuning vs Hijau)
        # -------------------------------------------------------------
        step3_lbl = Text("Step 3: Uji Motif Kuning di Panel 5 (Branch)", font_size=14, color="#f9e2af").move_to(step_box)
        panel_kuning = pagar[4]
        c3_branch = Circle(radius=0.32, color="#f1c40f", fill_opacity=1, fill_color="#1e1e2e").shift(RIGHT * 1.2 + DOWN * 1.0)
        c3_lbl = Text("C3", font_size=13, color=WHITE).move_to(c3_branch)
        c3_tag = Text("motif-kuning", font_size=11, color="#f1c40f").next_to(c3_branch, RIGHT, buff=0.15)
        a2_branch = Arrow(c2.get_right(), c3_branch.get_left(), buff=0.1, color="#f1c40f")

        self.play(
            Transform(step_lbl, step3_lbl),
            panel_kuning.animate.set_fill("#f1c40f").set_stroke("#f39c12").shift(UP * 0.15),
            GrowArrow(a2_branch), GrowFromCenter(c3_branch), Write(c3_lbl), Write(c3_tag),
            head_ptr.animate.next_to(c3_branch, UP, buff=0.1),
            head_lbl.animate.become(Text("HEAD -> exp/kuning", font_size=11, color="#f1c40f").next_to(c3_branch, UP, buff=0.4))
        )
        self.wait(1.5)

        # -------------------------------------------------------------
        # STEP 4: Kuning Ditolak & Hijau Disetujui (RC)
        # -------------------------------------------------------------
        step4_lbl = Text("Step 4: Kuning Ditolak! Warna Hijau Disetujui (v0.9.0-rc)", font_size=13, color="#a6e3a1").move_to(step_box)
        cross = Cross(c3_branch, stroke_color="#e74c3c", stroke_width=3)
        c4_rc = Circle(radius=0.32, color="#a6e3a1", fill_opacity=1, fill_color="#1e1e2e").shift(RIGHT * 1.2 + DOWN * 1.8)
        c4_lbl = Text("C4", font_size=13, color=WHITE).move_to(c4_rc)
        c4_tag = Text("v0.9.0-rc", font_size=11, color="#a6e3a1").next_to(c4_rc, DOWN, buff=0.15)
        a2_rc = Arrow(c2.get_right(), c4_rc.get_left(), buff=0.1, color="#a6e3a1")

        self.play(
            Transform(step_lbl, step4_lbl),
            Create(cross),
            panel_kuning.animate.set_fill("#2ecc71").set_stroke("#27ae60").shift(DOWN * 0.15),
            pagar.animate.set_fill("#2ecc71").set_stroke("#27ae60"),
            GrowArrow(a2_rc), GrowFromCenter(c4_rc), Write(c4_lbl), Write(c4_tag),
            head_ptr.animate.next_to(c4_rc, UP, buff=0.1),
            head_lbl.animate.become(Text("HEAD -> develop", font_size=11, color="#a6e3a1").next_to(c4_rc, UP, buff=0.4))
        )
        self.play(FadeOut(c3_branch), FadeOut(c3_lbl), FadeOut(c3_tag), FadeOut(a2_branch), FadeOut(cross))
        self.wait(1.5)

        # -------------------------------------------------------------
        # STEP 5: Pernis Kilap & Rilis Resmi v1.0.0
        # -------------------------------------------------------------
        step5_lbl = Text("Step 5: Pernis Kilap & Plat Nomor (v1.0.0 Release)", font_size=14, color="#fab387").move_to(step_box)
        final_tag = RoundedRectangle(corner_radius=0.1, width=1.8, height=0.5, fill_color="#fab387", fill_opacity=1, stroke_width=0)
        final_tag.shift(RIGHT * 2.2 + DOWN * 2.8)
        final_tag_txt = Text("TAG: v1.0.0", font_size=13, color="#1e1e2e", weight=BOLD).move_to(final_tag)
        sparkle = Star(color=YELLOW, fill_opacity=1).scale(0.3).next_to(pagar, UP, buff=0.2)

        self.play(
            Transform(step_lbl, step5_lbl),
            FadeIn(sparkle),
            DrawBorderThenFill(final_tag),
            Write(final_tag_txt)
        )
        self.wait(2.5)


# ==============================================================================
# LEVEL 2: SMARTPHONE & FIRMWARE (1:1 HD Square Animation)
# ==============================================================================
class SmartphoneGitSquareScene(Scene):
    def construct(self):
        # Header Top
        badge = RoundedRectangle(corner_radius=0.15, width=7.2, height=0.7, fill_color="#313244", fill_opacity=0.9, stroke_color="#89b4fa")
        badge.to_edge(UP, buff=0.3)
        badge_txt = Text("LEVEL 2: SMARTPHONE & FIRMWARE", font_size=18, color="#89b4fa", weight=BOLD).move_to(badge)
        self.play(FadeIn(badge), Write(badge_txt), run_time=0.8)

        divider = DashedLine(LEFT * 3.6, RIGHT * 3.6, color="#45475a").shift(DOWN * 0.3)
        sub_metafora = Text("LAPISAN PERANGKAT HP", font_size=12, color="#a6adc8").next_to(divider, UP, buff=0.15).to_edge(LEFT, buff=0.6)
        sub_git = Text("PELACAKAN HISTORI GIT", font_size=12, color="#a6e3a1").next_to(divider, DOWN, buff=0.15).to_edge(LEFT, buff=0.6)
        self.play(Create(divider), Write(sub_metafora), Write(sub_git), run_time=0.6)

        step_box = RoundedRectangle(corner_radius=0.1, width=7.0, height=0.55, fill_color="#1e1e2e", fill_opacity=0.9, stroke_color="#b4befe")
        step_box.shift(UP * 2.8)
        step_lbl = Text("Step 1: OS 14.1.0 Stabil di Tangan User", font_size=14, color=WHITE).move_to(step_box)

        # 3 Lapisan HP
        hw_box = Rectangle(width=4.8, height=0.55, fill_opacity=0.9, fill_color="#45475a", stroke_color="#6c7086").shift(UP * 0.5)
        hw_txt = Text("1. Hardware: SoC + Lensa Kamera Fisik", font_size=12, color=WHITE).move_to(hw_box)

        fw_box = Rectangle(width=4.8, height=0.55, fill_opacity=0.9, fill_color="#313244", stroke_color="#89b4fa").next_to(hw_box, UP, buff=0.15)
        fw_txt = Text("2. Firmware Kernel: OS 14.1.0 LTS", font_size=12, color="#89b4fa").move_to(fw_box)

        app_box = Rectangle(width=4.8, height=0.55, fill_opacity=0.9, fill_color="#181825", stroke_color="#a6e3a1").next_to(fw_box, UP, buff=0.15)
        app_txt = Text("3. User Apps: Kamera v1.8 Berjalan Normal", font_size=12, color="#a6e3a1").move_to(app_box)

        # Git Node Baseline
        c1 = Circle(radius=0.3, color="#89b4fa", fill_opacity=1, fill_color="#1e1e2e").shift(LEFT * 2.5 + DOWN * 1.8)
        c1_lbl = Text("v14.1", font_size=12, color=WHITE).move_to(c1)

        self.play(FadeIn(step_box), Write(step_lbl), Create(hw_box), Write(hw_txt), Create(fw_box), Write(fw_txt), Create(app_box), Write(app_txt), GrowFromCenter(c1), Write(c1_lbl))
        self.wait(1.5)

        # Step 2: Beta OS 15 Channel
        step2_lbl = Text("Step 2: Saluran Beta OS 15 (Branch release/15.0-beta)", font_size=13, color="#f9e2af").move_to(step_box)
        c2_beta = Circle(radius=0.3, color="#f9e2af", fill_opacity=1, fill_color="#1e1e2e").shift(LEFT * 0.5 + DOWN * 1.1)
        c2_lbl = Text("v15-b", font_size=12, color=WHITE).move_to(c2_beta)
        a1_beta = Arrow(c1.get_right(), c2_beta.get_left(), buff=0.1, color="#f9e2af")

        self.play(
            Transform(step_lbl, step2_lbl),
            fw_box.animate.set_stroke(color="#f9e2af"),
            Transform(fw_txt, Text("2. Firmware Kernel: OS 15.0 Beta Active", font_size=12, color="#f9e2af").move_to(fw_box)),
            GrowArrow(a1_beta), GrowFromCenter(c2_beta), Write(c2_lbl)
        )
        self.wait(1.5)

        # Step 3: Kamera Crash (Breaking Change)
        step3_lbl = Text("Step 3: Crash! Driver Kamera Tak Kompatibel", font_size=14, color="#f38ba8").move_to(step_box)
        warn_app = Rectangle(width=4.8, height=0.55, fill_opacity=0.95, fill_color="#f38ba8", stroke_color="#e74c3c").move_to(app_box)
        warn_txt = Text("3. Kamera CRASH (Driver Incompatible)", font_size=12, color="#1e1e2e", weight=BOLD).move_to(warn_app)

        self.play(Transform(step_lbl, step3_lbl), Transform(app_box, warn_app), Transform(app_txt, warn_txt))
        self.wait(1.5)

        # Step 4: Hotfix Adapter Driver
        step4_lbl = Text("Step 4: Pasang Adapter Driver (Hotfix Branch)", font_size=14, color="#89b4fa").move_to(step_box)
        c3_fix = Circle(radius=0.3, color="#89b4fa", fill_opacity=1, fill_color="#1e1e2e").shift(RIGHT * 1.5 + DOWN * 1.1)
        c3_lbl = Text("fix", font_size=12, color=WHITE).move_to(c3_fix)
        a_b_fix = Arrow(c2_beta.get_right(), c3_fix.get_left(), buff=0.1, color="#89b4fa")

        self.play(
            Transform(step_lbl, step4_lbl),
            GrowArrow(a_b_fix), GrowFromCenter(c3_fix), Write(c3_lbl),
            Transform(app_txt, Text("3. Kamera v2.0 (Adapter Berhasil Diuji)", font_size=12, color="#89b4fa").move_to(app_box)),
            app_box.animate.set_fill("#181825").set_stroke("#89b4fa")
        )
        self.wait(1.5)

        # Step 5: Rollback Aman untuk User Biasa
        step5_lbl = Text("Step 5: Rollback ke Titik Stabil (git reset --hard v14.1)", font_size=13, color="#a6e3a1").move_to(step_box)
        self.play(
            Transform(step_lbl, step5_lbl),
            fw_box.animate.set_stroke(color="#89b4fa"),
            Transform(fw_txt, Text("2. Firmware Kernel: OS 14.1.0 LTS (Safe)", font_size=12, color="#89b4fa").move_to(fw_box)),
            Transform(app_txt, Text("3. User Apps: Kamera v1.8 Kembali Normal", font_size=12, color="#a6e3a1").move_to(app_box)),
            app_box.animate.set_stroke(color="#a6e3a1")
        )
        self.wait(1.5)

        # Step 6: Rilis Resmi OS 15 Global
        step6_lbl = Text("Step 6: Peluncuran Global OS 15 (v15.0.0 Tag)", font_size=14, color="#a6e3a1").move_to(step_box)
        c_final = Circle(radius=0.35, color="#a6e3a1", fill_opacity=1, fill_color="#313244").shift(RIGHT * 2.8 + DOWN * 1.8)
        c_final_lbl = Text("v15", font_size=13, color=WHITE).move_to(c_final)
        a_main_final = Arrow(c1.get_right(), c_final.get_left(), buff=0.1, color="#a6e3a1")
        a_fix_final = Arrow(c3_fix.get_right(), c_final.get_top(), buff=0.1, color="#89b4fa")

        self.play(
            Transform(step_lbl, step6_lbl),
            GrowArrow(a_fix_final), GrowArrow(a_main_final),
            GrowFromCenter(c_final), Write(c_final_lbl),
            Transform(fw_txt, Text("2. Firmware Kernel: OS 15.0 Global Official", font_size=12, color="#a6e3a1").move_to(fw_box)),
            fw_box.animate.set_stroke(color="#a6e3a1")
        )
        self.wait(2.5)


# ==============================================================================
# LEVEL 3: MINECRAFT NETHER UPDATE (1:1 HD Square Animation)
# ==============================================================================
class MinecraftGitSquareScene(Scene):
    def construct(self):
        # Header Top
        badge = RoundedRectangle(corner_radius=0.15, width=7.2, height=0.7, fill_color="#313244", fill_opacity=0.9, stroke_color="#89b4fa")
        badge.to_edge(UP, buff=0.3)
        badge_txt = Text("LEVEL 3: MINECRAFT NETHER PIPELINE", font_size=18, color="#89b4fa", weight=BOLD).move_to(badge)
        self.play(FadeIn(badge), Write(badge_txt), run_time=0.8)

        divider = DashedLine(LEFT * 3.6, RIGHT * 3.6, color="#45475a").shift(DOWN * 0.3)
        sub_metafora = Text("VOXEL ASSETS & BIOMES", font_size=12, color="#a6adc8").next_to(divider, UP, buff=0.15).to_edge(LEFT, buff=0.6)
        sub_git = Text("MOJANG RELEASE PIPELINE", font_size=12, color="#a6e3a1").next_to(divider, DOWN, buff=0.15).to_edge(LEFT, buff=0.6)
        self.play(Create(divider), Write(sub_metafora), Write(sub_git), run_time=0.6)

        step_box = RoundedRectangle(corner_radius=0.1, width=7.0, height=0.55, fill_color="#1e1e2e", fill_opacity=0.9, stroke_color="#b4befe")
        step_box.shift(UP * 2.8)
        step_lbl = Text("Step 1: Overworld Vanilla (v1.15.2 LTS)", font_size=14, color=WHITE).move_to(step_box)

        # Voxel Grass Block
        ow_block = Square(side=1.3, fill_color="#2ecc71", fill_opacity=0.9, stroke_color="#27ae60").shift(LEFT * 2.2 + UP * 1.3)
        ow_lbl = Text("Grass Block\n(Overworld)", font_size=11, color="#1e1e2e", weight=BOLD).move_to(ow_block)

        c1 = Circle(radius=0.28, color="#a6e3a1", fill_opacity=1, fill_color="#1e1e2e").shift(LEFT * 3.0 + DOWN * 1.9)
        c1_lbl = Text("1.15", font_size=11, color=WHITE).move_to(c1)

        self.play(FadeIn(step_box), Write(step_lbl), DrawBorderThenFill(ow_block), Write(ow_lbl), GrowFromCenter(c1), Write(c1_lbl))
        self.wait(1.5)

        # Step 2: Nether Expansion Branch
        step2_lbl = Text("Step 2: Nether Biome Branch (feature/nether)", font_size=14, color="#f38ba8").move_to(step_box)
        nt_block = Square(side=1.3, fill_color="#e74c3c", fill_opacity=0.9, stroke_color="#c0392b").shift(RIGHT * 0.2 + UP * 1.3)
        nt_lbl = Text("Crimson Block\n(Nether)", font_size=11, color=WHITE, weight=BOLD).move_to(nt_block)
        c2_nether = Circle(radius=0.28, color="#f38ba8", fill_opacity=1, fill_color="#1e1e2e").shift(LEFT * 1.2 + DOWN * 1.1)
        c2_lbl = Text("N1", font_size=11, color=WHITE).move_to(c2_nether)
        a1_n = Arrow(c1.get_right(), c2_nether.get_left(), buff=0.1, color="#f38ba8")

        self.play(Transform(step_lbl, step2_lbl), DrawBorderThenFill(nt_block), Write(nt_lbl), GrowArrow(a1_n), GrowFromCenter(c2_nether), Write(c2_lbl))
        self.wait(1.5)

        # Step 3: Tabrakan Registry Blok ID 154
        step3_lbl = Text("Step 3: Tabrakan ID Blok! (Save Corrupted)", font_size=14, color="#fab387").move_to(step_box)
        glitch_box = Square(side=1.3, fill_color="#9b59b6", fill_opacity=0.9, stroke_color=YELLOW).move_to(nt_block)
        glitch_lbl = Text("MISSING\nTEXTURE", font_size=11, color=YELLOW, weight=BOLD).move_to(glitch_box)

        self.play(Transform(step_lbl, step3_lbl), Transform(nt_block, glitch_box), Transform(nt_lbl, glitch_lbl))
        self.wait(1.5)

        # Step 4: Refactor Namespaced ID
        step4_lbl = Text("Step 4: Refactor ke Namespaced ID (minecraft:crimson)", font_size=13, color="#a6e3a1").move_to(step_box)
        c3_fix = Circle(radius=0.28, color="#f38ba8", fill_opacity=1, fill_color="#1e1e2e").shift(RIGHT * 0.6 + DOWN * 1.1)
        c3_lbl = Text("N2", font_size=11, color=WHITE).move_to(c3_fix)
        a_n1_n2 = Arrow(c2_nether.get_right(), c3_fix.get_left(), buff=0.1, color="#f38ba8")

        self.play(
            Transform(step_lbl, step4_lbl),
            nt_block.animate.set_fill("#e74c3c").set_stroke("#c0392b"),
            Transform(nt_lbl, Text("minecraft:\ncrimson_nylium", font_size=10, color=WHITE).move_to(nt_block)),
            GrowArrow(a_n1_n2), GrowFromCenter(c3_fix), Write(c3_lbl)
        )
        self.wait(1.5)

        # Step 5: Snapshot Mingguan 20w06a
        step5_lbl = Text("Step 5: Komunitas Reddit Snapshot 20w06a", font_size=14, color="#f9e2af").move_to(step_box)
        snap_badge = Text("TAG: 20w06a", font_size=10, color="#f9e2af").next_to(c3_fix, UP, buff=0.15)
        self.play(Transform(step_lbl, step5_lbl), Write(snap_badge))
        self.wait(1.5)

        # Step 6: Non-Fast-Forward Merge ke Main
        step6_lbl = Text("Step 6: Merge Dimensi ke Main (git merge --no-ff)", font_size=13, color="#89b4fa").move_to(step_box)
        c_merge = Circle(radius=0.32, color="#a6e3a1", fill_opacity=1, fill_color="#313244").shift(RIGHT * 2.2 + DOWN * 1.9)
        c_merge_lbl = Text("M", font_size=12, color=WHITE).move_to(c_merge)
        a_main_m = Arrow(c1.get_right(), c_merge.get_left(), buff=0.1, color="#a6e3a1")
        a_n2_m = Arrow(c3_fix.get_right(), c_merge.get_top(), buff=0.1, color="#f38ba8")

        self.play(Transform(step_lbl, step6_lbl), GrowArrow(a_n2_m), GrowArrow(a_main_m), GrowFromCenter(c_merge), Write(c_merge_lbl))
        self.wait(1.5)

        # Step 7: Nether Update 1.16 Rilis & Hotfix 1.16.1
        step7_lbl = Text("Step 7: Rilis Global 1.16.0 & Hotfix 1.16.1", font_size=14, color="#a6e3a1").move_to(step_box)
        portal = RoundedRectangle(corner_radius=0.2, width=1.4, height=1.4, fill_color="#8e44ad", fill_opacity=0.9, stroke_color="#e056fd").shift(RIGHT * 2.5 + UP * 1.3)
        portal_lbl = Text("Nether Portal\nActive ✓", font_size=10, color=WHITE, weight=BOLD).move_to(portal)
        hotfix_tag = Text("1.16.1 Hotfix", font_size=10, color="#fab387").next_to(c_merge, DOWN, buff=0.2)

        self.play(Transform(step_lbl, step7_lbl), DrawBorderThenFill(portal), Write(portal_lbl), Write(hotfix_tag))
        self.wait(2.5)
