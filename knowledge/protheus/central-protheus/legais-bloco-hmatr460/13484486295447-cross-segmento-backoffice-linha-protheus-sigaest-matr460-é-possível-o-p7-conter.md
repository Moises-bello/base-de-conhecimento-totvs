---
article_id: 13484486295447
category: LEGAIS - BLOCO H/MATR460
content_hash: ac406885c92b982a424caf74a5ddac5c94f646ad496261a6108440388c0bfe0b
fetched_at: '2026-06-28T22:42:15.122286+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - É possível
  o P7 conter mais de 3 casas decimais no campo Quantidade?
type: support-article
updated_at: '2023-03-30T14:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13484486295447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-%C3%89-poss%C3%ADvel-o-P7-conter-mais-de-3-casas-decimais-no-campo-Quantidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:21 min** **Dúvida**É possível emitir o relatório P7 com mais de 3 casas decimais na Quantidade?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Para atender a legislação, o relatório Inventário Modelo 7 conterá no máximo 3 casas decimais no campo de Quantidade. Isso se deve pelo fato deste relatório ser o espelho do Bloco H do SPED Fiscal, onde, o mesmo define que o padrão do campo quantidade possui decimal de até 3.

Print extraído do Guia do EFD:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13484412768023)

Exemplo de um cenário onde o relatório P7 de um ambiente que tem mais de 3 casas decimais no campo Quantidade (mesmo assim o P7 só vai aparecer 3):

Kardex mostra as 4 casas decimais do ambiente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13484584272791)

P7 nunca passa das 3 casas da coluna "Quantidade"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13484625304727)

Este é um padrão do fonte do relatório P7 para atender o leiaute do Registro H010 do Bloco H do SPED.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)*
