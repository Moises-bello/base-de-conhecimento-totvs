---
article_id: 19488827340567
category: TAF - REINF
content_hash: 223bcdcab83fbfd50164ed89cd688a154f45641509643314a3da82236b763486
fetched_at: '2026-06-28T22:41:34.914519+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - TAF - REINF - Como excluir
  documentos do TAF
type: support-article
updated_at: '2023-12-01T18:48:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19488827340567-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-TAF-REINF-Como-excluir-documentos-do-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19488804136087) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como efetuar a exclusão de documentos que foram integrados para o TAF para a geração da Reinf?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice Linha Protheus - TOTVS Automação Fiscal - Todas as versões

**Solução**

Existe algumas formas de excluir documentos do TAF:

* De forma manual, pelas rotinas dos documentos: Docs de Entrada/Docs de Saida, Faturas/Recibos e Pagamentos
* Pelo gerenciador de integração
* Pela rotina Exclusão por período Fiscal.

**1 - Docs de Entrada/Docs de Saida, Faturas/Recibos e Pagamentos**

Para excluir um documento de forma manual, acessar as rotinas abaixo:

Nota: Atualizações > Movimentos Reinf > Docs de Entrada/Docs de Saída

Titulo: Atualizações > Movimentos Reinf > Docs de Entrada/Docs de Saída

Pagamento: Atualizações > Movimentos Reinf > Docs de Entrada/Docs de Saída

Efetuar o filtro na rotina pelo número do documento, acessar o botão **Excluir**.

**2 - Pelo gerenciador de integração**

**Atenção**: a exclusão pelo gerenciador irá excluir do TAF todos os cadastros e movimentos que foram gerados naquele ticket de integração: [CROSS Segmentos - Backoffice Linha Protheus - TAF - REINF - Como excluir lote de cadastros e movimentos integrados pelo Extrator fiscal.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9299691472279-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Como-excluir-lote-de-cadastros-e-movimentos-integrados-pelo-Extrator-fiscal-)

**3 - Pela rotina Exclusão por período Fiscal.**

**Atenção**: a exclusão pela rotina exclusão por período fiscal irá excluir todos os movimentos e cadastros vinculados, ao utilizar a opção "Movimentos Fiscais", referente ao período que for informado na rotina:

[Cross Segmentos Backoffice Protheus - Automação Fiscal - Exclusão por Periodo Fiscal.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024356232-Automa%C3%A7%C3%A3o-Fiscal-Funcionalidades-Limpeza-da-base-de-dados-para-retransmiss%C3%A3o-de-eventos-ao-Governo)

**OBS: Não excluir os documentos caso os mesmos já tenham sido apurados no painel reinf. Primeiro excluir a apuração e depois os documentos.**
