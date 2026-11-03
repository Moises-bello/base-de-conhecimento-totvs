---
article_id: 17272343171991
category: Call Center - Dúvidas Gerais
content_hash: 88c00ce2145ebeb805b4bd57877107b344a7386053deae3f324c6f92a61a65aa
fetched_at: '2026-06-28T22:41:26.973923+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - TK061NOCON
  A lista selecionada não é uma Lista de contato para Marketing ou Vendas
type: support-article
updated_at: '2025-01-10T19:49:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17272343171991-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-TK061NOCON-A-lista-selecionada-n%C3%A3o-%C3%A9-uma-Lista-de-contato-para-Marketing-ou-Vendas
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17272302633623) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao incluir um novo item na lista de contato, apresenta o HELP **"TK061NOCON"  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17272261958295)**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center (SIGATMK) - Todas as versões.  
 **Causa**

Este help é apresentado quando não existe o preenchimento do campo 'Contato' (U6\_CONTATO) ao efetuar uma nova inclusão de item na rotina.

**Solução**   
Devido uma validação padrão do campo 'Contato' o help é apresentado ao incluir/ atualizar um novo registro na linha SU6. Para que esse help não ocorra, o campo 'Contato' (U6\_CONTATO) deve estar preenchido.
