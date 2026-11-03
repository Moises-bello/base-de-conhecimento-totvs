---
article_id: 21069314802455
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 807fdd6f2b0eea359e5e014c8edfd832fa56049740bc27ad82d11068a910adfc
fetched_at: '2026-06-28T22:37:55.247003+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - FINA430 - Pontos
  de entrada disponíveis
type: support-article
updated_at: '2024-02-02T15:35:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21069314802455-Cross-Segmentos-Backoffice-Linha-Protheus-Financeiro-FINA430-Pontos-de-entrada-dispon%C3%ADveis
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21069314789015) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Quais são os pontos de entrada da rotina FINA430 - Retorno de Pagamentos?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução** **F430CIT - CNAB Citibank**O ponto de entrada **F430CIT** tem como finalidade tratar o **arquivo de retorno de contas a pagar**, CNAB do Citibank e será executado antes do processamento.  
[F430CIT - CNAB Citibank](https://tdn.totvs.com/display/public/mp/F430CIT+-+CNAB+Citibank+--+11795)  
  
**F430PORT - Define se utiliza o Portador ou o banco de retorno do CNAB na baixa do título**Ponto de entrada que permite definir o banco a ser usado na baixa do título no **retorno de CNAB a Pagar**, o **portador** ou o **banco de retorno do CNAB**.  
[F430PORT - Define se utiliza o Portador ou o banco de retorno do CNAB na baixa do título](https://tdn.totvs.com/pages/releaseview.action?pageId=648838953)**FA430FIL - Recebe a linha do arquivo de retorno a ser processada**Ponto de entrada permite obter o conteúdo da linha do arquivo de retorno quando utilizado **Modelo 1**, afim de realizar a utilização dos dados do processamento  
[FA430FIL - Recebe a linha do arquivo de retorno a ser processada](https://tdn.totvs.com/display/public/PROT/FA430FIL+-+Recebe+a+linha+do+arquivo+de+retorno+a+ser+processada)  
  
**F430VAR - Permite manipulação das Variáveis Private durante a baixa CNAB (Pagar)**O **ponto de entrada F430VAR** tem como finalidade tratar os dados para **baixa CNAB**. Antes de verificar a espécie do título, permitirá que qualquer exceção ou necessidade seja tratada no ponto de entrada através do **paramIXB**.

Esse ponto de entrada é executado em dois momentos diferentes, sendo uma durante a leitura do CNAB **Modelo 1 (MV\_PAR10 = 1)** e **CNAB Modelo 2 (MV\_PAR10 = 2)**. A quantidade de posições passadas por parâmetro difere entre as duas execuções e está melhor descrita no item "3 - Parâmetros").  
[F430VAR - Permite manipulação das Variáveis Private durante a baixa CNAB (Pagar)](https://tdn.totvs.com/pages/releaseview.action?pageId=641447402)

**FA430PA - Baixa de títulos**  
O **ponto de FA430PA** será utilizado para permitir ou não a baixa de um determinado tipo de título, no retorno da comunicação bancária.  
[FA430PA - Baixa de títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=6071226) **FA430SE2 - Reposicionamento de SE2**O **ponto de entrada FA430SE2** será utilizado para reposicionar o **SE2**.  
[FA430SE2 - Reposicionamento de SE2](https://tdn.totvs.com/display/public/mp/FA430SE2+-+Reposicionamento+de+SE2+--+11999)**FA430OCO - Reposicionamento do SEB**  
O **ponto de entrada FA430OCO** será utilizado para reposicionar o **SEB** utilizando campos específicos criados no arquivo **SEB**.  
[FA430OCO - Reposicionamento do SEB](https://tdn.totvs.com/display/public/mp/FA430OCO+-+Reposicionamento+do+SEB+--+11996)

**FA430LP - Altera a utilização do LP530 para o LP532  
Ponto de entrada FA430LP** altera a utilização do **LP530** para o **LP532**.  
[FA430LP - Altera a utilização do LP530 para o LP532](https://tdn.totvs.com/display/public/PROT/TUBVLE_DT_FA430LP_ALTERA_LP_532)  
**FA430LRM - Tratamento de dados**  
O **ponto de entrada FA430LRM** será utilizado no tratamento dos dados, antes da **baixa a paga**r do título via CNAB.  
[FA430LRM - Tratamento de dados](https://tdn.totvs.com/display/public/mp/FA430LRM+-+Tratamento+de+dados+--+11995)  
  
**F430TXBX permite informar a taxa da moeda estrangeira**  
O **ponto de entrada F430TXBX** tem como objetivo permitir informar a taxa da moeda estrangeira a ser considerada para efetivar a baixa via retorno de comunicação bancária **contas a pagar**.  
[F430TXBX permite informar a taxa da moeda estrangeira](https://tdn.totvs.com/display/public/PROT/O+ponto+de+entrada+F430TXBX+permite+informar+a+taxa+da+moeda+estrangeira) **F430BXA - Grava complemento de baixa**O **ponto de entrada F430BXA** tem como finalidade permitir a gravação de complemento das baixas **CNAB a pagar** do retorno bancário. Este ponto de entrada é chamado a cada registro do arquivo de retorno.  
[F430BXA - Grava complemento de baixa](https://tdn.totvs.com/display/public/PROT/F430BXA+-+Grava+complemento+de+baixa) **F430REJ - Trata registros rejeitados**O **ponto de entrada F430REJ** tem como finalidade tratar os dados de registro rejeitados antes de serem zerados.[F430REJ - Trata registros rejeitados](https://tdn.totvs.com/display/public/mp/F430REJ+-+Trata+registros+rejeitados+--+11796) **FA430FIG - Permitir modificar CNPJ do retorno DDA**Permite modificar o CNPJ obtido da leitura do **arquivo de retorno DDA**, de modo que a tabela **SA2** seja posicionada através do CNPJ modificado neste ponto de entrada.  
[FA430FIG - Permitir modificar CNPJ do retorno DDA](https://tdn.totvs.com/display/public/mp/FA430FIG+-+Permitir+modificar+CNPJ+do+retorno+DDA+--+114597) **F430GRAFIL - Gravação da filial de origem na tabela FIG - Conciliação DDA**

Ponto de entrada que permite manipular a gravação da filial pertencente ao CNPJ contido no **arquivo de** **retorno (.ret)**.  
[F430GRAFIL - Gravação da filial de origem na tabela FIG - Conciliação DDA](https://tdn.totvs.com/pages/releaseview.action?pageId=648838725) **FA430REN - Renomear arquivo de retorno CNAB**O **ponto de entrada FA430REN** será utilizado para renomear o arquivo de retorno CNAB.  
[FA430REN - Renomear arquivo de retorno CNAB](https://tdn.totvs.com/display/public/mp/FA430REN+-+Renomear+arquivo+de+retorno+CNAB+--+11998) **F430COMP - Execuções complementares**O **ponto de entrada F430COMP** é utilizado no **retorno de pagamentos CNAB (FINA430)**, nas execuções complementares após a gravação dos dados financeiros e das suas respectivas contabilizações. O mesmo será executado após efetuar os processos no retorno do arquivo bancário.[F430COMP - Execuções complementares](https://tdn.totvs.com/pages/releaseview.action?pageId=6071579) **F430CHK - Reenvio CNAB**Ponto de Entrada utilizado para garantir que arquivo não seja reenviado para **CNAB a pagar**.   
[F430CHK - Reenvio CNAB](https://tdn.totvs.com/display/public/mp/F430CHK+-+Reenvio+CNAB+--+11794)
