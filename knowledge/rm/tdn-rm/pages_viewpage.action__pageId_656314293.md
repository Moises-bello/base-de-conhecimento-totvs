---
content_hash: 48ca9e660dd53a1e8954174f70398c55761b8c651fc9e5311208e00d807422ff
fetched_at: '2026-06-29T00:11:13.077291+00:00'
page_id: '656314293'
product: rm
source: tdn-rm
title: Como o Portal de Imóveis calcula a comissão de uma venda?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656314293
version: 4
---

#FF9000Introdução

O Portal de Imóveis pode atribuir automaticamente a comissão do corretor que gerou a venda, mas para isto é necessário ter o percentual de comissão definido. O Portal possibilita que a comissão seja calculada pelo Empreendimento, Usuário, Imobiliária ou Grupo de Usuário, nesta ordem de precedência, ou seja, se definida uma comissão no cadastro do empreendimento esta irá sobrepor todas as demais.

Uma comissão pode ter seu valor lançado manualmente após proposta feita e entrando no menu de ações da proposta opção COMISSÃO (esta opção só aparece para propostas aprovadas). Ou calculada automaticamente pelo Portal de Imóveis baseado nos percentuais definidos no parágrafo acima. Para isto o parâmetro "Grava Comissão Diretamente" deve estar marcado como SIM.

Para saber mais sobre o menu de comissões, acesse o link clicando aqui: [Propostas - Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=570059863)

Se marcado como SIM ao salvar uma proposta o sistema criará automaticamente um valor de comissão. O Portal de Imóveis trata o percentual de comissão definido como sendo o teto de comissão a pagar, não permitindo lançar um valor maior que o definido pelo percentual aplicado aos componentes que estão com a opção de descontar comissão habilitados.

#FF9000Cálculos de Comissão

A comissão é calculada sobre o valor total da proposta multiplicando sobre o percentual da comissão do empreendimento, ou do usuário, ou da imobiliária ou do grupo do usuário, se todos estes campos estiverem zerados, o valor base de comissão e o valor da comissão serão zero.

Caso a soma das parcelas que permitem descontar comissão, não seja suficiente para pagar toda a comissão calculada, o valor da comissão será limitado no valor do componente que está marcado com *Desconta Comissão*.

É possível distribuir a comissão entre mais de um usuário, desde que esta não ultrapasse o teto permitido. Para lançar outras pessoas participantes da comissão basta inserir novos usuários clicando em ADICIONAR LINHA DE COMISSÃO.

Importante: No Portal de Imóveis existem parâmetros que permitem que o sistema calcule ou não o valor da comissão automaticamente e parâmetros que definem se uma proposta poderá avançar para próxima etapa sem comissão lançada. Para modificar estes parâmetros acesse Backend e em pesquisa de parâmetros utilize a palavra COMISSÃO:

* Grava comissão diretamente - para que o sistema já gere um valor de comissão para as propostas salvas

* Permitir efetivar propostas sem comissão - permite ou não que uma proposta avance para próxima etapa sem comissão gerada.
#FF9000Tipos de Comissão

## **Decrescente**

Este tipo de comissão retira o valor dos componentes na ordem em que estes aparecem até totalizar o valor da comissão.

Exemplo:

Empreendimento Zeus com comissão de 4%

Plano de pagamento

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Parcela** | **Data** | **Qtd** | **Valor** | **Comissão?** | **Total** |
| **Sinal** | 01/06/2019 | 1 | 5.000 | S | 5.000 |
| **Sinal** | 01/07/2019 | 1 | 5.000 | S | 5.000 |
| **Sinal** | 01/08/2019 | 1 | 5.000 | S | 5.000 |
| **Mensais** | 01/09/2019 | 10 | 2.000 |  | 20.000 |
| **Financiamento** | 01/10/2020 | 1 | 100.000 |  | 100.000 |
| **TOTAL** | | | | | **135.000** |
| **COMISSÃO PAGA PELA EMPRESA 4%** | | | | | **5.400** |

A comissão decrescente desconta o total de comissão da primeira parcela possível de se descontar comissão e se esta não possuir o valor total da comissão o restante será retirado das demais parcelas.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Parcela** | **Data** | **Qtd** | **Valor** | **Comissão?** | **Total** | **Comissão** |
| **Sinal** | 01/06/2019 | 1 | 5.000 | S | 5.000 | 5.000 |
| **Sinal** | 01/07/2019 | 1 | 5.000 | S | 5.000 | 400 |
| **Sinal** | 01/08/2019 | 1 | 5.000 | S | 5.000 | 0 |
| **Mensais** | 01/09/2019 | 10 | 2.000 |  | 20.000 |  |
| **Financiamento** | 01/10/2020 | 1 | 100.000 |  | 100.000 |  |
| **TOTAL** | | | | | **135.000** |  |
| **COMISSÃO PAGA PELA EMPRESA 4%** | | | | | **5.400** |  |

## **Parcelas Iguais**

Neste modelo de comissão o Portal de Imóveis irá encontrar o valor possível para igualar todas as parcelas de comissão entre os componentes possíveis de descontar a comissão. Exemplo

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Parcela** | **Data** | **Qtd** | **Valor** | **Comissão?** | **Total** |
| **Sinal** | 01/06/2019 | 1 | 2.000 | S | 2.000 |
| **Sinal** | 01/07/2019 | 1 | 7.000 | S | 7.000 |
| **Sinal** | 01/08/2019 | 1 | 4.000 | S | 4.000 |
| **Mensais** | 01/09/2019 | 10 | 2.000 |  | 20.000 |
| **Financiamento** | 01/10/2020 | 1 | 100.000 |  | 100.000 |
| **TOTAL** | | | | | **133.000** |
| **COMISSÃO PAGA PELA EMPRESA 4%** | | | | | **5.320** |

Total da comissão divido pela quantidade de componentes de onde se desconta a comissão, neste caso 5.320 / 3 = 1.773,33

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Parcela** | **Data** | **Qtd** | **Valor** | **Comissão?** | **Total** | **Comissão** |
| **Sinal** | 01/06/2019 | 1 | 2.000 | S | 2.000 | 1.773,33 |
| **Sinal** | 01/07/2019 | 1 | 7.000 | S | 7.000 | 1.773,33 |
| **Sinal** | 01/08/2019 | 1 | 4.000 | S | 4.000 | 1.773,33 |
| **Mensais** | 01/09/2019 | 10 | 2.000 |  | 20.000 |  |
| **Financiamento** | 01/10/2020 | 1 | 100.000 |  | 100.000 |  |
| **TOTAL** | | | | | **133.000** |  |
| **COMISSÃO PAGA PELA EMPRESA 4%** | | | | | **5.320** |  |

## **Parcelas proporcionais**

Nesta modalidade o valor da parcela de comissão é proporcional ao valor da parcela.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Parcela** | **Data** | **Qtd** | **Valor** | **Comissão?** | **Total** |
| **Sinal** | 01/06/2019 | 1 | 2.000 | S | 2.000 |
| **Sinal** | 01/07/2019 | 1 | 7.000 | S | 7.000 |
| **Sinal** | 01/08/2019 | 1 | 4.000 | S | 4.000 |
| **Mensais** | 01/09/2019 | 10 | 2.000 |  | 20.000 |
| **Financiamento** | 01/10/2020 | 1 | 100.000 |  | 100.000 |
| **TOTAL** | | | | | **133.000** |
| **COMISSÃO PAGA PELA EMPRESA 4%** | | | | | **5.320** |

O valor da comissão proporcional é calculado de acordo com a fórmula:

Valor da parcela / total de parcelas que descontam comissão \* valor total da comissão

Desta forma em nosso exemplo acima teremos:

TOTAL DA COMISSÃO: 5.320

TOTAL DAS PARCELAS QUE SE DESCONTA COMISSÃO: 13.000

* SINAL 1: 2.000 / 13.000 \* 5.320 = 818,46
* SINAL 2: 7.000 / 13.000 \* 5.320 = 2.864,61
* SINAL 3: 4.000 / 13.000 \* 5.320 = 1.636,92

Mais informações

---

[Frontend - Corretores - Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=563947886)

[Frontend - Gerencial - Comissões](https://tdn.totvs.com/pages/viewpage.action?pageId=624605091)

[Backend - Visão da Comissão](https://tdn.totvs.com/pages/viewpage.action?pageId=563947972)
