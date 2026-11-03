---
content_hash: 1e53325a91f6f4d8d4d08a49c1d3e9dcfb90aa1877a84741bed4bf26e03bad85
fetched_at: '2026-06-29T00:08:59.616116+00:00'
page_id: '364908488'
product: rm
source: tdn-rm
title: S-2230 - Afastamento Temporário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908488
version: 50
---

Este evento é utilizado para informar os afastamentos temporários dos empregados/servidores e trabalhadores avulsos, por quaisquer dos motivos elencados na tabela 18 – Motivos de Afastamento, bem como  eventuais alterações e prorrogações.

**Observações:**

* Caso o empregado/servidor possua mais de um vínculo, é necessário o envio do evento para cada um deles;
* Inclui-se nesse evento os períodos de afastamento cujo motivo seja o gozo de férias;
* Caso a coligada seja integrada com o Totvs Segurança e Medicina do Trabalho(SMT), e seja lançado atestado que gere afastamento, será criado um gatilho S-2230 na fila de eventos para esse funcionário;
* Afastamentos em que seu final seja menor ou igual à data atual acrescidos de 15 dias, será gerado na fila de eventos um gatilho do tipo inclusão para o evento S-2230 contendo a data de início e a data final;
* Afastamentos em que seu final seja maior do que a data atual acrescida de 15 dias, será gerado na fila de eventos dois gatilhos para o evento S-2230, sendo: um gatilho de início com data início e outro gatilho de término com data fim;
* Apenas poderá integrar com o TAF a inclusão de um novo afastamento caso o afastamento integrado anteriormente possua final, ou seja, deve ser respeitada a lógica de inclusão e encerramento para que não exista interseções entre afastamentos;
* Caso tenha que enviar algum afastamento temporário e não exista gatilho gerado na fila de eventos, deverá executar o processo ["Gerar gatilhos de Afastamento/Férias"](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.GerarGatilhosAfastamentoFerias.aspx) para gerar as informações desse evento.

### FAQ's disponíveis sobre esse assunto:

### Veja mapeamento dos campos que serão informados:

### Veja o Fluxograma do processo de Afastamento:

#### Exemplo de geração/envio do evento S-2230 - Afastamento Temporário:

61º Passo1º Passo1º Passo1º Passo

#### 1º Passo: Incluir um afastamento.

* Sempre que o usuário cadastrar um afastamento para um funcionário ou incluir um histórico de afastamento será gerado  um gatilho na fila de eventos para o evento S-2230 com status 0-pendente.
* Esse gatilho será visualizado através do menu  eSocial | Eventos de Tabela / Não Periódicos | Fila de eventos .

Existem três tipos de operação que influenciam nas informações a serem enviadas nesse evento: Inclusão, Início e término.

**Inclusão:** Envia o início e fim do afastamento;

**Início:** Envia apenas o início do afastamento;

**Término:** Envia apenas o fim do afastamento.

* Para afastamentos com data fim <= data atual +15 dias, será gerado na fila de eventos 1(um) gatilho para o evento S-2230 de inclusão, ou seja, contendo data inicio e data fim.

* Para afastamentos com data fim >=15 dias, serão gerados na fila de eventos 2(dois) gatilhos para o S-2230, sendo: 1 do tipo "Início" com data início e outro do tipo "Término" com data final do afastamento.

2º Passo2º Passo2º Passo

#### 2º Passo: Gerar o XML:

Na fila de eventos o usuário deverá gerar o XML para alterar o status do evento de 0-Pendente para 1-Gerado.

3º Passo3º Passo3º Passo

#### 3º Passo: Integrar Evento com o TAF:

Para isso deverá selecionar o evento e clicar Integrar TAF.

Neste momento o status do evento será alterado para 3-Enviado  para o TAF.:

4º Passo4º Passo4º Passo

#### 4º Passo: Enviar os eventos gerados na fila para o TOTVS Automação Fiscal (TAF)

* Acesse o produto Totvs Automação Fiscal (TAF)  e realize  o processamento para envio das informações do Totvs Folha de pagamento para o TAF.  
  + O usuário deve acessar o menu **"Integração"**e clicar em**"Processamentos":**
  + Ao clicar em **"Processamentos"**é apresentada a tela abaixo, onde o usuário deve marcar apenas o checkbox **"Transferir registros da TAFST2 para o TAF"**e clicar em**"Confirmar":**
  + Após executar todo o processo, o usuário pode optar por visualizar o evento importado através do **"Gerenciador de Integração":**
  + O  **"Gerenciador de Integração"** também pode ser acessado através do caminho abaixo:
  + No  **"Gerenciador de Integração"** é possivel acompanhar o status de todos os eventos que foram integrados ao TAF, o usuário consegue localizar os eventos através do registro do identificador **"Ticket TAF"**:  
      
      
      
    Maiores detalhes veja: [Integração Folha de Pagamento X TAF .](http://tdn.totvs.com/pages/releaseview.action?pageId=334334258)

5º Passo5º Passo5º Passo

#### 5º Passo: Atualizar status da integração com TAF :

 Para atualizar o status da integração do TAF terá as seguintes opções:

* Na fila de eventos selecionar   " Processos" | Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

Informações ImportantesInformações ImportantesInformações Importantes

**Informações Importantes:**

* Parâmetros utilizados na geração do evento de afastamento temporário :

**"****Desconsiderar o campo "Observação" do histórico de afastamento p/ o evento S-2230 exceto para afastamento tipo L-Licença s/Venc. "**  
**"Quantidade de dias anterior ao período de gozo de férias para envio do S-2230 (Máx. 60 dias)" .**  
**"Considerar o CID apenas para os motivos de afastamento obrigatórios ("T - Af. Ac. Trabalho" ou "O - Doença Ocupacional") na geração do XML do evento S-2230"**

Para mais detalhes acesse:[Configurações | Parametrizador | eSocial | Configurações Gerais 3/6](http://wikihelp.totvs.com.br/WikiHelp/FOP/Fop.ConfiguracoesGerais3.aspx)**.**

* Processo**"Gerar Gatilhos Afastamento / Férias":**

Esse processo permite gerar gatilhos de afastamentos para férias/afastamentos já cadastrados e que não existem na fila de eventos.

Para mais detalhes acesse: [Gerar Gatilhos Afastamento / Férias](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.GerarGatilhosAfastamentoFerias.aspx)

####
