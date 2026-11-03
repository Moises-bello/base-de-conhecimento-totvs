---
content_hash: 087d8bdd477031eb92c672e5bbdd0aa49c68a94feb07967efbea78fe71477533
fetched_at: '2026-06-29T00:10:10.516354+00:00'
page_id: '452719861'
product: rm
source: tdn-rm
title: Terminais de Coleta
type: documentation
url: https://tdn.totvs.com/display/LRM/Terminais+de+Coleta
version: 3
---

**Terminais de Coleta**

Utilize o terminal de coleta para controlar as batidas dos funcionários e visitantes, mas para isso o terminal a ser utilizado deverá ser inserido para os mesmos. Para isso é possível fazer o lançamento de terminais, onde é possível lançar para vários funcionários ou visitantes, ou mesmo inserir diretamente no cadastro.

É muito importante inserirmos nomes sugestivos para a descrição e a localização do terminal, para facilitar a organização de uma possível utilização de vários terminais.

Caso o código do terminal de coleta esteja inserido no arquivo de importação de batidas, ao realizar a importação o sistema conseguirá identificar se o funcionário pode utilizar o terminal de coleta, a natureza da batida e o tipo do terminal.

**Tipo de REP:** Será visualizado REP-C, REP-A e REP-P .

**Tipos de terminais**

**Ponto**

As batidas importadas pelo terminal de tipo Ponto serão importadas para serem visualizadas no espelho do funcionário e podem ou não fazer parte do cálculo de acordo com a parametrização no cadastro do funcionário.

**Refeitório**

As batidas importadas pelo terminal de tipo Refeitório são consideradas como batidas de refeição e serão importadas para a pasta refeições no cadastro do funcionário.

**Observação**

As opções abaixo são apenas para o controle de acesso. Não são utilizados para a importação de batidas do ponto dos funcionários ou visitantes.

**Acesso1**

Esta opção deve ser utilizada apenas para os funcionários terem acesso ao terminal. O controle de acesso é feito apenas pelo RM Acesso.

**Acesso2**

Esta opção deve ser utilizada apenas para os funcionários terem acesso ao terminal. O controle de acesso é feito apenas pelo RM Acesso.

**Estacionamento**

Esta opção deve ser utilizada apenas para os funcionários terem acesso ao Estacionamento. O controle de acesso é feito apenas pelo RM Acesso.

Além disso, será necessário associar um layout de relógio ao terminal para que o sistema consiga ler o arquivo (txt) no momento da importação. O layout contém todas as informações que o sistema precisa para importar as batidas coletadas pelo relógio de ponto.

**Observação:**

A utilização dos terminais de coleta está relacionada ao parâmetro 'Controla acesso de funcionários a terminais de coleta'.

A importação de batidas fará as considerações do terminal de coleta somente se o layout de relógio estiver contemplando o layout.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Layout de Relógio  
Importação de Batidas  
   
   
HelpWiki - RH - Automação de Ponto
