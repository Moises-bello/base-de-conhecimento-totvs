---
article_id: 4416988799639
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 90d74a2d4edd95ee080897b14965fd19c977144c381cc4026a64617631557acc
fetched_at: '2026-06-28T22:39:31.170058+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: MP - FIS - GNRE - ERROR.LOG Variable does not exist F6_DOCAEST
type: support-article
updated_at: '2021-12-24T14:55:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416988799639-MP-FIS-GNRE-ERROR-LOG-Variable-does-not-exist-F6-DOCAEST
---

**Dúvida**

Ao acessar a rotina Guia Nacional de Recolhimento é apresentado o error.log abaixo:  
  
THREAD ERROR ([15852], helio.goncalves) 24/12/2021 10:53:57  
variable does not exist F6\_DOCAEST on { ||F6\_DOCAEST}(FWMBROWSE.PRW) 12/06/2020 18:03:25 line : 1872  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - 12  
  
**Solução**Para solucionar o error.log mencionado neste artigo, será  necessário verificar se o campo F6\_DOCAEST existe na estrutura SX3.  
  
Como sugestão de consulta, poderá executar no banco de dados a query conforme abaixo para identificar se o campo existe na estrutura SX3:

SELECT F6\_DOCAEST, \* FROM SF6

Esse problema geralmente é ocasionado quando é executado o dicionário de dados somente no ambiente de homologação e copiado apenas a estrutura SX3 para o ambiente de produção.   
  
O correto a ser feito é executar a atualização do dicionário de dados contido nos links referente a Expedição Continua do módulo - FISCAL para que não só o campo F6\_DOCAEST, mas todos os campos da tabela SF6 sejam criados corretamente na estrutura SX3 e no banco de dados.

O link referente a expedição continua poderá ser baixado através do portal do cliente utilizando o caminho abaixo:

1-Acessar o site: suporte.totvs.com.br

2-Clicar em Downloads

3-Em Atualizações e Downloas, selecione no Campo "Outras Linhas de Produto" a opção "Totvs Linha Protheus"

4-Selecione a release correspondente ao seu ambiente

5-Atualizações Periódicas

6-Selecione e baixe o link correspondente ao seu ambiente.
