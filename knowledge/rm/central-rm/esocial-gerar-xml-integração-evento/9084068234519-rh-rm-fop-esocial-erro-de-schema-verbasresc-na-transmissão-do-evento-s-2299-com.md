---
article_id: 9084068234519
category: eSocial - Gerar XML/ Integração Evento
content_hash: de3031a6361f6b6acd47d6dda972a90324283dcde5fecf8b7647d88d2953dec2
fetched_at: '2026-06-28T22:47:12.932330+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro de Schema verbasResc na transmissão do evento
  S-2299 com o  Governo
type: support-article
updated_at: '2026-06-15T13:08:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9084068234519-RH-RM-FOP-eSocial-Erro-de-Schema-verbasResc-na-transmiss%C3%A3o-do-evento-S-2299-com-o-Governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21647224445975)Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao transmitir S-2299 ao Governo  é apresentada a mensagem **Erro de schema: Element '{**[**http://www.esocial.gov.br/schema/evt/evtDeslig/v\_S\_01\_00\_00}verbasResc':**](http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_00_00%7DverbasResc':)**Missing child element(s). Expected is ( {**[**http://www.esocial.gov.br/schema/evt/evtDeslig/v\_S\_01\_00\_00}dmDev**](http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_00_00%7DdmDev)**).**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9084066546455)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O incidente ocorre quando há obrigatoriedade no envio das verbas rescisórias, mas não foram consideradas no XML do evento S-2299 - Desligamento.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9091954086039)

**Solução**  
Para correção da ocorrência favor realizar as validações abaixo:  
  
**•** Falta de **distribuição do SEFIP**  
Para empresas que utilizam tomadores de serviço, o sistema irá buscar as verbas para montagem do XML na distribuição do SEFIP realizada. Caso exista rateio das verbas será apresentando o erro supracitado. Desta forma, verifique em **Encargos | FGTS| Distribuir Tomador** a distribuição realizada para o mês/ano correspondente ao período de apuração. Em seguida, acesse **eSocial | Fila de Eventos** selecione o S-2299 e gere o XML novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36808491082519)

**•** Falta de **preenchimento do CEI** para funcionários alocados em obra.

Para empresas que utilizam tomador de serviço e vincula o CEI no histórico de tomador do funcionário, no momento de distribuir o tomador, o mesmo precisa estar preenchido para que os eventos sejam gerados no XML S-2299.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30060619308567)**

**• Data de Obrigatoriedade** incorreta  
1. Acesse em **Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais 1/7** e confira as datas de obrigatoriedade dos eventos periódicos conforme cronograma eSocial.

Abaixo segue resumo do [Cronograma eSocial:](https://www.gov.br/esocial/pt-br/noticias/adiado-o-inicio-da-fase-de-envio-de-folhas-de-pagamento-para-orgaos-publicos-e-organizacoes-internacionais)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9092601339287)

2. Em seguida, acesse **eSocial | Fila de Eventos** selecione o S-2299 e gere o XML novamente.

**•** Falta ou preenchimento incorreto do **Tipo de regimento trabalhista**no **Registro**do funcionário

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21647224461463)

• **Situação do Funcionário** não constar como D - Demitido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23950446250647)

• **Rescisão não calculada**  
Para identificar se a rescisão foi calculada, a consulta abaixo no banco de dados do RM deverá retornar com o preenchimento 1:  
SELECT RESCISAOCALCULADA FROM PFUNC WHERE CHAPA='INSIRA AQUI A CHAPA DO FUNCIONÁRIO'

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21647211489431)

Coluna - rescisaocalculada | **1 = Calculada   0 = Não calculada**

**Saiba mais**  
Para mais informações acesse:

* [RH - RM - FOP- eSocial - Retificação do evento de rescisão/desligamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017501692-RH-RM-FOP-eSocial-Retifica%C3%A7%C3%A3o-do-evento-de-rescis%C3%A3o-desligamento?source=search)
* [Distribuição de SEFIP de meses anteriores para tomadores de serviços em retificação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028703594)
* [Histórico de rateio por tomador de serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026677233-RH-RM-FOP-eSocial-Hist%C3%B3rico-de-rateio-por-tomador-de-servi%C3%A7os?source=search)
