---
content_hash: df515a238906a0b68f72f34d429419fa6a2b5548483fbca2e3e82fb502d92015
fetched_at: '2026-06-29T00:09:20.241923+00:00'
page_id: '422545682'
product: rm
source: tdn-rm
title: Lucro Exploração (ECF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545682
version: 17
---

#f5f5f5#363636noneLucro Exploração (ECF)

## **01. Sobre****Sobre**

As demonstrações dos cálculos do Lucro da Exploração e da Isenção devem ser demonstradas na ECF nos registros:  

**N600:** Demonstração do Lucro da Exploração e  
**N610:** Cálculo da Isenção e Redução do Imposto Sobre o Lucro Real 

false

***Observação 1:*** A única informação do N610 possível de edição é o valor da Redução por Reinvestimento, que neste momento não **será atendido**. As demais informações do registro são calculadas pelo PVA, sem opção de edição. Portanto, esse registro não será gerado.

***Observação 2:* O PVA valida alguns dos valores do lucro da exploração (N600) com base na DRE. Para evitar advertências nesses valores, é imprescindível que o Evento Tributário esteja coerente com a DRE parametrizada no Contábil, além disso, o mapeamento do Plano de Contas Referencial deve estar correto.**

Esses registros serão gerados para os itens do Detalhamento da Apuração que estiverem com os Códigos da Tabela Dinâmica N600 associados aos respectivos Registros.   
Nos Parâmetros da ECF deve estar marcado a opção "Lucro da Exploração" para que o registro seja gerado.  
O valor da isenção ou redução do IRPJ deve ser informado nos Registros:

* **N620 - Cálculo do IRPJ Mensal por Estimativa** (Campos 18 e 19, Isenção e Redução do Imposto e Redução por Reinvestimento, respectivamente, e
* **N630 - Cálculo do IRPJ Com Base no Lucro Real** (Campos 17 e 18 de mesma nomenclatura).

No caso da CSLL, a redução deve ser informada nos registros N660 (5, 6, 7, 8 e 9) e N670 (8, 9, 10, 11 e 12).

Importante!

O PVA calcula várias linhas no momento da importação e entre elas, estão as linhas do Lucro da Exploração;

No caso do Prouni, o cálculo do PVA ficará incorreto uma vez que ele não comtempla a aplicação da POEB para o cálculo. A orientação da SERPRO é que o ajuste seja realizado manualmente após a importação da escrituração;

No caso do IRPJ, o total da isenção/redução é lançado sob um único Código: **N620.18** (lucro real por estimativa) e **N630.17** (lucro real). Esse Código deve estar informado no Item Tributário do Grupo de Deduções do Tributo do evento "pai";

No caso da CSLL, como não são todas as atividades que possuem isenção da CSLL, o sistema irá realizar os lançamentos nos registros N660 e N670 de forma fixa:   
N660 - Cálculo da CSLL Mensal por Estimativa;

Se o Item do Evento Tributário estiver classificado com o Código **N600.2**, a isenção será registrada com o código **N660.5** para Estimativa e **N670.8** para Lucro Real (Isenção sobre o Lucro da Exploração Relativo ao Prouni);

Se o Item do Evento Tributário estiver classificado com o Código **N600.6**, a isenção será registrada com o código **N660.6** para Estimativa e **N670.9** para Lucro Real (Isenção sobre o Lucro da Exploração de Eventos da Fifa);

Se o Item do Evento Tributário estiver classificado com o Código **N600.7**, a isenção será registrada com o código **N660.7** para Estimativa e **N670.10** para Lucro Real (Isenção sobre o Lucro da Exploração da Atividade de Serviços - SPE - Eventos da Fifa);

Se o Item do Evento Tributário estiver classificado com o Código **N600.8**, a isenção será registrada com o código **N660.8** para Estimativa e **N670.11** para Lucro Real (Isenção sobre o Lucro da Exploração de Eventos do CIO);

Se o Item do Evento Tributário estiver classificado com o Código **N600.9**, a isenção será registrada com o código **N660.9** para Estimativa e **N670.12** para Lucro Real (Isenção sobre o Lucro da Exploração da Atividade de Serviços - SPE - Eventos do CIO);

## **Regra de validação dos campos N620.18 e N630.17:****Sobre**

O valor a ser indicado nesta linha corresponde ao informado na linha N610/76 (total de isenções/reduções), observando-se que este não pode ser superior à soma algébrica das linhas:

false

**[(Imposto  Adicional)  (Linha N620/7  N620/8  N620/9  N620/10  N620/11  N620/12  N620/13  N620/14  N620/15  N620/16  N620/17)].**

Sobre o imposto de renda devido no Brasil, correspondente a lucros, rendimentos ou ganhos de capital auferidos no exterior, não é permitida a dedução ou aplicação de qualquer valor a título de incentivo fiscal, devendo essa parcela ser excluída dos valores das linhas N620/3 e N620/4 no cálculo do limite acima discriminado.  
Devido à complexidade é necessário fornecer memória de cálculo da isenção ao usuário, porque o processo acima não será visualizado.

---
