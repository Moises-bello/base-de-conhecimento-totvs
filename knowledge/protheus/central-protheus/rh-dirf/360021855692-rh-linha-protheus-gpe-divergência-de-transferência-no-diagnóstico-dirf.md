---
article_id: 360021855692
category: RH – DIRF
content_hash: 4035055f1202b14facd670e5dbff9a370a3029947f786c9d95f3246e36aab512
fetched_at: '2026-06-28T22:44:06.970309+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Divergência de transferência no diagnóstico DIRF
type: support-article
updated_at: '2025-08-19T20:50:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021855692-RH-Linha-Protheus-GPE-Diverg%C3%AAncia-de-transfer%C3%AAncia-no-diagn%C3%B3stico-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34302394066839)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**O que deve ser feito quando há divergências de transferências no diagnóstico da DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**O relatório gerado do diagnóstico da DIRF demonstrará as transferências realizadas independente do ano da DIRF.  
  
Deve ser analisada as divergências encontradas no ano de calendário da DIRF que esta sendo gerada.  
De acordo com o resultado do log, na rotina de **Transferência**, pelo caminho **>Atualizações >Funcionários >Transferências**, analise os campos indicados no log que estão inconsistentes e faça  ajuste se necessário.  
Considere sempre as **transferências realizadas na mesma versão** e que ficaram com campos incorretos ou em branco, tanto na origem quanto no destino.  
  
Após analisar as transferências e realizar os ajustes necessários, desconsidere as informações dos anos anteriores.  
  
Verifique também na **Manutenção Arquivo**, pelo caminho **>Miscelânea >DIRF >Manutenção Arquivo** se todas as informações foram geradas corretamente para funcionários que tiveram alguma transferência no ano calendário da DIRF em questão.

**Saiba mais**  
[RH - Linha Protheus - GPE - Como executar a rotina Diagnóstico de Base para a DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420653856279)
