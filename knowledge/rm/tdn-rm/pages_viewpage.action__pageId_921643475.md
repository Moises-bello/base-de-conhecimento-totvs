---
content_hash: ea0350253937c05aed6a7f7ab91839fa384d30c30c0ea7745f265416a7676905
fetched_at: '2026-06-29T00:12:07.177535+00:00'
page_id: '921643475'
product: rm
source: tdn-rm
title: DT - S-1210 - Criação do grupo <infoProcRet>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=921643475
version: 6
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1210 - Preenchimento do grupo <infoProcRet> |
| País: | Brasil |
| Issue: | [DRHROTRM-12941](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12941) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.246
* 12.1.2410.186
* 12.1.2502.110 e superiores

## **03. SITUAÇÃO/REQUISITO**

É necessário ajustar a geração do evento S-1210 para garantir que, sempre que houver uma verba enviada no S-1200 do período de apuração com incidência de IRRF igual a 9xxx, o grupo de processos seja informado obrigatoriamente.

## **04. SOLUÇÃO**

O produto foi ajustado para que o grupo <infoProcRet>, referente a informações de valores relacionados à não retenção de tributos ou a depósitos judiciais, seja gerado no evento S-1210 sempre que houver verbas com incidência de IRRF igual a 9xxx.

Para garantir a correta geração deste grupo, é necessário acessar o menu Cadastros | Eventos | Anexos | Anexo Processo de Suspensão de Incidência e preencher o cadastro do processo conforme as orientações abaixo:

  XML S-1210:

## **05.** **ASSUNTOS RELACIONADOS**

* [Leiaute Versão S-1.3 e NT 01/2024](https://tdn.totvs.com/pages/viewpage.action?pageId=862114556)
