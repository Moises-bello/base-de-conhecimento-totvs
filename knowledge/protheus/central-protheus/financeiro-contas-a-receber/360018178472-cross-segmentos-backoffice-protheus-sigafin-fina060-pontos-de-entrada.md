---
article_id: 360018178472
category: Financeiro - Contas a Receber
content_hash: ce33898ab618edee15c2092cf2e589120a97193f8f417fadf7d2577fc70f1881
fetched_at: '2026-06-28T22:38:14.197228+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFIN - FINA060 - Pontos de Entrada
type: support-article
updated_at: '2024-07-31T17:36:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018178472-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-FINA060-Pontos-de-Entrada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24348564539927)***Tempo aproximado para leitura: **00:10:00 min  
  
Dúvida**Quais são os pontos de entrada da Rotina **FINA060**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**Para customização dos pontos de entrada na rotina **FINA060**existem as opções abaixo:  
  
**F060BROW -** Revalidação de dados  
O ponto de entrada **F060BROW** será executado antes da ***Mbrowse*** pré validando os dados a serem exibidos.  
Para maiores informações, consulte: [F060BROW - Prevalidação de dados](http://tdn.totvs.com/pages/releaseview.action?pageId=6070906)  
  
**FA060TRF -** Restringe transferência de título para outro portador  
Permite que um titulo seja "travado", restringindo sua transferência para outro portador.  
Para maiores informações, consulte: [FA060TRF - Restringe transferência de título para outro portador](http://tdn.totvs.com/pages/releaseview.action?pageId=6071417)  
  
**F060SITUAC –** Incluir novas situações  
Este Ponto de Entrada permite utilizar novas situações incluídas na tabela 07 - Situações de Cobranças, do Configurador na geração dos borderôs de contas a receber.  
Para maiores informações, consulte: [F060SITUAC – Incluir novas situações](http://tdn.totvs.com/pages/releaseview.action?pageId=6071493)  
  
**F060DGV -** Manipulação de valores de retorno  
O ponto de entrada **F060DGV** possibilita manipular os valores de retorno da transferência descontada para a carteira.  
Para maiores informações, consulte: [F060DGV - Manipulação de valores de retorno](https://tdn.totvs.com/pages/viewpage.action?pageId=829308092)  
  
**FA60SIT2 -** Permite manipulação da **SE5**Ponto de entrada criado para completar a gravação da **SE5** gerada do estorno da cobrança descontada( **E5\_TIPODOC = "E2"** ). No momento da sua chamada está posicionado na **SE5** de estorno.  
Para maiores informações, consulte: [FA60SIT2 - Completar a gravação da SE5 gerada do estorno da cobrança descontada](https://tdn.totvs.com/display/PROT/DT_FA60SIT2_COMPLEMENTO_GRV_SE5)  
  
**F060SEA -** Gravação de dados do borderô  
O ponto de entrada **F060SEA** será executado durante a gravação dos dados do borderô (**SEA**) na transferência.  
Para maiores informações, consulte: [DT\_F060SEA\_Gravação\_de\_dados\_do\_borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=465391018)  
  
**F060ACT -** Grava transferência  
Ponto de Entrada que permite a leitura das das seguintes variáveis private: **cSituant** - Situação do título antes da transferência - Situação do título após a transferência.   
O Ponto de Entrada **F060ACT** será chamado após a gravação da transferência e antes da contabilização.  
Para maiores informações, consulte: [F060ACT - Grava transferência](http://tdn.totvs.com/pages/releaseview.action?pageId=6070904)  
  
**FA60TRAN -** Rotina de Transferência de contas a receber  
O ponto de entrada **FA60TRAN** será executado ao final da rotina de transferência de contas a receber, após gravação de dados e da contabilização.  
Para maiores informações, consulte: [FA60TRAN - Rotina de Transferência de contas a receber](http://tdn.totvs.com/pages/releaseview.action?pageId=6071249)  
  
**F060EXIT -** Mostra Número de Borderô  
Para maiores informações, consulte: [F060EXIT - Mostra Número de Borderô](http://tdn.totvs.com/pages/releaseview.action?pageId=59900691)  
  
**F060BOR -** Recuperação de número do borderô  
O ponto de entrada **F060BOR** será utilizado para recuperar o numero do próximo borderô.  
Para maiores informações, consulte: [F060BOR - Recuperação de número do borderô](http://tdn.totvs.com/pages/releaseview.action?pageId=6070905)  
  
**F060SITUAC –** Incluir novas situações  
Este Ponto de Entrada permite utilizar novas situações incluídas na tabela 07 - Situações de Cobranças, do Configurador na geração dos borderôs de contas a receber.  
Para maiores informações, consulte: [F060SITUAC – Incluir novas situações](http://tdn.totvs.com/pages/releaseview.action?pageId=6071493)  
  
**FA60FIL -** Filtro de registros processados do borderô  
O ponto de entrada **FA60FIL** será executado no filtro de registros que serão processados para a elaboração do borderô(tipo Indregua).  
Para maiores informações, consulte: [FA60FIL - Filtro de registros processados do borderô.](http://tdn.totvs.com/pages/releaseview.action?pageId=6071248)  
  
**F060CPBOR -** Seleção de campos  
O ponto de entrada **F060CPBOR** seleciona os campos que aparecerão na tela de seleção dos títulos para gerar o borderô. O retorno deve ser uma *string* contendo o nome dos campos que o usuário quer demonstrar.  
Para maiores informações, consulte: [F060CPBOR - Seleção de campos](http://tdn.totvs.com/pages/releaseview.action?pageId=6070907)  
  
**F060Trb -** Inclui novos campos  
Ponto de entrada que permite adicionar dados no *array* de campos a serem exibidos na tela de seleção de títulos. Este ponto de entrada foi incluído para que outros campos de tabelas diferentes da **SE1**, possam ser exibidos na tela de seleção de títulos. Para que este recurso funcione adequadamente, é necessário utilizar os Pontos de Entrada **F060COL** e **F060QRCP**.   
Para maiores informações, consulte: [F060Trb - Inclui novos campos](http://tdn.totvs.com/display/public/mp/F060Trb+-+Inclui+novos+campos+--+107704)  
  
**F060CHAV -** Altera chave de ordenação  
Ponto de Entrada **F060CHAV** que permite alterar a chave que ordena a exibição dos títulos na tela de seleção da opção "Borderô".  
Para maiores informações, consulte: [F060CHAV - Altera chave de ordenação](https://tdn.totvs.com/pages/releaseview.action?pageId=653137829)   
  
**FA060Qry -** Inclui condição SQL  
O ponto de entrada **FA060QRY** permite a inclusão de uma condição adicional na consulta **SQL** (*Query*) de seleção dos títulos a receber, para posterior marcação em tela.  
A condição adicionada deve seguir a *sintaxe* **SQL** e irá interferir na seleção dos títulos a receber que serão exibidos em tela.  
Para maiores informações, consulte: [FA060Qry Inclui condição SQL](http://tdn.totvs.com/pages/releaseview.action?pageId=6071120)  
  
**F060QRCP -** Manipula Query do borderô  
Ponto de entrada que permite a manipulação da *query* de seleção de títulos a serem considerados na montagem do borderô (**FINA060**). Este ponto de entrada foi incluído para que outros campos de tabelas diferentes da **SE1**, possam ser mostrados na tela de seleção de títulos. Para que este recurso funcione adequadamente, devem ser utilizados em conjunto com os Pontos de Entrada **F060COL** e **F060Trb**.  
Para maiores informações, consulte: [F060QRCP - Manipula Query do borderô](http://tdn.totvs.com/pages/releaseview.action?pageId=6071544)  
  
**F060PROC -** Disponibilização de informações após a confirmação da seleção de títulos para a remessa.

Ponto de entrada que disponibiliza informações após a confirmação da seleção de títulos para a remessa. A saber: Banco, Agência, Conta, Situação (carteira), Vencimento Inicial, Vencimento Final, Valor limite para borderô, Moeda a ser considerada, Contrato Bancário, Data de Emissão Inicial, Data de Emissão Final, Cliente De e Cliente Até.  
Para maiores informações, consulte: [DT\_F060PROC\_Disponibilização de informações após a confirmação da seleção de títulos para a remessa](http://tdn.totvs.com/pages/releaseview.action?pageId=201729988)  
  
**F060HIST -** Manipulação da variável **cHistorico**O ponto de entrada **F060HIST** será utilizado para manipular a variável **cHistorico** de acordo com o código da situação (**cSituacao**) enviado para tratamento no **RDMAKE**.  
Para maiores informações, consulte: [F060HIST - Manipulação da variável cHistorico](http://tdn.totvs.com/pages/releaseview.action?pageId=6070910)  
  
**F060NDES -** Validação de campos de natureza  
O ponto de entrada **F060NDES** é executado na validação dos campos de natureza, para os títulos inclusos em borderô com situação em cobrança descontada, com o objetivo de validar alguma das informações referente à natureza informada.  
Para maiores informações, consulte: [F060NDES - Validação de campos de natureza](http://tdn.totvs.com/pages/releaseview.action?pageId=6071449)  
  
**F060SEA2 -** Alteração das informações adicionais na tabela **SEA**O ponto de entrada **F060SEA2** altera antes de gravar, ou grava informações adicionais na tabela **SEA** na geração do Borderô.  
Para maiores informações, consulte: [F060SEA2 - Alteração das informações adicionais na tabela SEA](http://tdn.totvs.com/pages/releaseview.action?pageId=6071651)  
  
**FA60BDE -** Gravação de arquivos **SE1SE5SEA**O ponto de entrada **FA60BDE** será executado após a gravação dos arquivos **SE1**/ **SE5**/ **SEA** na transferência de contas a receber.  
Para maiores informações, consulte: [FA60BDE - Gravação de arquivos SE1, SE5, SEA](https://tdn.totvs.com/pages/releaseview.action?pageId=6071245)  
  
**FA060SE5 -** Contabiliza borderô  
O ponto de entrada **FA060SE5** será utilizado após a contabilização do borderô e executado ainda que não haja contabilização a ser efetuada.  
Para maiores informações, consulte: [FA060SE5 - Contabliza borderô](http://tdn.totvs.com/pages/releaseview.action?pageId=6071121)  
  
**F060POR2 -** Validação de Portador  
O ponto de entrada **F060POR2** valida o portador na transferência de situação cobrança quando a situação atual do título utiliza portador (diferente de 0= Carteira, F= Carteira Protesto, G= Carteira Acordo, H=Cobrança cartório) para uma situação em que não é utilizado portador.  
Para maiores informações, consulte: [F060POR2 - Validação de Portador](http://tdn.totvs.com/pages/releaseview.action?pageId=6071653)  
  
**F060ASIT -** Invalida a trava de título em borderô  
Este ponto de entrada desconsidera a trava da transferência de Agência / Conta de títulos a receber que estão em borderô.  
Para maiores informações, consulte: [F060ASIT - Invalida a trava de título em borderô](http://tdn.totvs.com/pages/releaseview.action?pageId=90276678)  
  
**F060DPM -** Marcação de títulos no borderô  
O ponto de entrada **F060DPM** será executado durante a marcação de títulos no borderô. O calculo do prazo médio só será calculado para as situações 2 e 7 (cobranças descontadas). O sistema efetua o seguinte cálculo:**<br>nDias := E1\_VENCREA - E1\_EMISSAO<br>nPrazo := nDias \* E1\_SALDO.**  
Para maiores informações, consulte: [F060DPM - Marcação de títulos no borderô](http://tdn.totvs.com/pages/releaseview.action?pageId=6070909)  
  
**FA60CAN1 -** Estorno de borderô do contas a receber  
O ponto de entrada **FA60CAN1** será executado antes da gravação do **SE1** no estorno do borderô do contas a receber.  
Para maiores informações, consulte: [FA60CAN1 - Estorno de borderô do contas a receber](http://tdn.totvs.com/pages/releaseview.action?pageId=6071246)  
  
**FA60CAN2 -** Gravação de **SE1** no estorno do borderô  
O ponto de entrada será executado após gravar o **SE1** (restauração) no estorno do borderô. Este ponto pode ser usado para gravar dados como a caixa portadora origem no **SE1** no estorno, para isto a caixa portadora origem deveria ter sido guardada no **SEA** em campos de usuário (pode ser usado o ponto **Fa60BDE** para isto).  
Para maiores informações, consulte: [FA60CAN2 - Gravação de SE1 no estorno do borderô](http://tdn.totvs.com/pages/releaseview.action?pageId=6071247)  
  
**F060VLTOT -** Alterar o valor que irá limitar a seleção de títulos do borderô  
O Ponto de Entrada **F060VLTOT** permite alterar o valor que irá limitar a seleção de títulos do borderô, podendo ser alterado via ponto de entrada o valor informando no campo Valor Limite apresentado na tela de informações de filtragem dos títulos.   
ara maiores informações, consulte: [F060VLTOT - Permite alterar o valor que irá limitar a seleção de títulos do borderô](https://tdn.totvs.com/pages/viewpage.action?pageId=791847963)  
  
**F060COL -** Colunas do *browse*Ponto de entrada que permite alterar a ordem das colunas do *browse* exibidas na tela de seleção de títulos, na montagem de um borderô de cobrança.  
Para maiores informações, consulte: [F060COL - Colunas do browse](http://tdn.totvs.com/display/public/mp/F060COL+-+Colunas+do+browse+--+107437)  
  
**F060OK -** Gravação dos dados  
Ponto de entrada para gravação dos dados na transferência/borderô  
Para maiores informações, consulte: [F060OK - Validação complementar do usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=667356403)  
**F060MARK -** Permissão a mais de um usuário  
O ponto de entrada **F060MARK** será utilizado para permitir que mais de um usuário utilize a rotina de geração de borderô ao mesmo tempo, controlando a marcação de títulos para envio ao borderô por usuário. Não possui retorno e parâmetros.  
Para maiores informações, consulte: [F060MARK - Permissão a mais de um usuário](http://tdn.totvs.com/pages/releaseview.action?pageId=6070911)  
  
**FA060VLD -** Valida seleção de título do borderô  
Ponto de Entrada cujo objetivo é a criação de regra de validação, para permitir ou bloquear a seleção do título na geração do borderô, por meio da rotina Transferências (**FINA060**).  
Para maiores informações, consulte: [FA060VLD - Valida seleção de título do borderô](https://tdn.totvs.com/pages/viewpage.action?pageId=465394171)  
  
**F060LEGEN -** Criação de legenda  
O ponto de entrada **F060LEGEN** permite criar a própria legenda na rotina de Transferências, sendo que, a legenda padrão do sistema é substituída. Pela regra da rotina, a legenda deve conter no mínimo quatro caracteres.  
Para maiores informações, consulte: [F060LEGEN - Criação de legenda](http://tdn.totvs.com/pages/releaseview.action?pageId=6071637)  
  
**F060CORES -** Altera cores da legenda

Ponto de entrada que permite mais opções na legenda rotina de transferências/borderô (FINA060/FINA061). Este ponto de entrada, irá adicionar as informações do ponto de entrada F060LEGEN, caso este esteja em uso.  
Para maiores informações, consulte: [F060CORES - Cores e regra para legendas](https://tdn.totvs.com/display/PROT/F060CORES+-+Cores+e+regra+para+legendas)  
  
**F060VLOK -** Validação de informações no borderô  
Este Ponto de Entrada permite que o usuário faça a validação das informações na tela onde são informados os parâmetros, para geração do borderô a receber. O mesmo será executado após clicar no botão *OK*, para a inclusão deste registro.  
Para maiores informações, consulte: [F060VLOK - Validação de informações no borderô](http://tdn.totvs.com/pages/releaseview.action?pageId=6071468)  
  
**Saiba Mais:**   
[Pontos de Entrada - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Pontos+de+Entrada+-+Financeiro+-+P12)
