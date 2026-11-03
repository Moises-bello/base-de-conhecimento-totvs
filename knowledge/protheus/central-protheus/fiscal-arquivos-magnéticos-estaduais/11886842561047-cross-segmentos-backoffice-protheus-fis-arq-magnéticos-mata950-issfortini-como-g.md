---
article_id: 11886842561047
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 8e9fab9bbf053271454c827f4fb4ee2cb10c3f2b5d6ce5e3425ac6c1e49b9ab5
fetched_at: '2026-06-28T22:42:09.197362+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - MATA950 - ISSFORT.INI
  - Como gerar o campo 30 -  Código de Natureza para importação do ISS Fortaleza (CEISS)?
type: support-article
updated_at: '2023-01-24T12:54:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11886842561047-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MATA950-ISSFORT-INI-Como-gerar-o-campo-30-C%C3%B3digo-de-Natureza-para-importa%C3%A7%C3%A3o-do-ISS-Fortaleza-CEISS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o campo **30 - Código de Natureza da Operação** para importação do **ISS Fortaleza (ISSFORT.INI)** pela Rotina **MATA950**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Para gerar o campo **30 - Código de Natureza da Operação** o Protheus valida os dados do campo **FT\_ISSST**, conforme trecho abaixo do código fonte:  
  
**//30-Código da Natureza da Operação**  
**IF (cAliasSFT)->FT*ISSST$"1|2|3|4|5|6" TRB->CODNAT := Val((cAliasSFT)->FT*ISSST)**  
**Else**  
**TRB->CODNAT := 7**  
**EndIf**  
  
Para alimentar o campo **FT\_ISSST**, é validado o conteúdo do campo **Pgto Imposto (F4\_ISSST)** do cadastro de **TES** utilizado na escrituração da nota.

![](https://totvssuporte.zendesk.com/attachments/token/lmGPtUJKJGjWbSmwaQFOdzprP/?name=image.png)  
  
Caso, a escrituração tenha sido feita sem o preenchimento do campo em questão, é preciso realizar o preenchimento conforme necessidade e reprocessar as notas.

Segue Boletim Técnico da Obrigação Fiscal:

https://tdn.totvs.com/pages/releaseview.action?pageId=698290690
