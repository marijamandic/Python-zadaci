from dataclasses import dataclass
from typing import List, Optional, Union, Dict, Any
from enum import Enum

@dataclass
class EventMessage:
    xmlns: str
    header: 'Header'
    payload: Union['PayloadJson1', 'PayloadJson2', 'PayloadJson3']

@dataclass
class Header:
    verb: str
    noun: 'NounEnum'
    timestamp: str
    messageId: str
    source: str
    properties: 'Properties'

@dataclass
class Properties:
    format: str
    businessDataIdentifier: 'BusinessDataIdentifier'

@dataclass
class BusinessDataIdentifier:
    businessDayFrom: str
    businessDayTo: str
    timeframe: str
    timeframeNumber: str
    processStep: str

@dataclass
class PayloadJson1:
    links: List['Link']
    rscKpi: Dict[str, str]

@dataclass
class PayloadJson2:
    failureReason: str
    operatorComment: str
    rscKpi: Dict[str, Any]

@dataclass
class Validation:
    status: str
    result: str
    validationType: str
    source: str
    validationMessages: List[str]

@dataclass
class PayloadJson3:
    messageId: str
    validation: Validation
    links: List['Link']

@dataclass
class Link:
    code: str
    link: str

class NounEnum(Enum):
    NounJson1 = "NounJson1"
    NounJson2 = "NounJson2"
    NounJson3 = "NounJson3"
