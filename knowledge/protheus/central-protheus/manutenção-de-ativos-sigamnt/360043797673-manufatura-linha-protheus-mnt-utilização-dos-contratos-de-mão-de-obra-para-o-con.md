---
article_id: 360043797673
category: Manutenção de Ativos (SIGAMNT)
content_hash: 484ab51e2fe8c16c922a27fc637d1b01560ba91acdf71747a8112365bfb1fd59
fetched_at: '2026-06-28T22:42:34.518455+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Utilização dos contratos de mão de obra
  para o controle de custos
type: support-article
updated_at: '2021-09-30T14:28:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043797673-Manufatura-Linha-Protheus-MNT-Utiliza%C3%A7%C3%A3o-dos-contratos-de-m%C3%A3o-de-obra-para-o-controle-de-custos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)**Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como funciona a utilização dos **Contratos de Mão de Obra** para o controle de custos?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**O processo de utilização de **Contratos de Mão de Obra**para o controle de custos permite o cadastro de contratos de mão de obra, com a finalidade de controlar o custo de serviço prestado por terceiros.  
Desta forma, ao incluir um contrato através da rotina de **Contratos - MNTA185**, é necessário relacionar ao prestador do serviço que é um terceiro fornecedor da mão de obra. Conforme imagem abaixo:

![](https://tdn.totvs.com/download/attachments/538502617/image2020-2-20_10-32-40.png?version=1&modificationDate=1582206859907&api=v2)

Em seguida é necessário incluir o funcionário que prestará o serviço terceirizado, através da rotina de **Funcionários - MNTA020**.  O contrato de mão de obra incluído anteriormente deve estar relacionado à esse funcionário através do campo **Contrato - T1\_CONTRAT**, conforme ilustração a seguir:

![](https://tdn.totvs.com/download/attachments/538502617/image2020-2-20_10-34-20.png?version=1&modificationDate=1582206859877&api=v2)

Após realizar os cadastros, basta relacionar o funcionário cadastrado anteriormente como um insumo realizado do tipo mão de obra à uma ordem de serviço, conforme exemplo a seguir:

![](https://tdn.totvs.com/download/attachments/538502617/image2020-2-20_10-39-32.png?version=1&modificationDate=1582206859843&api=v2)

Pode-se notar que no primeiro momento, após o reporte do insumo, o custo desta mão de obra continua zerado. Para consumir o valor acordado no contrato é necessário que após a inclusão dos insumos seja executada a rotina **Atualização do Custo de Mão de Obra Com Base no Contrato - MNTA175**. Esta atualização pode ser realizada em lote para diversos contratos e o período que desejado, no exemplo a seguir será  restrito a um contrato e somente ao mês de fevereiro de 2020.

![](https://tdn.totvs.com/download/attachments/538502617/image2020-2-20_10-44-51.png?version=1&modificationDate=1582206859803&api=v2)

Ao retornar a rotina de retorno de ordem de serviço e visualizar o insumo realizado, nota-se que o valor do contrato está vinculado ao custo do insumo.

![](https://tdn.totvs.com/download/attachments/538502617/image2020-2-20_10-48-36.png?version=1&modificationDate=1582206859757&api=v2)

O consumo de horas para insumos do tipo mão de obra vinculadas a um contrato podem ser verificados por meio das seguintes consultas/relatórios:

* **Relatório de Horas trabalhadas no contrato** **- MNTR715**
* **Relatório de Aplicação de Contrato - MNTR725**
