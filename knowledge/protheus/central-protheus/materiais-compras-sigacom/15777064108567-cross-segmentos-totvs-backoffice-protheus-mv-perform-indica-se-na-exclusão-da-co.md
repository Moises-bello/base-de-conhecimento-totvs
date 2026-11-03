---
article_id: 15777064108567
category: Materiais - Compras (SIGACOM)
content_hash: 8da666223957261da570d4af7cf3eef36b3bbae12676211e998d1f578482eff1
fetched_at: '2026-06-28T22:41:12.877833+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - MV_PERFORM - Indica se na exclusão
  da cotação será carregado ou não o Acols
type: support-article
updated_at: '2023-07-04T18:36:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15777064108567-Cross-Segmentos-Totvs-Backoffice-Protheus-MV-PERFORM-Indica-se-na-exclus%C3%A3o-da-cota%C3%A7%C3%A3o-ser%C3%A1-carregado-ou-n%C3%A3o-o-Acols
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15777047708311) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Ao Excluir Cotação o sistema Trava.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Versão 12

**Solução**

Recomendamos então que utilize o parâmetro MV\_PERFORM = .F.  para exclusão de cotações com grandes quantidades de registros.

O parâmetro **MV\_PERFORM**  Indica se na exclusão da cotação inteira ou por produto, será carregado o Acols, nesses tipos de exclusões não é apresentada a tela (grid).

Para melhorar a performance do sistema na exclusão da cotação, alterar o parâmetro MV\_PERFORM = .F. .

***Saiba Mais:***

[MV\_PERFORM - Indica se na exclusão da cotação será carregado ou não o Acols](https://tdn.totvs.com.br/pages/releaseview.action?pageId=354466007)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
