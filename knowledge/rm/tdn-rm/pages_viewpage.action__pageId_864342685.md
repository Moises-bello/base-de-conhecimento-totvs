---
content_hash: c16087238047f2d0e0f6492be757e72e7742c41772c13399d7c4848b20182bc0
fetched_at: '2026-06-29T00:11:55.834090+00:00'
page_id: '864342685'
product: rm
source: tdn-rm
title: DT - Encargos Base INSS Conforme DCTFWeb (Folha e 13º Salário)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864342685
version: 14
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Geração de Encargos |
| País: | Brasil |
| Issues | [DRHCALCRM-58](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-58); [DRHCALCRM-6836](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6836); [DRHCALCRM-6837](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6837); [DRHCALCRM-7053](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7053) |

## **02. VERSÃO**

Versão disponível a partir do release 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

O TOTVS Folha de Pagamento possui encargos que retornam a Base de INSS parte empresa separados os valores que contemplam o Cálculo da Folha atual e dissídio. Além disso não consideram o histórico de percentual de INSS e percentual redutor para empresas que possuem o beneficio da desoneração da Folha. Caso o usuário queira contemplar em uma base única os valores de Folha mensal e dissídio e aplicar o percentual cadastrado no histórico conforme é feito pela DCTFWeb, o mesmo deve fazer por fórmula.

## **04. SOLUÇÃO**

Foram criados dois novos encargos para retornar a Base de INSS conforme a DCTFWeb:

* Encargo tipo **T**:  Base INSS DCTFWeb
* Encargo tipo **U**: Base INSS 13º Salário DCTFWeb

Além disto, para estes novos encargos foi disponibilizado a opção para considerar o Histórico de Percentual para INSS da Seção e percentual de Redução cadastrado no Período de Apuração do eSocial.

## **05. DEMAIS INFORMAÇÕES**

* [Encargos - Folha de Pagamento](https://tdn.totvs.com.br/display/public/LRM/Encargos+-+Folha+de+Pagamento?draft=true)
