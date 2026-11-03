---
article_id: 360022766711
category: RH - Contrato Intermitente
content_hash: a2514067c5ab2b3920cd15e7d9112bb331e4e0bd714386ba050668a816bb748e
fetched_at: '2026-06-28T22:43:40.027392+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular Rescisão Contrato Intermitente
type: support-article
updated_at: '2024-12-30T19:53:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022766711-RH-Linha-Protheus-GPE-Como-calcular-Rescis%C3%A3o-Contrato-Intermitente
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25977209696791)** Tempo aproximado para leitura: **00:02:00 min*****Dúvida**Como Calcular Rescisão Contrato Intermitente  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para o cálculo da rescisão é necessário cadastrar um novo tipo de rescisão (Tabela auxiliar S043) com o **Tipo de aviso que desejar.**

Obs: O quadro abaixo é apenas um demonstrativo, todas as modalidades de aviso podem ser aplicadas ao empregado intermitente.

**![](http://tdn.totvs.com/download/attachments/327324780/image2018-1-2_10-15-17.png?version=1&modificationDate=1514895318000&api=v2)**

Na rescisão será calculada:  
-Saldo de salário, se houver convocações no período anteriores a data de demissão, férias e 13° proporcionais ao saldo de salário;  
-Aviso prévio indenizado, com o tipo de aviso A os dias de aviso são divididos por 2;  
-Férias e 13° sobre o aviso;  
-Multa do FGTS calculada com base na porcentagem informada no tipo de rescisão.  
Exemplo:  
![](http://tdn.totvs.com/download/attachments/327324780/image2018-1-2_10-36-47.png?version=1&modificationDate=1514896608000&api=v2)

No calculo acima temos:  
Saldo de salário referente a convocação que o funcionário teve até a data de demissão. Mesmo que exista mais de uma convocação, será gerada apenas uma verba de saldo de salário.  
As verbas de férias e 13° indenizado são calculadas com base no saldo de salário e proporcionalizadas pelas horas trabalhadas, assim como é realizado na folha.

Aviso prévio:  
**Para o cálculo do aviso prévio é feita uma média dos últimos 12 meses, considerando apenas os meses em que houve convocação**, neste exemplo temos:![](http://tdn.totvs.com/download/attachments/327324780/image2018-1-2_10-43-4.png?version=1&modificationDate=1514896985000&api=v2)

Valores recebidos:  
12/2017 => 666,60 + 300,00 = 966,60  
01/2018 => 600,00  
03/2018 => 2533,40  
04/2018 => 400,00 (saldo de salário)

O cálculo do aviso será apresentado da seguinte forma:  
( 966,60 + 600,00 + 2533,40 + 400,00 ) / 4 =  1125,00  
Como são 15 dias de aviso => 1125,00 / 30 \* 15 = 562,50

Sobre esse valor é calculado 1 avo de férias e 13°  
562,50 / 12 = 46,88  
OU  
1125,00 / 12 / 30 \* 15 = 46,88  
  
**Saiba Mais**

[Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)
