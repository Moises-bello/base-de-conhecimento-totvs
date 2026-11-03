---
content_hash: de34147782a3e9301053b29602d1ffb36ec33276c978630df83f6ef20283b888
fetched_at: '2026-06-29T00:11:55.055097+00:00'
page_id: '860243746'
product: rm
source: tdn-rm
title: DT - Integração RM x Feedz - Chefe/Supervisor Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=860243746
version: 9
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Feedz - Chefe/Supervisor Externo |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10035](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10035) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2310.237
* 12.1.2402.192
* 12.1.2406.121 e superiores

## **03. SITUAÇÃO/REQUISITO**

Passar a considerar chefes/supervisores externos na integração entre RM x Feedz.

## **04. SOLUÇÃO**

Implementamos uma melhoria no processo de integração RM X Feedz, onde o sistema agora considera o chefe/supervisor externo no envio e na associação de seus subordinados.

Para que a integração ocorra com sucesso, é necessário que, no cadastro do externo, os campos "Seção", "Função" e "Data de Início" sejam preenchidos na opção "**Dados Externo**".

Caso exista mais de um chefe/supervisor no mesmo nível da seção, é possível priorizar o envio utilizando o flag "Master" no cadastro do chefe/supervisor. Para isso, basta marcar o novo parâmetro "**Priorizar chefe master no envio**" disponível no processo de integração. Veja demonstração abaixo:

**Cadastro Chefe/Supervisor**

**Integração RM x Feedz**

**OBSERVAÇÃO:**

Em casos onde exista mais de um chefe/supervisor no mesmo nível da seção e ambos estão como master, será enviado o chefe com a menor chapa.  
Como o externo não possui chapa, a seleção será baseada no código do externo.

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Feedz](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)
