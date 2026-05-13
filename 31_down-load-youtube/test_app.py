#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test script to verify the YouTube downloader works."""

import sys
from youtube_downloader import get_video_formats, list_formats

# Test with a well-known YouTube video (Rick Astley's "Never Gonna Give You Up")
TEST_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

print("=" * 50)
print("[TEST] Testing YouTube Downloader")
print("=" * 50)

print(f"\nTesting with URL: {TEST_URL}")
print("[*] Fetching video info...")

formats, title = get_video_formats(TEST_URL)

if not formats or not title:
    print("[FAIL] Test FAILED: Could not fetch video info")
    sys.exit(1)

print(f"[OK] Video info fetched successfully!")
print(f"[*] Title: {title}")
print(f"[*] Total formats available: {len(formats)}")

print("\n[*] Available video formats:")
video_formats = list_formats(formats)

if not video_formats:
    print("[FAIL] Test FAILED: No video formats found")
    sys.exit(1)

print(f"\n[OK] Found {len(video_formats)} playable video formats")

print("\n" + "=" * 50)
print("[OK] All tests PASSED!")
print("=" * 50)
print("\nThe app is working correctly. You can now use it to download videos.")
