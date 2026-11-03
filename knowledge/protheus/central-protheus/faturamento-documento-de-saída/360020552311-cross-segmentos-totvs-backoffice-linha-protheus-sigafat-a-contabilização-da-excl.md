---
article_id: 360020552311
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 84e2f40c2b43cf3a38a013de708e97cbe9adb93371e59827d81c7a8ab0846eed
fetched_at: '2026-06-28T22:38:45.109411+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos- TOTVS Backoffice (Linha Protheus)- SIGAFAT- A contabilização
  da exclusão da nota não é efetuada em modo off-line.
type: support-article
updated_at: '2022-05-16T16:56:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020552311-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-A-contabiliza%C3%A7%C3%A3o-da-exclus%C3%A3o-da-nota-n%C3%A3o-%C3%A9-efetuada-em-modo-off-line
---

**Dúvida**

Como contabilizar a exclusão da nota em modo off-line?

**Ambiente**

Cross Segmentos- TOTVS Backoffice (Linha Protheus)- SIGAFAT - todas as versões.

**Solução**

**A exclusão do documento de saída não se contabiliza off line**, pois uma vez que são excluídos os dados das Tabelas SF2 e SD2, esta informação não é mais considerada, para ser posteriormente contabilizada.

Então, para que ocorra a contabilização, é necessário que seja realizada no próprio momento da exclusão.

No browse da rotina **MATA521A** - Exclusão do Documento de Saída, clicando '**F12**', há perguntas se deseja contabilizar e mostrar o LP, selecionar ambas como sim.

Quando demonstrar o Lançamento Contábil, certificar-se de o documento estar compatível com a regra do LP.

Caso a contabilização do documento de saída seja offline e ainda não tenha sido contabilizada, não será feita a contabilização da exclusão do documento de saída.

Obs: Inclusive, no Help de campo da pergunta "Contabiliza?" é informado: Indica se os lançamentos contábeis devem ser gerados durante a exclusão do documento de saída. Não será possível gerá- lo pela contabilização Off-Line (**CTBANFS**).

**SAIBA MAIS**: **[FAT0124\_LP\_Lançamento\_Padrão\_para\_contabilizar\_o\_Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=244940386)**
