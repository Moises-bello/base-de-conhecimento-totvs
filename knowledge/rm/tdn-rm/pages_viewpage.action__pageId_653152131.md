---
content_hash: d1ec08b352d2ac6f6a5fc99332b773d34e9c1a2b7aa202bf256a56ee778064d1
fetched_at: '2026-06-29T00:11:12.446634+00:00'
page_id: '653152131'
product: rm
source: tdn-rm
title: DT – Dependente IRRF - parâmetro "Considera a dedução de dependente somente
  até o mês de aniversário"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=653152131
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: |  |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Parametrizador |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-857](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-857?page=com.totvs.jira.plugin.pluginTotvs%3Aissue-zendesk-tab-panel) |

## **02. SITUAÇÃO/REQUISITO**

Ao calcular folha com regime caixa, o sistema está considerando o dependente de IRRF de acordo com a competência e não conforme caixa. Ao realizar folha competência de novembro/2020, caixa dezembro/2020, e o dependente faz aniversário em novembro, o dependente é considerado no cálculo de novembro. Ao realizar o lançamento da 2a parcela do 13 salário, o sistema recalcula o IRRF lançando juntamente com a folha do 13 salário.

## **03. SOLUÇÃO**

Foi explicado ao cliente que o procedimento é que o sistema processa o cálculo do dependente do IRRF de acordo o processo do Governo (DIRF), onde o dependente é considerado o ano inteiro para dedução de IRRF.

Foi criado o parâmetro “Considera a dedução de dependente somente até o mês de aniversário” que desmarca automaticamente o campo incidência 'IRRF' na Liberação de Competência, para o Grau de Parentesco '1-Filho(a) Válido' ou 'D-Enteado(a)' observando:  
a) se o dependente tem mais de 21 anos de idade ou  
b) se o dependente é universitário e tem mais de 25 anos;  
Também foi retirado da liberação de competência o parâmetro “Atualizar dependentes para IRRF”.

## **04. DEMAIS INFORMAÇÕES**

[Parâmetros de Cálculo 2/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=561848185)

[Liberação de Competência Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719172)

[Dependentes](https://tdn.totvs.com/display/public/LRM/Dependentes)
