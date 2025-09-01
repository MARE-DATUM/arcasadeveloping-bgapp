# BGAPP — Plataforma Científica para Biodiversidade Marinha de Angola 🇦🇴

Este repositório contém a implementação de uma plataforma Python especializada para investigação científica da **Zona Econômica Especial Marítima de Angola**. O sistema integra dados ambientais, biodiversidade e telemetria, suportando análises de biomassa, migração e ordenamento espacial com OGC APIs, STAC e integração com QGIS.

## 🌊 Características Específicas para Angola

- **Zona Econômica Exclusiva:** Configurada para 518.000 km² da ZEE angolana
- **Espécies Nativas:** Catálogo de 35+ espécies marinhas da costa angolana
- **Correntes Regionais:** Modelos das correntes de Benguela e Angola
- **Dados Pesqueiros:** Integração com estatísticas nacionais de pesca
- **Interface Móvel:** Otimizada para trabalho de campo em embarcações
- **Modo Offline:** Coleta de dados em áreas remotas com sincronização posterior

## Requisitos
- Python 3.11+
- Docker e Docker Compose
- (Opcional) `uv` ou `poetry` para gestão de dependências

## Arranque rápido
1. Copiar variáveis de ambiente:
   ```bash
   cp example.env .env
   ```
2. Subir a stack mínima:
   ```bash
   docker compose -f infra/docker-compose.yml up -d
   ```
3. Editar `configs/aoi.geojson` e `configs/variables.yaml` de acordo com a sua AOI e produtos.
4. (Opcional) Instalar dependências para executar conectores localmente:
   ```bash
   pip install -e .[dev,ingest,geo,orchestration]
   ```

## Estrutura
```
src/
  core/            # settings/utilitários
  ingest/          # conectores (CMEMS, MODIS, OBIS/GBIF, ERDDAP, etc.)
  process/         # processamento raster/cubos e métricas
  api/             # (futuro) processos pygeoapi
infra/
  docker-compose.yml
  pygeoapi/pygeoapi-config.yml
  pygeoapi/localdata/{aoi.geojson,occurrences.geojson,mcda.geojson}
  frontend/{index.html,dashboard.html}
configs/
  aoi.geojson
  variables.yaml   # crs: EPSG:4326
  species.yaml
scripts/
  fetch_obis_demo.py
  collect_metrics.py
  backup_minio.sh
notebooks/
dags/
  prefect_flow_demo.py
```

## 🚀 Serviços e URLs

### Serviços Backend
- **PostGIS:** `localhost:5432` (Base de dados espacial)
- **MinIO:** `http://localhost:9000` (Armazenamento de objectos, console: `:9001`)
- **STAC FastAPI:** `http://localhost:8081` (Catálogo de dados)
- **pygeoapi:** `http://localhost:5080` (APIs OGC abertas)
- **pygeoapi (protegido):** `http://localhost:8086` (login: demo/demo)
- **STAC Browser:** `http://localhost:8082` (Navegador de catálogo)
- **Keycloak:** `http://localhost:8083` (Autenticação, admin: admin/admin)
- **Admin API:** `http://localhost:8000` (API administrativa para gestão do sistema)

### Interfaces de Utilizador
- **⚙️ Painel Administrativo:** `http://localhost:8085/admin.html` *(ATUALIZADO - v2.1)*
  - 🎯 **Acesso direto** a todas as páginas e serviços BGAPP
  - 📊 **Monitorização em tempo real** do sistema
  - 🔧 **Gestão completa** de serviços (PostGIS, MinIO, STAC, etc.)
  - 📥 **Controlo de ingestão** com 9 conectores incluindo **CDSE Sentinel**
  - ⚙️ **Configuração** de AOI, espécies e variáveis
  - 👥 **Gestão de utilizadores** e segurança
  - 📝 **Logs do sistema** e backup/restore
  - 🚀 **Performance otimizada** com arquitetura modular
  - 🆕 **Novo conector Sentinel** via openEO para NDVI e bandas espectrais
- **🖥️ Dashboard Científico:** `http://localhost:8085/dashboard.html`
  - Índices de biodiversidade (Shannon, Simpson, Margalef)
  - Gráficos temporais e distribuição taxonômica
  - Filtros científicos avançados
  - Exportação de dados (CSV, GeoJSON, NetCDF)
- **📱 Interface Mobile:** `http://localhost:8085/mobile.html`
  - Coleta de dados em campo
  - GPS integrado e modo offline
  - Sincronização automática
- **🗺️ Mapa Interativo:** `http://localhost:8085` (Visualização básica)

### 🇦🇴 Coleções de Dados Angolanas
- `collections/aoi` — Zona Econômica Exclusiva de Angola
- `collections/occurrences` — Fauna marinha angolana (35+ espécies)
- `collections/fisheries` — Dados pesqueiros por zona (Norte/Centro/Sul)
- `collections/oceanography` — Correntes de Benguela e Angola
- `collections/mcda` — Mapas de adequação para conservação/pesca

## Makefile (atalhos)
```bash
make up | make ps | make down
make collections
make demo-data           # SPECIES/START/END opcionais
make metrics             # grava logs/metrics.jsonl
make backup              # backup local (pygeoapi/localdata)
```

## 🧪 Testes e Validação
```bash
# Testar integridade do painel administrativo
python scripts/test_admin_panel.py

# Iniciar painel administrativo automaticamente
python scripts/start_admin.py

# Verificar métricas do sistema
python scripts/collect_metrics.py
```

## 🌐 Acesso Remoto Seguro
```bash
# OPÇÃO 1: ngrok (Mais fácil - recomendado)
python scripts/setup_ngrok_tunnel.py

# OPÇÃO 2: Cloudflare Tunnel (Máxima segurança)
python scripts/setup_secure_access.py

# OPÇÃO 3: Túnel SSH (Se tens servidor)
python scripts/setup_ssh_tunnel.py
```

**Guia completo**: [docs/REMOTE_ACCESS_GUIDE.md](docs/REMOTE_ACCESS_GUIDE.md)

## Orquestração e CRS
- Orquestração de referência: Prefect 2.x (leve). Exemplo:
  ```bash
  python dags/prefect_flow_demo.py
  ```
- CRS padrão: EPSG:4326 (WGS84). Reprojeções para CRS locais (ex.: ETRS89 / PT-TM06) apenas quando necessário.

## Guia QGIS (OGC API Features)
1. Abrir QGIS → Data Source Manager → OGC API - Features
2. URL: `http://localhost:5080` → Conectar → Selecionar `aoi`, `occurrences` e `mcda`
3. Adicionar camadas ao projeto. Estilização:
   - `occurrences`: simbologia de pontos (vermelho, 3–4 px)
   - `mcda`: renderizador categorizado por `class` (alta/média/baixa)
4. Guardar projeto para referência.

## Licenças, ToU e Anonimização
- Copernicus (CDSE/CMEMS/CDS): dados abertos; citar fontes e termos.
- GBIF/OBIS: licenças por dataset (CC-BY/CC0). Citar DOI/origem.
- Movebank: muitos estudos requerem permissão explícita. Cumprir Data Use Terms.
- eBird: requer API key; limites/ToU. Dados completos via EBD sob pedido.
- Anonimização: para espécies sensíveis, aplique deslocamento/agregação espacial (ex.: jitter >1 km ou hex bins), supressão de locais de nidificação/ameaçados e janelas temporais agregadas (ex.: mensal).
- Governação: mantenha metadados de origem, datas de extração e versão; registe hashes dos ficheiros (ver `scripts/collect_metrics.py` para logging de base; expandir para hashing).

## 🧪 Exemplos de Uso para Angola

### Coleta de Dados Marinhos
```bash
# Dados de fauna marinha angolana (OBIS)
python -m src.bgapp.ingest.obis --taxonid 141438 --start 2024-06-01 --end 2024-06-30 \
  --aoi configs/aoi.geojson --out infra/pygeoapi/localdata/occurrences.geojson

# Dados pesqueiros da zona centro de Angola
python -m src.bgapp.ingest.fisheries_angola --type catch --zone zona_centro \
  --start 2024-01-01 --end 2024-12-31 --format geojson

# Dados oceanográficos regionais (Correntes de Benguela/Angola)
python -m src.bgapp.models.angola_oceanography --generate-grid --resolution 0.25 \
  --months 6,7,8,9 --out oceanography_angola.json

# Fontes de dados angolanas (INIP, UAN, MINAGRIP)
python -m src.bgapp.ingest.angola_sources --source inip --type fisheries \
  --start 2024-01-01 --end 2024-12-31
```

### Análise e Relatórios
```bash
# Gerar relatório científico automático
python -m src.bgapp.reports.angola_marine_report data/observations.json \
  --output relatorio_biodiversidade_angola

# Sincronização offline (para trabalho de campo)
python -m src.bgapp.offline.sync_manager --sync-all --export backup_campo.geojson

# Clorofila-a CMEMS (requer conta Copernicus Marine)
python -m src.bgapp.ingest.cmems_chla --start 2024-06-01 --end 2024-06-30 \
  --bbox 11.4,-18.5,16.8,-4.4  # ZEE Angola
```

## Desenvolvimento
- Linters: `ruff` e `mypy` configurados em `pyproject.toml`.
- Pre-commit:
  ```bash
  pip install pre-commit
  pre-commit install
  pre-commit run --all-files
  ```


