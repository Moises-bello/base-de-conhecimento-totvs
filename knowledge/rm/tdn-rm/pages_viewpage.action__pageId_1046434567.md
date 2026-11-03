---
content_hash: c373adbfce484ca0fec57cabc0573b1ccddf7b2c3ffef902461e4a78e4a83d58
fetched_at: '2026-06-29T00:05:50.981429+00:00'
page_id: '1046434567'
product: rm
source: tdn-rm
title: Parâmetro de Cálculo de Superfície Corporal — Oncologia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046434567
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Saúde Hospitais e Clinicas |
| Linha de Produto: | Linha RM |
| Segmento: | Saude |
| Módulo: | NEXUS |
| Função: | ONCOLOGIA - QUIMIOTERAPIA |
| Ticket: | 26512006 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DSAUGHNEXUS-846 |

## **02. SITUAÇÃO/REQUISITO**

 O sistema atualmente calcula a Superfície Corporal (SC) exclusivamente pelo método de Mosteller, utilizado como base para a dosagem de medicamentos oncológicos.

Essa limitação pode causar divergências em relação a protocolos que adotam o método Du Bois, impactando a precisão e segurança na dosagem de quimioterápicos prescritos.

Implementar uma parametrização que permita a seleção do método de cálculo da SC por unidade de atendimento, com a opção de escolher entre Mosteller e Du Bois, garantindo que a dosagem dos medicamentos oncológicos seja calculada de acordo com o método configurado, enquanto o método Mosteller permanece como padrão.

## **03. SOLUÇÃO**

Implementação da parametrização do cálculo da Superfície Corporal (SC) para prescrição oncológica permite a seleção entre as fórmulas Mosteller ou Du Bois, com default para Mosteller. Essa configuração poderá ser ajustada por unidade de atendimento na aba de Oncologia. O sistema aplicará automaticamente o método escolhido no cálculo da SC e na dosagem dos medicamentos, sem necessidade de interação manual do médico durante a prescrição. O método utilizado será exibido na tela de prescrição, garantindo transparência e auditoria. É fundamental que as prescrições anteriores não sejam alteradas, assegurando que novas prescrições adotem imediatamente o método configurado na unidade. Os critérios de aceite garantem que o sistema esteja alinhado às práticas clínicas, assegurando a precisão no cálculo da dosagem dos quimioterápicos.

## **04. DEMAIS INFORMAÇÕES**

<Não se aplica>

## **05. ASSUNTOS RELACIONADOS**

        Não se aplica
