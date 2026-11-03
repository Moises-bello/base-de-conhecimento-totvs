---
article_id: 9069943725847
category: MIDDLEWARE eSocial
content_hash: 936acc3c3b862079770e6b5bd1f784875ab29b0699550ba048c3f6c79581d0fb
fetched_at: '2026-06-28T22:43:04.962746+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Middleware - Como configurar o Schedule
  para envio dos eventos no Middleware GPEM921A()
type: support-article
updated_at: '2025-10-29T18:25:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9069943725847-RH-Linha-Protheus-GPE-eSocial-Middleware-Como-configurar-o-Schedule-para-envio-dos-eventos-no-Middleware-GPEM921A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25244428991127) Tempo aproximado para leitura: **00****:05:00 min****Dúvida**Como configurar o *Schedule* no *Middleware* para envio dos eventos ao RET/Governo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Dentre as configurações iniciais do *Middleware*, está a configuração do serviço que irá enviar os eventos automaticamente para o RET **GPEM921A()**. Para configurá-lo corretamente, basta seguir os passos descritos abaixo:  
  
Lembrando que a rotina **GPEM921A()** é completamente opcional.  
1. Acessar o configurador (**SIGACFG**) e depois o menu **Ambiente ->** ***Schedule -> Schedule***:

![image2020-3-25_14-30-12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069035483415)  
  
2. Na pasta *Schedule*, iniciar todos os serviços pelo primeiro botão de *play*:  
![image2020-3-25_14-52-3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069080552983)  
  
  
3. Configurar o ***Agent***, para isso basta clicar no globo verde, do canto superior direito da página:  
![image2020-3-25_14-58-50.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069453341207)  
  
4. Na parte inferior, é possível ajustar as configurações de acordo com o ambiente a ser utilizado:  
![image2020-3-25_15-2-3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069488334231)  
  
5. Configurar o **Agendamento**, pelo botão de **+** na sessão de **Detalhes**, da parte inferior da página:  
![image2020-3-25_15-7-52.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069491960599)  
  
6. Basta preencher os dados de acordo com o exemplo a seguir:  
![image2020-3-25_15-12-21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069512468631)

**IMPORTANTE**Ao selecionar Empresa/Filial durante a configuração do *JOB* deve-se selecionar apenas as filiais que são matriz, ou seja, as filais que estiverem informadas na rotina de cadastro do empregador (GPEA935).  
  
7. Configurar a recorrência conforme necessidade da empresa:  
![image2020-3-25_17-21-11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9069565951255)  
  
A rotina **GPEM921A()**, tem como objetivo transmitir os eventos da tabela **RJE** para o **RET** e possui 2 parâmetros que devem ser informados dentro dos parênteses **()**:  
  
**Parâmetro 1**- Competência (formato **AAAAMM**). Indica se deve considerar somente eventos gerados na competência indicada. Caso não seja informado, serão considerados todos os eventos com status em branco.  
  
**Parâmetro 2**- Dias de corte. Indica se deve ignorar eventos que estão na fila a mais de X dias (de acordo com o informado), e estão com status branco ou com erro (gerados indevidamente e ainda não foram excluídos).  
  
Depois de realizar as configurações acima, o resultado e o status de cada execução poderá ser visualizada pelo **Monitor** dos **Agendamentos,** logo abaixo de onde foi realizado seu cadastro.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Como identificar a versão do TSS utilizada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000610667-Cross-Segmentos-TOTVS-Backoffice-Linha-RM-Doc-Eletr%C3%B4nicos-Como-identificar-a-vers%C3%A3o-do-TSS-utilizada)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[Agenda de Eventos Tira Dúvidas Suporte](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-01-2023-retificada-em-20230124.pdf)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
