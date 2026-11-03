---
content_hash: ec15b47d4805e30125d9fcd41ea5c8b197c27e9245ea8adbcd6809f8cffebbfa
fetched_at: '2026-06-29T00:05:51.097169+00:00'
page_id: '1047368861'
product: rm
source: tdn-rm
title: DT Parâmetro de Cálculo de Superfície Corporal — Oncologia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1047368861
version: 1
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

\*\*Situação:\*\* O sistema atualmente calcula a Superfície Corporal (SC) exclusivamente pelo método de Mosteller, utilizado como padrão na prescrição oncológica.

\*\*Problema:\*\* Essa limitação pode gerar divergências em relação a protocolos que adotam o método Du Bois, impactando diretamente a dosagem dos quimioterápicos e comprometendo a segurança assistencial.

\*\*Objetivo:\*\* Implementar uma parametrização que permita selecionar entre os métodos de cálculo Mosteller e Du Bois por unidade de atendimento, garantindo que o método configurado seja automaticamente aplicado ao cálculo da SC e visível na tela de prescrição, sem alterar prescrições anteriores.

## **03. SOLUÇÃO**

Implementação da parametrização do método de cálculo da Superfície Corporal (SC) na prescrição oncológica para permitir a seleção entre as fórmulas Mosteller e Du Bois. O sistema seguirá utilizando o método Mosteller como padrão. Cada unidade de atendimento poderá configurar seu método preferido na aba Oncologia.

O cálculo da SC será aplicado automaticamente com base no método selecionado, sem necessidade de escolha manual pelo médico na hora da prescrição. O método utilizado será visível na tela de prescrição e nos dados da prescrição para auditoria.

Os critérios de aceite incluem a configuração de um método por unidade, garantindo que o valor da SC seja calculado em m² considerando peso (kg) e altura (cm). A alteração no método deve ser implementada nas novas prescrições sem impactar as já realizadas.

## **04. DEMAIS INFORMAÇÕES**

<Não se aplica>

## **05. ASSUNTOS RELACIONADOS**

        Não se aplica
