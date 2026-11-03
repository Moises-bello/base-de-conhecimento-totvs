---
content_hash: 05517c6a906be48ea893f09bb8b208895bcb24d7dd06f335d5c355fed53c8d35
fetched_at: '2026-06-29T00:11:20.597930+00:00'
page_id: '687154891'
product: rm
source: tdn-rm
title: FISCAL01-18087 - DT - Correção para erro de envio de nota fiscal com integração
  com o TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687154891
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e Envio |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18087 |

## **02. SITUAÇÃO/REQUISITO**

Ao fazer um envio de uma nota fiscal um erro genérico de parâmetro nulo é exibido. O erro aponta para um parâmetro “collection”. Ao investigar o problema em um ambiente de homologação de um cliente por meio da ferramenta dnSpy, foi possível rastrear o problema para uma chamada addRange de uma coleção que estava recebendo o retorno do método WsRemessa da classe RM.Fis.TSS.Envio.FisTSSNFESBRASEnvioInterno. Este método tem um retorno do tipo List<T> no entanto, em uma condição, o método retorna null. Dessa forma a exceção é lançada pelo addRange que não pode receber um parâmetro nulo.

## **03. SOLUÇÃO**

O método foi ajustado para retornar uma lista vazia na condição que antes retornava nulo. Nenhum comportamento foi alterado visto que todas as chamadas do método possuíam uma verificação para coleções vazias e não dependiam do retorno nulo.

Os seguintes métodos que poderiam apresentar o mesmo problema, também foram ajustados para retornar uma lista vazia ao invés de null: RM.Fis.NFe.FisNFeMod.**WsEnviarNFe**, RM.Fis.RotinasFiscais.FisNFSeServicosTSS.**WsEnviarNFe** e RM.Fis.TSS.Envio.FisTSSNFESBRASEnvioInterno.**WsSchema.**

Disponível a partir da versão 12.1.33
