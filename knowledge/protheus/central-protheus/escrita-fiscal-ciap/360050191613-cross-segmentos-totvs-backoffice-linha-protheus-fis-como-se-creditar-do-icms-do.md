---
article_id: 360050191613
category: Escrita Fiscal - CIAP
content_hash: 153850fdbc24f590aca1c161e0461bebb1bad2370ee3f112c5dd00fcdec8b284
fetched_at: '2026-06-28T22:39:33.860672+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como se creditar
  do ICMS do frete incluso na nota de compra do ativo imobilizado?
type: support-article
updated_at: '2023-09-12T18:28:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050191613-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-se-creditar-do-ICMS-do-frete-incluso-na-nota-de-compra-do-ativo-imobilizado
---

**Dúvida**

Como se creditar do ICMS do frete incluso na nota de compra do ativo imobilizado?

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80

**Importante**

**1.** Somente de forma automática na  entrada da nota pelo documento de entrada**(MATA103)**

**2.** Os campos abaixo não devem ser preenchidos manualmente, devem ser preenchidos automaticamente pelo documento de entrada conforme o imposto configurado.  
 **![](https://totvssuporte.zendesk.com/attachments/token/SVKUNTgAji8vQPi2qLMlG8qs1/?name=inline-1709488310.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/SIpDeK5grb99gJi0tLzxncOCj/?name=inline13607672.png)**

**Solução :**

**Processo a executar:**

**1.** No Configurador **(SIGACFG)**acesse**Ambientes/ Cadastros/ Parâmetros** configure o parâmetro a abaixo:

MV\_FTCIAP = S (Soma o valor do FRETE ao ICMS próprio).

## **TES:**

**Credita****ICMS**= Sim  
  
**Atu****. Ativo**= Sim ou não

**Desm****. IT. ATF**= Sim/Não 

**CFOP** =

**Calcula ICMS**= Sim  
  
**Livro Fiscal de ICMS**= Outros  
  
**Livro****Fiscal CIAP**=Sim  
  
**Mat. Consumo**= Não/Sim

**Desp . Ac . ICMS** = Sim/Não

**Boletim técnico Ciap**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=708871751>
