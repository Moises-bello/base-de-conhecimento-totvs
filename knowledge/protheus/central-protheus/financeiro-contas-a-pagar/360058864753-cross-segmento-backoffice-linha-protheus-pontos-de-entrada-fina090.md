---
article_id: 360058864753
category: Financeiro - Contas a Pagar
content_hash: 59cb64f236c729e1599b0eef81b623481afaec5f8ad93c2ac5aaf8b4a31bdbe8
fetched_at: '2026-06-28T22:38:07.210398+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Pontos de entrada FINA090
type: support-article
updated_at: '2023-10-10T21:27:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058864753-Cross-Segmento-Backoffice-Linha-Protheus-Pontos-de-entrada-FINA090
---

**[Remover as instruções entre colchetes]**  
**Dúvida**Quais os pontos de entrada da rotina **FINA090** ?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro – FINA090 - A partir da versão 17  
  
**Solução**Segue abaixo a relação dos pontos de entrada da rotina **FINA090**:

**F080EST -** O ponto de entrada **F080EST** será utilizado para gravar complemento do **cancelamento da** **baixa** após gerar lançamento de estorno no **SE5**  
[F080EST - Grava complemento de cancelamento](http://tdn.totvs.com/display/public/mp/F080EST+-+Grava+complemento+de+cancelamento+--+11659)  
  
**F090ADBTN** - Permite incluir botões na tela (enchoicebar), em que são selecionados os títulos a serem baixados de forma automática, na rotina de **Baixa Automática a Pagar (FINA090)**.  
[F090AdBtn - Inclui botões na tela](https://tdn.totvs.com/pages/releaseview.action?pageId=6071398)  
  
**F090ADDB -** O ponto de entrada para adição de rotinas do usuário ao menu do processo de **Baixas** **Automáticas**.  
[F090ADDB - Permite a inclusão de rotinas e botões no menu da rotina FINA090](http://tdn.totvs.com/display/PROT/F090AADD)  
  
**F090ADFR -** Ponto de entrada para manipulação do filtro que seleciona os registros pendentes de **adiantamentos (PA)** e/ou **notas de débito (NDF/DIC)** do fornecedor do título a ser baixado. Para verificação de **PA/NDF/DIC** pendentes e exibição de mensagem na baixa de títulos, é necessário ativar o parâmetro **MV\_VLTITAD**   
[F090ADFR - Manipulação do filtro que seleciona os registros de adiantamentos e/ou notas de débito do fornecedor.](http://tdn.totvs.com/pages/viewpage.action?pageId=60522692)

**F090AFIL -** O ponto de entrada **F090AFIL**inclui uma nova condição no filtro.  
[F090AFIL - Inclui uma nova condicional no filtro](http://tdn.totvs.com/display/PROT/F090AFIL+-+Inclui+uma+nova+condicional+no+filtro)  
  
**F090BROW -** O ponto de entrada **F090BROW** será executado antes da *Mbrowse* da **baixa automática**.  
[F090BROW - Baixa automática](http://tdn.totvs.com/pages/releaseview.action?pageId=6070944)  
  
**F090CHOK -**Ponto de Entrada que permite validar a utilização ou não das **baixas automáticas**. Este Ponto de Entrada é acionado após clicar no botão **OK** da tela **Baixas Automáticas** (tela na qual são selecionados os títulos a serem baixados). Após a validação, o Sistema finaliza o processo de acordo com o retorno do Ponto de Entrada para o *Browse* principal, onde são apresentados todos os títulos da **SE2**.  
[F090CHOK - Valida baixas automáticas](http://tdn.totvs.com/pages/releaseview.action?pageId=6071602)  
  
**F090CPOS -** O ponto de entrada **F090CPOS** tratara os campos que serão apresentados na tela de seleção dos títulos que serão baixados pela **rotina de baixa automatica.  
Parâmetros:** *Array aCampos* contendo dados dos campos que originalmente serão mostrados na tela de seleção de títulos. **Retorno:** *Array* contendo os campos com as alterações customizadas (ordenação dos campos diferentes, campos específicos do cliente, etc)**.**  
[F090CPOS - Tratamento de campos](http://tdn.totvs.com/display/public/mp/F090CPOS+-+Tratamento+de+campos+--+11678)  
  
**F090DESC -** O ponto de entrada **F090DESC** permite informar os descontos para cada título liberado para baixa que foi pago antecipadamente.  
[F090DESC - Concede desconto para cada título liberado para baixa que foi pago antecipadamente.](http://tdn.totvs.com/pages/viewpage.action?pageId=184779033)  
  
**F090FIL - O ponto de entrada F090FIL** será utilizado para filtrar dados para a **baixa automatica****.**  
[F090FIL - Filtro de dados](http://tdn.totvs.com/display/public/mp/F090FIL+-+Filtro+de+dados+--+11679)  
  
**F090FILB - Permite informar uma expressão para filtro dos títulos da tela principal da rotina Baixa Automática a Pagar, para execução em ambiente TopConnect ou CodeBase, de acordo com o RPO utilizado.**[F090FILB - Definir filtro em SQL - FINA090](http://tdn.totvs.com/display/public/mp/F090FILB+-+Defini)  
  
**Saiba mais Pontos de entradas e a Rotina FINA090 do Financeiro.**[Pontos de Entrada - Financeiro - P12](https://tdn.totvs.com/display/PROT/Pontos+de+Entrada+-+Financeiro+-+P12)  
[Baixas Pagar Automática - FINA090 - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=271852126)
