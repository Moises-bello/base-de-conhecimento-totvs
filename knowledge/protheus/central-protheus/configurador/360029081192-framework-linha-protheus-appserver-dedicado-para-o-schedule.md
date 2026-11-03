---
article_id: 360029081192
category: Configurador
content_hash: 3fbc74c7631c2d99a16a2d8bf915c6ed4716ef92e8ce41dbe3694cfd2238417b
fetched_at: '2026-06-28T22:42:18.918866+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - AppServer dedicado para o Schedule
type: support-article
updated_at: '2024-05-08T11:34:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029081192-Framework-Linha-Protheus-AppServer-dedicado-para-o-Schedule
---

**Dúvida**  
Como fazer para configurar uma instância do AppServer dedicada ao schedule?  
  
**Ambiente**  
Protheus - Configurador - Todas as versões  
  
**Solução**  
Segue abaixo procedimento para criar AppServer dedicado ao serviço de Schedule:  
  
1. Pare todos os serviços do Protheus (Servidor de Aplicação, Servidor de Licenças, DBAccess, Ctree, etc)  
2. Faça uma cópia da pasta Appserver (Ex.: appserver\_sched)  
3. Nesta nova pasta, abra o arquivo appserver.ini e altere a porta da seção [TCP] para uma nova porta  
4. Se for iniciar este Appserver como um Serviço, altere o nome do serviço na seção [Service] (tanto o Name= quanto o DisplayName=)  
5. Abra o arquivo smartclient.ini (da pasta do SmartClient), e adicione uma seção TCP para que possa selecioná-la ao abrir o Smartclient, quando quiser conectar no AppServer dedicado ao Schedule. Abaixo um exemplo de smartclient.ini com conexão TCP para a base principal e a base do Schedule:

```
[config]  
lastmainprog=SIGACFG,SIGAADV,SIGAMDI,APSDU  
envserver=P12LG  
  
[drivers]  
active=TCP,TCP-SCHED  
  
[TCP]  
server=localhost  
port=1223  
  
[TCP-SCHED]  
server=localhost  
port=1233
```

6. Após estas configurações, reinicie todos os serviços do Protheus, e acesse o Configurador pelo SmartClient, acessando pelo TCP-SCHED, e faça as configurações de agendamento necessárias.  
  
![2019-06-11_1055.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030708832)  
  
**Importante**  
Documentação completa do Schedule:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=271167961>
