---
article_id: 18179237998871
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 00c0bf9bce207f1efc98b5102cda71e3e61a77425f590af4bbe332f8ab339c20
fetched_at: '2026-06-28T22:38:57.123924+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 -
  É possível incluir Pedido de Venda e Documento de Entrada com Valor Unitário zerado
  na Transferência entre Filiais?
type: support-article
updated_at: '2023-10-11T11:32:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18179237998871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-%C3%89-poss%C3%ADvel-incluir-Pedido-de-Venda-e-Documento-de-Entrada-com-Valor-Unit%C3%A1rio-zerado-na-Transfer%C3%AAncia-entre-Filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18179195579799) Tempo aproximado para leitura: **00:03:30 min** **Dúvida**

É possível incluir Pedido de Venda e Documento de Entrada com **Valor Unitário (D2\_PRCVEN e D1\_VUNIT)** zerado nas rotinas de Transferência entre Filiais (MATA310/MATA311) utilizando o campo da TES **F4\_VALZERO igual a "Sim"** não respeita o comportamento da TES.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18179556677527)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Para as rotinas ***MATA310 e MATA311 não tem essa funcionalidade***, no padrão a rotina considera somente o valor maior que zero nos campos de Valores Unitários, quando populado com zero considera o valor igual a R$ 1,00.

Para alterar esse comportamento somente é possível customizando com o [ponto de Entrada MTA310OK](https://tdn.totvs.com/pages/releaseview.action?pageId=6087903).

Veja também todos os Pontos de Entrada disponíveis na rotina no link abaixo:

[Pontos de entrada da rotina Transferência entre Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Pontos-de-entrada-da-rotina-Transfer%C3%AAncia-entre-Filiais)

***Importante:***

 - Esse cenário não se trata de um erro, devido as rotinas MATA310 e MATA311 serem consideradas facilitadoras do processo padrão, portanto não contemplam todas as funcionalidades do processo padrão.

 - Uma outra alternativa é efetuar o processo de transferência entre Filiais Manualmente com as configurações desejadas.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-)

[SIGAEST - MATA310/MATA311 - Transferência entre Filiais utilizando o parâmetro MV\_FILTRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF)

[SIGAEST - MATA310/MATA311 - Como estornar Solicitações de Transferência entre Filiais?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12728743784087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-estornar-Solicita%C3%A7%C3%B5es-de-Transfer%C3%AAncia-entre-Filiais-)

[SIGAEST - MATA310 MATA311 - Como configurar tabela de preços para as Transferências?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8552373360023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-tabela-de-pre%C3%A7os-para-as-Transfer%C3%AAncias-)

[SIGAEST - MATA310/MATA311 - Pontos de entrada da rotina Transferência entre Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Pontos-de-entrada-da-rotina-Transfer%C3%AAncia-entre-Filiais)

[SIGAEST - Help PV BLOQUEADO na rotina de Transferência entre Filiais (MATA310 e MATA311*)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024378631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-PV-BLOQUEADO-na-rotina-de-Transfer%C3%AAncia-entre-Filiais-MATA310-e-MATA311-)
