---
article_id: 36571120171287
category: Reforma Tributária
content_hash: 82a5c7036345e3fc2ff55d83d5ea071bbe8cb0fc2ad64cfd992ac8133a041acb
fetched_at: '2026-06-28T22:39:53.726083+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria
  - Rejeição 1022: Grupo IBS/CBS não informado [nItem: 999]'
type: support-article
updated_at: '2025-11-25T13:42:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36571120171287-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1022-Grupo-IBS-CBS-n%C3%A3o-informado-nItem-999
---

**Dúvida**  
Como corrigir a Rejeição 1022: Grupo IBS/CBS não informado [nItem: 999]?  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Se CST do IBS/CBS (tag: IBSCBS/CST) informado possui indicador que exige informação do IBS/CBS (ind\_gIBSCBS = 1):  
- Grupo gIBSCBS não informado (id: UB15, grupo: imposto/IBSCBS/gIBSCBS) Exceção: Esta RV não se aplica no caso de tpNFDebito=07-Perda em estoque.  
Observação 1: Consultar Tabela de Indicadores de CST do IBS e da CBS.

<https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=>

Para não ocorrer a rejeição 1022  é necessario que o Protheus e TSS estejam com as atualizações da documentação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

Importa que os parâmetros abaixo estejam criados e configurados no Protheus.

[Documentação do parâmetro MV\_CSTGXML](https://tdn.totvs.com/pages/viewpage.action?pageId=1011566715)

[Documentação do parâmetro MV\_RTC55](https://tdn.totvs.com/pages/viewpage.action?pageId=1013641031)

Obs: Caso seu TSS esteja em ambiente Cloud e seja compartilhado não haverá necessidade de solicitar atualização, pois a equipe TSS Cloud mantem o TSS sempre atualizado.
