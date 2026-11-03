---
article_id: 360022158691
category: Materiais - Compras (SIGACOM)
content_hash: 6bba4eb873b9b116d67cb38c7f59c6646c12efd8736a83b5bff1d9b6246f7db2
fetched_at: '2026-06-28T22:41:07.597460+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como dar entrada em
  NF de Beneficiamento pelo Totvs Colaboração ou Importador XML ?
type: support-article
updated_at: '2024-06-13T16:53:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022158691-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-dar-entrada-em-NF-de-Beneficiamento-pelo-Totvs-Colabora%C3%A7%C3%A3o-ou-Importador-XML
---

**Dúvida**

Como dar entrada em NF de Beneficiamento pelo Totvs Colaboração ou Importador Xml ?  
  
**Ambiente**

Protheus – Compras – A partir da versão 12.17  
  
**Solução**

Para o lançamento de notas de beneficiamento pela funcionalidade do Totvs Colaboração, é necessário obter o CFOP do XML e inseri-lo no parâmetro MV\_XMLCFBN. Se esse campo estiver em branco, a nota será gerada como Tipo Normal.

Além disso, para a nota de beneficiamento, é preciso realizar a amarração 'Produto x Cliente' no módulo de Faturamento. Verifique o CNPJ do fornecedor e cadastre-o também como cliente para processar a nota de beneficiamento

***Saiba Mais :***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Algumas Regras para importação de NFe no Totvs Colaboração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025780771)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Códigos de erro Totvs Colaboração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527792-MP-SIGACOM-C%C3%B3digos-de-erro-Totvs-Colabora%C3%A7%C3%A3o)
* [TC06 - Erros (Códigos)](https://tdn.totvs.com/pages/viewpage.action?pageId=271663193)
* [SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML?source=search)
* [Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [TOTVS Colaboração - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=271661626)
* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
