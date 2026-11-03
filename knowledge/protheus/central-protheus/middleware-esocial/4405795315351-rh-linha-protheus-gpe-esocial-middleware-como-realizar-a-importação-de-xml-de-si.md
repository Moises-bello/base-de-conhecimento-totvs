---
article_id: 4405795315351
category: MIDDLEWARE eSocial
content_hash: 2ad38ad62c9f43da9e6cc55ecbba9e5258c32861445faf86db0e895697c6dc49
fetched_at: '2026-06-28T22:43:05.004889+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Middleware - Como realizar a importação
  de XML de sistemas terceiros para o Middleware
type: support-article
updated_at: '2025-07-24T20:07:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405795315351-RH-Linha-Protheus-GPE-eSocial-Middleware-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-de-sistemas-terceiros-para-o-Middleware
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25853034355095)**Tempo aproximado para leitura: 00:01:30 min **Dúvida**Como realizar a importação de XML de sistemas terceiros para o Middleware?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
**Solução**Para realizar a importação de XML de sistemas terceiros, existem algumas premissas para migração (Outros produtos para o *Middleware*):

* É necessário todos os **XMLs de Envio e Retorno** gerados em arquivos pelo *software* responsável pelo envios ao eSocial.
* O XML de Envio ao RET deverá ser iniciado pelo **node** principal **<eSocial>**;
* O XML de retorno deverá obrigatoriamente conter o node **<retornoEvento>**e poderá ter os seguintes *paths* até chegar nesse node:  

  - **/eSocial/retornoProcessamentoLoteEventos/retornoEventos**
  - **/evento/retornoEvento**
  - **/eSocial/retornoEvento**
* **Incluir o menu da** rotina **GPEM017D,** veja passo a passo: [RH - Linha Protheus - GPE - eSocial - Middleware - Como criar menu da rotina de Importação de xml de terceiros (GPEM017D)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17964181786135)

1 - Ao clicar na opção **Importação de XML para o Middleware**no Menu do SIGAGPE, será exibido o *browser* abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17964432490263)  
  
2 - Ao utilizarmos o botão **Importar**será apresentado o *Wizard* abaixo, clique em **Avançar**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17964480598807)  
  
3 - Ao clicar em **Avançar**será apresentado no wizard a seguinte tela:

**Diretório:**Nesta opção iremos informar o diretório configurado nas premissas de migração.

**Importar Eventos:** Esta opção irá realizar o envio dos XML's presentes nas pastas para a tabela intermediaria do Middleware (RED).![](https://centraldeatendimento.totvs.com/hc/article_attachments/17964599020055)  
  
4 - Ao fim do processo, clique em Concluir e no browse será exibido as informações de todos os eventos gravados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17964762021783)  
 **Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Boletim Técnico Importação de xml de Terceiros para *Middleware*](https://tdn.totvs.com/pages/releaseview.action?pageId=581861480)  
[RH - eSocial - Middleware](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005445753-RH-ESOCIAL-MIDDLEWARE)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
