---
article_id: 1500011068802
category: SIGAEST - CUSTOS
content_hash: ecba50ea74fc4454d3a0c8aa5e2d38845daecdd1bf46f3931e619b8b0083d6ff
fetched_at: '2026-06-28T22:39:02.394757+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do parâmetro
  MV_CUSFIL
type: support-article
updated_at: '2026-06-19T19:58:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CUSFIL
---

O parâmetro MV\_CUSFIL no TOTVS Protheus define a valorização do custo médio no estoque: "A" unifica por armazém, "F" por filial e "E" por empresa. Cada opção impacta diretamente o cálculo e contabilização dos custos, devendo ser alterada com análise interna e acompanhamento especializado para evitar impactos no estoque.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39760830329879) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

Qual a utilidade do parâmetro MV\_CUSFIL e o que ele faz quando está com conteúdos A, F ou E?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**IMPORTANTE:** Este parâmetro é considerado no momento da implantação dos custos da empresa, sendo que sua utilização refletirá diretamente nos custos conforme a apropriação definida.

**Qualquer alteração desse parâmetro deve ser precedida de uma análise interna**, visando compreender o conceito aplicado à apropriação escolhida. O suporte padrão não orienta que seja feita a alteração deste parâmetro sem o devido conhecimento sobre os custos e os impactos que a mudança poderá causar no cálculo de suas movimentações/apurações. **Recomenda-se que a análise seja realizada internamente, com o acompanhamento de um consultor analista in loco**, para garantir o correto entendimento da regra de negócios e usabilidade. Se por alguma razão o parâmetro for alterado, **deve-se reinstalar as procedures de 14 a 22 sempre.**

No sistema é possível realizar a valorização do **Custo Médio** de três formas diferentes, através da configuração do parâmetro MV\_CUSFIL:

* **A** - Custo unificado por Armazém (aglutina o custo no cálculo por armazém).
* **F** - Custo unificado por Filial (aglutina o custo no cálculo por filial).
* **E** - Custo unificado por Empresa (aglutina o custo no cálculo por empresa).

Na sequência, detalharemos o funcionamento de cada um dos métodos de valorização.

**Custo Médio por Armazém**

Neste método de valorização do custo médio, cada armazém cadastrado no ambiente Estoque e Custos terá o seu custo médio unitário individualizado, ou seja, se um produto for cadastrado em mais de um armazém, cada armazém terá um custo médio unitário diferente e, portanto, a contabilização dos movimentos gerados para este armazém obedecerá ao custo gerado para cada armazém.

**Exemplo:**

| **Filial** | **Produto** | **Armazém** | **Quantidade** | **CM Unitário** | **Custo Total** |
| --- | --- | --- | --- | --- | --- |
| 01 | Lápis | 01 | 100,00 | 1,15 | 115,00 |
| 01 | Lápis | 02 | 100,00 | 1,25 | 125,00 |
| 01 | Lápis | 03 | 100,00 | 1,35 | 135,00 |
| 02 | Lápis | 01 | 100,00 | 1,45 | 145,00 |
| 02 | Lápis | 02 | 100,00 | 1,55 | 155,00 |
| 02 | Lápis | 03 | 100,00 | 1,65 | 165,00 |
| **Total** |  |  |  |  | **840,00** |

**Observe** que o custo unitário para cada armazém é individualizado, ou seja, será sempre diferente.

**Custo Médio por Filial**

Neste método de valorização do custo médio, todos os armazéns de uma mesma filial possuem o mesmo custo médio unitário, ou seja, qualquer alteração no custo médio de um armazém é automaticamente repassada para todos os armazéns de uma mesma filial, desde que o Armazém contenha quantidade e valor no período, ou mesmo tenha efetuado alguma movimentação dentro desse período. Portanto, a contabilização dos movimentos gerados para este armazém obedecerá ao custo gerado para cada filial.

**Exemplo:**

| **Filial** | **Produto** | **Armazém** | **Quantidade** | **CM Unitário** | **Custo Total** |
| --- | --- | --- | --- | --- | --- |
| 01 | Lápis | 01 | 100,00 | 1,25 | 125,00 |
| 01 | Lápis | 02 | 100,00 | 1,25 | 125,00 |
| 01 | Lápis | 03 | 100,00 | 1,25 | 125,00 |
| 02 | Lápis | 01 | 100,00 | 1,55 | 155,00 |
| 02 | Lápis | 02 | 100,00 | 1,55 | 155,00 |
| 02 | Lápis | 03 | 100,00 | 1,55 | 155,00 |
| **Total** |  |  |  |  | **840,00** |

Observe que o custo médio unitário para a filial 01 é igual em todos os armazéns (valor 1,25), ou seja, o custo médio foi unificado por filial. Observe, também, que na filial 02, o custo médio unitário é igual em todos os armazéns (valor 1,55), ou seja, o custo médio também foi unificado por filial.

**Custo Médio por Empresa**

O conceito de custo unificado por empresa consiste em realizar o somatório dos custos de todas as filiais da empresa corrente e aplicar uma média de custos entre todos os armazéns, desde que o Armazém contenha quantidade e valor no período, ou mesmo tenha efetuado alguma movimentação dentro desse período.

Considere o uso do parâmetro **MV\_AGCUSTO** para custo por FILIAL e EMPRESA ([Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como aglutinar os custos por empresa ou filial on-line?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033016073-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-aglutinar-os-custos-por-empresa-ou-filial-on-line)).

> **Importante:** Quando configurado para utilizar o custo unificado por empresa, a rotina Recálculo de Custo Médio recalcula o custo de todas as filiais da empresa corrente e atualiza os campos padrões de fechamento de estoque da tabela SB2 – Saldos em Estoque, bem como os campos de fechamento do custo em partes, quando utilizado.

Exemplo:

| **Filial** | **Produto** | **Armazém** | **Quantidade** | **Custo Unificado Armazém** | **Custo Unificado Filial** | **Custo Unificado Empresa** |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | A | 01 | 1,00 | 10,00 | 15,00 | 22,50 |
| 01 | A | 02 | 1,00 | 15,00 | 15,00 | 22,50 |
| 01 | A | 03 | 1,00 | 20,00 | 15,00 | 22,50 |
| 02 | B | 01 | 1,00 | 25,00 | 30,00 | 22,50 |
| 02 | B | 02 | 1,00 | 30,00 | 30,00 | 22,50 |
| 02 | B | 03 | 1,00 | 35,00 | 30,00 | 22,50 |

> **Importante:** Com o uso do conceito de custo unificado por empresa, ao processar o recálculo de custo médio, o Sistema sempre considera para o cálculo todas as filiais da empresa corrente, independentemente da seleção do parâmetro Cálculo de Custos por existente na rotina.

**Aplicação Prática:**

Considerando uma empresa que possua duas filiais, como por exemplo, a filial 01 – São Paulo e a filial 02 – Rio de Janeiro, com movimentações de estoque, verifique como calcula o custo unificado por empresa.

1. **Na filial 01 - São Paulo** foi registrado o documento de entrada 000001/U com as seguintes características:

| **Filial** | **Produto** | **Armazém** | **Quantidade** | **Custo** |
| --- | --- | --- | --- | --- |
| 01 | A | 01 | 1,00 | 10,00 |
| 01 | A | 02 | 1,00 | 15,00 |
| 01 | A | 03 | 1,00 | 20,00 |

2. **Na filial 02 - Rio de Janeiro** foi registrado o documento de entrada 009000/U com as seguintes características:

| **Filial** | **Produto** | **Armazém** | **Quantidade** | **Custo** |
| --- | --- | --- | --- | --- |
| 02 | A | 01 | 1,00 | 25,00 |
| 02 | A | 02 | 1,00 | 30,00 |
| 02 | A | 03 | 1,00 | 35,00 |

Após a execução da rotina Recálculo de Custo Médio, o Sistema atualiza o campo **Vlr. Final (B2\_VFIM1)**, da tabela SB2 - Saldo em Estoque, com o custo unificado.

Exemplo de Cálculo:

**Filial 01 - São Paulo**

| **Filial** | **Produto** | **Armazém** | **Quantidade** | **Custo** |
| --- | --- | --- | --- | --- |
| 01 | A | 01 | 1,00 | 22,50 |
| 01 | A | 02 | 1,00 | 22,50 |
| 01 | A | 03 | 1,00 | 22,50 |

**Filial 02 - Rio de Janeiro**

| **Filial** | **Produto** | **Armazém** | **Quantidade** | **Custo** |
| --- | --- | --- | --- | --- |
| 02 | A | 01 | 1,00 | 22,50 |
| 02 | A | 02 | 1,00 | 22,50 |
| 02 | A | 03 | 1,00 | 22,50 |

A definição da unificação do Custo normalmente é definida no processo de implantação do Protheus na empresa. Caso perceba que o seu parâmetro está configurado de uma maneira não condizente com a sua regra de negócio, recomendamos fortemente que acione, por meio do seu Executivo de Soluções de Negócios, a visita de um analista especializado TOTVS para acompanhamento da mudança da unificação para que não gere impactos no período de estoque.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
