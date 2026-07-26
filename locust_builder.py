from seeds.builder import build_http_seeds_builder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan, SeedOperationsPlan

builder = build_http_seeds_builder()
result = builder.build(
    plan=SeedsPlan(
        users=SeedUsersPlan(
            count=10,
            credit_card_accounts=SeedAccountsPlan(
                count=1,
                physical_cards=SeedCardsPlan(count=1)
            )
        )
    )
)
print(result)
save_seeds_result(result=result, scenario="test-scenario")
load_seeds_result(scenario="test-scenario")