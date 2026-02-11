/*
 * SPDX-FileCopyrightText: 2019-2026 Christian Hundt
 * SPDX-FileCopyrightText: 2019-2026 Daniel Jünger
 * SPDX-FileCopyrightText: 2019-2026 Parallel and Distributed Architectures <hpc@informatik.uni-mainz.de>
 * SPDX-FileCopyrightText: 2019-2026 Robin Kobus
 *
 * SPDX-License-Identifier: MIT
 */

# pragma once

#include <cstdint>

#define THROW_EXCEPTIONS 1

namespace gossip {

    using gpu_id_t = uint16_t;
    // type of multisplit counters
    using cnter_t = uint64_t;

    enum class PEER_STATUS : uint8_t {
        SLOW = 0,
        DIAG = 1,
        FAST = 2
    };

} // namespace
