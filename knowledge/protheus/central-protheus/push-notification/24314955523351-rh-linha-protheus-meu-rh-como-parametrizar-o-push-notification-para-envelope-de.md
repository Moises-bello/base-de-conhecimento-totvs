---
article_id: 24314955523351
category: PUSH NOTIFICATION
content_hash: 306b2af86db2df4807a481feec335e58da53c5fbd1f8e97c4be9b5d2a31987f1
fetched_at: '2026-06-28T22:44:31.025599+00:00'
product: protheus
section_id: 24317079332887
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como parametrizar o Push Notification para Envelope
  de Pagamento no Meu RH
type: support-article
updated_at: '2025-07-29T11:50:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24314955523351-RH-Linha-Protheus-Meu-RH-Como-parametrizar-o-Push-Notification-para-Envelope-de-Pagamento-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24314930800151) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como parametrizar o ***Push Notification*** no Meu RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Para realizar a parametrização e utilizar a nova **funcionalidade** ***Push Notification**,* para informar a disponibilidade do Envelope de Pagamento, é preciso que os aplicativos nos celulares, estejam **obrigatoriamente** na versão **3.1.13** ou superior.  
  
É preciso garantir que o sistema esteja atualizado com o ultimo **pacote [acumulado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282-RH-Linha-Protheus-MEU-RH-Pacote-de-acumulado-do-RH-no-Portal-de-Cliente) do RH,** e realizar o Procedimento de Atualização do Dicionário e Base de Dados (**UPDDISTR**).  
  
Como os menus oficiais dessa funcionalidade estarão disponíveis apenas na nova *release* **(12.1.2410),** para as *releases* anteriores deverá ser **[criado os menus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035446693-Framework-Linha-Protheus-Como-incluir-e-utilizar-menus-customizados-com-o-dicion%C3%A1rio-no-banco-de-dados)** de forma manual.   
Para isso, necessário informar as rotinas **TCFA160** (Gatilho Envelope de Pagamento), **TCFA150** (Tipos de Notificação) e **TCFA170** (Visualização e Exclusão de *Tokens*/*Push*).  
  
Abaixo temos o exemplo de como informar a rotina **TCFA170** no menu:  
  
Acesse o módulo **SIGACFG > Ambiente > Cadastros > Menus > Selecione o Menu e clique em OK**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24314930802583)  
  
Informe o programa (rotina) e o módulo que utilizará a rotina e clique em OK  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24314930805655)  
  
Após confirmação de que os menus estão acessíveis e funcionais no sistema, quando os colaboradores acessarem o App Meu RH no *smartphone*, será registrado na tabela **RUY** os ***tokens*** de acesso para onde serão direcionados as notificações *push*:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24314930807831)  
  
Acesse a rotina **TCFA160** (Gatilho Envelope de Pagamento) e parametrize para o envio das notificações:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24314930809751)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24314955496343)  
  
Após execução da rotina será gerado o *log* de envio:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24314930814871)  
  
A notificação ***Push*** será exibida no *smartphone* dos colaboradores:  
![unnamed.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24314955501719)

**Saiba Mais:**

[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)

[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
