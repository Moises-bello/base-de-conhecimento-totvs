---
content_hash: 83144549962d291573395a385c65397a3de8433663c96d1cd47f1a3f98a5d872
fetched_at: '2026-06-29T00:09:20.078049+00:00'
page_id: '422545655'
product: rm
source: tdn-rm
title: INSS, SENAR, GILRAT e FUNRural
type: documentation
url: https://tdn.totvs.com/display/LRM/INSS%2C+SENAR%2C+GILRAT+e+FUNRural
version: 5
---

Em cumprimento da geração da EFD-Reinf – Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais, foram necessárias alterações no processo de apuração do INSS.  
 Para que ele seja corretamente apurado e gerado corretamente na rotina, as novas informações deverão ser imputadas no cadastro de INSS/PJ.  
 No cadastro de tributo, deverão ser criados tributos com as seguintes configurações:

| Tributo | Tipo Tributo | Procurar Alíquota no |
| --- | --- | --- |
| INSS | INSS | INSS/PJ - Fornecedor |
| INSS15 | INSS | INSS/PJ - Fornecedor |
| INSS20 | INSS | INSS/PJ - Fornecedor |
| INSS25 | INSS | INSS/PJ - Fornecedor |
| FUNRural | FunRural | INSS/PJ - Fornecedor |
| GILRAT | FunRural | INSS/PJ - Fornecedor |
| SENAR | FunRural | INSS/PJ - Fornecedor |

Desta forma ao incluir um Lançamento Fiscal estas informações poderão ser preenchidas na pasta Outros Tributos do item do lançamento.

***Atenção!*** Em um mesmo lançamento não poderá existir as informações de INSS e FunRural. O cadastro de lançamento não consiste a existência dos dois tributos simultaneamente, porém se forem adicionados juntos os dois serão gerados para a REINF.

* **Informações Originadas pelo Processo de Escrituração de Lançamentos (TOTVS Gestão de Estoque, Compra e Faturamento)**

Quando o movimento possuir o INSS nos tributos do item deverão, ser acrescentados os tributos INSS, INSS15, INSS20 e INSS25.

Para estes  quatro tributos deverá ser informado o tributo base INSS e respectivamente o INSS, INSS15, INSS20 e INSS25 como tipo de recolhimento.

Para todos os tributos, a opção "Procurar Alíquota Em" deve ser informado selecionado no Tributo .Desta forma quando o movimento gerado por este tipo for escriturado, as informações serão automaticamente gravadas nos campos correspondentes ao tributo INSS nos itens do Lançamento Fiscal.

Quando o movimento possuir o FunRural, nos tributos do Item do movimento, deverão ser acrescentados os tributos FunRural, GILRAT e SENAR. Para estes  três tributos deverá, ser informado o tributo base FunRural e respectivamente o FunRural, GILRAT e SENAR como tipo de recolhimento. Para todos, no item "Procurar Alíquota Em" deve ser informado selecionado no Tributo .Desta forma quando o movimento gerado por este tipo for escriturado, as informações serão automaticamente gravadas nos campos correspondentes ao tributo FunRural nos itens do Lançamento Fiscal.

A Apuração dos valores a serem pagos será feita como a somatória dos tributos.  
 **Total a pagar INSS** = INSS  INSS15, INSS20, INSS25  
 **Total a pagar FunRura**l = FunRural   SENAR  GILRAT
