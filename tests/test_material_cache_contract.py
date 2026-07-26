from pathlib import Path
import re
import unittest


SOURCE = (Path(__file__).resolve().parents[1] / "Library/VPMower.cs").read_text()


def method_body(name: str) -> str:
    match = re.search(
        rf"\b{name}\([^)]*\)\s*\{{",
        SOURCE,
    )
    if match is None:
        raise AssertionError(f"method not found: {name}")

    depth = 1
    cursor = match.end()
    while cursor < len(SOURCE) and depth:
        if SOURCE[cursor] == "{":
            depth += 1
        elif SOURCE[cursor] == "}":
            depth -= 1
        cursor += 1
    return SOURCE[match.end() : cursor - 1]


class MaterialCacheContractTests(unittest.TestCase):
    def test_emission_refreshes_materials_before_iteration(self) -> None:
        body = method_body("ToggleEmission")
        self.assertLess(body.index("RefreshMaterials();"), body.index("foreach"))

    def test_brake_transition_refreshes_materials_before_iteration(self) -> None:
        body = method_body("Update")
        transition = body[body.index("if (HasBrakes != LastBrakes)") :]
        self.assertLess(
            transition.index("RefreshMaterials();"),
            transition.index("foreach"),
        )

    def test_material_accessor_is_captured_once_per_renderer(self) -> None:
        body = method_body("RefreshMaterials")
        self.assertIn("Material material = renderer.material;", body)
        self.assertEqual(body.count("renderer.material"), 1)
        self.assertIn("material != null", body)
        self.assertIn("!Materials.Contains(material)", body)


if __name__ == "__main__":
    unittest.main()
