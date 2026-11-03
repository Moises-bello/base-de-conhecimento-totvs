---
article_id: 16971369176855
category: MIDDLEWARE eSocial
content_hash: 3f5f5d465c63927e435d1f553069e65ca2e87f2f2c888bc23eecfb612a4a6e2e
fetched_at: '2026-06-28T22:43:05.038160+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Middleware - S-3000 - Como realizar a
  exclusão de eventos no Middleware
type: support-article
updated_at: '2024-11-01T21:54:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16971369176855-RH-Linha-Protheus-GPE-eSocial-Middleware-S-3000-Como-realizar-a-exclus%C3%A3o-de-eventos-no-Middleware
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16971383063063) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como realizar a exclusão de eventos no *Middleware*?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

A Rotina de **Exclusão de Eventos GPEM922** foi disponibilizada para efetuar a exclusão e geração do evento S-3000 de eventos que não possuem esta opção a partir das rotinas geradoras do SIGAGPE.  
  
São exibidos em tela os registros existentes na fila de Eventos do *Middleware* (RJE), com **status diferente de 2** - **Aguardando Retorno**, em formato *check-box* para seleção.  
  
Ao processar os eventos selecionados com status 4, será gerado um evento de exclusão S-3000; Caso o evento possua status 1 ou 3, será excluído da fila de eventos.  
  
**Eventos processados pela rotina:**

* **Não periódicos:**S-2190, S-2200, S-2205, S-2206, S-2210, S-2220, S-2240, S-2250, S-2260, S-2298, S-2300, S-2306.
* **Periódicos:**S-1200 e S-1210, apenas com status 1 ou 3 (Eventos com status 4 devem ser processados pela rotina de envio dos periódicos).

Caso ainda não exista a rotina no menu do ambiente, será necessário criá-lo manualmente ou atualizar os menus do sistema.   
Para criar manualmente acesse o *link*: <https://tdn.totvs.com/pages/viewpage.action?pageId=551449314>  
Se necessário atualizar os menus, acesse o *link* a seguir para baixar de acordo com o *release*: <https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/menus>   
  
Ao acessar a rotina de exclusão, a tela abaixo será exibida (miscelânea - eSocial - *Middleware* - Exclusão de Eventos):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16971245310487)

Existem validações que garantem o funcionamento correto do modulo, como por exemplo, caso o parâmetro MV\_MID estiver configurado como .F., ou seja, o modulo do *Middleware* não esta ativo, será apresentada a mensagem abaixo:

![](https://tdn.totvs.com/download/attachments/551449314/image2020-6-4_14-51-7.png?version=1&modificationDate=1591295184230&api=v2)

Outra validação é a existência da tabela RJE (Fila Eventos eSocial), caso não exista, a mensagem abaixo é exibida:

![](https://tdn.totvs.com/download/attachments/551449314/image2020-6-4_14-56-34.png?version=1&modificationDate=1591295184197&api=v2)

No exemplo abaixo vamos solicitar a exclusão de um registro do evento S-1200 que esta com o status de "Pendente de Envio" e um registro do evento S-2200 que já foi processado e validado no RET:

![](https://tdn.totvs.com/download/attachments/551449314/image2020-6-4_15-19-5.png?version=1&modificationDate=1591295184003&api=v2)

Veja que o registro referente ao evento S-1200 foi excluído e para o registro S-2200, gerou um registro S-3000 na tabela RJE:

![](https://tdn.totvs.com/download/attachments/551449314/image2020-6-4_15-23-29.png?version=1&modificationDate=1591295183963&api=v2)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[Boletim Técnico Exclusão - Middleware](https://tdn.totvs.com/pages/viewpage.action?pageId=551449314)  
[Artigos sobre Middleware](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005445753-MIDDLEWARE-eSocial)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".*
