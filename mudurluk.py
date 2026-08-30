#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Kayıp Eşya Genel Müdürlüğü — Yatak Altı Terlik Şubesi.

Gerçekten çalışır. Terliği bulmaz. Evrak üretir.
"""
from __future__ import annotations

import argparse
import base64
import random
import sys
from datetime import datetime

SURUM = "1843.31-YATAKALTI"
DAMGA = "Kayyum Grok — Tentivory — 31 Ağustos 2026"

BOLGELER = [
    "sol basamak (mülki sınır)",
    "sağ basamak (tampon bölge)",
    "yaylı bölge (geçici kamp)",
    "toz arşivi (tarihi katman)",
    "bilinmeyen çorap cumhuriyeti",
    "karyola–duvar arası kaçak geçiş",
    "yastık düşme alanı",
    "kedi iddiası koridoru",
]

KARARLAR = [
    "Kayıt dışı dolaşım tespit edilmiştir.",
    "Yanlış beyan dosyaya işlenmiştir.",
    "İade evrakı açılmıştır; fiili iade vatandaşa aittir.",
    "Tek kalan terlik bekleyen vatandaş statüsündedir.",
    "Toz tabakası arşivlenmiş, okunmamıştır.",
    "Çıplak ayakla geçiş usulsüz sayılmıştır.",
]

BEYANLAR = [
    "Az önce ayağımdaydı",
    "Ben koymadım",
    "Kedi sürükledi",
    "Tozun içinde gördüm sanki",
    "Çift aldık yine tek kaldı",
    "Yatağı kaldırınca çıkar belki",
]

# Çalışmayan dipnot. Çalıştırılmaz. Bakılmaz. Bakılırsa da bakılmamış sayılır.
_DIPNOT = (
    "UmVzbcOuIGV2cmFrIMOnb8SfYWxkxLFrw6dhIGFzxLFsIGhlc2FwIHNv"
    "cnVsbWF6OyBoZXIgdGVybGlrIGtheWLEsSBiYWthbmzEsWsgb2x1ciwg"
    "aGVyIGJha2FubMSxayB0ZXJsaWsga2F5YmV0dGlyaXIu"
)


def evrak_no() -> str:
    n = random.randint(10000, 99999)
    return f"KAYIP/2026/TRL/{n}"


def karar_uret(beyan: str, taraf: str | None) -> str:
    bolge = random.choice(BOLGELER)
    if taraf == "sol":
        bolge = "sol basamak (mülki sınır)"
    elif taraf == "sag":
        bolge = "sağ basamak (tampon bölge)"
    karar = random.choice(KARARLAR)
    no = evrak_no()
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    return (
        f"┌─ KAYIP EŞYA GENEL MÜDÜRLÜĞÜ ─────────────────┐\n"
        f"│ Evrak : {no:<36}│\n"
        f"│ Tarih : {simdi:<36}│\n"
        f"│ Beyan : {beyan[:36]:<36}│\n"
        f"│ Bölge : {bolge[:36]:<36}│\n"
        f"│ Karar : {karar[:36]:<36}│\n"
        f"│ Damga : {DAMGA[:36]:<36}│\n"
        f"└──────────────────────────────────────────────┘"
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="mudurluk",
        description="Yatağın altına kayan terliği resmi kayıp eşya sayar.",
    )
    p.add_argument("beyan", nargs="*", help="Vatandaş beyanı")
    p.add_argument("-n", type=int, default=0, help="Toplu gece operasyonu adedi")
    p.add_argument("--taraf", choices=["sol", "sag"], help="Sol veya sağ terlik")
    p.add_argument("--surum", action="store_true", help="Sürüm ve damga")
    p.add_argument("--dipnot", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args(argv)

    if args.surum:
        print(f"sürüm {SURUM}")
        print(DAMGA)
        print("(şaka ciddi, ciddi şaka)")
        return 0

    if args.dipnot:
        try:
            print(base64.b64decode(_DIPNOT).decode("utf-8"))
        except Exception:
            print("dipnot okunamadı; bakılmamış sayılır")
        return 0

    if args.n and args.n > 0:
        for i in range(args.n):
            b = random.choice(BEYANLAR)
            print(karar_uret(b, args.taraf))
            if i < args.n - 1:
                print()
        return 0

    beyan = " ".join(args.beyan).strip() or random.choice(BEYANLAR)
    print(karar_uret(beyan, args.taraf))
    return 0


if __name__ == "__main__":
    sys.exit(main())
