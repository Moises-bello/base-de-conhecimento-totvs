---
content_hash: 27c677cdf4725987114fdd0a9fc6d97df0c8c14a372f4ad1c025169ce162ae74
fetched_at: '2026-06-29T00:11:33.280889+00:00'
page_id: '754964778'
product: rm
source: tdn-rm
title: DT - Importação de Movimento - Transfere arquivo para o servidor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=754964778
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Importação/Exportação de Movimento |
| País: | Brasil |
| Story: | [DRHCALCRM-3638](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3638)  [DRHCALCRM-3642](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3642)  [DRHCALCRM-4006](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-4006) |

## **02.****VERSÕES**

**A partir da Versão:**

* + **12.1.2306.1**

## **03. SITUAÇÃO/REQUISITO**

Para adequação do TOTVS Folha de Pagamento à novas tecnologias, se fez necessário alterar o funcionamento da manipulação de arquivos na Importação/Exportação de Movimento. Foi retirado da tela de Importação do Movimento, o parâmetro '**Transfere arquivo para o Servidor**'**.**

## **04. SOLUÇÃO**

Passamos por uma modernização, para garantir escalabilidade e compatibilidade com cloud, e agora ele é capaz de identificar automaticamente o local mais adequado para salvar esses arquivos. Isso significa que não precisamos mais definir o local que será gravado o arquivo, pois o sistema agora cuida disso.

O RM agora será responsável por identificar e definir automaticamente o local adequado para salvar os arquivos, levando em consideração todas as melhorias que foram implementadas.

## **05. ASSUNTOS RELACIONADOS**

[Importação de Movimento](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719187)
