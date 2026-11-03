---
article_id: 11936259269527
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 2231acf1cc7c92f859f6a82f0abc08d98ebc5693347c95d5d80dbf52f1f3ffe5
fetched_at: '2026-06-28T22:38:42.793862+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - CFOP do campo
  "Tes Ret.Simb" (F4_TESP3) na venda com Poder de Terceiros
type: support-article
updated_at: '2025-01-10T19:46:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11936259269527-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-CFOP-do-campo-Tes-Ret-Simb-F4-TESP3-na-venda-com-Poder-de-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Para utilizar o saldo de "Poder de Terceiros em meu Poder" para uma venda sem a necessidade de um retorno simbólico utilizamos o campo "Tes Ret.Simb" (F4\_TESP3), porém o CFOP que o sistema está carregando na venda é a de Retorno Simbólico e não o CFOP de Venda.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**  
O campo "Tes Ret.Simb" (F4\_TESP3) tem como objetivo baixar o saldo do Poder de Terceiros que está fisicamente na empresa permitindo a venda, porém, não gera a NF de retorno de Poder de Terceiros.  
  
Sendo assim, se a operação é de venda, deverá ser criada um TES específico para uso neste campo com a finalidade de devolver o saldo do Poder de Terceiros, campo "poder Terc." (F4\_PODER3) e o CFOP utilizado deverá ser o de venda e não o da operação de retorno simbólico.  
  
Exemplo :  
  
**TES de Venda**   
Campo "poder Terc." (F4\_PODER3) preenchido para não controlar Poder de Terceiros (pois é uma venda) e o campo "Tes Ret.Simb" (F4\_TESP3) possui outro TES:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11934780033047)

CFOP de Venda:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11935071130519)

TES para uso do Poder em Terceiros em seu poder para uma venda, "Tes Ret.Simb" (F4\_TESP3), apenas para baixa do saldo de Poder de Terceiros:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11935021741847)

Novamente CFOP de Venda:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11935084741015)

Dessa forma o sistema vai gerar a NF de venda, com o CFOP específico de Venda, realizando a baixa do saldo de Poder de Terceiros (tabela SB6)  
  
**Saiba mais**: [FAT0285 - Poder DE/EM Terceiro](https://tdn.totvs.com/x/xyCgGg)
