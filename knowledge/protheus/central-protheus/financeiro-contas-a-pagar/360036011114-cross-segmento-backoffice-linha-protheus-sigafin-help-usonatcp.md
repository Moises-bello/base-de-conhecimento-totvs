---
article_id: 360036011114
category: Financeiro - Contas a Pagar
content_hash: b12ccf34b9e83935c73f439d4cd7fe61fdbdec07130e2f6bfb3cff2cb4e2ea49
fetched_at: '2026-06-28T22:38:07.002399+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Help USONATCP
type: support-article
updated_at: '2022-04-19T19:12:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036011114-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Help-USONATCP
---

**Ocorrência**  
No módulo Financeiro, ao tentar incluir um título a pagar com determinada natureza, é exibido o Help **USONATCP - A natureza não poderá ser usada nesta rotina!**.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**   
Esse incidente ocorre, pois no cadastro da natureza, o campo **Uso Natureza** não está configurado para contas pagar ou para uso livre.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Escolha outra natureza que esteja configurada com o campo **ED\_USO igual a 0- Livre ou 2- Contas** **pagar** ou altere a natureza em questão deixando este campo configurado com uma dessas duas opções.
