# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.ledger.auth import DamlV1ClaimName
from dazl.ledger.config import PropertyBasedAccessConfig
from dazl.prim import Party
import jwt


def test_access_jwts_are_valid():
    config = PropertyBasedAccessConfig(act_as=[Party("Alice")])
    claims = jwt.decode(config.token, algorithms=["none"], options={"verify_signature": False})

    assert claims[DamlV1ClaimName]["actAs"] == ["Alice"]
