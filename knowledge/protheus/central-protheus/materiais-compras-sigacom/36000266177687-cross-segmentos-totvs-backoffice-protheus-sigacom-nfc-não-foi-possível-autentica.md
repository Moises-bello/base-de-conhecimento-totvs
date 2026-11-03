---
article_id: 36000266177687
category: Materiais - Compras (SIGACOM)
content_hash: d728ec518d1b96ed103a7d2e177d59bdc6c2aabee0ea14a85dbdf6432e451330
fetched_at: '2026-06-28T22:41:21.844664+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Não foi possível
  autenticar no servidor SMTP
type: support-article
updated_at: '2025-11-12T14:08:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36000266177687-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-N%C3%A3o-foi-poss%C3%ADvel-autenticar-no-servidor-SMTP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35999886383767) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao enviar proposta da cotação via Workflow para o email do fornecedor, é gerado o erro " Não foi possível autenticar no servidor SMTP ", como corrigir?

Caixa de email alterada - Encontrado o(s) seguinte(s) problema(s): Não foi possível autenticar no servidor SMTP - Valide as configurações de usuário e senha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35999507047319)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2310  
  
**Solução**  
Verifique como está preenchido o parâmetro **MV\_PGCWF****.**

Se estiver**habilitado,**execute novamente o WIZARD do COMPRADOR revisando todas as informações que estão sendo utilizadas. Para executar o Wizard do Comprador deve logar no Protheus com o usuário do comprador. É obrigatório que o email esteja preenchido no cadastro do usuário. Para maiores informações, siga procedimento da documentação abaixo.

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow utilizando o e-mail dos compradores no envio dos formulários no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19837259521559-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-utilizando-o-e-mail-dos-compradores-no-envio-dos-formul%C3%A1rios-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

Se estiver**desabilitado,**abra o cadastro da **Conta de Email**que irá utilizar para o envio do Workflow e revise todas as informações preenchidas se estão corretas. Segue abaixo documentação que mostra configuração usando Gmail e Outlook como provedores.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como configurar o Workflow do NFC em Outlook?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35802504484887-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-configurar-o-Workflow-do-NFC-em-Outlook)

Além disso, informe o NOME da Conta de Email no parâmetro MV\_WFMLBOX. Verificar se o parâmetro MV\_WFMLBOX está preenchido com o nome da caixa de email que foi cadastrada através do configurador, na rotina Contas de Email, o conteúdo do parâmetro deve ser igual a informação que consta no campo "Cx Correio".

**Observações**

Obs1. Atualmente a maioria dos provedores SMTP utilizam uma porta diferente da padrão, geralmente usam a 465 ou 587.

Obs2. O Gmail utiliza a porta 465 quando a segurança utilizada é a SSL e a porta 587 quando a segurança é a TLS.

Obs3. Para maiores informações consulte a documentação [**Configurar o SMTP para envio de relatórios por e-mail;**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=271166884)

**Obs4. Atualmente não existe a possibilidade de usar um email do Workflow específico para o Novo Fluxo de Compras. A Conta de Email que for informada no parâmetro****MV\_WFMLBOX será usada para todos os envios feitos pelo workflow de todas as rotinas e módulos. Porém temos uma melhoria sendo desenvolvida com previsão de entrega para 17/11.**

***Saiba Mais:***

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow utilizando o e-mail dos compradores no envio dos formulários no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19837259521559-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-utilizando-o-e-mail-dos-compradores-no-envio-dos-formul%C3%A1rios-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)
