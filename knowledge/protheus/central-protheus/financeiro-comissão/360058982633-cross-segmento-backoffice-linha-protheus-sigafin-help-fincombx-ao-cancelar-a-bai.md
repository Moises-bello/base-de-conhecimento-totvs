---
article_id: 360058982633
category: Financeiro - Comissão
content_hash: b63c39bb101cf62ac200fe4b58785f056725ce41aa55413edb6cc46cb42bd7d4
fetched_at: '2026-06-28T22:37:50.728485+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - HELP: FINCOMBX ao cancelar
  a baixa de título com comissão'
type: support-article
updated_at: '2026-02-10T17:07:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058982633-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-HELP-FINCOMBX-ao-cancelar-a-baixa-de-t%C3%ADtulo-com-comiss%C3%A3o
---

**Dúvida**  
Ao realizar o cancelamento de uma baixa, é exibido o help FINCOMBX?

**Ambiente**  
Microsiga Protheus – Financeiro – FINA070 – A partir da versão 12.  
  
**Solução**  
Quando um título possui vendedor com comissão, a baixa parcial gera o respectivo valor de comissão. Por esse motivo, o cancelamento deve ser realizado **sempre iniciando pelas parcelas mais recentes**, ou seja, da **última para a primeira**.

**Exemplo:**

Considere um título no valor de **R$ 10.000,00**, com as seguintes baixas parciais registradas:

* 1ª baixa: R$ 3.000,00
* 2ª baixa: R$ 2.000,00
* 3ª baixa: R$ 4.000,00

Para cancelar a **baixa de R$ 3.000,00** (1ª), será necessário primeiro **cancelar a baixa de R$ 4.000,00** (3ª), depois **a de R$ 2.000,00** (2ª), e só então será possível cancelar a baixa desejada.

![Gravar_2025_08_04_08_57_39_626.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33925930361239)

Essa sequência garante a integridade dos dados relacionados à comissão.

**Importante**

Caso a comissão já tenha sido paga e esteja vinculada ao módulo de Contas a Pagar, será apresentada a seguinte mensagem:

> ***“Existe título de comissão gerado no Contas a Pagar para esta baixa. Deseja excluí-lo agora?”***

Para prosseguir, basta confirmar a exclusão.  
Em seguida, será exibida uma mensagem informando que o registro será removido tanto da rotina de Contas a Pagar quanto da manutenção de comissão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33925930362903)

**Saiba mais**  
[Novo Conceito - Mensagem FINCOMBX](https://tdn.totvs.com/display/public/PROT/FINA070+Novo+Conceito+-+Mensagem+FINCOMBX)
