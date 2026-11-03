---
article_id: 25186146647575
category: Financeiro
content_hash: b724e2d0fdaa6b93cdd9b91fcfa626e7a1662920472992c9b7c45e74492769ce
fetched_at: '2026-06-28T22:38:03.110230+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA711 - Como é feito
  a atualização de saldos
type: support-article
updated_at: '2024-07-26T17:29:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25186146647575-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA711-Como-%C3%A9-feito-a-atualiza%C3%A7%C3%A3o-de-saldos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25186195690263) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como é atualizado o saldo das movimentações ao rodar o Job Fina711?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**

A atualização dos saldos é realizada pelo**Job FINA711** que é executado por grupo de empresas, sendo necessário o agendamento único para o grupo de empresas.  
   
O **Job FINA711** inclui registros nas tabelas**F75**e**F76** com informações das tabelas **SE1, SE2, SC5, SC6, SC7 e SC9**, salva no parâmetro **MV\_TFCJOBT** a data e hora da última execução.  
O ***Job*** é cadastrado automaticamente na execução do ***Wizard***. Para execução do **Job** é preciso um agente ativo no ***schedule*** do módulo **Configurador**:  
   
Sobre o conteúdo do parâmetro **MV\_TFCJOBT**  
   
A partir da liberação das perguntas para o ***JOB*** de **atualizações de saldos do NGF (FIN711)**, que possibilita ao cliente escolher se deverá processar os títulos e/ou pedidos, passou-se a armazenar a data de execução desses Jobs de forma isolada.  
  
**Exemplo:**

**TJOBDOC**: armazena a data e hora da última execução da atualização do saldo dos títulos;  
**TJOBORD**: armazena a data e hora da última execução da atualização do saldo dos pedidos;
