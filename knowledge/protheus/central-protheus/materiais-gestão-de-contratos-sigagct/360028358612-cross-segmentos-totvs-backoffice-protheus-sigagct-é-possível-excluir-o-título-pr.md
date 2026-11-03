---
article_id: 360028358612
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: a4282887aa364b98d660e25b50d60b77f36ccc6d958db22f89d1cd2cfe0b31a1
fetched_at: '2026-06-28T22:37:22.683400+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - É possível excluir
  o Título Provisório (PR) gerado no Financeiro pelo Gestão de Contratos ?
type: support-article
updated_at: '2023-09-05T18:20:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028358612-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-%C3%89-poss%C3%ADvel-excluir-o-T%C3%ADtulo-Provis%C3%B3rio-PR-gerado-no-Financeiro-pelo-Gest%C3%A3o-de-Contratos
---

**Dúvida**

Existe situação em que o **Título Provisório** tipo **PR** gerado no financeiro pelo SIGAGCT poderá ser excluído ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Quando o Contrato é alterado para vigente o módulo Gestão de Contrato cria os títulos Provisórios no módulo Financeiro na rotina Contas a Pagar ( Contrato de  Compras ) ou Contas a Receber (Contrato  de Vendas) que são relativos às parcelas do Cronograma Financeiro existente no contrato em questão.

***Por padrão, não é permitido excluir o registro dos títulos Provisórios diretamente no módulo Financeiro.***

Em um Contrato Vigente que já teve movimentações e medições, uma possibilidade de ser excluído um titulo provisório referente a uma parcela do Cronograma do Contrato, é realizar uma revisão destes contrato e zerar o saldo em aberto da parcela em questão do contrato, onde ao confirmar a Revisão como a parcela não possuirá saldo, o titulo relacionado será excluído.

Outras situações nas quais os **títulos provisórios** gerados pelo Gestão de Contratos são excluídos:

- Ao alterar/retornar a situação de um contrato de Vigente (onde os titulo foram criados) de volta para **Elaboração**, desde que não tenha ocorrido nenhuma movimentação.  exemplo uma medição.

- Alterar a situação de um contrato Vigente para **Sol. Finalização**.

- Alterar a situação de um contrato vigente para situação **Cancelado**.

***Saiba Mais:***

[MP - SIGAGCT - Como realizar o cancelamento de um Contrato no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052136373-MP-SIGAGCT-Como-realizar-o-cancelamento-de-um-Contrato-no-Gest%C3%A3o-de-Contratos-?source=search)

[MP - SIGAGCT - É possível alterar um contrato da situação de Solicitação de Finalização para Vigente ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022098611-MP-SIGAGCT-%C3%89-poss%C3%ADvel-alterar-um-contrato-da-situa%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%A3o-de-Finaliza%C3%A7%C3%A3o-para-Vigente-?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
