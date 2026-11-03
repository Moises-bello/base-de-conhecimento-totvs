---
article_id: 4420161801751
category: Financeiro
content_hash: c569a70f376f147af57a732339f845acbecac458e142a8ce18ff73af53a78193
fetched_at: '2026-06-28T22:38:01.191113+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - Integração RM X Protheus - Erro
  cadastro De/PARA Natureza FINI050 ACCOUNTPAYABLEDOCUMENT
type: support-article
updated_at: '2022-06-14T23:42:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420161801751-Cross-Segmentos-Backoffice-Linha-Protheus-Integra%C3%A7%C3%A3o-RM-X-Protheus-Erro-cadastro-De-PARA-Natureza-FINI050-ACCOUNTPAYABLEDOCUMENT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05 min****Ocorrência**Erro Integração **RM** apresenta array out of bounds ( 3 of 1 ) ] - [|THREAD ERROR ([14500], JOB\_WS\_, THIS) |array out of bounds ( 3 of 1 ) on V2000(**FINI050**.**PRW**) - (**FINI050** **ACCOUNTPAYABLEDOCUMENT**)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O problema pode ocorrer quando existe erro de Cadastro do De/para, e este exemplo no **DE/PARA** de cadastro **Natureza** que devem estar amarradas do **RM** com o **Protheus**: 

**Exemplo**

![ADRI.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4420158617111/ADRI.PNG)

Na imagem acima temos a linha com os campos **Valor Exterior** (origem **RM**) e **Valor Interno** (**Natureza** **Protheus**).

Porém esse processo precisa estar amarrado de forma adequada ao **Protheus**, seguindo suas particularidades como **Grupo de empresa | compartilhamento da SED | ED\_CODIGO**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420161734935/mceclip0.png)**

o **código do grupo de empresa** o uso do caractere PIPE "|" **compartilhamento e Natureza**.

Seguindo essas orientações será possível corrigir o problema e o Error.log ser contornado, sendo possível assim importar os títulos do **RM** para o **Protheus**.   

**Saiba Mais**[FIN0006\_INTG\_Adapters\_EAI](https://tdn.totvs.com/display/PROT/FIN0006_INTG_Adapters_EAI)
