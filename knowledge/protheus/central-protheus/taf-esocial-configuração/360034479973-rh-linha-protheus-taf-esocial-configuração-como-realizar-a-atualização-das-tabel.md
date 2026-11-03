---
article_id: 360034479973
category: TAF - eSocial - Configuração
content_hash: 2d75811978ed249d77ce31c34622edf734b3fa27f7cfc00d7cc5c5aa50e4b377
fetched_at: '2026-06-28T22:45:14.384490+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como realizar a atualização
  das tabelas autocontidas.
type: support-article
updated_at: '2026-06-23T20:43:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-realizar-a-atualiza%C3%A7%C3%A3o-das-tabelas-autocontidas
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25309910809367)* Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como realizar a atualização das tabelas autocontidas.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões  
  
**Solução**1 - Para realizar o procedimento da Atualização das Tabelas Autocontidas, pare o serviço TAF-WS:  
[Como parar o serviço TAF-WS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036631673)  
**Obs.:** Quem for PROTHEUS e não tiver a **WebService** configurada, pode ir para o próximo procedimento!  
  
2 - Acesse o configurador (**SIGACFG**):  
[Como acessar o configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036108413)  
  
3 - Acesse os parâmetros do sistema (Ambiente > Cadastros > Parâmetros) e procure pelo parâmetro **MV\_VAUTCON**;  
[Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233)  
  
4 - Ao editar o parâmetro **MV\_VAUTCON**, e deixe o campo vazio:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25309936609175)  
  
5 - Procure outro parâmetro **MV\_TAFWIZ** e certifique que esteja com o valor de **.T.**, se não estiver com este valor, altere-o:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25309936610967)  
  
6 - Acesse o **SIGATAF** e em seguida será exibido a tela abaixo:

![8.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044647033)  
Clique em **Avançar**:  
  
7 - Marque a caixa de seleção do "*status* autocontidas", para cada grupo de empresa que aparecer: **NÃO Atualizada:**![9.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043779574)  
Clique em **avançar**;8 - Na tela à seguir selecione as opções conforme imagem:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100925553)  
Clique em **avançar**;  
  
9 - Se o seu ambiente for **Protheus** e selecionou a opção **Layout TOTVS ou Tabela Compartilhada no SGBD (Importação de arquivos ou integração via ODBC)** preencha os campos abaixo com as informações que constam no arquivo de configuração **appserver.ini** localizado na pasta **(bin/appserver)** e procure a seção **[DBACCESS] ou [TOPCONNECT]**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086952414)  
Clique em **avançar**;  
  
10 - Se o seu ambiente for **RM/DATASUL** e selecionou a opção **Layout TOTVS ou Web Service (Importação de arquivos ou integração via WS)** preencha os campos abaixo com as informações que constam no arquivo de configuração **appserver.ini** localizado na pasta **(bin/app)** e procure a seção**[HTTPREST]**:

![11.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044647053)  
Clique em **avançar**;  
  
11 - Clique em **Processar as configurações realizadas neste assistente...** para inicializar a atualização das tabelas autocontidas:

![12.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044647073)  
  
12 - Após terminar o processo, clique em **Finalizar**:

![13.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043779614)  
  
13 - Se tiver o serviço TAF-WS parado, reinicialize o mesmo.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
