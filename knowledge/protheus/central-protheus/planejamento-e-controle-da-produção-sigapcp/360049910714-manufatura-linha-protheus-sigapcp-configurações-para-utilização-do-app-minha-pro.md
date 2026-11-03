---
article_id: 360049910714
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9a2bb6f4412dd146c611c0d4e5bdb21b540e5fec9a56e61cc6972648fb51b548
fetched_at: '2026-06-28T22:42:42.115680+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Configurações para utilização do APP
  Minha Produção
type: support-article
updated_at: '2026-04-20T15:47:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049910714-Manufatura-Linha-Protheus-SIGAPCP-Configura%C3%A7%C3%B5es-para-utiliza%C3%A7%C3%A3o-do-APP-Minha-Produ%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17128462590103)** Tempo aproximado para leitura: **00:01:55 min**  
  
**Dúvida**  
Quais configurações devem ser realizadas para a utilização do **App Minha Produção**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O aplicativo *mobile* **Minha Produção** possibilita a realização de apontamento de produção.  
  
Para configuração realize os seguintes passos:  
  
1 - Configurar o serviço **Rest** do **Protheus** para consulta e sincronização das informações, informando **Empresa** e **Filial** na cláusula **PrepareIn**, através da qual deve ocorrer a conexão;  
  
2 - Baixar e instalar o aplicativo de nome **Minha Produção** em seu dispositivo móvel pelo **Google Play Store**. O aplicativo está disponível para **Smartphone** com **Android** a partir da **versão 5.0**;  
  
3 - **Usuário** e **senha** válidos para um ambiente **Protheus**.  
  
4 - Criação de um **alias** no **TOTVS Mingle**, a plataforma que redireciona as requisições do *app* para o produto. Para solicitar a criação do **alias**, acesse o endereço: [TOTVS Mingle](https://mingle.totvs.com.br/landpage/), informe *e-mail*, selecione o **App Minha Produção**, defina o *backend* como **Protheus**, informe a **empresa** e a **filial**, a mesma para a qual foi configurado o serviço **Rest**, o **endereço/porta** do servidor *rest* e o nome do servidor.  
  
5 - No primeiro acesso do aplicativo **Minha Produção**, após exibir a tela de apresentação e o termo de aceite, será apresentada a tela de **Configurações Avançadas**, onde será informado o modo de conexão, que deverá ser igual a **Mingle**; o produto, que deverá ser igual a **Protheus** e; o **alias** de acesso ao **TOTVS** **Mingle**. A partir deste momento, estará disponível o acesso à tela de *login* do usuário.  
  
**Importante**  
Para cada **empresa/filial** deverá ser solicitado um **alias** no **TOTVS Mingle**.  
  
**Saiba mais**  
Para mais detalhes sobre o aplicativo, consulte nossa documentação no **TDN - TOTVS Developer Network**, conforme os *links*:   
[REST com ERP Microsiga Protheus](https://tdn.totvs.com/display/framework/02.+REST+com+ERP+Microsiga+Protheus)  
[Configuração REST](https://tdn.totvs.com/pages/viewpage.action?pageId=185747842)  
[Guia de uso – Minha Produção](https://tdn.totvs.com/pages/releaseview.action?pageId=606095034#tudo-sobre-funcionalidades-interfaces-Linha-Protheus)
