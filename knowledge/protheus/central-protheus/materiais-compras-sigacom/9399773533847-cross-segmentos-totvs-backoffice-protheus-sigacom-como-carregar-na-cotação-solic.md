---
article_id: 9399773533847
category: Materiais - Compras (SIGACOM)
content_hash: 61475b58f8029b34627e433083d7ea0a5033019f6836d33bb34490b1272aa6ee
fetched_at: '2026-06-28T22:41:14.498941+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Carregar na Cotação
  Solicitação de Compras de todas as Filiais?
type: support-article
updated_at: '2022-10-07T14:18:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9399773533847-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Carregar-na-Cota%C3%A7%C3%A3o-Solicita%C3%A7%C3%A3o-de-Compras-de-todas-as-Filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**  
Como Carregar na Cotação Solicitação de Compras de todas as Filiais?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de Contratos - Todas as versões  
  
**Solução**

* Para que as solicitações de compra de todas as filiais, sejam carregadas em tela é necessário que os perguntas*Filtrar por data*e*Filtra Sc Gerada*, estejam configuradas igual a não. 

  Caso opte por filtrar por data e/ou Filtra SC já gerada igual sim, serão apresentadas somente as solicitações da filial logada. Este procedimento é necessário, devido a rotina Gerar Cotação (**MATA131**) trabalhar com filiais de entrega, onde as mesmas podem ser diferentes da filial de inclusão da solicitação.
* Documentação técnica referente ao conceito da rotina Gerar Cotações (MATA131) e conceito do parâmetro**MV\_COTFILT.**

**Pontos de entrada:**

Gerar cotação:

[MP - SIGACOM - Pontos de Entrada disponíveis na rotina Gera Cotação - MATA131](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001417762-MP-SIGACOM-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Gera-Cota%C3%A7%C3%A3o-MATA131)

Atualizar cotação:

[Cross Segmento - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada na rotina de Atualiza Cotações ( MATA150 )](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028037612-Cross-Segmento-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-na-rotina-de-Atualiza-Cota%C3%A7%C3%B5es-MATA150-)

Analise de cotação:

[MP - SIGACOM - Pontos de Entrada para Análise de Cotação (MATA161)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026227233-MP-SIGACOM-Pontos-de-Entrada-para-An%C3%A1lise-de-Cota%C3%A7%C3%A3o-MATA161-)

**Saiba mais.**

[DT Parametrização rotina Gerar Cotações](https://tdn.totvs.com/pages/releaseview.action?pageId=687149766)

[PCOM19004 - Carregar Solicitação de Compras de todas as Filiais](https://tdn.totvs.com/pages/viewpage.action?pageId=686485271)

[PCOM19005 - Parâmetro MV\_COTFILT - Habilitar tela de filtro](https://tdn.totvs.com/pages/viewpage.action?pageId=687148823)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
