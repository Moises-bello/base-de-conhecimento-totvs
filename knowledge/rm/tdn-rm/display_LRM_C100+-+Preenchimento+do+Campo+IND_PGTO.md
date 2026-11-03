---
content_hash: 705513b1de82c775d38973aed9d479a1752be403e9f2cdaeb21a7163c7cad75e
fetched_at: '2026-06-29T00:10:26.868407+00:00'
page_id: '515290160'
product: rm
source: tdn-rm
title: C100 - Preenchimento do Campo IND_PGTO
type: documentation
url: https://tdn.totvs.com/display/LRM/C100+-+Preenchimento+do+Campo+IND_PGTO
version: 3
---

O campo "IND\_PAGTO" do registro C100 da EFD Contribuições vai seguir as seguintes consistências para ser gerado: quando se trata de Lançamentos Originados do Nucleus (Movimento), é gerado usando a mesma regra de geração da NF-e, onde é verificado a condição de pagamento informada no movimento.   
  
Caso o Lançamento não seja proveniente do Movimento, será verificada a Data de Vencimento do lançamento fiscal (Integrações > Financeiro).   
Se a data de Vencimento for igual à Data de Emissão, o campo será gerado como "A Vista"; Se for diferente, o campo será gerado como "A prazo"; Se não estiver preenchida, será gerado como "Outros".

Esta alteração, além de manter a compatibilidade com o envio da NF-e, foi realizada para melhorar a performance da rotina, uma vez que não é mais realizado um select oneroso para o Banco de Dados, para verificar as faturas vinculadas ao Lançamento Fiscal.
