---
content_hash: f5977fb0ced299f111bce5f767e372b4560882bb39cf74d23d017ab0499341a4
fetched_at: '2026-06-29T00:10:38.929689+00:00'
page_id: '545626583'
product: rm
source: tdn-rm
title: Novidades da ECD
type: documentation
url: https://tdn.totvs.com/display/LRM/Novidades+da+ECD
version: 3
---

Com a implementação do Layout 8.0 referente ao ano-calendário 2019 da ECD os seguintes registros sofreram mudanças:

* **Bloco C:**Os registros do Bloco C não reflete em nenhum impacto no sistema, pois são preenchidos pelo próprio PGE do Sped Contábil, após a recuperação das informações da ECD anterior feita pelo usuário do programa, no menu Escrituração/Recuperar ECD anterior;
* **Registro 0000:** Adicionado os campos 21, 22 e 23:
  + 21:  Trata se a escrituração é centralizada ou descentralizada;
  + 22: Indica se houve mudança no plano de contas. Se houve algum registro I157 na escrituração significa que houve mudança no plano de contas;
  + 23: Código do Plano de Contas Referencial que será utilizado para o mapeamento de todas as contas analíticas.
* **J100:** Só poderão existir duas linhas de nível 1 no Balanço Patrimonial: Ativo (ou Ativo Total) e Passivo (ou Passivo Total, que engloba o Patrimônio Líquido);
* **J150:** Só poderá existir uma linha de nível 1 na DRE, que será o “Resultado do Exercício (Lucro ou Prejuízo Líquido do Exercício). Ou seja se a origem para elaboração do registro for plano de contas, é importante que exista **APENAS UMA** conta de primeiro nível entre as contas de resultado, caso contrário recomendamos que utilize como origem a ferramenta de demonstrações contábeis.
