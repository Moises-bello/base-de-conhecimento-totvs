---
article_id: 360042773913
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 902bc1b8bc83d39fce15156ab39607eae88d9ade26b0b51a317fb3bb56a18b82
fetched_at: '2026-06-28T22:38:33.014155+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Atualização automática do
  cadastro produto x clientes
type: support-article
updated_at: '2026-05-22T12:53:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042773913-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Atualiza%C3%A7%C3%A3o-autom%C3%A1tica-do-cadastro-produto-x-clientes
---

**Dúvida**  
Como é efetuado a atualização automática do cadastro produto x clientes?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.

**Solução**

A atualização automática do **cadastro Produtos X Clientes** (**MATA370**) é efetuado no momento do faturamento da nota de saída.

Na rotina "**Documentos de Saída (MATA460A)**" ao clicar no botão "**Prep.Doc's**", o sistema apresenta um grupo de perguntas para serem preenchidas, dentre essas perguntas tem a opção "**Atualiza Cli.X Prod?**", esta pergunta deve estar configurada como "**Sim**", desta forma todos os faturamentos passarão a popular a tabela (**SA7**) do cadastro de **Produtos X Clientes**.

![](https://totvssuporte.zendesk.com/attachments/token/GG7R8nPKhlThNlvQvDGqYCuU9/?name=inline-1501415613.png)

**Saiba mais:**

[FAT0114\_Cadastro\_Produtos\_X\_Clientes\_MATA370\_x\_Relatório\_Lista\_de\_Precos\_MATR785](https://tdn.totvs.com/x/1E_ZDg)
