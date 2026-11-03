---
content_hash: 1b6474ee1cbda28528b6f827139cd716c2c354264728081120266d527fcef3e0
fetched_at: '2026-06-29T00:05:47.003328+00:00'
page_id: '1005449135'
product: rm
source: tdn-rm
title: Serviço de seleção automática de Alíquota
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1005449135
version: 6
---

## **Conteúdo**

**3Conteúdo**

# 1.**Serviço de seleção automática de alíquota IBS/CBS**

2.1. **O que é**

O **Serviço de seleção automática de alíquota** para os tributos **IBS/CBS** é um recurso do **TOTVS Gestão Fiscal** que auxilia no preenchimento automático do campos *Alíquota/Alíquota Cheia* no Cadastro do Item do Movimento, utilizando informações previamente registradas no sistema.

Esse preenchimento segue uma regra definida, com base em dados de entrada específicos, conforme o fluxo descrito abaixo. O objetivo é determinar corretamente a **alíquota** vigente.

## 2.2. **Ordem de seleção**

O processo de seleção automática irá apresentar a alíquota de um determinado Munícipio/Estado (IBS) e da Federação (CBS) baseado na data de emissão da NF e o local de operação informado.

A ordem de busca para tributo **IBS** nas vigências cadastradas obedecem a seguinte ordem de prioridade:

1. Vigência cadastrada que contenha Munícipio ou Estado vinculados nos anexos
2. Vigência cadastrada como alíquota de referência

## 2.3. **Exemplo**

Tela do sistema

Em um movimento cuja data de emissão é **14/10/2025** e o local de operação **Belo Horizonte/Minas Gerais**

Precisamos de uma alíquota cadastrada cujo MunícipioBelo Horizonte e o Estado Minas Gerais estejam cadastrados ou uma alíquota de referência que englobe a data de emissão no período vigente

As alíquotas retornadas para IBS/CBS:  
IBS Estadual: **6%**

IBS Municipal: **9,5%**

CBS: **10%**
