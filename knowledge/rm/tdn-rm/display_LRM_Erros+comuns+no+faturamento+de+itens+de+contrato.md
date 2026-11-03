---
content_hash: e9bb425c76385b0afe4094a7764cbac4145352aafb344e5617824566c6346a25
fetched_at: '2026-06-29T00:09:25.274676+00:00'
page_id: '423938096'
product: rm
source: tdn-rm
title: Erros comuns no faturamento de itens de contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Erros+comuns+no+faturamento+de+itens+de+contrato
version: 6
---

Estes são alguns dos erros mais comuns que podem ocorrer durante o faturamento de um item de contrato, seja pela visão da tela de manutenção de contratos quanto na tela de Lotes   
  
**Causas**

1. Status do Item de Contrato não permite faturamento.

**Solução:**Verificar se o status do item permite faturamento, para isso você deve editá-lo no Menu Cadastro/Tabelas de Contratos/Status do Contrato, e verificar o campo "Faturamento".

2**.** Item totalmente Faturado.

**Solução:**Se o status de faturamento for do item for "Faturado" indica que o mesmo já foi totalmente faturado e que não há mais o que faturar;

         3. O período de faturamento é menor que períodos já faturados.

**Solução:**Se o "Status de faturamento" estiver como "Parc. Faturado" deve-se verificar se já existem movimentos já faturados para o mesmo item em períodos posteriores ao período de faturamento.

          4**.**O item de contrato não permite o faturamento com lançamentos em aberto para movimentos gerados para aquele item.

**Solução:**Verifique se o item de contrato já gerou movimentos anteriormente e se os lançamentos desses movimentos estão em aberto. Caso exista a necessidade de se faturar nessa situação a opção "Fatura Com Notas em Atraso" deve ser marcada no item do contrato.

5**.** Campo "Preço de Faturamento" incorreto.

**Solução:**O campo "preço de Faturamento" deve ser maior que 0,00 (zero).

6**.**Consistência do campo "N.F. Acompanha Boleto".

**Solução:**Se o campo "N.F. Acompanha Boleto".  estiver marcado no item, ele deverá ser marcado também no lote de faturamento do contrato.

          7. Tipo de Movimento informado incorretamente.

**Solução:**Verifique se o tipo de movimento parametrizado no item de contrato é o mesmo informado durante a tentativa de faturamento, seja pela Grid. ou pelo lote de faturamento do contrato.

8.Faturamento de item no período de carência.

**Solução:**Verificar no item de contrato na pasta datas os campos "Dias de carência" e "carência temporária".

9. Tipo de item incorreto entre lote e item de contrato.

**Solução:** Verificar se o tipo de item para faturamento (medição, periódico, não periódico) está consistente entre item e lote de faturamento.

10. Filtros obrigatórios e opcionais no lote de faturamento.

**Solução:**Verificar se os itens que se deseja faturar se adéquam aos filtros informados no lote de faturamento, todas as informações devem estar consistentes.

11. Mensagens de consistências no(s) movimento (s) a ser(em) criado(s).

**Solução:**Verificar as mensagens de erro no log de faturamento do lote.
