---
content_hash: 77d8256811f2a132a9477dc4d9664f39ecf5393e608712405c640bbc3b5a68e3
fetched_at: '2026-06-29T00:08:59.660594+00:00'
page_id: '364909099'
product: rm
source: tdn-rm
title: Eventos Periódicos - Gerar, Monitorar e Enviar os Eventos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364909099
version: 19
---

### Para gerar os eventos periódicos o TOTVS Folha de pagamento disponibiliza os seguintes processos:

1. Período de apuração para a definição da competência da movimentação a ser enviada para o eSocial;
2. Gerar XML para criação dos arquivos dos eventos periódicos;
3. Eventos periódicos uma visão com todos eventos periódicos gerados que permite controlar e acompanhar o status de cada evento
4. Gestão da integração com o TAF

Os processos acima podem ser acionados no TOTVS Folha de Pagamento | eSocial |  Eventos Periódicos e TOTVS Folha de Pagamento | eSocial | Processos

Abaixo são explicados o passo a passo de cada processo

### 1) Período de Apuração

#### I - Criar o Período de apuração em Totvs Folha de Pagamento | eSocial | Período de Apuração. Na visão do Período de apuração clique em Incluir. E informe os dados para abertura do Período.

Para mais detalhes acesse em [Período de Apuração](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.PeriodoApuracao.aspx).

**Observação:** O período de apuração também poderá ser criado no momento da geração do XML.

### 2) Gerar XML

Neste módulo será gerada a estrutura de XML dos registros para a Fila de Eventos Periódicos para [Integrar com TAF](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.IntegrarTAF.aspx) (Sistema da TOTVS responsável pela validação e transmissão dos dados para o governo).

#### I - Para gerar os arquivos contendo o XML dos eventos periódicos acione o processo TOTVS Folha de Pagamento | eSocial | Eventos Periódicos | Gerar XML.

#### II - Será apresentada a tela do processo para gerar o XML dos eventos periódicos

#### 

#### III - Informe o filtro dos funcionários, Período de Apuração e os eventos periódicos a serem processados

#### Observação I:

O Parâmetro "Regerar XML" é usado gerar o XML considerando os eventos que consta já gravados na fila de eventos ou irá criar/recriar a fila de eventos conforme o filtro de funcionário informados.

Quando Marcado desabilita o filtro de funcionário e processa a fila de eventos já gravados. Estando desmarcado habilita o filtro de funcionários, cria ou recria a fila de eventos.

Para mais detalhe acesse [Gerar XML Periódicos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.GerarXMLPeriodicos.aspx).

Observação II:

Após gerar o XML resolva toda e qualquer inconsistência registra nos logs do processo

#### IV - Após informar os parâmetros acima selecione a coligada e execute o processo para gerar o XML.

### 3) Fila para Eventos Periódicos

Após executar o processo de Gerar o XML os eventos periódicos podem ser analisados e controlados na fila de eventos em TOTVS Folha de Pagamento | eSocial | Eventos Periódicos

Através da fila de eventos será possível monitorar os eventos como: seus status, tipos de Operações, além de erros de geração e informações da integração com TAF/TSS.  

Além de monitorar os eventos é disponibilizado os processos para: Gerar XML, Integrar com TAF, Atualizar Status Integração TAF e Gerar Evento de Exclusão (S-3000).

 

Para maiores detalhes acesse [Eventos Periódicos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosPeriódicoss.aspx).

### 4) Integrar com TAF

Após gerar o XML seja pelo processo do menu principal ou pela fila de evento e depois de resolvido quaisquer inconsistência informada no log

O TAF - TOTVS Automação Fiscal é a nova plataforma da TOTVS especializada na consolidação dos movimentos fiscais de forma +compacta para atender as obrigações acessórias impostas pelo Governo, e tem como objetivo suportar o processo tributário permeando as Obrigações Principais e Acessórias pelas Demonstrações, Apurações e Cálculos de Tributos.

Conheça mais em: <http://tdn.totvs.com/display/TAF/Manual+do+TAF>
