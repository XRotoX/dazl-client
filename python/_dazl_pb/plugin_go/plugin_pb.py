# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse

from .. import protoc

__all__ = ["run_plugin"]


def run_plugin(request: "CodeGeneratorRequest") -> "CodeGeneratorResponse":
    # the default Go plugin already seems to respect copyright headers, so we don't actually
    # need to make any changes to the generated code
    return protoc.run_plugin("go", request)
