---
article_id: 360028310031
category: Financeiro - Contas a Receber
content_hash: 80b8628760615a718bc54561fc01c2368f23b405644e791ae1c2dc6749f605a8
fetched_at: '2026-06-28T22:38:15.105399+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - MATA040 - Cadastrar mais de 5 vendedores
type: support-article
updated_at: '2021-04-28T15:17:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028310031-MP-SIGAFIN-MATA040-Cadastrar-mais-de-5-vendedores
---

**Dúvida**Como deve ser cadastrador mais de 5 vendedores?  
   
 **Ambiente**

Protheus – Financeiro – A partir da versão 11.80]  
  
**Solução**

Criar campos de usuário no Configurador e configurar como Marcado e visível para todos os módulos.

Recomendamos basear-se nos campos do padrão como referência.

C5\_VEND\* (exp. C5\_VEND**6**)

C5\_COMIS\*

E1\_VEND\*

E1\_COMIS\*

E1\_BASCOM\*

E1\_VALCOM\*

F2\_VEND\*

D2\_COMIS\*

C6\_COMIS\*

Obs: Apartir do 9° vendedor deve ser utilizado letras ( exemplo: E1\_VENDA, E1\_VENDB, E1\_VENDC e seus respectivos campos nas demais tabelas.
