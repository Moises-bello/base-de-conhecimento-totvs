---
article_id: 360017734431
category: Originação de Grãos (OG)
content_hash: 4cfb3b09041a1ed0df9bd4642edb292c29b3872eee0597d2f0a6fbd134fe9c08
fetched_at: '2026-06-28T22:45:38.976205+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Dados não são exibidos no relatório de contratos
type: support-article
updated_at: '2025-06-24T11:38:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017734431-Agro-Linha-Protheus-AGR-Dados-n%C3%A3o-s%C3%A3o-exibidos-no-relat%C3%B3rio-de-contratos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20350788971671)*** Tempo aproximado para leitura:**00:00:45 min  
  
Dúvida**Ao imprimir o relatório **OGR285 - Extrato de Contratos**, as informações de **Cadência de Entrega**, **Entregas**, **Fixações**, **Contas a Pagar**, **Contas a Receber**, **Amostras**, **Autorizações e Alterações do Contrato** não são exibidas. Como fazer para que estas informações sejam exibidas?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**As informações não são exibidas porque os **parâmetros/perguntas** estão com o conteúdo **0**. Para que estas informações sejam exibidas é necessário que os parâmetros sejam preenchidos com o conteúdo **1**.   
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar a rotina **OGR285** e alterar o conteúdo dos parâmetros de acordo com as informações que devem ser exibidas. **0** para **Não** e **1** para **Sim**;  
2. Imprimir o Relatório;  
3. Para que o valor mais adequado fique salvo, basta que ele seja informado uma única vez nos parâmetros, e quando a rotina for aberta novamente, o valor virá carregado.  
  
**Importante**  
O Sistema valida o conteúdo **0** como **Não** e o conteúdo **1** como **Sim**.
