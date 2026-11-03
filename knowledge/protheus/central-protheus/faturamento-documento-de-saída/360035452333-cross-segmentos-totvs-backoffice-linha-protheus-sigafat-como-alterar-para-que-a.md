---
article_id: 360035452333
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 876a275c4c8db94f54a3e2ab880d54fa40f218a80fd8bf2dee616b8030820711
fetched_at: '2026-06-28T22:38:45.052915+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como alterar
  para que a data de saída da nota fiscal seja diferente da data de emissão
type: support-article
updated_at: '2023-02-14T11:39:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035452333-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-alterar-para-que-a-data-de-sa%C3%ADda-da-nota-fiscal-seja-diferente-da-data-de-emiss%C3%A3o
---

**Dúvida**

Como alterar para que a data de saída da nota fiscal seja diferente da data de emissão?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT – A partir da versão 11.80  
  
**Solução**

Por padrão o Danfe mostra a informação da data de saída igual à emissão, pois o XML busca a data do campo **F2\_EMISSAO**. Não há campo específico para Data de Saída pois a tag <**dSaiEnt**> não é obrigatória no XML. 

Existe um parâmetro onde você pode deixar a data de saída da mercadoria em branco.

**MV\_DSAIENT**  
Descrição: Define se a data de entrada e saída da NF-e não será gerada.  
.T. = Não será gerada  
.F. = Será gerada

De qualquer forma há como realizar essa adequação:   
É possível customizar o fonte **NFESEFAZ.PRW**para indicar o campo **C6\_ENTREG**(ou outro campo criado manualmente na **SC5**Cabeçalho do Pedido) para ser levado para a Tag <**dSaiEnt**> no XML e consequentemente no Danfe.

Outra possibilidade é customizar por Ponto de Entrada (ao invés de customizar direto no Fonte **NFESEFAZ**). Neste caso, utilizar o Ponto **PE01NFESEFAZ**(<http://tdn.totvs.com/pages/releaseview.action?pageId=6077191>)
