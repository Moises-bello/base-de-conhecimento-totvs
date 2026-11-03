---
content_hash: ebc67db2e50124038dba658337f98871836505158cc1ebc4f3dac55c138bd03a
fetched_at: '2026-06-29T00:05:47.893052+00:00'
page_id: '1019332756'
product: rm
source: tdn-rm
title: DT - eSocial - Retificação Informações Complementares Períodos Anteriores -
  S-1210
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1019332756
version: 6
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | eSocial - Retificação Informações Complementares Períodos Anteriores - S-1210 |
| País: | Brasil |
| Épico: | [DRHROTRM-15187](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15187) |

## **02. VERSÃO**

* 12.1.2502.254
* 12.1.2506.211
* 12.1.2510.139 e superiores

## **03. S****ITUAÇÃO/REQUISITO**

A partir de **Janeiro de 2026**, em atendimento às novas regras do eSocial (previstas no Leiaute S-1.3), será liberado um novo processo para gerenciar a retificação de valores complementares do evento **S-1210 (Pagamentos de Rendimentos do Trabalho)**.

Este novo processo foi desenvolvido para permitir a **retificação exclusiva** de informações complementares transmitidos em anos anteriores, tais como:

* Dedução de Dependente
* Pensão Alimentícia
* Previdência Privada
* Despesas Médicas e Reembolsos

## **04.****SOLUÇÃO**

  Todos os detalhes para **correta parametrização** do sistema e **exemplos de utilização** estão disponíveis no **documento a seguir**:



Foi implementado o  processo que utiliza o parâmetro **Ano Retificação** para delimitar o escopo da correção. Ao informar o ano em que a retificação será enviada (ex: **2026**), o sistema identifica e lista os funcionários que, no ano imediatamente anterior (**2025**), possuíam eventos S-1210 transmitidos com status 10 na fila de eventos (caso possua eventos na tabela de eventos complementares é necessária a restauração dos eventos) passíveis de ajustes.

É fundamental notar que esta ferramenta é destinada **apenas à correção dos informações complementares.** Caso haja necessidade de **alteração de valores de rubricas** principais da folha de pagamento, o procedimento padrão de **reabertura da folha e reenvio dos eventos na competência original** deve ser utilizado.

## **05.** **TABELAS UTILIZADAS**

* PESOCIALRETIFICPERIODOANTERIOR

## **06. DEMAIS INFORMAÇÕES**
