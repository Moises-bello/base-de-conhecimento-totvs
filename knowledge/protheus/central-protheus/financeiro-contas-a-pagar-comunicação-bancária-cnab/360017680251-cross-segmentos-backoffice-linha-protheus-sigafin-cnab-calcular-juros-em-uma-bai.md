---
article_id: 360017680251
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: b90488622647623bb3769d31f4283bb8b2b7d91d79f2b6cff496b64d79933a53
fetched_at: '2026-06-28T22:37:55.315398+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Calcular juros
  em uma baixa Cnab quando banco não considera juros no valor recebido
type: support-article
updated_at: '2024-06-20T17:45:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017680251-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Calcular-juros-em-uma-baixa-Cnab-quando-banco-n%C3%A3o-considera-juros-no-valor-recebido
---

**Dúvida**O que é necessário para calcular o juros em uma  baixa CNAB, quando o banco não considera juros no valor recebido?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**Para calcular os juros quando o título é baixado parcialmente no **Retorno de Cobrança (FINA200)**, deverá informar o total do valor recebido através do ponto de entrada: **F200VAR**.   
Para baixar o título totalmente, o valor recebido deve ser tratado de forma a somar o valor do título com juros.  
  
A utilização do ponto de entrada: **F200VAR** é necessário quando o banco não retorna o valor do juros na posição: Valor Recebido no retorno CNAB. Para estes casos, onde os valores dos juros não consta na posição valor recebido, utilize o ponto de entrada: **F200VAR**, para que o sistema entenda a soma e considere da forma correta e baixe totalmente.

**Exemplo:****nValRec := nValRec + nJuros****Saiba Mais**[F200VAR - CNAB Receber - Manipular variáveis no processamento do retorno](https://tdn.totvs.com/pages/viewpage.action?pageId=235308494)
