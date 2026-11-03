---
content_hash: ce0ad44e825465c43cc04d5773d5a63cdca215c1d7dc6987e86872dddf6dc8f4
fetched_at: '2026-06-29T00:11:36.738361+00:00'
page_id: '773506859'
product: rm
source: tdn-rm
title: DT - Férias Coletivas - Antecipação de Férias sem cadastramento de abono automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773506859
version: 13
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Férias Coletivas |
| País: | Brasil |
| Story | [DRHCALCRM-3477](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3477) |

Versão

O recurso está disponível somente a partir da versão 12.1.2306.109.

## **02. SITUAÇÃO/REQUISITO**

Ao fazer o cadastro de Férias Coletivas, quando está marcado o parâmetro no sindicato '**Permite antecipação de dias de férias do próximo período aquisitivo'** e o funcionário possui saldo de dias fracionados,  atualmente está ocorrendo o cadastro automático de 0,5 dia de Abono de Férias no período aquisitivo atual, sem a possibilidade de antecipar os dias de gozo de férias fracionados.

## **03. SOLUÇÃO**

Foi criado o parâmetro **"Não pagar 0,5 dia de abono pecuniário quando o saldo de Férias for Fracionado"** no cadastro de Sindicatos, na aba de Férias. Ao marcar essa opção, o sistema irá antecipar os dias de gozo de férias fracionados do próximo período e não cadastrará automaticamente 0,5 dia de abono.

## **07. EXEMPLO**

Considerando um funcionário que possui 12,5 dias de Saldo Férias, o comportamento do parâmetro será o seguinte:

Parâmetro Desmarcado, Parâmetro Marcadopasso1,passo2yespasso1

Parâmetro desmarcado no sindicato:

Cadastrando 20 dias de Férias Coletivas:

É cadastrado 20 dias de Férias e 0,5 dia de abono:

Na aba 'Antecipação de Férias' do cadastro de Férias do funcionário é informado 8 dias antecipados:

nopasso2

Parâmetro marcado no sindicato:

Cadastrando 20 dias de Férias Coletivas:

É cadastrado 20 dias de Férias e não foi cadastrado dia de abono:

Na aba 'Antecipação de Férias' do cadastro de Férias do funcionário é informado 7,5 dias antecipados:

## **05. DEMAIS INFORMAÇÕES**

O parâmetro criado estará disponível apenas quando o parâmetro "Permite antecipação de dias de férias do próximo período aquisitivo" estiver marcado. Além disso, esse parâmetro terá efeito somente para Férias Coletivas. No caso de Férias Globais, mesmo que o parâmetro esteja marcado, o sistema irá cadastrar automaticamente 0,5 dia de abono pecuniário.

## **06. ASSUNTOS RELACIONADOS**
