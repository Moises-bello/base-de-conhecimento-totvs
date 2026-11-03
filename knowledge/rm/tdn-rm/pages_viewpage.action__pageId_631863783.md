---
content_hash: cec5b19ecd9bd0f2c9bc75e792d44882fc2c51e581a2dba9e0dc227c9ab25b52
fetched_at: '2026-06-29T00:11:05.518929+00:00'
page_id: '631863783'
product: rm
source: tdn-rm
title: DT - MP905 - Férias - Contrato Verde Amarelo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=631863783
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Férias |
| País: | Brasil |
| Ticket: | [10828100](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D%20%3D%20%2210828100%22) |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FOPCALCULO01-10045](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-10045)  [DRHCALCRM-109](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-109) |

## **02. SITUAÇÃO/REQUISITO**

Os funcionários que estão sob regime Contrato Verde Amarelo e que recebem o pagamento das férias mês a mês, ao realizar o cálculo das férias do funcionário, estava sendo efetuado o pagando do valor das férias novamente, causando pagamento em duplicidade e não está abatendo o que foi pago durante o período aquisitivo do funcionário. O cliente solicita que o processo seja ajustado para abater os valores pagos de férias mês a mês, conforme determina a Legislação vigente.

## **03. SOLUÇÃO**

Foram efetuadas algumas implementações no sistema para realizar automaticamente o cálculo das férias com o abatimento dos valores pagos mês a mês à titulo de férias no período aquisitivo em que o funcionário estava sob regime de contrato Verde Amarelo (Tipo de funcionário V). Para abatimento das férias pagas mês a mês dos funcionários com contrato Verde Amarelo (Tipo de funcionário V) , foram criados os códigos de cálculo abaixo:

* **446 - Férias Antecipadas Contrato Verde Amarelo,**Provento do tipo valor.
* **447 - Abatimento Férias Contrato Verde Amarelo,**Desconto do tipo valor.
* **448 - Abatimento Férias Contrato Verde Amarelo Primeiro Mês,**Desconto do tipo valor.
* **449 - Abatimento Férias Contrato Verde Amarelo Segundo Mês,**Desconto do tipo valor.
* **450 - Saldo Devedor Férias Contrato Verde Amarelo,**Base de Cálculo do tipo valor.

O usuário deverá informar o código do evento criado com o código de cálculo '**446 - Férias Antecipadas Contrato Verde Amarelo'**nos eventos lançados na ficha financeira mês a mês do período em que o funcionário tinha o contrato verde amarelo à título de férias, médias e 1/3 de férias.

Após informar o código do evento, o usuário deverá calcular as férias normalmente para o funcionário. Ao calcular as férias,  o sistema irá lançar os eventos com os códigos de cálculo **'38 - Férias', '40 - 1/3 Férias' e os eventos de médias de férias**e também irá lançar o evento com código de cálculo '**447 - Abatimento Férias Contrato Verde Amarelo'**abatendo as férias pagas mês a mês ao funcionário para as férias integrais no mês. Quando o valor dos abatimentos forem maiores que os proventos de férias do funcionário,  o sistema irá lançar o evento com código de cálculo '**450 - Saldo Devedor Férias Contrato Verde Amarelo'**para que seja descontado o restante do valor do funcionário desde que sejam férias referentes ao mesmo período aquisitivo de férias.

Para o cálculo das férias partidas, o usuário deverá informar o código do evento criado com o código de cálculo '**446 - Férias Antecipadas Contrato Verde Amarelo'**nos eventos lançados na ficha financeira mês a mês do período em que o funcionário tinha o contrato verde amarelo à título de férias, médias e 1/3 de férias.

Após informar o código do evento, o usuário deverá calcular as férias normalmente para o funcionário. Ao calcular as férias,  o sistema irá lançar os eventos com os códigos de cálculo **'41 - Férias no mês', '42 - Férias no próximo mês', '76 -1/3 Férias no mês', '77 - 1/3 Férias no próximo mês' e os eventos de médias de férias** e também irá lançar os eventos com código de cálculo '**448 - Abatimento Férias Contrato Verde Amarelo Primeiro Mês' e  '449 - Abatimento Férias Contrato Verde Amarelo Segundo Mês',**abatendo as férias pagas mês a mês ao funcionário para as férias partidas no mês e próximo mês. Quando o valor dos abatimentos forem maiores que os proventos de férias do funcionário,  o sistema irá lançar o evento com código de cálculo '**450 - Saldo Devedor Férias Contrato Verde Amarelo'**para que seja descontado o restante do valor do funcionário desde que sejam férias referentes ao mesmo período aquisitivo de férias.

## **04. DEMAIS INFORMAÇÕES**

[Código de Cálculo 446 - FÉRIAS ANTECIPADAS CONTRATO VERDE AMARELO](https://tdn.totvs.com.br/pages/viewpage.action?pageId=631864088)

[Código de Cálculo 447 - ABATIMENTO FÉRIAS CONTRATO VERDE AMARELO](https://tdn.totvs.com.br/pages/viewpage.action?pageId=631864135)

[Código de Cálculo 448 - ABATIMENTO FÉRIAS CONTR.VERDE AMARELO PRIMEIRO MÊS](https://tdn.totvs.com.br/pages/viewpage.action?pageId=631864182)

[Código de Cálculo 449 - ABATIMENTO FÉRIAS CONTR.VERDE AMARELO SEGUNDO MÊS](https://tdn.totvs.com.br/pages/viewpage.action?pageId=631864229)

[Código de Cálculo 450 - SALDO DEVEDOR FÉRIAS CONTRATO VERDE AMARELO](https://tdn.totvs.com.br/pages/viewpage.action?pageId=631864277)

## **05. ASSUNTOS RELACIONADOS**

* [Medida Provisória 905/2019](https://tdn.totvs.com/pages/viewpage.action?pageId=527841155)
