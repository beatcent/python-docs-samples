#!/usr/bin/env python

# Copyright 2017 Google, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

import analyze


@pytest.mark.slow
def test_analyze_shots(capsys):
    analyze.analyze_shots('gs://demomaker/gbikes_dinosaur.mp4')
    out, _ = capsys.readouterr()
    assert 'Shot 1:' in out


@pytest.mark.slow
def test_analyze_labels(capsys):
    analyze.analyze_labels('gs://demomaker/cat.mp4')
    out, _ = capsys.readouterr()
    assert 'label description: cat' in out


@pytest.mark.slow
def test_analyze_explicit_content(capsys):
    analyze.analyze_explicit_content('gs://demomaker/cat.mp4')
    out, _ = capsys.readouterr()
    assert 'pornography' in out
