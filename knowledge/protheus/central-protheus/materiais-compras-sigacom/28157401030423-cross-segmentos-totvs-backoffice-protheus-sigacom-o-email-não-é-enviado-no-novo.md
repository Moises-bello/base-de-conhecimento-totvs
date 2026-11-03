---
article_id: 28157401030423
category: Materiais - Compras (SIGACOM)
content_hash: d65811229380b413adb5dd2c96129c347c16c416fabfbc82f3133998939efa63
fetched_at: '2026-06-28T22:41:10.096856+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O email não é enviado
  no Novo Fluxo de Compras.
type: support-article
updated_at: '2025-08-18T20:30:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28157401030423-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-email-n%C3%A3o-%C3%A9-enviado-no-Novo-Fluxo-de-Compras
---

**Dúvida**Ao utilizar o Novo Fluxo de Compras é exibida a mensagem que o email foi enviado com sucesso, porém o mesmo não chega ao destinatário. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28157674620311)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12.

**Solução**

**Procedimento para Identificação e Resolução de Problemas.**

O parâmetro **MV\_WFSNDAU** é fundamental no processo de envio automático do Workflow.

* **Acesse o Configurador**:
  + Menu → Ambiente → Configurações → Configurador.
* **Pesquise o parâmetro**:
  + Na aba "Parâmetros", busque por **MV\_WFSNDAU**.
* **Verifique o valor atual**:
  + Certifique-se de que o valor está configurado como **.T.**
* **Caso necessário, ajuste o valor**:
  + Alterne para **.T.** e salve as alterações.
* **Realize testes no Workflow**:
  + Execute um teste para confirmar se o envio automático está funcionando corretamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28157617104151)

2 - Verificar se o parâmetro MV\_WFMLBOX está preenchido com o nome da caixa de email que foi cadastrada através do configurador, na rotina Contas de Email, o conteúdo do parâmetro deve ser igual a informação que consta no campo "Cx Correio".

3 - Se o ajuste do parâmetro **MV\_WFSNDAU** para **".T."** não resolver o problema, o próximo passo é realizar um teste detalhado usando a rotina **WFTEST**.

[WFTEST - Teste envio de Workflow](https://tdn.totvs.com/display/public/PROT/WFTEST)

Caso ocorra o erro **CANNOT FIND METHOD** durante a execução da rotina **WFTEST**, deverá ser aplicada a atualização abaixo em seu ambiente:

Link para download da atualização: [Pacotes de Atualização - Workflow](https://tdn.totvs.com/pages/releaseview.action?pageId=852315120)

4 - Se o problema persistir, mesmo após verificar os fluxos e o parâmetro **MV\_WFSNDAU**, é essencial validar as configurações do servidor de e-mail. Pode haver falha na autenticação ou no envio, dependendo das configurações do ambiente. 

Nesse caso pedimos que realize a criação de uma conta no GMAIL e configure a autenticação em duas etapas para obter a senha de APP. Para realizar esse processo verifique a documentação abaixo:

**[Fazer Login com senha de APP - GMAIL](https://support.google.com/accounts/answer/185833?hl=pt-BR)**

Segue o passo a passo detalhado para realizar a configuração da nova conta de e-mail no Protheus por meio do módulo **SIGACFG:**

* **Acesse o Módulo Configurador (SIGACFG)**:

  + Faça login no sistema Protheus.
  + Acesse o módulo **Configurador (SIGACFG)**.

* **Navegue até as Configurações de E-mail**:

  + No menu superior, clique em **Ambiente** > **Workflow** > **Contas de e-mail**.

* **Exclua Contas de E-mail Existentes**:

  + Verifique se há contas de e-mail cadastradas.
  + Caso existam, selecione-as e clique em **Excluir** para remover qualquer configuração antiga.

* **Inclua a Nova Conta de E-mail**:

  + Clique em **Incluir** para adicionar uma nova conta.
  + Preencha os campos conforme as informações obtidas no passo anterior:
    - **Servidor SMTP**: `smtp.gmail.com`
    - **Porta**: 465 (SSL) ou 587 (TLS)
    - **Tipo de Conexão**: Escolha entre SSL ou TLS conforme a porta utilizada.
    - **E-mail do Remetente**: Insira o endereço da conta Gmail criada.
    - **Usuário**: O mesmo endereço de e-mail.
    - **Senha**: Cole a senha de aplicativo gerada no Gmail.
  + Confirme a inclusão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28157655458455)

* **Teste o Envio de E-mail**:

  + Após configurar a conta, realize um teste enviando um e-mail pelo **WFTEST** (Workflow > Testar e-mail).
  + Verifique se o e-mail é enviado com sucesso.

**SAIBA MAIS EM :**

[**Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[**Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não é possível realizar o envio do email (PGCA010).**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27661824040215-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-%C3%A9-poss%C3%ADvel-realizar-o-envio-do-email-PGCA010)

[**Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que fazer quando o "Clique Aqui" no email do formulário não está habilitado? Novo Fluxo de Compras - NFC (PGCA010).**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24511855484183-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-fazer-quando-o-Clique-Aqui-no-email-do-formul%C3%A1rio-n%C3%A3o-est%C3%A1-habilitado-Novo-Fluxo-de-Compras-NFC-PGCA010?source=search)

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)**
