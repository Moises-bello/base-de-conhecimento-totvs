---
article_id: 360050348373
category: Faturamento - Integrações
content_hash: 475b9514ed54dcdaaa393a70e9ebdc8b781689fa4739b32266be20c600d1d84b
fetched_at: '2026-06-28T22:38:26.576671+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: 'MP - FAT - Configuração Integração GFE x Faturamento Protheus  '
type: support-article
updated_at: '2022-01-14T17:49:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050348373-MP-FAT-Configura%C3%A7%C3%A3o-Integra%C3%A7%C3%A3o-GFE-x-Faturamento-Protheus
---

**Dúvida**  
Configuração Integração GFE x Faturamento Protheus   
  
**Ambiente**Microsiga Protheus -  todas as versões.  
  
**Solução**

Configurar os parâmetros no programa **GFEX000 - Parâmetros Módulo**. Esse programa está disponível no menu, em **Atualizações** > **Cadastros** >**Parâmetros** > **Parâmetros Módulo.**Na aba **Integração ERP**, os parâmetros:

* **Origem dos Cadastros - MV\_CADERP** deverá possuir o valor **1 - ERP**;
* **ERP Integrado - MV\_ERPGFE** deverá possuir o valor **2-Protheus**;

Na aba **Integração Protheus**, os parâmetros:

* **GFE Ativo - MV\_INTGFE** deverá estar marcado, e no **SIGACFG - Configurador**, este parâmetro **MV\_INTGFE**deve estar com o valor **.T.**
* **Modo Integração - MV\_INTGFE2** deverá possuir o valor **1-Direta**;
* **Código do Emitente - MV\_EMITMP** deverá possuir o valor **1-Numeração Própria**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075683193/mceclip1.png)

[![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075684653/mceclip2.png)](https://centraldeatendimento.totvs.com/hc/es/articles/360037463313)

**Importante**  
  
Para dúvida gerais e mensagens da integração favor acessar o link abaixo  
<https://tdn.totvs.com/x/RbMbF>  
O Manual completo de Integração está disponível no link  
<https://tdn.totvs.com/x/wwGVIQ>
