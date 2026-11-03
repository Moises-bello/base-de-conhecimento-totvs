---
content_hash: 5ce050a09af6bd04a50184f69cc839269a69a5be54e2ae6437ec6b1f7363784a
fetched_at: '2026-06-29T00:09:59.352381+00:00'
page_id: '452718308'
product: rm
source: tdn-rm
title: Código de Cálculo 344 - Indenização Adicional na Dispensa Antes Data Base
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718308
version: 24
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Informações complementares**

## **01. VISÃO GERAL**

Este código de cálculo deve ser informado em um evento do tipo Provento e Valor. Ele não terá cálculo interno no sistema e no evento deverá ser informado uma fórmula criada pelo usuário. Ele será apenas o identificador do evento da indenização.

O evento com código de cálculo 344 só será lançado quando:

* + Rescisão do Tipo 2 - Inc. Empregador sem justa causa
  + O parâmetro 'Lança indenização adicional na dispensa sem justa causa, no período de 30 dias, antes da data base' estiver marcado
  + Rescisão for até 30 dias antes da data base informada nos campos Dia e Mês no sindicato.

Observação

Quando o funcionário possuir aviso prévio indenizado, os dias de aviso serão projetados considerando a data da rescisão o ultimo dia projetado. Caso esse ultimo dia seja até 30 dias antes da data base e o parâmentro para lançar o evento de indenização esteja marcado, será lançado o evento de CC344. Mais informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=225261381>

## **02. EXEMPLO DE UTILIZAÇÃO**

**Com o parãmetro marcado no sindicato para lançar a indenização adicional e a data base informada é 01/04:**

1. Antes da Data Base, 2. Na data Base, 3. Após a data Base, 4. Rescisão tipo 3passo1,passo2,passo3,passo4yespasso1

Funcionário com tipo de demissão 2, demitido dia 10/02/2023 com 30 dias de aviso prévio indenizado. Logo, pela projeção o será considerado a data de desligamento 12/03/2023:

   

Ao executar o cálculo da rescisção lançou o evento de Código de Cálculo 344 com o valor retornado pela Fórmula:

nopasso2

Funcionário com tipo de demissão 2, demitido dia 10/02/2023 com 50 dias de aviso prévio indenizado. Com a projeção dos dias de aviso, será considerado a data de demissão dia 01/04/2023, a mesma da data base informada no sindicato:

Não foi lançado o evento de Código de Cálculo 344:

nopasso3

Funcionário com tipo de demissão 2, demitido dia 13/02/2023 com 50 dias de aviso prévio indenizado. Com a projeção dos dias de aviso, será considerado a data de demissão dia 04/04/2023, posterior a data base informada no sindicato:

 

Não foi lançado o evento de Código de Cálculo 344:

nopasso4

Funcionário com tipo de demissão 3, demitido dia 13/02/2023 com 45 dias de aviso prévio indenizado. Com a projeção dos dias de aviso, será considerado a data de demissão dia 30/03/2023, anterior a data base informada no sindicato:

 

Não foi lançado o evento de Código de Cálculo 344:

**Com o parãmetro desmarcado no sindicato para lançar a indenização adicional e a data base informada é 01/04:**

Funcionário com tipo de demissão 2, demitido dia 01/02/2023 com 45 dias de aviso prévio indenizado. Com a projeção dos dias de aviso, será considerado a data de demissão dia 18/03/2023, a mesma da data base informada no sindicato:

Não foi lançado o evento de Código de Cálculo 344:

## **03.** **INFORMAÇÕES COMPLEMENTARES**

[Sindicatos](https://tdn.totvs.com/display/LRM/Sindicatos)
