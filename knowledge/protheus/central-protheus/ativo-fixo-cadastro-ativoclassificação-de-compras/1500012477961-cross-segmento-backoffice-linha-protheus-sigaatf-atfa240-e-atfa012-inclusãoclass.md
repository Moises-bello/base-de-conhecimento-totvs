---
article_id: 1500012477961
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 5abaa22f5c5ca7c156a374197baf165711c72d89590ba416755450d37490afb1
fetched_at: '2026-06-28T22:41:48.451174+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF- ATFA240 e ATFA012 Inclusão/classificação
  de um bem com quantidade menor que 1.
type: support-article
updated_at: '2021-11-04T13:51:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012477961-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-e-ATFA012-Inclus%C3%A3o-classifica%C3%A7%C3%A3o-de-um-bem-com-quantidade-menor-que-1
---

**Dúvida**É possível a classificação de um bem com quantidade menor que 1?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS Ativo Fixo - Todas as versões.  
  
**Solução**

Sim, Ao incluir uma Nota fiscal através do módulo de compras, que gera ativo fixo ou ao incluir um bem pela rotina de cadastro (ATFA012). O campo N1\_QUANTD (Quantidade) fica disponível para edição, podendo ser informado a quantidade menor que 1, conforme exemplo a baixo:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019815001/mceclip0.png)**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019543302/mceclip1.png)

Obs.

1) O Campo N1\_QUANTND esta disponível para edição somente ao classificar o bem ou na aquisição.

2) O campo N1\_QUANTND está disponível para todos os tipo de ativo (N3\_TIPO), porem deve ser avaliado com muito critério, para que "metade" de um bem (0,5) por exemplo, comece a gerar depreciação antes do bem estar propriamente pronto para o uso.

**Importante!**

Se falta algum componente para um bem, importante que a classificação (ATFA240) seja feita com o tipo de ativo= adiantamento (tipo 3) e após a aquisição de todos os componentes, executar a baixa de adiantamento e a inclusão do bem completo. Dessa forma os componentes do bem não serão depreciados antes do bem ter sido finalizado.

Rotina ATFA251- Baixa de adiantamento e desmembra ativo.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006767052-MP-SIGAATF-ATFA251-Agregar-Aglutinar-Desmembrar-bens-do-ativo>
