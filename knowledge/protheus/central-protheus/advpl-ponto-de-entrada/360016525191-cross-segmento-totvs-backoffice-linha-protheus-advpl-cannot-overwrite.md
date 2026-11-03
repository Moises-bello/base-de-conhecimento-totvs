---
article_id: 360016525191
category: ADVPL - Ponto de Entrada
content_hash: 9439649583912608dbde7f9e75107c4624be9823b9f7ca7a7f5540078b20eb1e
fetched_at: '2026-06-28T22:40:11.672389+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Cannot Overwrite '
type: support-article
updated_at: '2021-05-21T16:51:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016525191-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cannot-Overwrite
---

**Dúvida**  
Como resolver o erro *Cannot Overwrite TOTVS programs*  apresentado no momento da compilação de um fonte?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.3  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

1. É necessário excluir o **rdmake**compilado no **RPO**e compilá-lo novamente para contornar o problema.
2. Localize o **rdmake**no projeto, clique com o botão direito do mouse e selecione a opção 'Excluir fonte(s) do **RPO**
3. Compile novamente o **rdmake**

**Obs.:**  Essa recomendação serve para todos os fontes, como pontos de entrada e relatórios como NFESEFAZ podem exibir a mesma mensagem *" Cannot overwrite TOTVS programs "* é só descompilar e compilar o seu fonte XXX.PRW

**Saiba mais**

**[Totvs Developer Studio - Compilar e descompilar (Excluir) fontes do RPO.](http://tdn.totvs.com/pages/releaseview.action?pageId=274332945)**
