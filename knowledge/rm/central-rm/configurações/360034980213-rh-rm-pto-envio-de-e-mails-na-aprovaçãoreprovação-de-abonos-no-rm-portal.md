---
article_id: 360034980213
category: Configurações
content_hash: f8921de41b86dbc765e985cfc89fb8e3c833e5862b550b6913fbe88b1c372ad6
fetched_at: '2026-06-28T22:46:29.913380+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO - Envio de e-mails na aprovação/reprovação de abonos no RM Portal
type: support-article
updated_at: '2026-03-13T15:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034980213-RH-RM-PTO-Envio-de-e-mails-na-aprova%C3%A7%C3%A3o-reprova%C3%A7%C3%A3o-de-abonos-no-RM-Portal
---

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16782226718871) Tempo aproximado para leitura: 00:00:30 min**  
  
**Dúvida**  
Como parametrizar envio de e-mails de aprovação/reprovação de abonos no RM Portal ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.22  
  
**Solução**  
Para parametrizar o envio de e-mails de aprovação/reprovação de abonos no RM Portal, é necessário que a **Nova Gestão de Abonos** esteja **habilitada**. Para informações sobre a nova Gestão de Abono acesse o link abaixo:

[RH - RM - PTO - Nova gestão de abonos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025539653)

Para as configurações do e-mail, siga os passos abaixo no **Automação de Ponto**.

1. Acesse o módulo de **Automação de Ponto**, selecione a guia **Configurações** e clique no menu **Parametrizador,** ao abrir o assistente clique em avançar.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39014915112343)
2. No **Parametrizador**, selecione a opção **RM Portal** e clique em **Avançar**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39014902485015)
3. Selecione o **grupo de quiosque**desejado e clique no botão **Parametrizar**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39014915117975)
4. Avance até a etapa **E-mails** e marque os parâmetros: **Envio de e-mail para o subordinado ao aprovar/reprovar um abono** e **Envio de e-mail para o gestor ao solicitar um abono para aprovação.**  
   ![]()

**Observações**  
Para que a parametrização funcione corretamente, os seguintes cadastros já devem ter sido realizados:

* Cadastro de usuários no sistema
* Associação de usuários a funcionários
* Cadastro de grupo de quiosque (RM Portal)
* Associação do grupo de quiosque aos funcionários
* Associação dos funcionários na estrutura de chefes e supervisores
* Configuração de envio de emails no RM:  
    
  [Framework - Linha RM - Frame - Configurar Envio de E-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001046067-Framework-Linha-RM-Frame-Configurar-Envio-de-E-mail)
