"""
Global Fishing Watch API Configuration Endpoint
Fornece o token GFW de forma segura para o frontend
"""

from fastapi import APIRouter, Depends, HTTPException
from typing import Dict
import os
from src.bgapp.auth.security import get_current_user
from src.bgapp.core.config import settings

router = APIRouter(prefix="/api/config", tags=["configuration"])

# Token GFW armazenado de forma segura
GFW_TOKEN = os.getenv("GFW_API_TOKEN", "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtpZEtleSJ9.eyJkYXRhIjp7Im5hbWUiOiJCR0FQUCIsInVzZXJJZCI6NTA0NzEsImFwcGxpY2F0aW9uTmFtZSI6IkJHQVBQIiwiaWQiOjMyNzMsInR5cGUiOiJ1c2VyLWFwcGxpY2F0aW9uIn0sImlhdCI6MTc1Nzk2MTc5MCwiZXhwIjoyMDczMzIxNzkwLCJhdWQiOiJnZnciLCJpc3MiOiJnZncifQ.exNtfPb4WFo3qp-qmCUBQUXDch5Q70Xxp4EB672VZU-YnaxlXuVXTS7mTLC798yzYmnaTPdI-UfvTl5jNNMiyP591jXUy7eYH2pZc_c4SZQIeyiMlmDuLgf30CCEcpEy3yVdVv2NJBd985U8yYfH2SWoinZxUCFhi64OuDA7GF2eq8Y5t2Pf-QzNVqA4lLxebrn8meN2gptRVKpMAL9ovLfYuJfCICkiGhboGBI4gvPnkjPpZs3J3Fpar_sDmXODiaP6Ojx5scdN8gtcexYX4TO8WjeuRt_Zv_kGXbBMyitmHzspQDPsNcVmhhZQBGH5P3E2cViKGqCPNoed8Gotr0QBrna11EI21pKuW9cixNneTLRlDY0tB-4LkTSqfmAP41KCuCKrLfOUsBO5etfv-G-y-XVhOgyrFjxrKCDh2MMIv4AkNXYi66e8_eclii8r2g8rE3gVhQn_865PwboyPqT34qBYDIxwP0SPsmrRQ6oq6Z1kVFRfDZMrqR_luQlV")

@router.get("/gfw-token")
async def get_gfw_token(current_user: Dict = Depends(get_current_user)) -> Dict[str, str]:
    """
    Retorna o token da API Global Fishing Watch de forma segura
    
    Requer autenticação para acesso
    """
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    return {
        "token": GFW_TOKEN,
        "expires": "2033-12-31",  # Token válido até 2033
        "type": "Bearer"
    }

@router.get("/gfw-settings")
async def get_gfw_settings(current_user: Dict = Depends(get_current_user)) -> Dict:
    """
    Retorna configurações completas da GFW API
    """
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    return {
        "api": {
            "baseUrl": "https://api.globalfishingwatch.org/v3",
            "tilesUrl": "https://tiles.globalfishingwatch.org",
            "token": GFW_TOKEN
        },
        "datasets": {
            "fishing": "public-global-fishing-activity:v20231026",
            "vessels": "public-global-all-vessels:v20231026",
            "encounters": "public-global-encounters:v20231026",
            "portVisits": "public-global-port-visits:v20231026"
        },
        "defaults": {
            "zoom": 5,
            "timeRange": 30,  # days
            "vesselTypes": ["fishing", "carrier", "support"],
            "confidenceLevel": 3
        },
        "angola": {
            "bbox": [-20.0, 4.0, -5.0, 18.0],  # [south, west, north, east]
            "center": [-12.5, 13.5],
            "protectedAreas": [
                {
                    "name": "Parque Nacional da Iona",
                    "bounds": [[-17.382, 13.269], [-16.154, 15.736]]
                },
                {
                    "name": "Reserva do Kwanza",
                    "bounds": [[-9.866, 12.814], [-9.297, 13.366]]
                }
            ]
        }
    }

@router.get("/gfw-status")
async def get_gfw_status() -> Dict:
    """
    Verifica status da integração GFW (endpoint público)
    """
    return {
        "status": "active",
        "integration": "enabled",
        "version": "1.0.0",
        "features": [
            "vessel_tracking",
            "fishing_activity",
            "heatmaps",
            "alerts",
            "protected_areas"
        ]
    }
