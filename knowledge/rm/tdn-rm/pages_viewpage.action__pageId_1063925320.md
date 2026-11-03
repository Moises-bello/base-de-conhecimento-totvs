---
content_hash: eb4f257f6abfee0a5632afd9175a837930d66956006b9d2af38e6f04dc4590d6
fetched_at: '2026-06-29T00:05:53.031145+00:00'
page_id: '1063925320'
product: rm
source: tdn-rm
title: DT - Integração RM x Ahgora - Envio de Alteração de Chefia da Hierarquia por
  Posição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1063925320
version: 12
---

## **1. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Ahgora - Envio de Alteração de Chefia da Hierarquia por Posição |
| País: | Brasil |
| Épico: | [DRHROTRM-16199](https://jiraproducao.totvs.com.br/browse/DRHROTRM-16199) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2506.297
* 12.1.2510.223
* 12.1.2602.141 e superiores

## **03. SITUAÇÃO/REQUISITO**

Gerar gatilho para os subordinados ao realizar alterações nas posições por meio do processo Manutenção de Hierarquia/Posição no produto TOTVS Gestão de Pessoas | Gestão Organizacional na integração Ponto Web (Ahgora).

## **04. SOLUÇÃO**

Realizada melhoria nos produtos **TOTVS Folha de Pagamento** e **TOTVS Gestão de Pessoas** para garantir que, ao realizar alterações de posições por meio do processo **Manutenção de Hierarquia/Posição** (Gestão Organizacional), os gatilhos dos subordinados sejam atualizados automaticamente para o status **NI (Não Integrado)**.

Com essa evolução, as alterações passam a ser enviadas para a fila de processamento, assegurando maior consistência das informações hierárquicas do colaborador no **Ponto Web (Ahgora)**.

#### EXEMPLO:

Diagrama da Hierarquia

Hierarquia Atual

Subordinada Integrada

Realizada a alteração da Hierarquia

Processo executado com sucesso

Status do gatilho alterado para não integrado (**NI**).

Json enviado com atualização do chefe

## **05. DEMAIS INFORMAÇÕES**

* [Integração RM X Ahgora](https://tdn.totvs.com/pages/viewpage.action?pageId=877866931)
