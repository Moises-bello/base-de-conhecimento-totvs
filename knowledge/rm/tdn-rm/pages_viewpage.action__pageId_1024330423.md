---
content_hash: fbac60b1038151d970c379149013ee17d20543de27a2b6560f7a819ad6560ec6
fetched_at: '2026-06-29T00:05:48.196896+00:00'
page_id: '1024330423'
product: rm
source: tdn-rm
title: DT - eSocial - Inclusão da tag <notAFT> nos eventos de remuneração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024330423
version: 7
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | eSocial - Inclusão da tag <notAFT> nos eventos de remuneração |
| País: | Brasil |
| Issue: | [DRHROTRM-15040](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15040 "View this issue") |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2502.
* 12.1.2506.
* 12.1.2510. e superiores

## **03. SITUAÇÃO/REQUISITO**

Em cumprimento à [Nota Técnica 04/2025 do eSocial,](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-04-2025-rev-26-08-2025.pdf/) foi incluída a tag **notAFT** **– Notificação da Auditoria Fiscal do Trabalho** nos layouts dos eventos de pagamento e desligamento, cuja obrigatoriedade passa a vigorar a partir de 1º de janeiro de 2026.

O principal objetivo dessa tag é identificar os recibos de pagamento que se referem a valores apurados em fiscalizações trabalhistas. Essa sinalização é fundamental para permitir a comunicação adequada entre o eSocial, a Auditoria Fiscal do Trabalho e o FGTS Digital, assegurando:

* o correto recolhimento das guias correspondentes;
* a baixa adequada das Notificações Fiscais do Trabalho relacionadas.

## **04. SOLUÇÃO**

A geração do XML dos eventos **S-1200**, **S-2299** e **S-2399** passou a considerar a nova tag **notAFT**, disponível na tabela **PFPERFF**.

Sempre que o campo **“Notificação da Auditoria Fiscal do Trabalho”** estiver preenchido, a tag **`<notAFT>`** será automaticamente incluída no XML, com o respectivo valor informado, garantindo o envio conforme o layout definido pelo eSocial.

Para o preenchimento desse campo, acesse o menu Administração de Pessoal | Funcionários | Anexos | Movimento | Ficha Financeira, em seguida, edite o período desejado e informe corretamente o valor no campo **“Notificação da Auditoria Fiscal do Trabalho”**, conforme demonstrado abaixo:

Ao gerar o XML do evento de remuneração, o produto irá buscar o valor informado nesse campo para o preenchimento da tag **`<notAFT>`**, conforme demonstrado no exemplo do evento **S-1200** abaixo.

## **05. DEMAIS INFORMAÇÕES**
