---
article_id: 37839781307671
category: Financeiro - Smart View
content_hash: b637364e488e5abda3dc899083f014e6358e45d2f57c538e085b3c3371de3270
fetched_at: '2026-06-28T22:37:44.687006+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINSV022 - Naturezas Financeiras
  - Qual relatório possibilita a emissão de naturezas cadastradas?
type: support-article
updated_at: '2026-01-22T12:12:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37839781307671-Cross-Segmentos-Backoffice-Linha-Protheus-FINSV022-Naturezas-Financeiras-Qual-relat%C3%B3rio-possibilita-a-emiss%C3%A3o-de-naturezas-cadastradas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37839781245079) Tempo aproximado para leitura: **00:06 min**

**Dúvida**  
Qual o relatório disponível para emitir a listagem de naturezas financeiras cadastradas no Protheus, após a descontinuação dos relatórios em ADVPL (FINR)?  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33.  
  
**Causa**

Com a descontinuidade dos relatórios **FINR** baseados em fontes ADVPL, a TOTVS disponibiliza os novos relatórios exclusivamente através da ferramenta **Smart View**.

Em razão da ausência de manutenção dos relatórios FINRs, os respectivos fontes foram liberados, possibilitando a realização de customizações, conforme documentação disponível no link:  
[**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Programas e Fontes de relatórios da area financeiro Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19877623150743-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Programas-e-Fontes-de-relat%C3%B3rios-da-area-financeiro-Protheus)

Para a listagem de naturezas, recomenda-se utilizar o novo objeto **Lista de Naturezas Financeiras (FINSV022)**.

Esta nova estrutura permite a visualização intuitiva dos dados de naturezas cadastradas no ambiente (SED) oferecendo dois recursos principais de saída:

1. **Recurso Relatório (PDF):** Gera um documento formatado para impressão PDF.
2. **Visão de Dados (XLSX):** Permite a manipulação dos dados em planilha, facilitando filtros e análises externas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37839756388119)

Recurso: **Relatório** - oferece os dados retornados no filtro para download em **PDF**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37839756392471)

Recurso: **Relatório** - oferece os dados retornados no filtro para download em**xlsx**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37839781260951)

***Importante:** A manutenção e suporte padrão são restritos aos relatórios ativos e via Smart View. Caso o cliente opte por utilizar os fontes descontinuados (FINRs) liberados para customização, a responsabilidade pela manutenção do código passa a ser do próprio cliente/parceiro.*

Saiba Mais

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Relatórios Descontinuados e Evoluídos - Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35450062315799-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Relat%C3%B3rios-Descontinuados-e-Evolu%C3%ADdos-Financeiro)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Qual é o prazo limite para a manutenção dos relatórios FINR permanecer disponível?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33040712240791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Qual-%C3%A9-o-prazo-limite-para-a-manuten%C3%A7%C3%A3o-dos-relat%C3%B3rios-FINR-permanecer-dispon%C3%ADvel)  
[Configuração inicial Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=665287989)  
[Requisitos Mínimos](https://tdn.totvs.com/pages/viewpage.action?pageId=678582172)
