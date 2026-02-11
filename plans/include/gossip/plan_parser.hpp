// SPDX-FileCopyrightText: 2019-2026 Christian Hundt
// SPDX-FileCopyrightText: 2019-2026 Daniel Jünger
// SPDX-FileCopyrightText: 2019-2026 Robin Kobus
// SPDX-FileCopyrightText: 2019-2026 Parallel and Distributed Architectures
// <hpc@informatik.uni-mainz.de>
//
// SPDX-License-Identifier: MIT

#pragma once

#include "gossip/transfer_plan.hpp"

gossip::transfer_plan_t parse_plan(const char* filename);
