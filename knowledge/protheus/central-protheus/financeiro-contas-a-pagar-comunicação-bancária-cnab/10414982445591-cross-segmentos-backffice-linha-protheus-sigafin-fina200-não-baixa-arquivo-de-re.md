---
article_id: 10414982445591
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 032dd0dc027cb39f37c7b1a120f431d322381adf5d4d748c46e59ae6d90a53bc
fetched_at: '2026-06-28T22:37:55.232396+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backffice Linha Protheus - SIGAFIN - FINA200 - Não baixa
  arquivo de retorno quando o título tem acréscimos e Juros
type: support-article
updated_at: '2022-11-25T21:43:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10414982445591-Cross-Segmentos-Backffice-Linha-Protheus-SIGAFIN-FINA200-N%C3%A3o-baixa-arquivo-de-retorno-quando-o-t%C3%ADtulo-tem-acr%C3%A9scimos-e-Juros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a baixa via retorno CNAB FINA200 de um título que possui acréscimos e Juros, o titulo não é baixado.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse cenário ocorre devido o valor original do título não bater com o valor recebido no arquivo de retorno, onde o valor do retorno consta o acréscimo somado ao valor da nota, mas sem referência do valor nas posições de Multa ou Juros para o acréscimo.  
  
**Solução**Neste caso, deve ajustar o parâmetro **MV\_REC2TIT = 1**, para que no momento da baixa via **RETORNO**, seja gerado um **RA** com o **valor do Acréscimos** e assim irá encerrar o título integralmente.

**Saiba mais:**  
[Retorno Cobranças (FINA200 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312167427)
