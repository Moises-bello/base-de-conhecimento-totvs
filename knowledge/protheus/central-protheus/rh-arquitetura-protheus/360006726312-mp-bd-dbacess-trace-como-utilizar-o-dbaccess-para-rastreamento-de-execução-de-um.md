---
article_id: 360006726312
category: RH - Arquitetura Protheus
content_hash: 2ef7557f7a308f823e962c3bb7d9efd7f0d4d248820d1b243f3b803b9ff80c8d
fetched_at: '2026-06-28T22:43:03.243053+00:00'
product: protheus
section_id: 206960847
source: central-protheus
title: MP - BD - DBACESS - TRACE - Como utilizar o DBACCESS para rastreamento de execução
  de uma rotina
type: support-article
updated_at: '2021-07-30T19:34:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006726312-MP-BD-DBACESS-TRACE-Como-utilizar-o-DBACCESS-para-rastreamento-de-execu%C3%A7%C3%A3o-de-uma-rotina
---

**Dúvida**Como gerar o Trace através do *DbAccess*?  
  
**Ambiente**  
Protheus – Arquitetura Protheus – A partir da versão 11.80  
  
**Solução**O *DBACESS* pode ser uma ótima ferramenta para utilização de rastreamento de rotinas que estão sendo executadas, o mesmo gera um *log* gravando estas informações e tais podem ser utilizadas para auxiliar na descoberta e correção de erros, uma vez que, além de mencionar tabelas, este *log* gera os *select's*que poderão ser utilizados para filtro no próprio banco de dados.  
Para utilizar o ***DBACESS*** para rastreamento de execução de uma determinada rotina, siga os seguintes passos:  
  
1. Acesse o sistema no SIGAGPE ou SIGAPON por exemplo, e abra a rotina que será rastreada. Neste exemplo será executado o *log* para o cálculo da **folha de pagamento;**2. Execute o ***DBMonitor*** que fica dentro da pasta ***DbAccess***, normalmente instalado no C: do servidor e faça a limpeza das mensagens gravadas anteriormente. Para isso, acesse a aba Mensagens e clique em Limpar;

![](http://tdn.totvs.com/download/attachments/240308476/image2016-6-24%209%3A21%3A48.png?version=1&modificationDate=1466767455000&api=v2)  
  
3. Selecione a aba **Usuários** e clique sobre a opção que mostra a rotina que está aberta no momento e que será rastreada, neste caso o **GPEM020**, e clique em **Rastrear;**

![](http://tdn.totvs.com/download/attachments/240308476/image2016-6-24%209%3A22%3A56.png?version=1&modificationDate=1466767456000&api=v2)

4. O Sistema dará início ao rastreamento da rotina, então, execute a rotina para que sejam gravados os dados no Trace, deixe executar por um tempo razoável;

![](http://tdn.totvs.com/download/attachments/240308476/image2016-6-24%209%3A34%3A58.png?version=1&modificationDate=1466768124000&api=v2)![](http://tdn.totvs.com/download/attachments/240308476/image2016-6-24%209%3A35%3A10.png?version=1&modificationDate=1466768137000&api=v2)

5. Após executar por um tempo, acesse novamente o ***DBMonitor*** onde será apresentada uma tela para **salvar** o *log* de execução;

![](http://tdn.totvs.com/download/attachments/240308476/image2016-6-24%209%3A35%3A57.png?version=1&modificationDate=1466768183000&api=v2)![](http://tdn.totvs.com/download/attachments/240308476/image2016-6-24%209%3A36%3A6.png?version=1&modificationDate=1466768192000&api=v2) 

**Saiba mais**[MP - BD0034 - DBACESS - TRACE - Como utilizar o DBACCESS para rastreamento de execução rotina?](http://tdn.totvs.com/pages/viewpage.action?pageId=240308476)
