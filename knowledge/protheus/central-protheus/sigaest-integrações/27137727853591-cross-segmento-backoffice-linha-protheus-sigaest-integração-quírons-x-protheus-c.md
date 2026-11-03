---
article_id: 27137727853591
category: SIGAEST - INTEGRAÇÕES
content_hash: 5dad91fcc6736928b4f6488fba8b6ea2737c0fb52835ff972ab5860bedd2356f
fetched_at: '2026-06-28T22:38:46.205940+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração Quírons
  x Protheus - Como funciona o Fluxo de integração de estoque
type: support-article
updated_at: '2025-03-12T12:26:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27137727853591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-Qu%C3%ADrons-x-Protheus-Como-funciona-o-Fluxo-de-integra%C3%A7%C3%A3o-de-estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27137679044375) Tempo aproximado para leitura: **000:03:20 min** **Dúvida**Como é o fluxo de integração de estoque entre Protheus x Quírons  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**A integração entre Protheus x Quírons, tem fluxos a serem seguidos, então primeiramente é importante entender como está configurado a integração no Quírons:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27137679045399)**

[Clique aqui](https://intercom.help/quirons/pt-BR/articles/6097239-configuracao-integracao-estoque) para maiores detalhes sobre a configuração no Quírons.

[Clique aqui](https://tdn.totvs.com/x/tKL0Jg) para maiores detalhes sobre a configuração no Protheus.

**IMPORTANTE:** O Quírons integra movimentações 399 e 599, sendo assim se utiliza Request, deve se atentar ao tipo de movimento selecionado.

1 – Request à Que irá enviar uma Solicitação ao Armazém (SCP) ao Protheus. Neste fluxo para que seja possível fazer a entrega do Epi no Quírons é necessário que no Protheus siga o [processo de pré-requisição e baixa da requisição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Solicita%C3%A7%C3%A3o-Pr%C3%A9-Requisi%C3%A7%C3%A3o-e-Baixa-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-MATA105-MATA106-MATA185).

Dentro desse fluxo, ao gerar a solicitação ao armazém e realizar a baixa, o Protheus vai realizar a atualização de estoque no Quírons por meio do adapter MATA105 - Request:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27138249500695)

**IMPORTANTE:** Fazer uma baixa do Protheus sem que tenha uma SA (Solicitação ao Armazém) associada não irá integrar com o Quírons.

2 – Movement à que irá enviar uma Baixa de Estoque ( SD3). Neste caso após a conclusão da integração poderá ser entregue o EPI no Quírons.

Dentro desse Fluxo, o adapter responsável por atualizar o estoque é o MATI225 - StockLevel.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27138249504535)

Porém para que essa atualização ocorra, existem algumas validações que o sistema realiza para enviar a atualização, sendo elas:

- Ter o JOB SCHEDESTMG ([Clique aqui para mais detalhes](https://tdn.totvs.com/x/2WQcEQ)) configurado no Schedule, esse serviço que vai rodar a atualização do estoque (Adapter MATI225 StockLevel);

- Ao realizar uma movimentação de estoque que atualize a SB2, o sistema atualiza o campo B2\_DMOV e o SCHEDESTMG compara com os campos B2\_DULT e B2\_HULT, dessa maneira o SCHEDESTMG vai entender que esse saldo precisa ser atualizado no Quírons.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27148438976535)

- Mesmo que tenha o Adapter MATA241 ou MATA105 configurado, a atualização de estoque não será realizada por eles.

**Observação:** Nesse cenário o Adapter MATA241 StockTurnover deve estar configurado apenas para receber e não enviar, Pois o Quírons que vai realizar a baixa do EPI e atualizar por esse adapter o saldo em estoque.

**IMPORTANTE:** No processo acima não corre a atualização de saldo automaticamente no Quírons após realizar a baixa de estoque. O saldo somente será atualizado ao executar o job SCHEDESTMG.

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
