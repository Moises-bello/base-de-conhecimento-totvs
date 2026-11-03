---
article_id: 360024262952
category: Materiais - Gestão de Compras Públicas - (SIGAGCP)
content_hash: a0ddb889b758e692d2e3d3eb391be116ddca691f8e645e24a437c1a2bf1587db
fetched_at: '2026-06-28T22:37:18.364290+00:00'
product: protheus
section_id: 1500001550562
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCP - Como não obrigar que
  o Órgão Gerenciador seja participante da ata de registro de preço ?
type: support-article
updated_at: '2022-07-28T11:20:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024262952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCP-Como-n%C3%A3o-obrigar-que-o-%C3%93rg%C3%A3o-Gerenciador-seja-participante-da-ata-de-registro-de-pre%C3%A7o
---

**Ocorrência**Como não obrigar que o Órgão Gerenciador seja participante da ata de registro de preço ?

**Ambiente**Microsiga Protheus  – Gestão de Compras Públicas– A partir da versão 12.17  
  
**Causa**O Sistema está obrigando a inclusão do Órgão gerenciador como participante da Ata de Registro de Preço. Porém existem casos que o mesmo será apenas o gerenciador e não participará da Ata.  
  
**Solução**Conforme Decreto: 7892/2013 - O órgão gerenciador realizará todos os atos de controle e administração do SRP, não sendo obrigatória sua presença como Aderente a Ata de Registro de Preços.

De acordo com o Decreto nº 7.892/2013 temos:  
Art. 2º Para os efeitos deste Decreto, são adotadas as seguintes definições:  
I - Sistema de Registro de Preços - conjunto de procedimentos para registro formal de preços relativos à prestação de serviços e aquisição de bens, para contratações futuras;  
II - ata de registro de preços - documento vinculativo, obrigacional, com característica de compromisso para futura contratação, em que se registram os preços, fornecedores, órgãos participantes e condições a serem praticadas, conforme as disposições contidas no instrumento convocatório e propostas apresentadas;  
III - órgão gerenciador - órgão ou entidade da administração pública federal responsável pela condução do conjunto de procedimentos para registro de preços e gerenciamento da ata de registro de preços dele decorrente;  
IV - órgão participante - órgão ou entidade da administração pública que participa dos procedimentos iniciais do Sistema de Registro de Preços e integra a ata de registro de preços;  
V - órgão não participante - órgão ou entidade da administração pública que, não tendo participado dos procedimentos iniciais da licitação, atendidos os requisitos desta norma, faz adesão à ata de registro de preços.

Decreto nº 7.892/2013, as competências do órgão gerenciador são:  
DAS COMPETÊNCIAS DO ÓRGÃO GERENCIADOR  
Art. 5º Caberá ao órgão gerenciador a prática de todos os atos de controle e administração do Sistema de Registro de Preços, e ainda o seguinte:  
I – registrar sua intenção de registro de preços no Portal de Compras do Governo federal;  
[...]  
VII - gerenciar a ata de registro de preços;  
VIII - conduzir eventuais renegociações dos preços registrados;  
[...]  
§ 1º A ata de registro de preços, disponibilizada no Portal de Compras do Governo federal, poderá ser assinada por certificação digital.  
§ 2º O órgão gerenciador poderá solicitar auxílio técnico aos órgãos participantes para execução das atividades previstas nos incisos III, IV e VI do caput.

Cenário Atual: Ao incluir um Edital o sistema me obriga a inserir o Órgão Gerenciador para todos os itens da Licitação, ao inserir o órgão gerenciador ele solicita que uma quantidade seja inclusa para o mesmo no qual está incorreto conforme mencionado no Decreto: “Gerenciar sem consumir”.

Causa: Com a quantidade obrigatório no Gerenciador a quantidade licitada sempre será a mais que a necessidade do solicitante, ao gerar Ata Registro Preço para realizar a manutenção preciso inserir a diferença no qual se transformara em Pedido de Compra ou Contrato sem necessidade.

Importante: Inserir um Edital para um órgão gerenciador apenas controlar a aquisição de produtos e de importância visto que a Lei e o Decreto menciona que um processo de licitação do Tipo Concorrência ou Pregão deve comandar o tramite.

A Rotina de Inclusão de Ata de Registro de Preço manualmente não atende essa demanda, visto que o Órgão gerenciador deve estar no Parâmetro MV\_GCPORG, a partir disso ele não pode gerenciar uma Ata e automaticamente o sistema o coloca como Carona.

Analise Consultoria Segmentos disponível no link:  
[http://tdn.totvs.com/pages/releaseview.action?pageId=273311520](http://tdn.totvs.com/pages/releaseview.action?pageId=273311520 "Follow link")

Embasamento:  Decreto Federal nº 7.892/2013; Lei 8666/93

***Saiba Mais:***

[Gestão de Contratos Públicos](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=341222185)

[Mais Artigos Materiais - Gestão de Compras Publicas (SIGAGCP)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550562)
