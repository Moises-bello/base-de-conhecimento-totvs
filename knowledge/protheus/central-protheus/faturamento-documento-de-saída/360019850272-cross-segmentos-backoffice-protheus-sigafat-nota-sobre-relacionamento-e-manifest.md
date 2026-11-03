---
article_id: 360019850272
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 0dc65fa59c0e6e98efeafe6771d6304cf915146400444f7e5d678a48b20f3535
fetched_at: '2026-06-28T22:38:44.099253+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Nota sobre Relacionamento
  e manifestação de CTE (Conhecimento de Transporte) em nota Nota Fiscal de Saída
type: support-article
updated_at: '2025-10-24T12:25:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019850272-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Nota-sobre-Relacionamento-e-manifesta%C3%A7%C3%A3o-de-CTE-Conhecimento-de-Transporte-em-nota-Nota-Fiscal-de-Sa%C3%ADda
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35853920660375) Tempo aproximado para leitura: **00:02:00 min******

**Dúvida**

É possível relacionar e manifestar CTE (Conhecimento de Transporte) em nota Nota Fiscal de Saída?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT – Todas as versões.

**Solução**

Por padrão, não é possível vincular um conhecimento de frete eletrônico à uma Nota de Saída, não faz parte da regra de negócios do módulo tratar CTe no documento de saída.

Hoje, o CTe é tratado apenas em módulo de Transporte (SIGATMS), e no módulo Compras (SIGACOM) que possui uma rotina que vincula o CTe ao Documento de Entrada.

A tratativa para cobrança de frete em Documentos de saída, é atribuir o valor no campo C5\_FRETE na emissão do Pedido de Vendas, neste caso o valor é somado e destacado no Documento de Saída e, também, compõe o título a receber (caso o TES seja configurado para gerar duplicata).

**Alternativas**:

* Caso a nota fiscal já esteja emitida e necessite adicionar o valor do Frete, é possível emitir uma nota de complemento de preço para cobrança do custo de frete;
* Caso utilize o módulo de TMS, como o módulo já possui de forma nativa a emissão de CTE, acesse a documentação para a emissão do Cte e para dúvidas da rotina consulte a equipe de atendimento Protheus TMS: [TMS0021 - Configuração básica para Emitir CT-e](http://tdn.totvs.com/pages/viewpage.action?pageId=269419567)
* Caso não seja transportador, utilize a opção Manifesto do destinatário, acesse a FAQ e para dúvidas da rotina consulte a equipe de atendimento Protheus SPED/TSS: [MDF-e - Manifesto Eletrônico de Documentos Fiscais](http://tdn.totvs.com/pages/viewpage.action?pageId=172299455)

**Importante:** Caso seja necessário gerar MDF-e de CTe, apenas o módulo de TMS efetua o procedimento em questão.

O MDF-e via SpedNfe somente é gerado pra Nota fiscal, segue documentação de TMS com os procedimentos para efetuar o MDF-e de um Cte: [Logística - Linha Protheus - TMS - Como emitir um MDF-e para CT-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019631891-Log%C3%ADstica-Linha-Protheus-TMS-Como-emitir-um-MDF-e-para-CT-e)

**Saiba mais:**

[FAT0079 Relacionar um CT-e ao Documento de Saída](https://tdn.totvs.com/x/BQQ-Dg)
