---
article_id: 38428750568599
category: Financeiro - Smart View
content_hash: 2b232a0d41e975c480898be2afe6ca05a8657b6f64116b1c135ae84360a23e8a
fetched_at: '2026-06-28T22:37:44.895928+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - Smartview -  Qual relatório subistitui
  o FINR855, Títulos a pagar x impostos retidos?
type: support-article
updated_at: '2026-02-18T16:43:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38428750568599-Cross-Segmentos-Linha-BackOffice-Protheus-Smartview-Qual-relat%C3%B3rio-subistitui-o-FINR855-T%C3%ADtulos-a-pagar-x-impostos-retidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38432304617111) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Qual o relatório disponível para emitir a títulos a pagar com impostos retidos (FINR855), após a descontinuação dos relatórios em ADVPL (FINR)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro a partir da Release 12.1.33  
  
  
**Solução**  
Com a descontinuidade dos relatórios **FINR** baseados em fontes ADVPL, a TOTVS passou a disponibilizar os novos relatórios exclusivamente por meio da ferramenta Smart View.

Em razão da ausência de manutenção dos relatórios FINRs, os respectivos fontes foram liberados, possibilitando a realização de customizações, conforme documentação disponível no link:  
[**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Programas e Fontes de relatórios da area financeiro Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19877623150743-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Programas-e-Fontes-de-relat%C3%B3rios-da-area-financeiro-Protheus)

Para a emissão do relatório de **Títulos a Pagar com Impostos Retidos** (antigo FINR855), recomenda-se a utilização do novo objeto:

**Títulos a Pagar x Impostos Retidos (FINSV015)**

Essa nova estrutura contempla:

* Títulos a pagar em aberto ou baixados, conforme parâmetros informados pelo usuário;
* Identificação das retenções realizadas no título principal;
* Exibição dos dados correspondentes aos títulos de tributos vinculados.

O relatório pode ser emitido no formato **“Relatório”**, possibilitando a geração dos dados já estruturados para impressão em PDF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38476933350167)
