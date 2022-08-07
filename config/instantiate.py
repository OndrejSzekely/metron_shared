"""
Instantiation from Hydra Config.
"""


from enum import Enum
from typing import Any
import hydra
from omegaconf import DictConfig
import param_validators as param_val


class HydraInstantiateConversion(Enum):
    """
    Defines Hydra's instantiation conversion options. Basically how to handle list and dict like objects,
    whether they are represented via OmegaConf structs or Python structs.
    """

    NO_CONVERSION = "none"
    PARTIAL = "partial"
    ALL = "all"


def instantiate_from_hydra_config(
    hydra_object_config: DictConfig,
    conversion: HydraInstantiateConversion = HydraInstantiateConversion.NO_CONVERSION,
    **kwargs
) -> Any:
    """
    Instantiates object from Hydra object config <hydra_object_config>. It has to contain <_target_> attribute.

    Args:
        hydra_object_config (DictConfig): Object's Hydra config DictConfig.
        conversion (HydraInstantiateConversion): Defined how non-primitive values in OmegaConf are handled.
            See https://hydra.cc/docs/advanced/instantiate_objects/overview/#parameter-conversion-strategies.
        **kwargs: Key-worded arguments which are passed into a constructor of the instantiated class.
    Returns (Any): Instantiated object.
    """
    param_val.check_type(hydra_object_config, DictConfig)
    param_val.check_type(conversion, HydraInstantiateConversion)
    
    return hydra.utils.instantiate(hydra_object_config, _convert_=conversion.value, **kwargs)