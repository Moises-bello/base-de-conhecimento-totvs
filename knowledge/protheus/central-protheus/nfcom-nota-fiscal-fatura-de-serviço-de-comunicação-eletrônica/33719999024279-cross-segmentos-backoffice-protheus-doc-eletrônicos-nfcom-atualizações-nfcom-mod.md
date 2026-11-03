---
article_id: 33719999024279
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: 5629fbbce6d62c3fd62c99ac160340f18a442c2ba80fafaa68d84fc357bb797d
fetched_at: '2026-06-28T22:39:55.098177+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Atualizações
  NFCOM (Modelo 62)
type: support-article
updated_at: '2025-11-14T12:21:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33719999024279-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Atualiza%C3%A7%C3%B5es-NFCOM-Modelo-62
---

**Dúvida**  
Quais são as atualizações necessárias para implantar a NFCOM (Nota Fiscal Fatura de Serviço de Comunicação Eletrônica)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**  
Seguem abaixo os requisitos para implantação:  
  
**PROTHEUS**  
**1.** Atualização da rotina **SPEDNFE |** [**12.1.2310**](https://suporte.totvs.com/portal/p/10098/download?e=1124963)**[Somente garantia estendida]** **-** [**12.1.2410**](https://suporte.totvs.com/portal/p/10098/download?e=1171486)  
**2.** Inclusão dos arquivos **include danfcom.ch** na pasta includes dentro do Protheus **|** [**12.1.2310**](https://r.totvs.io/p/1211713) **-** [**12.1.2410**](https://r.totvs.io/p/1211710) e **tlpp-core.th |** [**Procedimentos**](https://tdn.totvs.com/pages/viewpage.action?pageId=619741238)  
**3.** Compilar os **rdmakes da NFComSefaz e danfcomii**: [clique aqui.](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)  
**4.** Aplicar o dicionário de dados fiscal, contendo a inclusão de novos campos na tabela de Complementos Fiscais (SFX), além da alteração do tamanho do F3\_PROTOC, de 15 para 17 caracteres: [12.1.2410.](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1182881)  
  
**TSS**  
**1.** Realizar a aplicação do pacote acumulado: [12.1.2410](https://suporte.totvs.com/portal/p/10098/download?e=1164047).  
**2.** Realizar a aplicação do pacote pontual: [12.1.2410.](https://r.totvs.io/p/1220974)  
**3.** Realizar a atualização das URL's do TSS: [clique aqui.](https://suporte.totvs.com/portal/p/10098/download?e=761864)  
**4.** Realizar a atualização dos schemas do TSS: [clique aqui.](https://suporte.totvs.com/portal/p/10098/download?e=761857)  
  
**Documentação Técnica do Desenvolvimento**: <https://tdn.totvs.com/pages/releaseview.action?pageId=959022386>.  
  
**IMPORTANTE**: Realizar um backup de toda a base (TSS e Protheus) antes das atualizações, evitando qualquer tipo de problema ou paralisação do ambiente.
