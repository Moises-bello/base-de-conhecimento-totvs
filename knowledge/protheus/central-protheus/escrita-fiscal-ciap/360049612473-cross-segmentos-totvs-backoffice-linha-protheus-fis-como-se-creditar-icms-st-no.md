---
article_id: 360049612473
category: Escrita Fiscal - CIAP
content_hash: ddbb1850b7fa930adf0738a7b534c2fe54b00fd0c8297f3f3f47c4dc4e1b538c
fetched_at: '2026-06-28T22:39:33.873055+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como se creditar
  ICMS ST no CIAP?
type: support-article
updated_at: '2021-07-29T13:09:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049612473-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-se-creditar-ICMS-ST-no-CIAP
---

**Dúvida**

Como se creditar ICMS ST no CIAP ?

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80

**Importante**

**1.** Somente de forma automática na  entrada da nota pelo documento de entrada**(MATA103)**

**2.** Os campos abaixo não devem ser preenchidos manualmente, devem ser preenchidos automaticamente pelo documento de entrada conforme o imposto configurado.  
 **![](https://totvssuporte.zendesk.com/attachments/token/SVKUNTgAji8vQPi2qLMlG8qs1/?name=inline-1709488310.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/SIpDeK5grb99gJi0tLzxncOCj/?name=inline13607672.png)**

**Solução :**

**Processo a executar:**

1. No Configurador **(SIGACFG)**acesse**Ambientes/ Cadastros/ Parâmetros** configure o parâmetro a abaixo:

MV\_STCIAP = S (Soma o valor do ICMS-ST ao ICMS próprio).  
  
***2.*** Informe % MVA  produto ou na exceção fiscal

## **TES:**

**Credita****ICMS**= Sim  
  
**Atu****. Ativo**= Sim ou não

**Desm****. IT. ATF**= Sim/Não 

**CFOP** = 1406 – Padrão.  
  
**Calcula ICMS**= Sim  
  
**Livro Fiscal de ICMS**= Outros  
  
**Livro****Fiscal CIAP**=Sim  
  
**Mat. Consumo**= Não  
  
**Mkp ICM Comp. (F4\_MKPCMP)** = **Não;**  
  
**Marg. Solid. (F4\_MKPSOL)** = **Configuração.**  
  
**Boletim técnico Ciap**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=187532625>
