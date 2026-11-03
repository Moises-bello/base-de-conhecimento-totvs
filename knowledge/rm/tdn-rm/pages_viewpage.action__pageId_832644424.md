---
content_hash: 7a127323d8f3033690e0f79a289074c84cba460ceeb73b6201fe51f6e6c8b3fa
fetched_at: '2026-06-29T00:11:49.408133+00:00'
page_id: '832644424'
product: rm
source: tdn-rm
title: Contrato de Locação - Anexo - Carência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=832644424
version: 16
---

## **Objetivo**

---

A funcionalidade de carência permite estabelecer um período específico o qual determinadas obrigações financeiras, como pagamento de condomínio ou fundo promocional serão suspensas.

## **Configuração da Carência**

---

No momento da configuração de uma carência, será possível definir as seguintes informações na visão:

**Entidade:** Selecione, Fundo promocional ou Condomínio  
**Data Inicial e Data final:** Refere-se a data selecionada para que não seja cobrado valor no contrato.

* Ao preencher o campo "Dias", o sistema calculará a próxima data final de carência, iniciando a contagem a partir da data inicial especificada como ponto de partida. Por exemplo: Se a data inicial for definida como 01/01/2000 e forem inseridos 4 dias, a data final será 04/01/2000 (contando-se o dia inicial como parte do período de carência);
* A carência apenas poderá ser incluída ou editada em contratos que possuem os status: Efetivado, Elaboração, Proposta;
* Quando ocorrer um fechamento de condomínio dentro do período de carência, o sistema não permitirá editar ou excluir essa carência, nem incluir uma nova carência com a mesma data de fechamento.

## **Aplicação da Carência no Condomínio**

---

Estando configurado um período de aplicação de carência para a entidade de "Condomínio" o sistema irá valer-se dessa informação para realizar os cálculos de fechamentos nas competências que incidem carência.

É importante ressaltar que, após a carência ser definida no contrato de locação, somente se aplicará ao condomínio se o empreendimento estiver integrado a locação.

**Exemplo de cálculo de carência no fechamento de condomínio**

Neste exemplo teremos um contrato de locação com uma carência definida num período de **20/01/2021  até  25/01/2021**, totalizando 6 dias.

Este contrato também **possui pro rata** na competência de Janeiro.

Ao realizar o fechamento do condomínio na competência 01/24, teremos o cálculo abaixo:

Período Contrato.:  inicial [15/01/2024]   final [31/12/2025]  
Fator............:  (Valor Total / Dias Mês)  =  ( 2500 / 30 ) = 83,3333  
Nº Dias Mês.......:  30  
Período carência.:  inicial [20/01/2024]   final [25/01/2024]  
Nº Dias carência..:  06  
Nº Dias utilizado.:  11 => (Nº Dias utilizado - Nº Dias Carência) =  17 - 6   
Nº Dias vacância..:  20 => (Nº Dias vacância  + Nº Dias Carência) =  14 + 6   
Cálculo pró-rata.:  ( Fator  \*  Nº Dias utilizado)  
Cálculo pró-rata.:  ( 83,3333  \*  11 ) = 916,67

Ou seja, sempre que existir pro-rata e carência num mesmo período, os números de dias de carência serão subtraídos no cálculo de dias utilizado e da mesma forma, adicionados aos dias de vacância neste período em específico.

Todo o valor calculado para vacância serão gerados para os respectivos responsáveis do Empreendimento. Para entender mais sobre o **[rateio de vacância, clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=680244548).**

Para entender mais sobre os **[cálculos de fechamento, clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105086)**

## **Aplicação da Carência no Fundo Promocional**

---

Estando configurado um período de aplicação de carência para a entidade de "Fundo Promocional" o sistema irá valer-se dessa informação para realizar os cálculos de FPP's nas competências que incidem carência.

É importante ressaltar que, após a carência ser definida no contrato de locação, não será possível mais alterá-la quando houve FPP's já gerados no contrato.

**Exemplo de cálculo de carência no fundo promocional**

Neste exemplo teremos um contrato de locação com uma carência para a entidade de Fundo Promocional, definida num período de **01/01/2024  até  21/01/2024**, totalizando 21 dias.

Ao realizar o processo de geração de lançamentos do fundo promocional, na competência 01/24, teremos o cálculo abaixo:

Período carência.:  inicial [01/01/2024]   final [21/01/2024]  
Qte dias carência..............: 21  
Proporção diária carência......: (Valor / Total Dias)  = 2200 / 31 = 70,97  
Valor pró-rata dia carência....: (Dias \* Proporção diária) = (  21 \* 70,97   ) = 1490,32

O valor da parcela na competência [01/2024]: (Valor Parcela - Valor Carência) = (2200 - 1490,32) = 709,68

Importante:

* Carência igual ou superior a 30 dias, sempre irá considerar 100% de vacância na competência do fechamento.
* **Contratos que não são pró-rata** e possuem carência de pelo menos 1 dia são considerados com 100% de vacância na competência do fechamento.
