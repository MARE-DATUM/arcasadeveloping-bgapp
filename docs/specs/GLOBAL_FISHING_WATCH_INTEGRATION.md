# 🎣 Global Fishing Watch API Integration Spec
## Especificação de Implementação para BGAPP

**Data de Criação:** 16/09/2025
**Versão:** 1.0.0
**Status:** Em Desenvolvimento

---

## 📋 Sumário Executivo

### Objetivo
Integrar a Global Fishing Watch (GFW) API no BGAPP para enriquecer os mapas com dados de atividade pesqueira em tempo real, melhorando a experiência do utilizador e fornecendo informações valiosas para gestão marinha.

### Benefícios Esperados
- **🎣 Monitorização de Pesca:** Visualização em tempo real de atividades pesqueiras
- **🚢 Tracking de Embarcações:** Acompanhamento de navios e frotas pesqueiras
- **📊 Análise de Densidade:** Mapas de calor de atividade pesqueira
- **🌊 Gestão Sustentável:** Apoio à gestão de recursos marinhos
- **⚠️ Alertas:** Detecção de pesca ilegal ou em áreas protegidas

---

## 🔑 Credenciais da API

```javascript
const GFW_API_CONFIG = {
  token: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtpZEtleSJ9.eyJkYXRhIjp7Im5hbWUiOiJCR0FQUCIsInVzZXJJZCI6NTA0NzEsImFwcGxpY2F0aW9uTmFtZSI6IkJHQVBQIiwiaWQiOjMyNzMsInR5cGUiOiJ1c2VyLWFwcGxpY2F0aW9uIn0sImlhdCI6MTc1Nzk2MTc5MCwiZXhwIjoyMDczMzIxNzkwLCJhdWQiOiJnZnciLCJpc3MiOiJnZncifQ.exNtfPb4WFo3qp-qmCUBQUXDch5Q70Xxp4EB672VZU-YnaxlXuVXTS7mTLC798yzYmnaTPdI-UfvTl5jNNMiyP591jXUy7eYH2pZc_c4SZQIeyiMlmDuLgf30CCEcpEy3yVdVv2NJBd985U8yYfH2SWoinZxUCFhi64OuDA7GF2eq8Y5t2Pf-QzNVqA4lLxebrn8meN2gptRVKpMAL9ovLfYuJfCICkiGhboGBI4gvPnkjPpZs3J3Fpar_sDmXODiaP6Ojx5scdN8gtcexYX4TO8WjeuRt_Zv_kGXbBMyitmHzspQDPsNcVmhhZQBGH5P3E2cViKGqCPNoed8Gotr0QBrna11EI21pKuW9cixNneTLRlDY0tB-4LkTSqfmAP41KCuCKrLfOUsBO5etfv-G-y-XVhOgyrFjxrKCDh2MMIv4AkNXYi66e8_eclii8r2g8rE3gVhQn_865PwboyPqT34qBYDIxwP0SPsmrRQ6oq6Z1kVFRfDZMrqR_luQlV',
  baseUrl: 'https://api.globalfishingwatch.org/v3',
  endpoints: {
    vessels: '/vessels',
    events: '/events',
    activity: '/4wings/tiles',
    heatmap: '/4wings/heatmap',
    encounters: '/encounters',
    portVisits: '/port-visits',
    vesselInfo: '/vessel-info',
    ais: '/ais',
    vms: '/vms',
    stats: '/stats'
  }
};
```

---

## 🏗️ Arquitetura de Integração

### 1. Componente Principal: GFWIntegration

```javascript
// infra/frontend/assets/js/gfw-integration.js

class GFWIntegration {
  constructor() {
    this.apiConfig = GFW_API_CONFIG;
    this.map = null;
    this.layers = new Map();
    this.activeFilters = {
      timeRange: { start: null, end: null },
      vesselTypes: [],
      flags: [],
      gearTypes: []
    };
  }
  
  // Métodos principais
  async initialize(leafletMap) {...}
  async loadVesselActivity(bounds) {...}
  async loadFishingEvents(params) {...}
  async createHeatmapLayer(data) {...}
  async trackVessel(mmsi) {...}
  async detectIllegalFishing(areaPolygon) {...}
}
```

### 2. Endpoints da API

#### 2.1 Vessel Activity
```javascript
GET /4wings/tiles/{z}/{x}/{y}
Headers: {
  'Authorization': `Bearer ${token}`,
  'Content-Type': 'application/json'
}
Query Parameters:
- dataset: 'public-global-fishing-activity'
- start-date: 'YYYY-MM-DD'
- end-date: 'YYYY-MM-DD'
- vessel-groups: ['fishing', 'carrier', 'support']
```

#### 2.2 Vessel Information
```javascript
GET /vessels/{vesselId}
Response: {
  id: string,
  mmsi: number,
  name: string,
  flag: string,
  type: string,
  length: number,
  tonnage: number,
  gear_type: string
}
```

#### 2.3 Fishing Events
```javascript
GET /events
Query Parameters:
- type: 'fishing'
- start-date: 'YYYY-MM-DD'
- end-date: 'YYYY-MM-DD'
- bbox: 'minLon,minLat,maxLon,maxLat'
```

---

## 📊 Funcionalidades a Implementar

### Fase 1: Integração Base (Semana 1)
- [x] Configuração segura do token da API
- [ ] Classe base GFWIntegration
- [ ] Integração com map-controller.js existente
- [ ] Carregamento de tiles de atividade pesqueira
- [ ] Visualização básica no mapa

### Fase 2: Funcionalidades Avançadas (Semana 2)
- [ ] Filtros temporais (últimas 24h, 7 dias, 30 dias, personalizado)
- [ ] Filtros por tipo de embarcação
- [ ] Filtros por bandeira/país
- [ ] Heatmap de densidade de pesca
- [ ] Tracking de embarcações individuais

### Fase 3: Análise e Alertas (Semana 3)
- [ ] Detecção de pesca em áreas protegidas
- [ ] Análise de padrões de pesca
- [ ] Sistema de alertas em tempo real
- [ ] Relatórios estatísticos
- [ ] Exportação de dados

### Fase 4: UI/UX Enhancements (Semana 4)
- [ ] Painel de controle dedicado GFW
- [ ] Animações de movimento de embarcações
- [ ] Timeline interativo
- [ ] Legendas dinâmicas
- [ ] Modo de comparação temporal

---

## 🎨 Interface de Utilizador

### Controlos do Mapa
```html
<div class="gfw-controls">
  <!-- Filtro Temporal -->
  <div class="time-filter">
    <label>Período:</label>
    <select id="gfw-time-range">
      <option value="24h">Últimas 24 horas</option>
      <option value="7d">Últimos 7 dias</option>
      <option value="30d">Últimos 30 dias</option>
      <option value="custom">Personalizado</option>
    </select>
  </div>
  
  <!-- Tipo de Visualização -->
  <div class="view-type">
    <button class="active" data-view="activity">Atividade</button>
    <button data-view="heatmap">Mapa de Calor</button>
    <button data-view="tracks">Rotas</button>
    <button data-view="events">Eventos</button>
  </div>
  
  <!-- Filtros -->
  <div class="filters">
    <div class="filter-group">
      <label>Tipo de Embarcação:</label>
      <checkbox-group>
        <input type="checkbox" value="fishing" checked> Pesca
        <input type="checkbox" value="carrier"> Transporte
        <input type="checkbox" value="support"> Apoio
      </checkbox-group>
    </div>
    
    <div class="filter-group">
      <label>Tipo de Pesca:</label>
      <checkbox-group>
        <input type="checkbox" value="trawlers"> Arrasto
        <input type="checkbox" value="longliners"> Palangre
        <input type="checkbox" value="purse_seines"> Cerco
      </checkbox-group>
    </div>
  </div>
</div>
```

---

## 🔄 Integração com Componentes Existentes

### 1. Map Controller
```javascript
// infra/frontend/assets/js/map-controller.js
class BGAPPMapController {
  async initializeComponents() {
    const componentInitializers = [
      // ... componentes existentes ...
      { name: 'gfwIntegration', class: 'GFWIntegration' }, // NOVO
    ];
  }
}
```

### 2. Admin Dashboard
```typescript
// admin-dashboard/src/components/gfw/gfw-management.tsx
export function GFWManagement() {
  // Interface de gestão GFW
  // - Configuração de alertas
  // - Visualização de estatísticas
  // - Gestão de áreas monitorizadas
}
```

---

## 📈 Métricas de Sucesso

### KPIs Técnicos
- **Tempo de Resposta:** < 2s para carregar tiles
- **Taxa de Sucesso:** > 99% de requests bem-sucedidos
- **Performance:** Suporte para > 1000 embarcações simultâneas
- **Cache Hit Rate:** > 80% para tiles recorrentes

### KPIs de Negócio
- **Adoção:** 70% dos utilizadores usando funcionalidades GFW
- **Engagement:** Aumento de 40% no tempo de sessão
- **Insights:** 10+ alertas úteis gerados por semana
- **Satisfação:** NPS > 8 para novas funcionalidades

---

## 🚀 Plano de Deployment

### Ambiente de Desenvolvimento
1. Implementar integração base
2. Testes unitários e de integração
3. Validação com dados reais

### Staging
1. Deploy em ambiente de teste
2. Testes de carga
3. Validação com utilizadores beta

### Produção
1. Deploy gradual (feature flag)
2. Monitorização intensiva
3. Rollout completo após 1 semana

---

## 📚 Documentação Técnica

### Exemplos de Uso

#### Carregar Atividade de Pesca
```javascript
const gfw = new GFWIntegration();
await gfw.initialize(map);

// Carregar atividade na área visível
const bounds = map.getBounds();
const activity = await gfw.loadVesselActivity({
  bounds: bounds,
  startDate: '2025-01-01',
  endDate: '2025-01-31',
  vesselTypes: ['fishing']
});
```

#### Detectar Pesca Ilegal
```javascript
// Definir área protegida
const protectedArea = {
  type: 'Polygon',
  coordinates: [[...]]
};

// Detectar violações
const violations = await gfw.detectIllegalFishing(protectedArea);
if (violations.length > 0) {
  alert(`Detectadas ${violations.length} possíveis violações!`);
}
```

---

## 🔒 Segurança e Conformidade

### Gestão de Token
- Token armazenado de forma segura (variável de ambiente)
- Rotação regular de tokens
- Logs de acesso auditáveis

### Proteção de Dados
- Conformidade com GDPR/LGPD
- Anonimização de dados sensíveis
- Criptografia em trânsito

### Rate Limiting
- Implementar cache local para reduzir chamadas
- Respeitar limites da API (1000 req/hour)
- Implementar retry com backoff exponencial

---

## 📞 Contactos e Suporte

- **API Documentation:** https://globalfishingwatch.org/our-apis/
- **Developer Portal:** https://globalfishingwatch.org/data/
- **Support Email:** apis@globalfishingwatch.org
- **Status Page:** https://status.globalfishingwatch.org/

---

## 🎯 Próximos Passos

1. **Imediato:** Implementar classe GFWIntegration
2. **Hoje:** Configurar token seguro e testar conexão
3. **Esta Semana:** Integrar visualização básica no mapa
4. **Próxima Semana:** Adicionar filtros e controles UI
5. **Mês:** Lançar versão beta com todas funcionalidades

---

*Documento criado para o projeto BGAPP - Blue Growth Application Platform*
*Última atualização: 16/09/2025*
