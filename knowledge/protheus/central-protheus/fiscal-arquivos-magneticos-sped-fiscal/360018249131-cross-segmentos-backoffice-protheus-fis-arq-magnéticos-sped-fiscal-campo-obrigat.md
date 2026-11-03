---
article_id: 360018249131
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 045cc8824bb7445f8bbaf288e333dd7b70b80c2fa37bfb11476ca446393425ef
fetched_at: '2026-06-28T22:42:01.132016+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Campo obrigatório COD_OR no registro E116 e E316
type: support-article
updated_at: '2025-02-11T20:56:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018249131-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Campo-obrigat%C3%B3rio-COD-OR-no-registro-E116-e-E316
---

**Ocorrência**O sistema não está preenchendo o campo COD\_OR do registro E116 ou E316 causando erro de validação no arquivo do Sped Fiscal.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013443792/mceclip0.png)

**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
   
 **Causa**   
 Esse incidente ocorre, pois a parametrização do sistema está incorreta. Provavelmente, o Código da Obrigação a Recolher não foi informado na Guia de Recolhimento (**tabela SF6**).  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Acesse a rotina Guia Nacional de Recolhimento (**MATA960 - tabela SF6**);  
  
 2. Preencha o campo **Cód.Obrig.** (**F6\_COBREC**) com o devido código de recolhimento;

![COD_OR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360013462911/COD_OR.gif)

3. Gere novamente o arquivo do Sped Fiscal.
