---
content_hash: 934a4dedbae1e6e5c54f2da4471cf5b75b5485d2125e6f72aaa2327598541d6d
fetched_at: '2026-06-29T00:11:40.848514+00:00'
page_id: '795085662'
product: rm
source: tdn-rm
title: Alterações - S-2220 - S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795085662
version: 7
---

false

**A partir das Versões:**

* 12.1.2302.235
* 12.1.2306.182
* 12.1.2310.116 e superiores

**CONTEÚDO**

IMPORTANTE!

---

## **01. VISÃO GERAL**

Este documento visa apresentar as mudanças no evento S-2220 para atender o Leiaute do eSocial versão S-1.2.

## **02. ALTERAÇÕES REALIZADAS**

### **02.01.** **TAG <nrCRM> - NÚMERO DO CRM**

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Campo {nrCRM}: alterado tamanho do campo nos grupos {medico} e {respMonit} | 1-8 | 1-10 |

**Alteração**: Os campos <nrCRM> do grupo <medico> e <nrCRM> do grupo <respMonit> foram atualizados na geração do XML, passando a aceitar até 10 caracteres.

XML:

**Importante!**

O cadastro de Profissional da Saúde e de Responsáveis pelas Monitorações Biológicas permitem que seja informado nos campos relacionados ao CRM mais de 10 caracteres, pois já existiam no sistema mesmo antes do eSocial. Contudo, na geração do XML o sistema irá truncar o valor informado, apresentando somente até o 10º caractere do cadastro.

## **03. MAPEAMENTO DO EVENTO**

Acesse o mapeamento do evento clicando no link abaixo:

* + [Evento S-2220](https://tdn.totvs.com/display/LRM/Evento+S-2220)
