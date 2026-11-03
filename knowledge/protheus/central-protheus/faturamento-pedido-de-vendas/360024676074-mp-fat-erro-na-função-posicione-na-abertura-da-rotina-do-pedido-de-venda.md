---
article_id: 360024676074
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: fe1d2927bb8eb64c63451ef0bbec3ebb38d3b05ad7ab68c3312fa214e4e0dd7d
fetched_at: '2026-06-28T22:38:41.300759+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT-Erro na função POSICIONE na abertura da rotina do pedido de venda
type: support-article
updated_at: '2021-04-28T15:50:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024676074-MP-FAT-Erro-na-fun%C3%A7%C3%A3o-POSICIONE-na-abertura-da-rotina-do-pedido-de-venda
---

**Ocorrência**

Ao abrir o pedido de vendas ocorre o erro abaixo:

**Alias does not exist: TEPX RECICLAGEM DE MATERIAIS BENEFICIADO**  
**on POSICIONE(APLIB080.PRW) 15/03/2019 14:54:46 line : 4402**

[TOTVS build: 7.00.131227A-20190114 NG]   
Called from POSICIONE(APLIB080.PRW) 15/03/2019 14:54:46 line : 4402   
Called from { |o| POSICIONE(SA1->A1\_NOME) }(APLIB090.PRW) 15/03/2019 14:54:46 line : 4402   
Called from FWMBROWSE:ADDCOLUMN(FWBROWSE.PRW) 15/03/2019 14:54:49 line : 1140   
Called from FWBRWMODELCONFIG:APPLYCONFIG(FWBRWMODELCONFIG.PRW) 15/03/2019 14:54:49 line : 330   
Called from FWMBROWSE:LOADCONFIG(FWBROWSE.PRW) 15/03/2019 14:54:49 line : 6410   
Called from FWMBROWSE:ACTIVATE(FWBROWSE.PRW) 15/03/2019 14:54:49 line : 910   
Called from FWMBROWSE:ACTIVATE(FWFORMBROWSE.PRW) 15/03/2019 14:54:49 line : 423   
Called from FWMBROWSE:ACTIVATE(FWMBROWSE.PRW) 15/03/2019 14:54:49 line : 630   
Called from BROWSEDEF(MATA410.PRX) 17/07/2018 15:34:42 line : 329   
Called from MATA410(MATA410.PRX) 17/07/2018 15:34:42 line : 144   
Called from \_\_EXECUTE(APLIB090.PRW) 15/03/2019 14:54:46 line : 679   
Called from MDIEXECUTE(APLIB260.PRW) 15/03/2019 14:54:46 line : 877   
Called from STATICCALL(APLIB260.PRW) 15/03/2019 14:54:46 line : 877

**Ambiente**

Microsiga Protheus - todas a versões.  
   
 **Causa**

O erro ocorre por que no browser do pedido de vendas (**MATA410**) está sendo chamado a função  **Posicione** para o campo **A1\_NOME**, porém a resposta retornada pela função é nula, veja o trecho do erro abaixo:  
  
STACK { |o| **POSICIONE(SA1->A1\_NOME)** }(APLIB090.PRW) 15/03/2019 14:54:46  
  
**Local CodeBlock 1: O(U) :NIL**  
  
STACK POSICIONE(APLIB080.PRW) 15/03/2019 14:54:46  
  
**Local 1: CALIAS(C) :TEPX RECICLAGEM DE MATERIAIS BENEFICIADO**  
  Local 2: NORDEM(U) :NIL  
  Local 3: CEXPR(U) :NIL  
  Local 4: CCPO(U) :NIL  
  Local 5: CNICKNAME(U) :NIL  
  Local 6: CSAVALIAS(C) :SXQ  
  Local 7: CRET(U) :NIL

A chamada da variável **CAlias** deveria trazer a informação da tabela que está sendo lida, porém, está trazendo o nome do cliente, desta forma, o sistema se perde para buscar a demais informações.  
  
 **Solução**

Como o erro ocorre browser da rotina e não no clique do botão incluir, a chamada da função Posicione pode estar sendo efetuada por:

1 - **Ponto de entrada:** sendo ponto de entrada, desabilite o ponto de entrada através da rotina catálogo de personalizações do Configurador e posteriormente, revise o rdmake de customização e recompile ao RPO para poder utilizar na rotina;

2 - **Filtro de usuário na tela do pedido**: sendo filtro de usuário, efetue a *manutenção de perfil de usuário* **(<http://tdn.totvs.com/pages/viewpage.action?pageId=271165124>)** e limpe as chamadas relacionadas a rotina *mata410*. Depois reinicie o Smartclient e refaça o processo;

3 - Inicializador padrão ou validação de usuário, no campo **C5\_CLIENTE**: sendo informação advpl inserida no inicializador padrão ou validação de usuário no campo C5\_CLIENTE, vá em Configurador, Base de Dados, Dicionário, Base de Dados, selecione a tabela **SC5**, edite a tabela.

3.1 - Selecione o campo **C5\_CLIENTE** e edite.

3.2 - Retire a informação inserida no inicializador padrão ou validação de usuário e confirme a tabela.

3.3 - Atualize o dicionário de dados , reinicie o Smartclient e refaça o processo.

**Obs: Para realizar o procedimentos acima requer um analista com conhecimento em ADVPL e estrutura Protheus.**

**Em caso de dúvida, acione a equipe de Framework para orientação em estrutura e manutenção de perfil, para dúvida em ponto de entrada, acione a equipe de ADVPL.**
