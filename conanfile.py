# SPDX-FileCopyrightText: 2026 Markus Vieth <vieth@uni-mainz.de>
# SPDX-FileCopyrightText: 2026 Parallel and Distributed Architectures <hpc@informatik.uni-mainz.de>
#
# SPDX-License-Identifier: BSL-1.0

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout, CMakeConfigDeps


class GossipRecipe(ConanFile):
    name = "gossip"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    package_type = "header-library"
    exports_sources = (
        "include/*",
        "CMakeLists.txt",
        "examples/*",
        "plan_parser/*",
    )

    def requirements(self):
        self.requires("pararch.hpc_helpers/0.1.15")
        self.requires("nv-cccl/3.2.0")
        self.requires("clipp/1.2.3")
        self.requires("nlohmann_json/3.12.0")

    def build_requirements(self):
        self.requires("cmake/4.2.3")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeConfigDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.cache_variables["CMAKE_CUDA_STANDARD"] = self.settings.get_safe(
            "compiler.cppstd"
        )
        tc.cache_variables["CMAKE_CUDA_FLAGS"] = (
            "-Xcompiler='-Wall -Wextra' --expt-relaxed-constexpr --extended-lambda -lineinfo"
        )
        tc.generate()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []

    def package_id(self):
        self.info.clear()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
