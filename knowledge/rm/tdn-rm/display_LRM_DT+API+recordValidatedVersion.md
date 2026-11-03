---
content_hash: b57c6707bd0eedeaafa1a50d5e4e62886e1a8fcc2f6aec60a23f5ff8a5f51f63
fetched_at: '2026-06-29T00:11:27.485050+00:00'
page_id: '725745406'
product: rm
source: tdn-rm
title: DT API recordValidatedVersion
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+API+recordValidatedVersion
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Automação de Ponto (CHRONUS) |
| Função: | Verificar se o RM está atualizado com os novos campos referente a portaria 671/2021 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHJORNRM-3515 |

## **02. SITUAÇÃO/REQUISITO**

Para atender a portaria 671/2021 foram criados novos campos nas tabelas utilizadas na integração com o Suricato, sendo necessário disponibilizar uma API para verificar se o RM está atualizado com esses novos campos.

## **03. SOLUÇÃO**

Desenvolvida a API **recordValidatedVersion**que verifica se os novos campos estão presentes no ambiente.

Exemplo de chamada do método via postman:

**"version671": "yes"** significa que o ambiente está atualizado.

**"version671": "no"** significa que o ambiente está desatualizado.

## **04. ASSUNTOS RELACIONADOS**

* [Importação de batidas integrada via API](https://tdn.totvs.com/pages/releaseview.action?pageId=682054374)
