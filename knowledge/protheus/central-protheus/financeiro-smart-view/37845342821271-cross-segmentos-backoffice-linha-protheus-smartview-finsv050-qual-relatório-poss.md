---
article_id: 37845342821271
category: Financeiro - Smart View
content_hash: 118b4a826648214c719d6b8e2805f90e4d83c1c8dd80a4eaf646c6b22880c97d
fetched_at: '2026-06-28T22:37:44.850616+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - Smartview - FINSV050 - Qual relatório
  possibilita a emissão da listagem de bancos cadastrados?
type: support-article
updated_at: '2026-01-22T12:14:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37845342821271-Cross-Segmentos-Backoffice-Linha-Protheus-Smartview-FINSV050-Qual-relat%C3%B3rio-possibilita-a-emiss%C3%A3o-da-listagem-de-bancos-cadastrados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37845356444183) Tempo aproximado para leitura: **00:06 min**

**Dúvida**  
Qual o relatório disponível para emitir a listagem de bancos cadastrados no Protheus, após a descontinuação dos relatórios em ADVPL (FINR)?  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33.  
  
**Causa**

Com a descontinuidade dos relatórios **FINR** baseados em fontes ADVPL, a TOTVS disponibiliza os novos relatórios exclusivamente através da ferramenta **Smart View**.

Em razão da ausência de manutenção dos relatórios FINRs, os respectivos fontes foram liberados, possibilitando a realização de customizações, conforme documentação disponível no link:  
[**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Programas e Fontes de relatórios da area financeiro Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19877623150743-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Programas-e-Fontes-de-relat%C3%B3rios-da-area-financeiro-Protheus)

Para a listagem de Bancos, recomenda-se utilizar o novo objeto **Lista de Bancos (FINSV050)**.

Esta nova estrutura oferece uma visualização intuitiva dos dados dos Bancos cadastrados no ambiente (SA6), utilizando a visão de dados como recurso.

**Visão de Dados (XLSX):** Permite a manipulação dos dados em planilha, facilitando filtros e análises externas.  
Também é possível agrupar os campos por qualquer coluna, bem como ordenar da forma que achar conveniente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37845356445079)

**Importantes**

Este relatório foi incorporado recentemente e ainda não consta no pacote de menu padrão. Realize a inclusão manual do programa no menu do módulo Financeiro (SIGAFIN).

**Saiba Mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como adicionar um novo menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25803711858071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-adicionar-um-novo-menu)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Relatórios Descontinuados e Evoluídos - Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35450062315799-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Relat%C3%B3rios-Descontinuados-e-Evolu%C3%ADdos-Financeiro)

[Smart View - Financeiro](https://tdn.totvs.com/display/public/PROT/Smart+View+-+Financeiro)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Qual é o prazo limite para a manutenção dos relatórios FINR permanecer disponível?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33040712240791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Qual-%C3%A9-o-prazo-limite-para-a-manuten%C3%A7%C3%A3o-dos-relat%C3%B3rios-FINR-permanecer-dispon%C3%ADvel)  
[Configuração inicial Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=665287989)  
[Requisitos Mínimos](https://tdn.totvs.com/pages/viewpage.action?pageId=678582172)
