---
article_id: 360040055333
category: Comércio Exterior - Easy Import Control - Licença de Import
content_hash: 5abf27419c04a45da77458b386f0ab67d1e42e1193569e656559f3a6b93d7926
fetched_at: '2026-06-28T22:39:42.699652+00:00'
product: protheus
section_id: 1500001549682
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Error: falied
  to load function U_EICGI333'
type: support-article
updated_at: '2021-10-06T20:34:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040055333-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Error-falied-to-load-function-U-EICGI333
---

**Dúvida**A rotina manutenção de PLI apresenta o erro - Falied to load function U\_EICGI333, como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Neste caso, o erro está sendo apresentado no fonte **EICGI333**. Por favor, remover o **EICGI333\_RDM.PRW** do repositório.  
As orientações para o procedimento estão em: [Totvs Developer Studio - Compilar e descompilar (Excluir) fontes do RPO.](http://tdn.totvs.com/pages/releaseview.action?pageId=274332945)  
Caso não tenha o RDMAKE, crie um fonte com o nome **EICGI333\_RDM.PRW** em seguida faça a remoção do **EICGI333\_RDM.PRW**, conforme documentação acima.
