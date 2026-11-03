---
article_id: 38645681928343
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 6f4833d925e5ced0ada294bff80958dce7b8b4289fba323cc2da1bc50ce21bfa
fetched_at: '2026-06-28T22:41:48.487206+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - ATFA012 -
  Vinculo de Componentes incluidos manualmente ao bem princial
type: support-article
updated_at: '2026-02-26T11:51:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38645681928343-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Ativo-Fixo-ATFA012-Vinculo-de-Componentes-incluidos-manualmente-ao-bem-princial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38645681905303) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como realizar o vínculo de um componente (bem principal em construção) a um ativo de adiantamento (Tipo 03) quando a inclusão é realizada manualmente através da rotina Ativos (ATFA012)?  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - A partir da versão 12.1.33  
  
  
**Solução**  
Por padrão do sistema, o campo Bem em Cons. (N1\_SLBMCON) e o campo Item Bm Com (N1\_CDCONTR) não são habilitados para preenchimento manual durante a inclusão de um ativo através da rotina ATFA012.   
Essa funcionalidade de vinculação automática de componentes durante a entrada é nativa apenas para ativos originados de Documentos de Entrada (MATA103) e classificados via Classificação de Compras (ATFA240).

Para despesas ou ativos lançados manualmente que precisam ser incorporados a um bem principal em construção, a orientação oficial é realizar a inclusão do componente normalmente e, ao término da construção do bem, efetuar a unificação dos valores, através do processo de Aquisição por Transferência (ATFA251).

**Passos**

1. Acesse o módulo Ativo Fixo (SIGAATF);
2. Realize a inclusão do componente/despesa através da rotina Atualizações > Ativo Imobilizado > Ativos (ATFA012);

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38645681907223)
3. Preencha os dados do ativo normalmente, sem o vínculo imediato ao bem principal;

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38645681907607)
4. No momento em que o bem principal estiver concluído e pronto para receber os valores dos componentes, acesse Atualizações > Movimentos > Aquisição por Transferência (ATFA251);

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38645728449175)
5. Utilize a rotina de Aglutinação para vincular os componentes (adiantamentos/despesas) ao bem principal. Este processo consolidará os valores, permitindo a correta gestão do ativo finalizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38645681908759)

**Saiba Mais**  
[ATFA251 - Agrupar, Aglutinar ou Desmembrar bens do ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006767052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA251-Agrupar-Aglutinar-ou-Desmembrar-bens-do-ativo)  
[Criação de bem em construção(AI) para receber componentes](https://tdn.totvs.com/pages/releaseview.action?pageId=567740807)  
[Como cadastrar Bem em Construção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38509993611671-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Como-cadastrar-Bem-em-Constru%C3%A7%C3%A3o)
