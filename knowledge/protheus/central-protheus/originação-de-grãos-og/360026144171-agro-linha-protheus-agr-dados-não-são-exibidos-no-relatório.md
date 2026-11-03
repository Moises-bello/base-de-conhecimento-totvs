---
article_id: 360026144171
category: Originação de Grãos (OG)
content_hash: bbfdc34459127a6ae815bd77ae319fd43ab90650ac6433ea5a7fd3227861f6f1
fetched_at: '2026-06-28T22:45:38.972714+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Dados não são exibidos no relatório
type: support-article
updated_at: '2025-06-24T19:17:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026144171-Agro-Linha-Protheus-AGR-Dados-n%C3%A3o-s%C3%A3o-exibidos-no-relat%C3%B3rio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20350494283159)*** Tempo aproximado para leitura: **00:00:30 min****Ocorrência**Ao acessar a rotina de **Extrato de Contratos - OGR285** e imprimir o relatório, as informações de **Cadência de Entrega**, **Entregas**, **Fixações**, **Contas a Pagar**, **Contas a Receber**, **Amostras**, **Autorizações** e **Alterações do Contrato** não são exibidas. Como faço para que estas informações sejam exibidas?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**As informações não são exibidas porque os **parâmetros/perguntas** estão com o conteúdo **0**. Para que estas informações sejam exibidas é necessário que os parâmetros sejam preenchidos com o conteúdo **1**. O Sistema entende o conteúdo **0** como **Não** e o conteúdo **1** como **Sim**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **OGR285** e altere o conteúdo dos parâmetros de acordo com as informações que devem ser exibidas. **0** para **Não** e **1** para **Sim**;  
2. Imprima o Relatório;  
3. Para que o valor mais adequado fique salvo, basta que ele seja informado uma única vez nos parâmetros, e quando a rotina for aberta novamente o valor virá carregado.
