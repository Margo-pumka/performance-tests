from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    @property
    def plan(self) -> SeedsPlan:
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                debit_card_accounts=SeedAccountsPlan(
                    count=1,
                    virtual_cards=SeedCardsPlan(count=1)
                )
            )
        )

    @property
    def scenario(self) -> str:
        return 'existing_user_issue_virtual_card'

if __name__ == '__main__':
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
