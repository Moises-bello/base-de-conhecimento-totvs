---
article_id: 28570030464151
category: Materiais - Compras (SIGACOM)
content_hash: 5264a437e845884ce972f83b03ba9cfcf96e0dd320465a37efb4ac143a614580
fetched_at: '2026-06-28T22:41:20.075144+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - MATA103 - Ocorrência
  do help A103VALSD4
type: support-article
updated_at: '2024-12-16T19:15:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28570030464151-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-MATA103-Ocorr%C3%AAncia-do-help-A103VALSD4
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28569993138327) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao incluir ou classificar uma nota que possua Empenho na rotina Documento de Entrada MATA103, sistema gera help A103VALSD4.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Comporas - a partir da 12.1.33  
  
**Solução**Quando uma nota que possui vínculo com Ordem de Produção (OP) é incluída ou classificada na rotina Documento de Entrada MATA103 o sistema verifica se há Empenho da Ordem de Produção (OP) através da função A103ValSD4.

Se existir empenho, o sistema consulta o conteúdo do parâmetro MV\_NFESD4 para saber se deverá ou não gerar o help. Segue abaixo opções de conteúdo desse parâmetro e sua respectiva função.

PARAMETRO MV\_NFESD4: (V)isualizar / (S)im / (N)ao

VV - Sempre mostra janela de confirmação (Default)  
SV - Quando o produto não faz parte do empenho da OP confirmar item.  
NV - Quando o produto não faz parte do empenho da OP não confirmar item.  
VS - Quando a qtde empenhada e menor que qtde do item confirmar movimentação.  
VN - Quando a qtde empenhada e menor que qtde do item não confirmar movimentação.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
