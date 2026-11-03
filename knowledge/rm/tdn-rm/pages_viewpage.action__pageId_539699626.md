---
content_hash: 3ecceaebf90d513d83e76d52eba51283fa6d78ee79746adc1989d3bb840290da
fetched_at: '2026-06-29T00:10:37.333667+00:00'
page_id: '539699626'
product: rm
source: tdn-rm
title: Sugestão de Férias PortalRM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=539699626
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Folha de Pagamento |
| Função: | Sugestão de férias PortalRM |
| Ticket: | [Ticket #7568857](https://totvssuporte.zendesk.com/agent/tickets/7568857 "View ticket on the Zendesk portal")/[Ticket #5326360](https://totvssuporte.zendesk.com/agent/tickets/5326360 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FOPROTINAS01-10811](https://jiraproducao.totvs.com.br/browse/FOPROTINAS01-10811)/[FOPROTINAS01-8086](https://jiraproducao.totvs.com.br/browse/FOPROTINAS01-8086) |

## **02. SITUAÇÃO/REQUISITO**

Passa a ser vedado o início das férias no período de 2 (dois) dias que \_antecede\_feriado ou dia de repouso semanal remunerado (art. 134, § 3º, acrescentado pelo Projeto de Lei 6.787/2016), Essa previsão tem como objetivo não prejudicar o empregado quanto ao gozo das *férias individuais*, evitando que estas iniciem no período de 2 (dois) dias antes de feriado ou repouso semanal remunerado, pois nesses dias o empregado já estaria descansando de forma remunerada, Porém em jornadas 6/2 e 12x36, o sistema não permite o cadastro da férias devido a nova lei, e o sistema deveria permitir o cadastro para funcionários cadastrados nas respectivas jornadas.

## **03. SOLUÇÃO**

Foi criado em Configurações > Parametrizador > RM Portal > Férias o parâmetro  "Não impedir marcação de férias para jornada 12x36", quando marcado o sistema deverá permitir o a marcação de sugestão de férias, desde que não seja dia de folga ou feriado do respectivo funcionário.

Escalas de Trabalho

Para a escala de trabalho, como por exemplo, 6/2, o sistema validará a folga do funcionário conforme sua escala de trabalho, não necessitando do parâmetro 'Não impedir marcação de férias para jornada 12x36'. 

## **04. DEMAIS INFORMAÇÕES**

Para que o sistema considere a marcação do parâmetro "Não impedir marcação de férias para jornada 12x36", ele irá validar o campo tipo jornada e-Social dentro do cadastro de horário, o mesmo deverá estar preenchido com a jornada 12x36.
