---
article_id: 30818385435671
category: MIDDLEWARE eSocial
content_hash: d05a5be0f095fef3e91629e3aae65c61b1ba20e98f168cfbcdbae2e539280919
fetched_at: '2026-06-28T22:43:05.021294+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Middleware - O que analisar quando o
  evento está com status aguardando retorno
type: support-article
updated_at: '2025-07-25T16:28:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30818385435671-RH-Linha-Protheus-GPE-eSocial-Middleware-O-que-analisar-quando-o-evento-est%C3%A1-com-status-aguardando-retorno
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30818412791447) Tempo aproximado para leitura: **00:02:00min****Dúvida**O que analisar quando o evento está com status aguardando retorno?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa dúvida, avalie se o schedule está configurado realizando os seguintes passos:  
  
1. Acessar o configurador (SIGACFG) e depois o menu Schedule:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820041498903)

2. Para configurar o Agente, clique no Agente, do canto superior esquerdo da página:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820041503127)

Adicionar agentes padrão em outras ações

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820057573911)

Dessa forma, será configurado o agentes padrões do sistema, após isso iniciar o agente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820041507351)

3. Configurar o Agendamento, pelo botão de *Agend.* da parte superior da página:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820041507863)

Para realizar a criação clique em "Novo"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820057576087)

Inclua a rotina de agendamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820041509015)

**Importante:** Cliente irá definir o modelo de execução da schedule do retorno eSocial

Preencher os dados de acordo com o exemplo a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820057577367)

Recorrência:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820041509911)

Incluir configurações de empresas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30820057580439)

A rotina GPEM921B, tem como objetivo consultar os eventos que foram enviados ao RET, e não possui parâmetros.  
Depois de realizar as configurações acima, o resultado e o status de cada execução poderá ser visualizada pelo Monitor dos Agendamentos, logo abaixo de onde foi realizado seu cadastro.  
  
**Informações Complementares:**  
A recorrência do *Schedule*, isto é, a o intervalo de tempo em que será executado, poderá ser ajustado de acordo com a necessidade.  
Após a execução da *schedule* deve ser atualizado o evento no **Monitor**- [Monitor em THF](https://tdn.totvs.com/display/public/PROT/eSocial+do+Futuro+-+Monitor+em+THF)

**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos sobre Middleware](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005445753-MIDDLEWARE-eSocial)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
