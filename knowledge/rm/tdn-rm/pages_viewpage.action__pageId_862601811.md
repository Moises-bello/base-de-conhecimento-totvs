---
content_hash: 4d456f14543d8b24a14317e1f97816a609bf44f138f8580a3f3b6f4bc17258ab
fetched_at: '2026-06-29T00:11:55.625661+00:00'
page_id: '862601811'
product: rm
source: tdn-rm
title: DT - Rescisão Coletiva - Informar parâmetros selecionados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862601811
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Rescisão Coletiva |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-6172](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6172) |

## **02. VERSÃO**

Este recurso estará disponível a partir do release 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

Ao executar processos em lote, o usuário seleciona os filtros que deseja aplicar na execução do processo. Ao avançar nas telas geralmente até existe uma tela onde ele precisa confirmar a execução do processo, mas não são exibidos para ele quais foram os parâmetros e filtro selecionado. Ao operar o sistema o usuário pode cometer equívocos e selecionar um parâmetro a mais ou a menos sem querer e não vai ter a oportunidade de perceber isso antes da execução do processo.

## **04. SOLUÇÃO**

Criado um step de confirmação de parâmetros informados no processo de rescisão coletiva.

Cada página de dados/parâmetros do wizard ocupa uma aba na tela de confirmação "Parâmetros de Rescisão Coletiva Informados".

Considerações:

* As quatro abas do exemplo abaixo só serão exibidas no Tipo de Rescisão 6 (seis).
* No Tipo de Rescisão 5, não será exibida a aba "Parâmetros de Cálculo da Rescisão".
* E em todos os outros Tipos de Rescisão, não será exibida a aba "Parâmetros/Dados da Transferência", ou seja, serão exibidas as abas "Dados do Aviso Prévio", "Dados da Rescisão" e "Parâmetros de Cálculo da Rescisão".

## **05. DEMAIS INFORMAÇÕES**

[Documento Referência - Rescisão Coletiva](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719318)
