---
article_id: 6190694734359
category: Call Center - Televendas
content_hash: 64457c27af6050fbdb9a958500831bb55ca3b8927bd84573e55ff560cb44ee06
fetched_at: '2026-06-28T22:41:30.378447+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: 'Cross Segmentos-TOTVS Backoffice (Linha Protheus) - SIGATMK - Impostos agregados
  - Call Center - Televendas '
type: support-article
updated_at: '2022-05-19T13:24:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6190694734359-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Impostos-agregados-Call-Center-Televendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Realizo uma venda com IPI no Call Center, gero uma NF no Faturamento, altero a alíquota no cadastro do Produto e os valores da NF e o Televendas ficam divergentes.    
  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus) - SIGATMK – Todas as versões  
  
**Solução**O fato gerador dos impostos é a geração da Nota Fiscal (NF), portanto, até gerar a NF a alíquota do imposto é uma variável (pois pode ter alteração por meio de legislação entre a proposta da venda - Call Center - e a geração da NF)  
  
Sendo assim, ao alterar a alíquota no cadastro de produtos após a emissão da NF, o sistema pode carregar a nova alíquota em operações anteriores a geração da NF (pois não há gravação do calculo do imposto até a geração da NF)  
  
Considerando que o IPI é um imposto que agrega no total da NF, além da alíquota, o valor total do Televendas pode ficar divergente também devido ao imposto.  
  
Portanto, o imposto a ser sempre avaliado deve ser o gravado em Nota Fiscal e não das rotinas anteriores a geração da mesma.  
  
Este tratamento do Call Center é o mesmo utilizado para Planilha Financeira do pedido de venda do Faturamento .
