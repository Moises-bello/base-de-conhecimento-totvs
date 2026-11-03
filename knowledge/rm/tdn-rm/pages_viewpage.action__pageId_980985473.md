---
content_hash: bc3152d04711037d128366a6ca5fb92e7b47fc4474e617772bb68fc087154f0a
fetched_at: '2026-06-29T00:12:15.527424+00:00'
page_id: '980985473'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Gerar gatilho automático para Chefe e Supervisor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=980985473
version: 10
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Implementação de gatilho o menu Chefe/Supervisor |
| País: | Brasil |
| Story: | [DRHROTRM-13967](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13967) |

## **02.** **RELEASES**

* 12.1.2410.291
* 12.1.2502.195
* 12.1.2506.137 e superiores

## **03. SITUAÇÃO/REQUISITO**

Tratativa para que, no menu Administração de Pessoal | Cadastros | Chefe e Supervisores, o sistemadispare gatilhos automáticos sempre que houver alterações nas informações de chefe ou supervisor.

## **04. SOLUÇÃO**

Foi implementada uma tratativa para que os gatilhos sejam modificados para o status "**Não integrado**" sempre que houver movimentações de pessoal, (transferência, inclusão e exclusão) no registro de chefe/supervisor.

**🔄 Exemplo:**  
Em um cenário de **transferência de um chefe**, o sistema altera o status do gatilho, permitindo que a nova informação seja considerada e integrada adequadamente.

Menu Administração de Pessoal | Chefes e Supervisores

Menu Administração de Pessoal | Ahgora - Funcionários enviados:

Json enviado:

Através do menu Administração de Pessoal | Funcionário | Rescisão, foi realizada atransferência do chefe (chapa 00077) para outra filial, conforme demonstrado abaixo:

Em seguida através do menu Administração de Pessoal | Chefes e Supervisores é preenchido o campo "Data Final", conforme demonstrado abaixo:

No menu Administração de Pessoal | Ahgora, é possível visualizar que os gatilhos foram automaticamente alterados para o status **"Não integrados"**, permitindo o reenvio das informações com a nova chefia para o Ponto Web da Ahgora:

## **05****. DOCUMENTAÇÃO**
