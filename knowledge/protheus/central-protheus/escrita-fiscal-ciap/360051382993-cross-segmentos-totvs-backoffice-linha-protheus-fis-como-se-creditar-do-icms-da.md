---
article_id: 360051382993
category: Escrita Fiscal - CIAP
content_hash: 01a1fc7522992a100a8c800b0537ae6cc6a9fc2ee9beead62ebfe065358e9af6
fetched_at: '2026-06-28T22:39:33.854607+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como se creditar
  do ICMS da nota de conhecimento de frete vinculada a nota de compra do ativo imobilizado?
type: support-article
updated_at: '2022-04-25T13:22:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051382993-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-se-creditar-do-ICMS-da-nota-de-conhecimento-de-frete-vinculada-a-nota-de-compra-do-ativo-imobilizado
---

**Dúvida**

Como se creditar do ICMS da nota de conhecimento de frete vinculada a nota de compra do ativo imobilizado?  
  
**Ambiente**  
Protheus - Livros Fiscais - A partir da versão 11.80

**Importante :**

**1.** Não será agregado ao valor do ICMS próprio

2. Na apropriação do CIAP o parâmetro MV\_FTCIAP=S o valor referente ao frete será considerado junto com o valor de ICMS, para a composição da parcela de apropriação do período.

**3**. Será descontado o valor do frete no registro G140, quando o valor do frete é lançado na nota fiscal de compra

**4.** Os valores de ICMS próprio zero para fornecedores optantes do simples nacional.

**5.** Somente de forma automática na  entrada da nota pelo documento de entrada**(MATA103)**

**6.**Os campos abaixo não devem ser preenchidos manualmente, devem ser preenchidos automaticamente pelo documento de entrada conforme o imposto configurado.

**![](https://totvssuporte.zendesk.com/attachments/token/SVKUNTgAji8vQPi2qLMlG8qs1/?name=inline-1709488310.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/SIpDeK5grb99gJi0tLzxncOCj/?name=inline13607672.png)**

**Solução :**

**Processo a executar:**

**1.** No Configurador**(SIGACFG)**acesse**Ambientes/ Cadastros/ Parâmetros**configure o parâmetro a abaixo:

MV\_FTCIAP = S 

## **2.** TES

**Credita****ICMS**= Sim  
  
**Atu****. Ativo**= Sim

**CFOP** =

**Calcula ICMS**= Sim

**Livro Fiscal de ICMS**= Outros

**Livro****Fiscal CIAP**=Sim

**3.** Evidencia  MANUTENÇÃO CIAP

![](https://totvssuporte.zendesk.com/attachments/token/kUb6WzeKaOcZYbQm6tgUEi529/?name=inline-414530924.png)​

**4.** Demostrado no livro corretamente o valor do ICMS do ICMS bem 120,00 e ao ser apropriado o valor mensal do mensal do ICMS do bem 2,50 + 0,25 ICMS da nota de conhecimento do frete totalizando 2,75.

![](https://totvssuporte.zendesk.com/attachments/token/3jgnzxfJQ5ooeanCxiclj4SAb/?name=inline-845758368.png)​

**4.** Deve estar com atualização abaixo:

A Release Oficial foi expedida e publicada na Central de Downloads.  
O pacote pode ser acessado no endereço: 12.1.27:<https://r.totvs.io/p/971974> ; 12.1.25:<https://r.totvs.io/p/971973> ; 12.1.23:<https://r.totvs.io/p/971972> ; 12.1.17:<https://r.totvs.io/p/971971> ;

Segue resposta da nossa consultoria tributaria  
<https://tdn.totvs.com/pages/releaseview.action?pageId=437257747>
