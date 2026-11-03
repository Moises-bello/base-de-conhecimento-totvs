---
article_id: 29368652379671
category: Ativo Fixo - Aquisição por Transferência
content_hash: e076c08f244ec43dbcb6a52fd29483892c74823b012bdf5970d30c6ea8651b2b
fetched_at: '2026-06-28T22:41:56.932345+00:00'
product: protheus
section_id: 1500001535341
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA251 - AF251ICMS
type: support-article
updated_at: '2025-01-20T17:57:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29368652379671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA251-AF251ICMS
---

**Ocorrência**Na rotina ATFA251 - Aquisição por transferência apresenta o help AF251ICMS  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29368648912791)

**Ambiente:**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - a partir da release 12.1.2210

**Solução:**Este Help ele pode ser apresentado pelos 3 motivos abaixo:

1. **Valor de ICMS não está sendo usado totalmente:**

   No procedimento da rotina ATFA251 - Aquisição por transferência, o valor do bem selecionado deve ser rateado em 100%. Por exemplo:

   - Se o bem NFE0001 for selecionado e criado como o bem XXX001, o valor original do mesmo deve ser R$ 82.000 e o ICMS R$ 18,00, totalizando 100%.

   - Se o bem NFE0001 for selecionado e dividido em dois bens, XXX001 e XXX002, o rateio pode ser feito em 40% e 60%. Assim, XXX001 terá R$ 32,80 e ICMS de R$ 7,20, enquanto XXX002 terá R$ 49,20 e ICMS de R$ 10,80.
2. **Bens que possui valor de ICMS e está informado para não gerar o código Ciap:**  
   Para bens que está fazendo o processo de aquisição por transferência caso o campo "Gera CIAP" esteja = Não , será necessário ter ao menos um bem com o valor total do ICMS e com "Gera Ciap" = SIM, para que ele não apresente o help.  
     
   Essa regra foi criada para que haja conformidade nas informações da rotina ATFA251  
     
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29368648913559)
3. **Bens estão com o campo "Calcula Pis" = a "Sim" e outros = a "Não"**  

   Este help acontece também quando os bens que está selecionando, nos seus cadastrados pela rotina ATFA012, alguns deles estão com o campo "Calcula Pis" = a "Sim" e outros = a "Não"  
     
   ![](https://totvssuporte.zendesk.com/attachments/token/DX3L4jpSG4EqCiEBpHm58J8kY/?name=image.png)

   Dessa forma, no momento que é realizado o processo na rotina ATFA251, o sistema não consegue localizar as informações corretas, pois ele adiciona duas linhas na aba "Detalhes do imposto"  
     
   ![](https://totvssuporte.zendesk.com/attachments/token/M48CcAycE35aRFusHTsASaIiu/?name=image.png)

   Portanto, é necessário que acesse os bens que deseja realizar a aquisição por transferência, localize o campo "Calcula Pis", e deixem todos com a mesma informação, todos com "Sim", ou todos como "Não".

**Saiba mais:**<https://tdn.totvs.com/pages/releaseview.action?pageId=675552223>  
<https://tdn.totvs.com/pages/releaseview.action?pageId=746498405>
