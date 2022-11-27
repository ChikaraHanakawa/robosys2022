#!/bin/bash -xv
# SPDX-FileCopyrightText: 2022 Chikara Hanakawa
# SPDX-License-Identifier: BSD-3-Clause

ng () {
      echo NG at line $1
      res=1
}

out=$(seq 0 9)
[ "${out}" = 0 ] || ng ${LINENO}
