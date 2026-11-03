---
content_hash: 2577bd0f6775eb4c7eb6a9b27548d8249081e9b8af78e2bde8f944d375407fa5
fetched_at: '2026-06-29T00:11:11.009787+00:00'
page_id: '644742948'
product: rm
source: tdn-rm
title: Lançamento automático da Guia de Honorário individual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=644742948
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Para alguns convênios é necessário ter uma guia de honorário individual para cada prestador e procedimento executado.

Para isso, as seguintes condições devem ocorrer, para que a guia seja lançada e associada ao honorário:

* Padrão de faturamento **ANS - Tiss** do convênio
* Informação específica igual "**Faturamento para médicos**"
* Pacientes **internados**
* **Parâmetro marcado**: 'Lançar automaticamente a guia de honorário individual quando utilizar o padrão especial "Faturamento para médicos", para paciente internado e quando não for informado a guia associada'

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

1. Ao lançar um honorário para um médico e o atendimento for de internação, o padrão do convênio é TISS e padrão específico Faturamento para médicos
2. Não informar uma guia associada
3. O sistema fará a inclusão da guia de Honorário individual, automaticamente e fará o vínculo com o honorário lançado

 

## **03.** **TABELAS UTILIZADAS**

* SZATENDHONORARIO
* SZATENDAUTORIZ
