---
article_id: 360055937193
category: Escrita Fiscal - CIAP
content_hash: b054b505237c5ab8da446dd074f550fc3e59da93c819be9fb3c48f9399785ca2
fetched_at: '2026-06-28T22:39:33.845782+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como se creditar
  do ICMS da nota de conhecimento de frete com ICMS complementar vinculada a nota
  de compra do ativo imobilizado?
type: support-article
updated_at: '2022-04-25T13:16:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055937193-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-se-creditar-do-ICMS-da-nota-de-conhecimento-de-frete-com-ICMS-complementar-vinculada-a-nota-de-compra-do-ativo-imobilizado
---

**Dúvida**

Como se creditar do ICMS da nota de conhecimento de frete com ICMS complementar vinculada a nota de compra do ativo imobilizado?  
  
**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80

**Importante :**

**1.** Não será agregado ao valor do ICMS próprio

2. Na apropriação do CIAP o parâmetro MV\_FTCIAP=S o valor referente ao frete será considerado junto com o valor de ICMS, para a composição da parcela de apropriação do período.

**3**. Será descontado o valor do frete no registro G140, quando o valor do frete é lançado na nota fiscal de compra

**4.** Os valores de ICMS próprio zero para fornecedores optantes do simples nacional.

**5.** Somente de forma automática na  entrada da nota pelo documento de entrada**(MATA103)**

**6.**Os campos abaixo não devem ser preenchidos manualmente, devem ser preenchidos automaticamente pelo documento de entrada conforme o imposto configurado.

**![](https://totvssuporte.zendesk.com/attachments/token/SVKUNTgAji8vQPi2qLMlG8qs1/?name=inline-1709488310.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/SIpDeK5grb99gJi0tLzxncOCj/?name=inline13607672.png)**

**Solução :**

**Processo a executar:**

**1.** No Configurador**(SIGACFG)**acesse**Ambientes/ Cadastros/****Parâmetros configure** o parâmetro a abaixo:

MV\_FTCIAP = S 

## **2.**TES

**Credita****ICMS**= Sim  
  
**Atu****. Ativo**= Sim

**CFOP** =

**Calcula ICMS**= Sim

**Cal.dif.icm**

**Livro Fiscal de ICMS**= Outros

**Livro****Fiscal CIAP**=Sim

**3.**Evidencia  MANUTENÇÃO CIAP

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091324574/mceclip0.png)**

**4. Demostrado no livro corretamente o valor do ICMS do ICMS bem 120,00 e ao ser apropriado o valor mensal do mensal do ICMS do bem 2,50 + 0,56+ ICMS da nota de conhecimento do frete totalizando 3,06.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091324954/mceclip1.png)**

**4.** Deve estar com atualização abaixo:

A Release Oficial foi expedida e publicada na Central de Downloads.  
O pacote pode ser acessado no endereço: 12.1.27:<https://r.totvs.io/p/983682> ; 12.1.25:<https://r.totvs.io/p/983681> ; 12.1.23:<https://r.totvs.io/p/983680> ; 12.1.17:<https://r.totvs.io/p/983679> ;

Segue resposta da nossa consultoria tributaria  
<https://tdn.totvs.com/pages/releaseview.action?pageId=437257747>
