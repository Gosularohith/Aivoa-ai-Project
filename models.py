from datetime import datetime
from typing import List, Optional
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class HCP(Base):
    __tablename__ = "hcps"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    specialty = Column(String(255))
    workplace = Column(String(255))
    interactions = relationship("Interaction", back_populates="hcp")

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    hcp_id = Column(Integer, ForeignKey("hcps.id"))
    date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)
    summary = Column(Text)
    outcome = Column(String(255))
    entities = Column(JSON)  # Extracted entities like products discussed
    status = Column(String(50), default="logged")  # logged, edited, etc.
    
    hcp = relationship("HCP", back_populates="interactions")
    versions = relationship("InteractionVersion", back_populates="interaction")

class InteractionVersion(Base):
    __tablename__ = "interaction_versions"
    id = Column(Integer, primary_key=True, index=True)
    interaction_id = Column(Integer, ForeignKey("interactions.id"))
    notes = Column(Text)
    summary = Column(Text)
    outcome = Column(String(255))
    modified_at = Column(DateTime, default=datetime.utcnow)
    
    interaction = relationship("Interaction", back_populates="versions")
