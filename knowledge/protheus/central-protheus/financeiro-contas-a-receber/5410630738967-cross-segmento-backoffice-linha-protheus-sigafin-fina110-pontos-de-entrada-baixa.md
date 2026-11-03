---
article_id: 5410630738967
category: Financeiro - Contas a Receber
content_hash: b3125a330fd2d15f74e04c04c61e829b1909717abdd793d3c16b2da3458a1bf1
fetched_at: '2026-06-28T22:38:12.813397+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA110 - Pontos de
  Entrada Baixas Automáticas
type: support-article
updated_at: '2025-06-23T18:23:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5410630738967-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA110-Pontos-de-Entrada-Baixas-Autom%C3%A1ticas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28275401193751)** Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Quais pontos de entrada disponíveis para a rotina de baixas automáticas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA110 - A partir da versão 11.80  
  
**Solução**Segue abaixo a relação dos **pontos de entrada** da rotina **FINA110:**

**F110BOR** Verifica se o borderô pode ser baixado ou não, e será chamado na função F110BxBord().

<http://tdn.totvs.com/pages/releaseview.action?pageId=6070955>  
  
**F110BROW** Antes da Mbrowse validando previamente os dados a serem exibidos.

<http://tdn.totvs.com/pages/releaseview.action?pageId=6070956>  
  
**F110BtOK** Confirmação da tela em que são selecionados os títulos a receber para baixa.

<http://tdn.totvs.com/pages/releaseview.action?pageId=6070957>  
  
**F110CPOS** Alteração de exibição dos campos a serem exibidos na baixa a receber aut.

<http://tdn.totvs.com/pages/viewpage.action?pageId=152800281>  
  
**F110FIL** Será utilizado como chave de filtro complementar para Indregua ou SQL.

<http://tdn.totvs.com/display/PROT/F110FIL+-+Chave+de+Filtro+--+11692>  
  
**F110REC** Gera recibo de títulos baixados automaticamente no contas a receber.

<http://tdn.totvs.com/pages/viewpage.action?pageId=46072592>  
  
**F110SE5** Manipulação de títulos processados na tabela SE5  
<http://tdn.totvs.com/pages/viewpage.action?pageId=146965587>  
  
**F110TIT** Marca e desmarca item para baixa   
<http://tdn.totvs.com/display/public/mp/F110TIT+-+Marca+e+desmarca+item+para+baixa+--+11693>  
  
**F110TOK** Validação de dados da baixa   
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070960>

**10BUT:** Inclui botão

<https://tdn.totvs.com/pages/releaseview.action?pageId=6071168>

**F110QRCP** - Substitui a query de busca de títulos a serem baixados teste

<https://tdn.totvs.com/pages/releaseview.action?pageId=634829628>

**FCalDesc** - Desconto na baixa automática

<https://tdn.totvs.com/pages/releaseview.action?pageId=184778942>

**FA110DES -** Calcula desconto

<https://tdn.totvs.com/display/public/mp/FA110DES+-+Calcula+desconto+--+11934>

**FA110JUR** - Calcula juros

<https://tdn.totvs.com/display/public/mp/FA110JUR+-+Calcula+juros+--+11935>

**FA110MUL** - Cálculo de multa

<https://tdn.totvs.com/pages/releaseview.action?pageId=6071171>

**FA110SE5** - Baixa a receber automática

<https://tdn.totvs.com/pages/releaseview.action?pageId=6071172>

**FA110TOT** - Gravação de dados complementares ao registro totalizador

<https://tdn.totvs.com/pages/releaseview.action?pageId=184779993>

**Saiba Mais**<https://tdn.totvs.com/pages/viewpage.action?pageId=389547437>
