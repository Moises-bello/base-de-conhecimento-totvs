---
content_hash: 27500a9f8e3b2a738bc1a46962f3570571deca5326d0923d06553ecea17ebed4
fetched_at: '2026-06-29T00:09:18.662416+00:00'
page_id: '421388739'
product: rm
source: tdn-rm
title: Realocação Orçamentária de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388739
version: 2
---

O processo de realocação orçamentária de lançamentos só ficará disponível quando o parâmetro "Ação sobre orçamento ao exceder orçamento" em Controle Gerencial | Integração Financeira estiver marcado como Bloqueia.

Para que um lançamento afete o orçamento é necessário que o tipo de documento do mesmo afete orçamento. Essa definição é feita dentro do cadastro no mesmo na aba Dados adicionais | Efeito sobre o orçamento.  
 Caso seja marcado Diminui Valor Realizado, será gerado um acréscimo no valor disponível para o orçamento.  
 Se marcado Aumenta Valor Realizado, o valor disponível para orçamento será subtraído. Nessa situação, se o valor exceder o valor total do orçamento, será apresentada uma mensagem:

*Mensagens do Controle Orçamentário*  
 *O Lançamento excede o valor disponível para o Orçamento.*  
 *Centro de Custo: xx.x* *Valor Excedente: R$ xxxx,xx*  
 *O Lançamento ficará Bloqueado!*

Quando isso acontecer, o campo Bloqueado Orçamento na aba Dados Adicionais do Lançamento ficará marcado.

Os processos de liberar lançamento bloqueado por orçamento, reprocessar lançamento bloqueado por orçamento e realocação orçamentária é liberado através de permissão de acesso em Perfil | Acesso a menu.

**Liberar Lançamento Bloqueado por Orçamento**

Atualiza o Valor Orçado no orçamento para o período movimentado acrescentando o valor bloqueado. Em seguida a movimentação orçamentária do extrato é desfeita e feita uma nova com o valor total. O lançamento é desbloqueado.

**Reprocessar Lançamento Bloqueado por Orçamento**

Quando o Valor Orçado no cadastro de Orçamento foi alterado manualmente e já há saldo suficiente para cobrir o valor bloqueado. O lançamento é reprocessado, a movimentação anterior de orçamento excluída e incluída uma nova com todo o valor movimentado. O lançamento é desbloqueado.

**Realocação Orçamentária**

No registro de Orçamento realocado o Valor Recebido é atualizado com o valor vindo dos orçamentos selecionados no processo. Os orçamentos cedentes têm o Valor Cedido atualizado. O lançamento é reprocessado para considerar os novos valores e desbloqueado.
