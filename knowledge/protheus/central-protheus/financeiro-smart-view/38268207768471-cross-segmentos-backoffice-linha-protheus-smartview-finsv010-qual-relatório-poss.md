---
article_id: 38268207768471
category: Financeiro - Smart View
content_hash: b8d7d06adf13f35ff1c1d2c77e30065b2dc8e29ccb3786a68f1c2dde5469ddcf
fetched_at: '2026-06-28T22:37:44.846641+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - Smartview - FINSV010 - Qual relatório
  possibilita a emissão da listagem de baixas?
type: support-article
updated_at: '2026-02-09T17:33:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38268207768471-Cross-Segmentos-Backoffice-Linha-Protheus-Smartview-FINSV010-Qual-relat%C3%B3rio-possibilita-a-emiss%C3%A3o-da-listagem-de-baixas
---

**Dúvida**  
Qual é o relatório disponível para emitir a listagem de baixas realizadas no Protheus, após a descontinuação dos relatórios em ADVPL (FINR)?  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33.  
  
**Causa**

Com a descontinuidade dos relatórios**FINR** baseados em fontes ADVPL, a TOTVS disponibiliza os novos relatórios exclusivamente através da ferramenta **Smart View**.

Em razão da ausência de manutenção dos relatórios FINRs, as respectivas fontes foram liberadas, possibilitando a realização de customizações, conforme documentação disponível no link:  
[**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Programas e Fontes de relatórios da area financeiro Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19877623150743-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Programas-e-Fontes-de-relat%C3%B3rios-da-area-financeiro-Protheus)

Para a listagem de baixas, recomenda-se utilizar o novo objeto Baixas **(FINSV010)**.

O relatório FINSV010 emite as baixas na Carteira a Pagar ou a Receber, conforme o período e a moeda selecionados.

O documento apresenta informações detalhadas dos títulos, tais como nome do cliente ou fornecedor, natureza, vencimento, histórico, data da baixa, valor original e valor total pago. Além disso, relaciona os valores de juros, multas e taxa de permanência.

A Relação de Baixas pode ser emitida no formato "Visão de Dados" (XLSX).

Esse formato permite manipular os dados em planilha, facilitando a aplicação de filtros e análises externas. Além disso, é possível agrupar os campos por qualquer coluna e ordenar conforme sua necessidade.

![](https://tdn.totvs.com/download/attachments/769164286/image2023-6-9_14-54-14.png?version=1&modificationDate=1686333488040&api=v2)

**Saiba Mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como adicionar um novo menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25803711858071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-adicionar-um-novo-menu)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Relatórios Descontinuados e Evoluídos - Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35450062315799-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Relat%C3%B3rios-Descontinuados-e-Evolu%C3%ADdos-Financeiro)

[Smart View - Financeiro](https://tdn.totvs.com/display/public/PROT/Smart+View+-+Financeiro)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Qual é o prazo limite para a manutenção dos relatórios FINR permanecer disponível?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33040712240791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Qual-%C3%A9-o-prazo-limite-para-a-manuten%C3%A7%C3%A3o-dos-relat%C3%B3rios-FINR-permanecer-dispon%C3%ADvel)  
[Configuração inicial Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=665287989)  
[Requisitos Mínimos](https://tdn.totvs.com/pages/viewpage.action?pageId=678582172)
