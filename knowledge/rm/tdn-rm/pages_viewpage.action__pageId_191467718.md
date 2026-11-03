---
content_hash: a1c93546feb3d280aae09d57a013b64277dcdecf2be8d1604e200422c1bfe38a
fetched_at: '2026-06-29T00:05:59.648673+00:00'
page_id: '191467718'
product: rm
source: tdn-rm
title: RMFIS00002_10.002 - Item Tributário - campo "Operação"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=191467718
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: 11.82.38 e** **12.1.5.105** |
| **Processo** | **:** | Evento Tributário |
| **Subprocesso** | **:** | Parametrização |
| **Data da publicação** | **:** | 03/07/2015 |

**Dica para utilização do campo "Operação", dentro do Item Tributário.**

Imagine o cenário de uma empresa tributada pelo Regime do **Lucro Presumido** que está parametrizando seu Evento Tributário e que essa empresa pratica atividade de transporte de cargas estando sujeita ao percentual de presunção do lucro de 8%.

Sabemos que os seguintes valores **NÃO** integram a **receita bruta** para apuração do tributo (Lei 8.541/1992, artigo 14, § 4°):

1. As vendas canceladas;
2. Os descontos incondicionais concedidos;
3. Os impostos não cumulativos cobrados destacadamente do comprador ou contratante dos quais o vendedor dos bens ou o prestador dos serviços seja mero depositário.

Portanto, esses valores devem ser **deduzidos** da receita bruta.

Considere que os valores acima foram contabilizados nas seguintes contas específicas:

* 4.2.1.01.005 - Receita com prestação de serviços          $ 1.464.628,69
* 4.2.1.01.006 - (-) Descontos concedidos                         $        4.000,00

, ficaria assim parametrizado o Evento Tributário:

Note que a conta onde foram registradas as receitas está com a Operação “**Soma**” e a conta onde foram registrados os descontos, está com a Operação “**Subtração**”. Dessa forma, ao calcular o valor do Grupo "Receita Bruta" do Evento Tributário, o sistema irá diminuir um do outro:

**OBSERVAÇÃO**: Nos dois Itens Tributários, o Código da Tabela Dinâmica será o mesmo (*4 - Receita Bruta Sujeita ao Percentual de 8%*), pois ao gerar a ECF, o que deve ser informado é o resultado final (*$1.460.628,69*).

**Quando, então, vou utilizar o Grupo de "Exclusões”?**

Este Grupo deve ser utilizado para excluir da Base de Cálculo os valores permitidos pela legislação (*no caso do Lucro Presumido*):
