---
article_id: 360051016354
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 94e073530b8fbed6c39a12409f8fa89acba7a23fa5c50a02ea2a02813d5ef429
fetched_at: '2026-06-28T22:42:47.104581+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Utilização de Gatilhos no APP Minha
  Produção
type: support-article
updated_at: '2024-06-27T13:31:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051016354-Manufatura-Linha-Protheus-SIGAPCP-Utiliza%C3%A7%C3%A3o-de-Gatilhos-no-APP-Minha-Produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24473067476503)***Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**É possível utilizar gatilhos para preenchimento de campos baseados na ação de outro campo no **APP Minha Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
No **Protheus** existe o recurso de se preencher campos baseados na ação de outro campo e isso pode ser feito sem a necessidade de criar ou alterar rotinas existentes.  
Porém, no aplicativo **mobile Minha Produção**, a comunicação entre essa aplicação e o **Protheus** é realizado através de **APIs- Application Programming Interface**, onde:  
  
1 – O **APP Minha Produção** executa a **API** do **Cadastro de formulários - FormRegistration**, buscando os formulários cadastrados no **Protheus** para o usuário.  
  
2 – É realizada a digitação das informações do apontamento de produção no **APP Minha Produção**. Nesse momento, é chamada a **API** de **Apontamento de produção - ProductionAppointment** para efetuar as consistências dos campos digitados no **APP Minha Produção** e o envio, via **MsExecAuto**, para o respectivo programa de apontamento de produção, que poderá ser **MATA250 - Produção Simples** ou **MATA681 - Produção PCP MOD2**.  
  
**Importante**  
Como a comunicação entre o **APP Minha Produção** e o **Protheus** é realizada via **API** somente após a confirmação do apontamento, não é possível executar os gatilhos de cada um dos campos.  
  
**Saiba mais**  
Para mais detalhes sobre o aplicativo consulte nossa documentação no **TDN** conforme o *link*:   
[Guia de uso – Minha Produção](https://tdn.totvs.com/pages/releaseview.action?pageId=606095034#tudo-sobre-funcionalidades-interfaces-Linha-Protheus)
