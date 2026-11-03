---
article_id: 360052277153
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e09f028aad54851c9b85cf77cb8f47cd2104075bacef588198e2bef974fab510
fetched_at: '2026-06-28T22:42:03.827792+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - SPED FISCAL - BLOCO G - CAMPO 4 (SALDO_IN_ICMS) DO REGISTRO G110
type: support-article
updated_at: '2021-04-28T14:24:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052277153-MP-FIS-SPED-FISCAL-BLOCO-G-CAMPO-4-SALDO-IN-ICMS-DO-REGISTRO-G110
---

**Ocorrência**

Ao gerar o arquivo do **Sped Fiscal** ocorre o erro de validação no registro **G110 - Campo 4 SALDO\_IN\_ICMS**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081242354/mceclip0.png)  
   
 **Ambiente**

Microsiga Protheus – Livros Fiscais – A partir da versão 12.1.17  
   
 **Causa**

Quando é realizado o preenchimento na Wizard, do **Sped Fiscal**, com o **Campo "Início Obrigação Escrituração Fiscal CIAP"** = **Não**, conforme abaixo, o **campo 4 (SALDO\_IN\_ICMS)** do registro **G110** é zerado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081242414/mceclip1.png)  
   
 **Solução**

Para solucionar essa ocorrência, realize o procedimento abaixo:

1. Aplique o pacote atualizado:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615333-MP-FIS-Atualiza%C3%A7%C3%A3o-do-Ambiente-Fiscal-M%C3%B3dulo-09-para-a-correta-gera%C3%A7%C3%A3o-dos-Arquivos-Magn%C3%A9ticos-fiscais-?source=search>

2. Gere o **Sped Fiscal** novamente.

Mais Informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=552571106>
