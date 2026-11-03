---
article_id: 4415795724951
category: Materiais - Compras (SIGACOM)
content_hash: 258c414f444615d7c5309df180bdbc558d93e7f64cdc84fe062516aeca8fe67d
fetched_at: '2026-06-28T22:41:13.105467+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Aglutina Contabilização
  e Histórico no Documento de Entrada
type: support-article
updated_at: '2022-05-16T22:35:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415795724951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Aglutina-Contabiliza%C3%A7%C3%A3o-e-Hist%C3%B3rico-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03 min** **Dúvida**

Ao aglutinar a Contabilização do Documento de Entrada, o histórico, esta buscando sempre o primeiro fornecedor.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12

**Solução**

Na contabilização do Documento de Entrada com histórico aglutinado, o sistema faz uma avaliação para saber qual é o histórico que ele vai utilizar.

Para essa avaliação, a rotina utiliza o parâmetro **MV\_AGLHIST,**caso esteja com o conteúdo em**.F.** aglutina os históricos utilizando o primeiro registro de histórico, se estiver como .**T**., a rotina considera o histórico na regra de busca,

**IMPORTANTE :**Em caso de contabilização com parâmetro **"Aglutina Histórico =  Sim"** não serão gravados campos customizados.

Ex: A rotina "Documento de Entrada (MATA103)" possui um parâmetro de usuário que determina se deseja ou não aglutinar os lançamentos na contabilização, neste caso campos de usuário não terá seus dados gravados.

***Obs:***

A geração de continuação de histórico dos lançamentos de integração dependera da aglutinação de lançamentos de acordo com a origem da contabilização, sendo assim, a continuação de histórico só será gerada caso o lançamento seja aglutinado em uma única linha, nos casos onde as entidades utilizadas são os mesmos nos lançamentos efetuados. O controle de aglutinação é realizado pela rotina de origem do lançamento contábil, algumas é possível ativar e desativar este controle por meio dos parâmetros (F12).

***Saiba Mais:***

* [MV\_CT5HIST - Histórico de lançamento padrão](https://tdn.totvs.com/x/-rooJ)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
