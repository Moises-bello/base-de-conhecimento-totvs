---
article_id: 360026385053
category: Gestão de Transportes (TMS)
content_hash: 0390de64db5a68d09cac16424b7c7a6429b8d96780736fb8410182a4474418e9
fetched_at: '2026-06-28T22:45:27.594791+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Contrato não encontrado para Fornecedor
  quando está configurado a rentabilidade
type: support-article
updated_at: '2023-11-01T19:51:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026385053-Log%C3%ADstica-Linha-Protheus-TMS-Contrato-n%C3%A3o-encontrado-para-Fornecedor-quando-est%C3%A1-configurado-a-rentabilidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:17 min  
  
Ocorrência**No fechamento da viagem, como resolver o problema da mensagem: **Contrato não encontrado para Fornecedor**.  
  
 **Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**O *help* é apresentado quando no **Pergunte** do **F12**,a opção**Rentab. Prévia Fechamento?** está configurada igual a **Sim**e não encontra o **Contrato** **de** **fornecedor**.  
  
O Sistema busca o **Contrato do Fornecedor** para montar o **Gráfico de Rentabilidade**, como não possui contrato, o sistema apresenta o *help* e não executa o fechamento.  
  
**Solução**Caso não trabalhe com o conceito de **Rentabilidade**, deverá alterar o valor da opção **Rentab. Prévia Fechamento** para **Não** no **F12** da rotina e fechar a viagem novamente.  
  
Caso trabalhe, deverá cadastrar o **Contrato de Fornecedor** referente ao carreteiro da viagem e demais cadastros importantes para funcionamento da rentabilidade e efetuar o fechamento da viagem novamente.  
  
**Saiba mais**Mais informações sobre a **Rentabilidade Prévia** podem ser verificadas no *link*: [Rentabilidade Prévia](http://tdn.totvs.com/pages/releaseview.action?pageId=286012727)
