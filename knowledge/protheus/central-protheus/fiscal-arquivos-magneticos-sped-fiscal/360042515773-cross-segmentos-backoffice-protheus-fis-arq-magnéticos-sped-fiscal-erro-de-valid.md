---
article_id: 360042515773
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 3fb562bee1c13da26f587f96d5ef73254764c5eb0d04f2d03071034082a7fc9c
fetched_at: '2026-06-28T22:42:02.477827+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  Erro de validação "Campo obrigatório CLAS_ESTAB_IND do Registro 0002"
type: support-article
updated_at: '2025-02-11T21:34:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042515773-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Erro-de-valida%C3%A7%C3%A3o-Campo-obrigat%C3%B3rio-CLAS-ESTAB-IND-do-Registro-0002
---

**Ocorrência**Ao importar o arquivo magnético do **Sped Fiscal**, novo **Layout 014**, ocorre o erro de validação do **Registro 0002** (Classificação do estabelecimento Industrial ou equiparado a industrial) **"Campo obrigatório CLAS\_ESTAB\_IND"**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056028714/mceclip0.png)  
  
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**A pergunta da Wizard **Classe de Atividade Industrial** não foi preenchida.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Acesse a rotina **SPEDFISCAL**;  
 2. Na aba **Identificação do Contribuinte**, preencha a pergunta **Classe de Atividade Industrial** com a opção que a empresa se enquadra;  
![](https://totvssuporte.zendesk.com/attachments/token/6MaKClnExQPfyuKPCNk4Vn9qm/?name=inline1978412976.png)  
3. Preencha as demais perguntas e gere o arquivo magnético;  
4. Importe o arquivo no **PVA**, veja que o erro não ocorrerá novamente.

​
