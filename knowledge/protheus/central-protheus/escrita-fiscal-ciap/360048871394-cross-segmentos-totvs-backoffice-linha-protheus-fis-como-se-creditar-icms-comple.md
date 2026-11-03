---
article_id: 360048871394
category: Escrita Fiscal - CIAP
content_hash: 4bdffd6f170dadeb3b5a7db5462d86daccc42bb6c92b5f89ab9defcb2f5c7453
fetched_at: '2026-06-28T22:39:33.865485+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como se creditar
  ICMS complementar no CIAP?
type: support-article
updated_at: '2023-02-16T14:15:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048871394-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-se-creditar-ICMS-complementar-no-CIAP
---

**Dúvida**

Como se creditar ICMS complementar no CIAP ?  
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80

**Importante**

**1.** Somente de forma automática na  entrada da nota pelo documento de entrada**(MATA103)**

**2.** Os campos abaixo não devem ser preenchidos manualmente, devem ser preenchidos automaticamente pelo documento de entrada conforme o imposto configurado.  
 **![](https://totvssuporte.zendesk.com/attachments/token/SVKUNTgAji8vQPi2qLMlG8qs1/?name=inline-1709488310.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/SIpDeK5grb99gJi0tLzxncOCj/?name=inline13607672.png)**

**Solução:**

**1.** No Configurador **(SIGACFG)**acesse**Ambientes/ Cadastros/ Parâmetros** configure o parâmetro a abaixo:

MV\_DACIAP = S  (Soma o valor do ICMS complementar ao ICMS próprio)

**2.** Configuração TES

**Credita****ICMS**= Sim  
  
**Atu****. Ativo**= Sim ou não

**Desm****. IT. ATF**= Sim/Não 

**CFOP** =   
  
**Calcula ICMS**= Sim  
  
**Livro Fiscal de ICMS**= Outros  
  
**Livro****Fiscal CIAP**=Sim  
  
**Mat. Consumo**= sim/Não  
  
**Cal.Dif. ICM = Sim**  
  
**Boletim técnico Ciap**

<https://tdn.totvs.com/pages/releaseview.action?pageId=708871751>
