---
article_id: 4420114336663
category: RH - Cadastros
content_hash: 51fd55c8042694e4df92f3814a73ba61d76cbe00652a649d2a9d38443724e75f
fetched_at: '2026-06-28T22:44:52.905244+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como incluir Afastamentos e Férias quando utiliza
  somente o módulo de Ponto Eletrônico
type: support-article
updated_at: '2026-02-11T13:59:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420114336663-RH-Linha-Protheus-PON-Como-incluir-Afastamentos-e-F%C3%A9rias-quando-utiliza-somente-o-m%C3%B3dulo-de-Ponto-Eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36225388957975) Tempo aproximado para leitura: 02:00:00 min**  
  
**Dúvida**  
Como incluir Afastamentos e Férias quando utiliza somente o módulo de Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para cadastrar um Afastamento Médico ou Férias no módulo de **Ponto Eletrônico**, é necessário incluir um Período de Folha que corresponda às datas das ausências, e deixar o roteiro FOL como ativo.  
Mesmo quando o cliente não possui o módulo **07 - Gestão de Pessoal**, é possível incluir a rotina no menu do **SIGAPON** via modulo Configurador, conforme o passo a passo abaixo:  
  
**1 -** No modulo **Configurador,** acesse o caminho: **Ambiente > Cadastros > Menu** - selecione apenas o módulo de **Ponto Eletrônico** e clicar em **OK**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420127167511)  
  
  
**2 -** Posicione sobre a opção **SIGAPON** e **Adicionar,** para mover todos os menus do módulo para direita:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420127186455)  
  
  
**3 -** É possível incluir a rotina de Períodos em qualquer menu do módulo. Neste caso, vamos incluir na opção **Cadastro de Funcionários**, portanto posicione nesta opção e clicar em **Novo Item**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420127205527)  
  
  
**4 -** A **descrição** é o nome da rotina que aparecerá no menu, neste caso, deixamos como Períodos.  
O **programa** é o fonte da rotina, nesse caso é o **GPEA400**.  
Em **Módulo**, deve ser selecionada a opção **Gestão de Pessoal**, e por fim, em **Tipo**, deve ser selecionada a opção **Função Protheus,** e clicar **OK**:![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420121856279)  
  
  
**5 -** Para confirmar a inclusão do novo menu, clicar em **Gerar** e informe **SIGAPON,** posteriormente clicar em **Gerar** novamente e confirme a inclusão:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420121883799)  
  
  
**6 -** Acessando o **SIGAPON**, o novo menu poderá ser visualizado no caminho escolhido realizado no modulo configurador, exemplo:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420127345815)  
  
  
7 - Neste exemplo, vamos cadastrar uma Férias em Janeiro/2025, portanto, é necessária a criação do **período de Janeiro**, incluir o **roteiro FOL** e deixar ele **ativo**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31230415396119)  
  
  
**8 -** Na rotina de **Afastamentos**, informe o **código da ausência** e **data início/fim** do afastamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31230418960535)  
  
  
9 - Acessando a rotina de **Integrados**, por exemplo, o **calendário** do funcionário será montado **validando** **o afastamento**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31230415408663)

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
