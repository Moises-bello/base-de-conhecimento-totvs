---
article_id: 17886310166679
category: Financeiro - Reinf
content_hash: 9146b8e52537256a8ca13fb1f60a73d959c11c06e9b5059ff6a749342ddfd2a6
fetched_at: '2026-06-28T22:37:51.874258+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Valores do
  PCC não são apresentados no registro T158
type: support-article
updated_at: '2023-09-28T20:43:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17886310166679-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Valores-do-PCC-n%C3%A3o-s%C3%A3o-apresentados-no-registro-T158
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17887499106071)** Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**O que posso avaliar quando os valores do PCC não são gerados no registro T158?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - REINF - A partir da versão 12.1.33  
  
**Solução**A solução para essa ocorrência envolverá avaliar parâmetros, compartilhamento de tabelas e também uma atualização.

   
**01 - Validar compartilhamento das tabelas, conforme artigos:**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Compartilhamento das novas tabelas do REINF Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12750702835351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Compartilhamento-das-novas-tabelas-do-REINF-Financeiro?source=search)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como gerar o layout T158 REINF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16095149270423-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-gerar-o-layout-T158-REINF?source=search)  
   
**02 - Validar parâmetros:**  
**MV\_TAFVLRE** = 2\_01\_02  
**MV\_TAFAMBR** = 1 -Produção  2-Homologação  
Consulte o parâmetro **MV\_INTTAF** , ele foi descontinuado e precisa estar como **N**.  
Consulte o parâmetro **MV\_TAFLPRC**, precisa estar com o conteúdo padrão **2000**.  
   
**03 - Garantir atualizações:**

**12.1.2210:** <https://suporte.totvs.com/portal/p/10098/download?e=1117595>   
**12.1.2210**: <https://suporte.totvs.com/portal/p/10098/download?e=1119309>  
 

**Saiba Mais**

**Acompanhe nossa página e fique por dentro de tudo sobre a REINF no FINANCEIRO**

<https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro>
