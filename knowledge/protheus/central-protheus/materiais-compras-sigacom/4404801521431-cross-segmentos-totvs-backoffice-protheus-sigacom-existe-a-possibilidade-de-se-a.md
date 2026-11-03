---
article_id: 4404801521431
category: Materiais - Compras (SIGACOM)
content_hash: 8bbdf567771b443eb985bbb4a49dde3f3103b771a651b2611fd550b110bdbc7d
fetched_at: '2026-06-28T22:41:18.625799+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Existe a possibilidade
  de se alterar o campo E2_TIPO do Título Financeiro gerado por um Documento de Entrada
  ?
type: support-article
updated_at: '2022-11-25T14:46:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404801521431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Existe-a-possibilidade-de-se-alterar-o-campo-E2-TIPO-do-T%C3%ADtulo-Financeiro-gerado-por-um-Documento-de-Entrada
---

**Dúvida**Existe a possibilidade de se alterar o campo E2\_TIPO do Título Financeiro gerado por um Documento de Entrada, que sempre gera com Tipo NF ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**

No padrão do módulo de Compras, o tipo do título principal E2\_TIPO do Titulo gerado por Documento de entrada conforme a origem do lançamento sempre é gerado como "NF", independente da espécie utilizada do documento.   
Não há um parâmetro ou ponto de entrada específico que possibilite alterar essa informação do campo E2\_TIPO.  
Também não instruímos esse tipo de alteração visto que o campo E2\_TIPO faz parte da chave única da tabela SE2 e pode-se gerar inconsistências futuras em seu ambiente.

***Saiba Mais :***

[MP - SIGACOM - Pontos de entrada do Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332-MP-SIGACOM-Pontos-de-entrada-do-Documento-de-Entrada-MATA103?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
