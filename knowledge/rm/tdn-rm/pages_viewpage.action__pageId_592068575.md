---
content_hash: 6d896be44f455a34fec9cd48b3ad6a20097f2b34e76d03ecddcc41d246594417
fetched_at: '2026-06-29T00:10:56.143678+00:00'
page_id: '592068575'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Cadastros > Replicação de Pacientes entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592068575
version: 7
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Guia Passo a Passo**

ItensVisão Geral

## **01. VISÃO GERAL**

Esse processo realiza a cópia dos pacientes entre as coligadas dentro de um intervalo definido de horas por exemplo 12 horas retroativas. A partir da definição dessas horas o processo irá definir como Data Hora Inicial a Data Hora do Servidor no momento do processamento menos a quantidade de horas informada no campo **Quantidade de Horas Retroativas** e com Data Hora Final a Data Hora do Servidor. É importante salientar que somente os pacientes com **CPF** informados no ato do cadastro serão selecionados. A performance desse processo irá depender da quantidade de horas definidas, como sugestão esse processo deverá ser executado sempre em períodos de menor concorrência.

Guia Passo a Passo

## **02. GUIA PASSO A PASSO**

Adicione as etapas envolvidas:

1.Navegue no menu Atendimento>Dados do Paciente

2.Na visão de Dados de Paciente Selecione Processos > Processo de Replicação de Pacientes

3.Na tela do Processo defina a quantidade de horas retroativas que o processo irá usar como base.

## Artigos relacionados
