---
article_id: 360026258491
category: Financeiro - Contas a Pagar
content_hash: 0991b249a66ee1ffad74983d263af8dbe3bdb65ef68f05fc410a634f22f8fc6b
fetched_at: '2026-06-28T22:38:09.671303+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - Pontos de
  entrada disponíveis da Rotina Compensação Contas a Pagar
type: support-article
updated_at: '2022-05-19T20:44:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026258491-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Pontos-de-entrada-dispon%C3%ADveis-da-Rotina-Compensa%C3%A7%C3%A3o-Contas-a-Pagar
---

**Dúvida**Quais são os pontos de entrada disponíveis da Rotina **Compensação Contas a Pagar** (**FINA340**) ?

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA473 - Todas as versões  
  
**Solução**Pontos de entrada disponíveis na rotina **FINA340** (**Compensação contas a pagar**)

**F340BROW** - Manipula dados  
O ponto de entrada **F340BROW** será chamado antes do *browse* e poderá ser utilizado no tratamento dos dados apresentados.Para maiores informações, consulte:   
[F340BROW - Manipula dados](http://tdn.totvs.com/display/public/mp/F340BROW+-+Manipula+dados+--+11751)

**F340LIBT** - Permite baixa de títulos sem liberação  
O ponto de entrada **F340LIBT** indica se haverá a validação de liberação do título no momento da **compensação**. Para maiores informações, consulte:   
[DT\_F340LIBT\_Perimite\_baixa\_titulos\_sem\_liberacao](http://tdn.totvs.com/display/public/PROT/DT_F340LIBT_Perimite_baixa_titulos_sem_liberacao)

**F340DTFIN** - Valida data de pagamento  
O ponto de entrada **F340DTFIN** poderá ser utilizado para flexibilizar a forma pela qual o cliente possa decidir se quer validar a data do parâmetro **MV\_DATAFIN** ou não.  
Para maiores informações, consulte:   
[F340DTFIN - Valida data de pagamento](http://tdn.totvs.com/display/public/mp/F340DTFIN+-+Valida+data+de+pagamento+--+11755)

**F340TAXA** - Permite alterar taxa moeda  
O ponto de entrada **F340TAXA** permite alterar as taxas das moedas que serão utilizadas na **compensação do contas a pagar**. Para maiores informações, consulte: [DT\_F340TAXA\_Permite\_alterar\_taxa\_moeda](http://tdn.totvs.com/display/public/PROT/DT_F340TAXA_Permite_alterar_taxa_moeda)

**FA340ATLIS** - Manipulação de *array* na tela de compensação  
Este ponto de entrada permite a manipulação do *Array* **aTitulos**, para alteração do **listBox** da tela de compensação. Para maiores informações, consulte:   
[F340ATLIS - Manipulação de Array na tela de compensação](http://tdn.totvs.com/pages/releaseview.action?pageId=6071424)

**F340TOTCP** - Manipula valores totais de títulos  
O ponto de entrada **F340TOTCP** possibilita manipular os valores totais de títulos a serem compensados. Para maiores informações, consulte:

[F340TOTCP - Manipulação dos valores totais dos títulos a serem compensados](https://tdn.totvs.com/pages/viewpage.action?pageId=639940552)

**F340MKTIT** - Customização dos títulos selecionados  
O ponto de entrada **F340MKTIT** permite a customização dos títulos já selecionados na *markbrowse*. Permitindo a manipulação da *array* que contém os títulos.  
Para maiores informações, consulte:   
[F340MKTIT - Customização dos títulos selecionados](http://tdn.totvs.com/pages/releaseview.action?pageId=6071343)

**F340NAT** - Posiciona arquivos  
O ponto de entrada **F340NAT** será utilizado para posicionamento no arquivo de **natureza** (**SED**) no registro correspondente a **natureza** do título principal para tratamentos específicos. Utilize o *Recno* (passado como parâmetro) do título principal para posicionar o arquivo de **contas a pagar** e em seguida posicione no arquivo de **naturezas**.  
Para maiores informações, consulte:   
[F340NAT - Posiciona arquivos](http://tdn.totvs.com/display/public/mp/F340NAT+-+Posiciona+arquivos+--+11757)

**F340\_PA** - Contabiliza títulos  
O ponto de entrada **F340\_PA** será executado após contabilizar cada título de **compensação a pagar**.  
Para maiores informações, consulte:   
[F340\_PA - Contabiliza títulos](https://tdn.totvs.com/pages/viewpage.action?pageId=624114132)

**F340SE5** - Manipula movimentos bancários processados na compensação  
O ponto de entrada **F340SE5** manipula **movimentos bancários** processados, tendo como parâmetro o **Recno** dos registros **SE5** que foram utilizados na **compensação**.  
Para maiores informações, consulte:   
[F340SE5 - Manipulação dos movimentos bancários processados na compensação](https://tdn.totvs.com/pages/viewpage.action?pageId=639937075)

**F340GRV** - Valida a inclusão na rotina de compensação de contas a pagar  
O ponto de entrada **F340GRV** valida a inclusão na rotina de **compensação** **de contas a pagar**.  
Para maiores informações, consulte:   
[F340GRV - Valida a inclusão na rotina de Compensação de Contas a Pagar](https://tdn.totvs.com/pages/viewpage.action?pageId=74645538)

**F340ACAN** - Indica se o registro poderá ser estornado ou não.  
Este ponto de entrada permite que seja criada uma regra para informar quando será estornado ou não.  
Para maiores informações, consulte:  
[DT\_F340ACAN\_Permite\_para\_o\_processo\_estorno](http://tdn.totvs.com/display/public/PROT/DT_F340ACAN_Permite_para_o_processo_estorno)

**FA340QRY** - Complemento de *query* para **cancelamento de compensação de Títulos**  
O ponto de entrada **FA340QRY** retorna uma condição que complementa uma *query* no **cancelamento de compensação entre títulos**.  
Para maiores informações, consulte:  
[FA340QRY - Complemento da consulta no cancelamento de compensação a pagar](https://tdn.totvs.com/pages/viewpage.action?pageId=653408955)

**F340CAN** - Cancela compensação  
O ponto de entrada **F340CAN** é chamado assim que se efetuar a confirmação do **cancelamento de compensação**.  
Para maiores informações, consulte:  
[F340CAN - Cancela compensação](http://tdn.totvs.com/pages/releaseview.action?pageId=6071016)

**F340GREST** - Gravação de dados adicionais no estorno da compensação CP  
O ponto de entrada **F340GREST** permite gravações adicionais na tabela **SE5** quando é feito o estorno de uma **compensação** **de contas a pagar**.  
Para maiores informações, consulte:  
[F340GREST - Gravação de dados adicionais no estorno da compensação CP](http://tdn.totvs.com/pages/releaseview.action?pageId=6071690)

**F340FCAN** - Gravações complementares  
Ponto de entrada permite gravação de informação complementares no momento do **estorno da compensação**.  
Para maiores informações, consulte:   
[DT\_F340FCAN\_Ponto\_para\_gravacoes\_complementares](http://tdn.totvs.com/display/public/PROT/DT_F340FCAN_Ponto_para_gravacoes_complementares)

**F340FLCP** - Filtra títulos  
O ponto de entrada **F340FLCP** permite implementar uma expressão complementar no filtro de títulos.  
Para maiores informações, consulte:   
[F340FLCP - Filtra títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=6071019)

**F340FCPTOP** - Filtra seleção títulos  
Ponto de entrada para filtrar a seleção dos títulos que serão **compensados** - Ambiente *TOPconnect*.  
Para maiores informações, consulte:   
[DT F340FCPTOP Cria filtro na rotina de compensação cp](https://tdn.totvs.com/pages/viewpage.action?pageId=274328751)
