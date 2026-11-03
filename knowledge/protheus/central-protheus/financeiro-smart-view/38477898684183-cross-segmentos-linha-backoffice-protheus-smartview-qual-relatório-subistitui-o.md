---
article_id: 38477898684183
category: Financeiro - Smart View
content_hash: c1c024a3ead758ca68031e76d3d16319f7c2c4365f245d71fb7aaa3cbabb46da
fetched_at: '2026-06-28T22:37:44.892722+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - Smartview -  Qual relatório subistitui
  o FINR158, Títulos a pagar por natureza?
type: support-article
updated_at: '2026-02-18T17:22:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38477898684183-Cross-Segmentos-Linha-BackOffice-Protheus-Smartview-Qual-relat%C3%B3rio-subistitui-o-FINR158-T%C3%ADtulos-a-pagar-por-natureza
---

**Dúvida**  
Qual o relatório disponível para emitir a títulos a pagar por natureza (FINR158), após a descontinuação dos relatórios em ADVPL (FINR)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro a partir da Release 12.1.33  
  
  
**Solução**  
Com a descontinuidade dos relatórios **FINR** baseados em fontes ADVPL, a TOTVS passou a disponibilizar os novos relatórios exclusivamente por meio da ferramenta Smart View.

Em razão da ausência de manutenção dos relatórios FINRs, os respectivos fontes foram liberados, possibilitando a realização de customizações, conforme documentação disponível no link:  
[**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Programas e Fontes de relatórios da area financeiro Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19877623150743-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Programas-e-Fontes-de-relat%C3%B3rios-da-area-financeiro-Protheus)

Para a emissão do relatório de **Títulos a Pagar por naturezas** (antigo FINR855), recomenda-se a utilização do novo objeto:

**Títulos a Pagar por Naturezas (FINSV028)**

Essa nova estrutura contempla:

* Títulos a pagar em aberto ou baixados, conforme parâmetros informados pelo usuário;
* Identificação das naturezas através do título principal;

O relatório pode ser emitido no formato **“Visão de Dados”**, possibilitando a geração dos dados em formato de planilha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38477943843095)
