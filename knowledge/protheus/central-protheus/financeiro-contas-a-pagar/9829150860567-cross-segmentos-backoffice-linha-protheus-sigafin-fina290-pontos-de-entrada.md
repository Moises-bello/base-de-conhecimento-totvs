---
article_id: 9829150860567
category: Financeiro - Contas a Pagar
content_hash: d492ad902777a44f0ac4ef4624c9e3430f7a420091944cb94bd92346a6c08359
fetched_at: '2026-06-28T22:38:07.118137+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA290 -  Pontos de
  Entrada
type: support-article
updated_at: '2026-02-25T16:57:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9829150860567-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA290-Pontos-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38637085504023) Tempo aproximado para leitura: **00:05:min**  
  
**Dúvida**  
Quais os Pontos de Entrada  da rotina FINA290?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Os pontos de entrada da rotina **FINA290** são:  
  
**F290BFIL - Expressão de filtro na rotina Faturas a Pagar**

Ponto de Entrada permite que na rotina faturas a pagar exista expressão de filtro para execução somente em ambiente TOP, a expressão deve ser SQL.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=47908511](https://tdn.totvs.com/pages/releaseview.action?pageId=47908511)

**F290PRE - Pré-valida faturas a pagar**

O ponto de entrada F290PRE tem como finalidade a pré-validação do faturas a pagar.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=6071009](https://tdn.totvs.com/pages/releaseview.action?pageId=6071009)

**F290FORNP - Bloqueia dados**

Ponto de Entrada que permite o bloqueio os dados "Gerar p/ Fornecedor" e "Loja" na primeira tela da rotina Faturas a pagar.

Para maiores informações, consulte: [http://tdn.totvs.com/display/public/mp/F290FORNP+-+Bloqueia+dados+--+111871](https://tdn.totvs.com/display/public/mp/F290FORNP+-+Bloqueia+dados+--+111871)

**F290BTIT - Seleção de títulos para fatura a pagar**

Através deste ponto de entrada, será possível definir quais as colunas que serão apresentadas na tela de seleção de títulos para geração de uma Fatura a Pagar.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=6071582](https://tdn.totvs.com/pages/releaseview.action?pageId=6071582)

**F290FPG - Criação de botões**

Ponto de entrada para criação de botões em ações relacionadas na rotina Fatura a Pagar.

Para maiores informações, consulte: [http://tdn.totvs.com/display/public/PROT/F290FPG](https://tdn.totvs.com/display/public/PROT/F290FPG)

**FI290MT - Desabilita a tela de Parcelas a serem geradas**

O Ponto de entrada FI290MT é utilizado para desabilitar a tela de "Parcelas a serem geradas" em Parcelas a Pagar. É importante dizer que, este ponto de entrada pode ser utilizado somente se o ponto de entrada F290CON existir.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=57410566](https://tdn.totvs.com/pages/releaseview.action?pageId=57410566)

**FA290HPAD - Customização do campo E2\_HIST**

O Ponto de entrada FA290HPAD permite a customização do campo E2\_HIST para que seja gravado em todos os títulos selecionados ao gerar a fatura.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=177504264](https://tdn.totvs.com/pages/releaseview.action?pageId=177504264)

**F290BAIXA -  Histórico da contabilização**

Ponto de entrada executado após a baixa do titulo que gerou a fatura. Pode ser retornado um histórico utilizado na contabilização, por meio da variável STRLCTPAD.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=110432885](https://tdn.totvs.com/pages/releaseview.action?pageId=110432885)

**FI290GE5 - Gravação da movimentação bancária**

Ponto de entrada executado após a gravação da movimentação bancária (SE5).

Para maiores informações, consulte: <https://tdn.totvs.com/pages/viewpage.action?pageId=653132877>

**FAT290SE5 - Gravação dos títulos faturados**

O ponto de Entrada FAT290SE5 grava os títulos faturados.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=145358956](https://tdn.totvs.com/pages/releaseview.action?pageId=145358956)

**FA290 - Grava faturas a pagar**

Executado durante a gravação dos dados da fatura no SE2 e antes da contabilização.

Para maiores informações, consulte: [http://tdn.totvs.com/display/public/mp/FA290+-+Grava+faturas+a+pagar+--+11968](https://tdn.totvs.com/display/public/mp/FA290+-+Grava+faturas+a+pagar+--+11968)

**FI290COLS - Inclui colunas no faturas a pagar**

O ponto de entrada FI290COLS permite incluir novos campos no aHeader / aCols da rotina de Faturas a Pagar.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=95027219](https://tdn.totvs.com/pages/releaseview.action?pageId=95027219)

**F290LIBT - Desabilita verificação de liberação**

O ponto de entrada F290LIBT é utilizado para desabilitar a verificação da liberação dos títulos, permitindo que os títulos que ainda não foram liberados possam ser selecionados na tela da fatura.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=6071007](https://tdn.totvs.com/pages/releaseview.action?pageId=6071007)

**F290OWN - Filtro de Indregua**

O ponto de entrada F290OWN será executado na preparacao do filtro da Indregua. Se o ponto de entrada existir nao sera considerada a filtragem por data de emissao, contudo os demais itens do filtro serão mantidos.

Para maiores informações, consulte: [http://tdn.totvs.com/display/public/mp/F290OWN+-+Filtro+de+Indregua+--+11744](https://tdn.totvs.com/display/public/mp/F290OWN+-+Filtro+de+Indregua+--+11744)

**F290FIL - Confirma tela de faturas**

Ponto de entrada F290FIL é executado após confirmar a tela de faturas a pagar e  utilizado na montagem do filtro da Indregua.

Caso o ponto de entrada exista, o filtro retornado é anexado ao filtro padrão.

Para maiores informações, consulte: [http://tdn.totvs.com/display/public/PROT/F290FIL+-+Confirma+tela+de+faturas+--+11742](https://tdn.totvs.com/display/public/PROT/F290FIL+-+Confirma+tela+de+faturas+--+11742)

**F290CHK - Filtro para seleção dos títulos**

O ponto de entrada F290CHK  altera os títulos que podem ser incluídos numa fatura a pagar, como por exemplo, selecionar tipo PR.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=46072220](https://tdn.totvs.com/pages/releaseview.action?pageId=46072220)

**FA290C - Cancela faturas a pagar**

Executado após a confirmação do Cancelamento da Fatura, antes da exclusão do registro.

Para maiores informações, consulte: [http://tdn.totvs.com/display/public/mp/FA290C+-+Cancela+faturas+a+pagar+--+11969](https://tdn.totvs.com/display/public/mp/FA290C+-+Cancela+faturas+a+pagar+--+11969)

**FA290OKC - Validação da fatura se possuir abatimento**

O ponto de Entrada FA290OKC realiza validação de abatimento no cancelamento do Faturas a Pagar.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=147817553](https://tdn.totvs.com/pages/releaseview.action?pageId=147817553)

**F290CN2 - Ponto de entrada para tratamento especifico de dados do titulo a ser deletado**

**F290CAN - Complemento de gravação**

O ponto de entrada F290CAN sera utilizado para complementar a gravação após cancelamento da fatura.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=6071004](https://tdn.totvs.com/pages/releaseview.action?pageId=6071004)

**F290TIT - Verificação de título para compor fatura**

O ponto de entrada F290TIT verifica se título pode ser marcado para compor a Fatura, se alterada a marcação do título. O ExecBlock  dever  retornar .F., para não ter alteração dos acumuladores de valores e número de títulos.

Para maiores informações, consulte: [http://tdn.totvs.com/pages/releaseview.action?pageId=6071644](https://tdn.totvs.com/pages/releaseview.action?pageId=6071644)

**F290VAL - Retorna array contendo os títulos marcados**

**Saiba mais**  
[Pontos de Entrada - Financeiro - P12](https://tdn.totvs.com/display/PROT/Pontos+de+Entrada+-+Financeiro+-+P12)
