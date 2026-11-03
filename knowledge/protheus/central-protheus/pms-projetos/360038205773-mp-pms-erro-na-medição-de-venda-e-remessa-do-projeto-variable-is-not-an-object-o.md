---
article_id: 360038205773
category: PMS - Projetos
content_hash: 7d9cf46a70662e6136f9124b1767a941dfbcd92e914277d8bdff731a3615417c
fetched_at: '2026-06-28T22:37:15.049248+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: 'MP-PMS-Erro na medição de venda e remessa do projeto: variable is not an object  on
  {|| Pms600Change(cArquivo,@nTotal,@nQuant)'
type: support-article
updated_at: '2021-04-29T21:13:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038205773-MP-PMS-Erro-na-medi%C3%A7%C3%A3o-de-venda-e-remessa-do-projeto-variable-is-not-an-object-on-Pms600Change-cArquivo-nTotal-nQuant
---

**Ocorrência**

Ao efetuar a medição de venda e remessa de um projeto, gera o erro:

**variable is not an object on {|| Pms600Change(cArquivo,@nTotal,@nQuant) , nPercFat:=0, nQuantFat:=0, nValFat:=0, oGetTot:Refresh(), oPercFat:Refresh(), oGetQtde:Refresh(), oValFat:Refresh() }(PMSA600.PRW) 08/03/2017 10:07:12 line : 410**

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O erro era ocasionado devido a uma inconsistência no binário (APPSERVER).

**Solução**

A correção foi efetuada na issue **mtec**-**3334**, todavia ao associar esta correção ao ticket do cliente está recebendo a  seguinte mensagem do desenvolvimento:

A Release Oficial 13.2.3.48 foi expedida e publicada na Central de Downloads.  
O pacote pode ser acessado no endereço: **[https://suporte.totvs.com](https://suporte.totvs.com/),** seção de Downloads.

Não esqueça de responder a nossa Pesquisa de Satisfação para melhor atendê-lo.

**Ou seja, a indicação é para efetuar o download do appserver versão 13.2.3.48 no portal do cliente, conforme abaixo:**  
1. Efetue o download do último **APPSERVER** com versão igual ou acima a 13.2.3.48 na central de dowloads:

APPSERVER VERSAO 12 WINDOWS 13.2.3.48 ATÉ A RELEASE 12.1.17 -  <https://suporte.totvs.com/portal/p/10098/download?e=761039#detail/657319>

APPSERVER VERSAO 12 LINUX 13.2.3.48 ATÉ A RELEASE 12.1.17 -

<https://suporte.totvs.com/portal/p/10098/download?e=761039#detail/657318>

2. Atualize o APPServer do seu ambiente .

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
