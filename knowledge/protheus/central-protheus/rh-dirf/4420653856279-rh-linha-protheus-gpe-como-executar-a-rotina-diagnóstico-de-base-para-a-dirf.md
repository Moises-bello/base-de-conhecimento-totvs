---
article_id: 4420653856279
category: RH – DIRF
content_hash: a07e9d5e65a7bf5c8ebe3fc6293508de0961762f91440a9d6c6ff002498ee7fd
fetched_at: '2026-06-28T22:44:06.867346+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como executar a rotina Diagnóstico de Base para
  a DIRF
type: support-article
updated_at: '2025-06-16T19:20:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420653856279-RH-Linha-Protheus-GPE-Como-executar-a-rotina-Diagn%C3%B3stico-de-Base-para-a-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23563878867607) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como executar a rotina Diagnóstico de Base para a DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**A rotina Diagnóstico para a DIRF valida as inconsistências entre o acumulado do funcionário, cadastro de verbas, acumulado de plano de saúde, transferências e cálculo de férias, conforme opções abaixo:

1 - **Avaliar Inconsistências da SRD:** Irá verificar se os campos Processo, Período, Roteiro e Número de Pagamento da tabela de histórico de movimentos (SRD) estão preenchidos. Encontradas inconsistências, os registros serão listados no LOG e deverão ser corrigidos via sistema.

2 - **Avaliar Inconsistências da SRV:** Irá verificar se existem verbas com incidência de IR (RV\_IR) e sem configuração para DIRF (RV\_DIRF). Encontrando inconsistências, os registros serão listados no LOG e deverão ser corrigidos via sistema.

3 - **Avaliar inconsistências no cadastro de plano de saúde:** Irá verificar se existe registros na tabela de planos ativos (RHK). Caso não seja encontrado nenhum registro, será informado no LOG. Caso a empresa não forneça plano de saúde, não é necessário marcar esta opção.

4 - **Avaliar inconsistências na SRE (Transferências):** Irá verificar se existe incoerência nos dados de origem e destino das transferências. Por exemplo, se funcionário saiu do Centro de Custo "A" e foi para o "B", na próxima transferência o Centro de Custo Origem deve ser "B", caso contrário, será exibido a inconsistência no LOG.

5 - **Avaliar inconsistências no cálculo de plano de saúde:** Irá verificar se os valores gravados na tabela de histórico de cálculo de plano de saúde (RHS) estão coerentes com os dados do histórico de movimento (SRD). Encontrando divergências, o registro será exibido no LOG.  
  
Pelo caminho **>Miscelânea >DIRF >Gerar Arquivo**, selecione a opção **Diagnóstico** e clique em Avançar:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420642504343)  
  
Faça a seleção conforme exemplo abaixo mas para o ano calendário da DIRF em questão e clique em Avançar:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11321581729943)  
  
Sistema gerará um log com as inconsistências encontradas:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420635751319)

Avalie as inconsistências e ajuste se necessário.  
  
  
**Saiba mais**  
[Artigos DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
