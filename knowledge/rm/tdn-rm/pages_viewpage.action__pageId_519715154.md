---
content_hash: 7fa0e00a781f9a0b1b2e89470888f500e39d5df85cfc5b66a9b04a1bbf32d0d5
fetched_at: '2026-06-29T00:10:30.282099+00:00'
page_id: '519715154'
product: rm
source: tdn-rm
title: Contabilização - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519715154
version: 22
---

Inibe reversão de Valores na provisão mensal de férias para situações onde houve abatimento de férias

Marcando esse parâmetro, no momento da contabilização do encargo de férias, o sistema irá contabilizar como valor de encargo de férias o valor do avo adquirido no mês, evitando, desta forma, valores negativos no encargo de provisão de férias e a consequente reversão de contas. Assim, os valores de férias aos funcionários poderão ser contabilizados através dos eventos de férias na movimentação.

OBSERVAÇÃO:

Com este parâmetro marcado as colunas 'Valor (com abatimento no mês)" e "Valor (sem abatimento no mês)" existentes em Cadastros | Funcionários | Anexos | Histórico de Provisões e em Encargos | Contabilização | Históricos | Provisões serão preenchidas.

DICA:

Veja também: [Exemplos para regra de cálculo dos encargos 5 - Provisão de FGTS de férias e 6 - Provisão de encargos de férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=790646098#1-1)

*Exemplo:* O funcionário tirou férias

* + Com o parâmetro **MARCADO:**

| Provisão **Acumulada de férias** | Valor Contabilizado baseado na provisão Mensal |
| --- | --- |
| R$1.200,00 | R$100,00 |
| R$1.300,00 | R$100,00 |
| R$1.400,00 | R$100,00 |
| **R$300,00** | **R$100,00** |

Ao contabilizar a provisão mensal de férias, o sistema abate o valor das mesmas (Salário de R$1.500,00 menos Férias no valor de R$1.200,00 = Provisão de Férias de R$300,00).

O Sistema gera o lançamento contábil no valor de R$100,00. Para calcular esse valor, o sistema considera o valor da provisão acumulada sem abater o valor das férias pagas ao funcionário e contabiliza apenas o valor do avo de férias, dessa forma o valor não ficará negativo e consequentemente não ocorra inversão das contas contábeis do encargo de férias.

* + Com o parâmetro **DESMARCADO**:

| Provisão **Acumulada de férias** | Valor Contabilizado baseado na provisão Mensal |
| --- | --- |
| R$1.200,00 | R$100,00 |
| R$1.300,00 | R$100,00 |
| R$1.400,00 | R$100,00 |
| **R$300,00** | **R$-1.100,00** |

Ao contabilizar a provisão mensal de férias, o sistema abate o valor das mesmas (Salário de R$1.500,00 menos Férias no valor de R$1.200,00 = Provisão de Férias de R$300,00).

O sistema gera o lançamento contábil no valor de R$1.100,00. Sendo esse, o valor da provisão do mês atual menos o valor da provisão do mês anterior, que ficará negativo ocorrendo então a inversão das contas contábeis.

Com o parâmetro marcado o sistema guarda os seguintes valores no histórico de provisões:

* **Valor:** O valor da provisão de férias abatendo férias no mês ou não, conforme parametrizado pelo usuário no campo "Provisão abate o valor das férias do mês" no momento da geração do histórico de provisões.
* **Valor (com abatimento no mês):** O valor da provisão com abatimento das férias do mês.
* **Valor (sem abatimento no mês):** O valor da provisão sem abatimento das férias do mês.
* **Valor pago de férias no mês:** Este campo será preenchido com o valor da provisão com abatimento das férias do mês, menos o valor da provisão sem abatimento das férias do mês.

Veja um exemplo de variação destes campos:

* + A empresa confirmou o parâmetro "Inibe reversão de Valores na provisão mensal de férias para situações onde houve abatimento de férias".
  + O funcionário tirou férias em maio
  + A empresa gera provisão abatendo férias do mês.

| Mês | Valor de provisão de Férias | Valor com abatimento de Férias | Valor sem abatimento de Férias |
| --- | --- | --- | --- |
| Janeiro | R$1.300,00 | R$1.300,00 | R$1.300,00 |
| Fevereiro | R$1.400,00 | R$1.400,00 | R$1.400,00 |
| Março | R$1.500,00 | R$1.500,00 | R$1.500,00 |
| Abril | R$1.600,00 | R$1.600,00 | R$1.600,00 |
| Maio | R$500,00 | R$500,00 | R$1.700,00 |

Quando o parâmetro está desmarcado a provisão é calculada sempre através da subtração do Valor de provisão de Férias do mês - o Valor de provisão de Férias do mês anterior (R$500,00 - R$1.600,00 = R$-1.100,00 ).

Quando o parâmetro está marcado a provisão é calculada sempre através da subtração do Valor sem abatimento de Férias do mês atual - o Valor com abatimento de Férias do mês anterior (R$1.700,00 - R$1.600,00 = R$100,00).

Acontece que na base do cliente as férias do mês atual já foram liberadas, portanto o campo Valor sem abatimento de férias está sendo gerado com o abatimento de férias, é como se no exemplo acima o mês de maio estivesse sendo informado da seguinte maneira:

| Mês | Valor de provisão de Férias | Valor com abatimento de Férias | Valor sem abatimento de Férias |
| --- | --- | --- | --- |
| Maio | R$500,00 | R$500,00 | R$500,00 |

Nesta situação a conta valor sem abatimento do mês atual - valor com abatimento do mês anterior seria a seguinte:  R$500 - R$1.600,00 = R$-1.100,00.

Portanto, para que o parâmetro funcione de maneira adequada é necessário efetuar a provisão antes de liberar as férias que iniciam e terminam no mês atual.

Atenção

Caso o usuário já tenha gerado o Histórico de Provisões dentro da competência atual e alterado esse parâmetro, o Histórico de Provisões DEVERÁ ser gerado novamente para refletir as alterações.

O sistema só irá manter as contas quando o funcionário estiver ativo. Para os funcionários demitidos no mês, o sistema não pode validar esse campo, quando ao gerar a provisão com a opção de "Zerar para demitidos no mês", pois a contabilização terá que zerar os encargos provisionado mês a mês na contabilidade, ao demitir o funcionário.

*Exemplo*  
Funcionário tinha uma provisão até outubro/2020 acumulada no valor de 10.000,00,  
Em novembro o mesmo foi demitido, e ao gerar a provisão mensal de férias, foi solicitado para zerar provisão para demitidos no mês;  
Então a provisão mensal será 0 -10.000,00 e ficará -10.000,00 (ou seja, valor negativo). Se o sistema não inverter as contas, irá levar mais 10.000,00 para cada conta, acumulando um valor de 20.000,00, ao invés de zerar o valor do funcionário na contabilidade.

Não lança histórico de provisões para estagiários

Este parâmetro foi criado com o objetivo de bloquear o lançamento de provisões 13° para estagiários.

Ao gerar  Histórico de Provisão, para funcionários do tipo 'T' com o parâmetro marcado, o processo irá gerar provisões referente a 13° com registro zerado, retornará valor apenas para funcionários dos tipos demais.

**Observação:** O parâmetro não impede o lançamento de provisões de férias ou por formula para funcionários do tipo 'T'.

Permite contas iguais a Débito e a Crédito

Quando esse parâmetro é marcado, o sistema possibilita o processamento da contabilização com a mesma conta para débito e crédito em um evento ou encargo. No entanto, a fim de garantir a compatibilidade com o RM Saldus, o sistema gera dois lançamentos, um para débito e outro para crédito.

Por outro lado, se o parâmetro for desmarcado, o RM Labore impede o uso simultâneo da mesma conta para débito e crédito.

Ajustar diferença (até R$ 0,99) entre débito e crédito lançando a diferença na última partida (Menu Configurações | Folha Normal | Contabilização | Parâmetros I)

Este parâmetro foi criado para os cenários em que a diferença entre as contas de débito e crédito seja de até R$ 0,99, permitindo que essa diferença seja registrada na última partida dos lançamentos contábeis.

## **Documentação**

* [Contabilização por centro de custo cadastrado na Seção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10658246199063-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-por-centro-de-custo-cadastrado-na-Se%C3%A7%C3%A3o)
* [Contabilização por centro de custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8895372319511-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-por-centro-de-custo)
