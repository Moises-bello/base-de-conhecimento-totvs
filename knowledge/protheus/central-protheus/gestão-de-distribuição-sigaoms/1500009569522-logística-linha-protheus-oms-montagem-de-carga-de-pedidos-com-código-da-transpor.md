---
article_id: 1500009569522
category: Gestão de Distribuição (SIGAOMS)
content_hash: 75b5747e4bf19a61e05c13bcccef3b37980dcc8d5f917cea7499ca40f8a32c67
fetched_at: '2026-06-28T22:45:49.923635+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Montagem de carga de pedidos com código
  da transportadora para redespacho informado
type: support-article
updated_at: '2022-02-14T17:17:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009569522-Log%C3%ADstica-Linha-Protheus-OMS-Montagem-de-carga-de-pedidos-com-c%C3%B3digo-da-transportadora-para-redespacho-informado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:06 min**  
**Dúvida**O que muda na **Montagem de Carga - OMSA200**, quando o **pedido de venda** estiver com o **Código da transportadora para Redespacho** informado?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - A partir da versão 12  
  
**Solução**Ao efetuar a **Montagem da Carga**, com pedido de venda, onde foi informado o **Código da transportadora para Redespacho**, no bloco de Pedidos da rotina, as informações de **Estado**, **Município**, **Bairro**, **CEP - Código de Endereçamento Postal** e **Endereço** serão determinadas conforme a seguinte regra:  
  
**Endereço da Transportadora:** quando informado no campo **Redespacho - C5\_REDESP** do Pedido, esta transportadora, será exibida neste mesmo bloco no campo **Redespachante - DAI\_REDESP**.  
   
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse **Atualizações/Pedidos/Pedidos de Venda - MATA410,** efetue a inclusão de um pedido de venda, informando no campo **Carga -** **C5\_TPCARGA** o valor **1 - Utiliza** e no campo **Redespacho - C5\_REDESP** informe o **Código da transportadora para Redespacho, cadastro MATA050 - Transportadoras.** O pedido deverá ser liberado;  
  
2. Acesse **Atualizações/Cargas/Montagem de Carga - OMSA200**, verifique a parametrização do grupo de perguntas para que os pedidos de venda sejam apresentados de acordo com range desejado. Na tela de montagem de carga, com os pedidos listados, no **bloco de Pedidos**, serão apresentado as informações da **transportadora de Redespacho.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014665262/mceclip0.png)**

Ao ao preencher o campo **Redespacho - C5\_REDESP** no **Pedidos de Venda - MATA410,** no processo de **Montagem de Carga - OMSA200,** a rotina passa a considerar essa **Transportadora como local de entrega.** Trata-se de uma particularidade desse processo, onde  a **busca das Rotas** passa a ser feito com base no **cadastro** **MATA050 - Transportadoras  - tabela SA4,** usando o campo de **CEP - A4\_CEP.**Para que a **Montagem de Carga - OMSA200 seja feito com a seleção de uma rota é preciso que o cadastro de Pontos Por Zona e Setor - OMSA090 seja feito por CEP e não por Clientes.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4424839825175/mceclip0.png)**

**Caso o cadastro de Pontos Por Zona e Setor - OMSA090 seja feito por Clientes,** o Sistema não encontrará a referência de rotas, zonas ou setor e nos blocos Rotas, Zonas e Setor será apresentada uma caixa de verificação com a descrição **igual a 999999 - Pedidos sem roteirização**.

**Importante**Para que o Sistema apresente o **código e nome** **da transportadora para Redespacho** na montagem da carga, será necessário atualizar o **Pacote acumulado de Atualizações do TOTVS OMS** e aplicar o **Dicionário de dados**, conforme *link*: [Pacote Acumulado do TOTVS OMS](https://tdn.totvs.com/pages/releaseview.action?pageId=556880961)  
  
**Saiba mais**Mais informações sobre a rotina de **Montagem de Carga - OMSA200**, poderão ser acessadas no *link*: [Montagem de Carga - OMSA200](https://tdn.totvs.com/pages/viewpage.action?pageId=551446517)
