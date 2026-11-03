---
content_hash: 63b7db386f346a618fb798cac5fb51eb7ea3802983bfd01fc271e335573707d1
fetched_at: '2026-06-29T00:09:18.660039+00:00'
page_id: '421388738'
product: rm
source: tdn-rm
title: Realocação Orçamentária de Extratos de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388738
version: 5
---

O processo de realocação orçamentária de extratos de caixa só ficará disponível quando o parâmetro "Ação sobre orçamento ao exceder orçamento" em Controle Gerencial | Integração Financeira estiver marcado como Bloqueia.

Para que um extrato de caixa afete o orçamento é necessário definir o efeito que o extrato realizará sobre o mesmo na aba dados adicionais do extrato.

Caso seja marcado Diminui Valor Realizado, será gerado um acréscimo no valor disponível para o orçamento.

Se marcado Aumenta Valor Realizado, o valor disponível para orçamento será subtraído. Nessa situação, se o valor exceder o valor total do orçamento, será apresentada uma mensagem:

*Mensagens do Controle Orçamentário*

*O Extrato de Caixa excede o valor disponível para o Orçamento.*  
 *Centro de Custo: xx.x* *Valor Excedente: R$ xxxx,xx*  
 *O Extrato de Caixa ficará Bloqueado!*

Quando isso acontecer, o campo Bloqueado Orçamento ficará marcado.

Os processos de liberar extrato bloqueado por orçamento, reprocessar extrato bloqueado por orçamento e realocação orçamentária é liberado através de permissão de acesso em Perfil | Acesso a menu.

**Liberar Extrato Bloqueado por Orçamento**

Atualiza o Valor Orçado no orçamento para o período movimentado acrescentando o valor bloqueado. Em seguida a movimentação orçamentária do extrato é desfeita e feita uma nova com o valor total. O extrato é desbloqueado.

**Reprocessar Extrato Bloqueado por Orçamento**

Quando o Valor Orçado no cadastro de Orçamento foi alterado manualmente e já há saldo suficiente para cobrir o valor bloqueado. O extrato/lançamento é reprocessado, a movimentação anterior de orçamento excluída e incluída uma nova com todo o valor movimentado. O extrato é desbloqueado.

**Realocação Orçamentária**

No registro de Orçamento realocado o Valor Recebido é atualizado com o valor vindo dos orçamentos selecionados no processo. Os orçamentos cedentes têm o Valor Cedido atualizado. O Extrato é reprocessado para considerar os novos valores e desbloqueado.
