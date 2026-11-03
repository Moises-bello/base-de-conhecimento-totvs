---
article_id: 360028440511
category: Comércio Exterior - Easy Import Control - Miscelanea
content_hash: c79eaa5016fe7262477dc33cb7004c86ab5190cd535540d43bd04da508279f59
fetched_at: '2026-06-28T22:39:42.017770+00:00'
product: protheus
section_id: 1500001549702
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Integração com
  Despachante
type: support-article
updated_at: '2021-12-27T13:30:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028440511-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Integra%C3%A7%C3%A3o-com-Despachante
---

**Dúvida**Existe integração do SIGAEIC com o despachante?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Procedimentos para Utilização

Condições Prévias:

É imprescindível que seja informado nos seguintes parâmetros:

* **MV\_WFSMTP**: o nome do servidor, se necessário com a porta. (Exemplo: smtp.empresa.com.br:111);
* **MV\_RELAUSR** : o e-mail do usuário. (Exemplo: [empresa@empresa.com.br);](mailto:empresa@empresa.com.br);)
* **MV\_RELAPSW** : a senha do usuário.(Exemplo: 123456);
* **MV\_RELAUTH**: se necessita de autenticação.(Exemplo: .T.);
* **MV\_WFTCONN** : o numero de tentativas de acesso ao servidor de e-mails.(Exemplo: 5)
* **MV\_RELTIME** : o conteúdo 120;
* Possuir um **PO** ou processo de embarque para envio de arquivo para o despachante.

**Sequência 01 – Geração de arquivo:**

1. No **Easy Import Control (SIGAEIC)** acesse **Miscelanea/ Int. Despachante (EICEI100)**.
2. No serviço **Envio de PO**, selecione a pasta **Gerados**. Clique na ação **Int. PO**.
3. Informe o PO e o código do despachante. Clique em **OK**.
4. Marque o registro e clique em **Confirmar**.
5. Confirme a geração do arquivo. Clique em **Sim**.
6. Clique em **OK**.

**Obs.:**Para gerar o arquivo do serviço **Envio de Embarque** será utilizado o mesmo procedimento do serviço **Envio do PO**.

**Sequência 02 – Envio de arquivo:**

1. No módulo **Easy Import Control (SIGAEIC)** acesse **Miscelanea/ Int. Despachante (EICEI100)**.
2. Para enviar o arquivo gerado para o despachante, na pasta **Gerados** do serviço **Envio de PO**, selecione o arquivo a ser enviado e clique na ação **Enviar****e-mail**.
3. Confirme o arquivo que será enviado. Clique em **Sim**.
4. Será carregado o e-mail cadastrado do despachante selecionado, caso não esteja cadastrado, informe o e-mail do destinatário no campo **Para** e as outras informações necessárias. Clique em **Enviar**.
5. Será confirmado o envio. Clique em **OK**.

**Obs.:**Para o envio do arquivo para o serviço **Envio de Embarque** será utilizado o mesmo procedimento do serviço **Envio de PO**.

**Sequência 03 – Recebimento do arquivo:**

1. No módulo **Easy Import Control (SIGAEIC)** acesse **Miscelanea/ Int. Despachante (EICEI100)**.
2. Para receber os arquivos do despachante, selecione o serviço **Recebimento do Numerário**, clique na ação **Configuração**.
3. Clique na opção **“...”** (reticências).
4. Visualize as opções e selecione o caminho onde se encontra os arquivos importados. Clique em **Salvar**e na sequência em **Confirmar**.
5. No serviço **Recebimento de Numerário**, selecione a pasta **Recebidos**. Clique na ação **Receber arquivo**.
6. Os nomes dos arquivos conterão a data e a hora que foi recebido.

**Obs.:**Para configuração do caminho e recebimento dos arquivos importados do serviço **Recebimento de Despesas** ou **Recebimento de NF**, será utilizado o mesmo procedimento do serviço **Recebimento de numerário**, porem é obrigatório informar caminhos diferentes para os outros serviços.

**Sequência 04 – Processamento do arquivo:**

1. No módulo **Easy Import Control (SIGAEIC)** acesse **Miscelânea/ Int. Despachante (EICEI100)**.
2. Para processar o arquivo recebido, no serviço **Recebimento do Numerário** e na pasta **Recebidos** selecione um arquivo e clique na ação **Processar**.
3. Clique em **Previa**.

O sistema apresenta a janela **Resumo**. Clique na opção **Retorna**presentena mesma e na sequência, em **Integra**.

4. Novamente o sistema apresenta a janela **Resumo**. Repita o passo anterior clicando em **Retorna**.
5. Clique em **Confirmar**.
6. Se o arquivo estiver com status rejeitado será registrado na pasta **Rejeitados**. Caso o arquivo estiver com status aceito será registrado na pasta **Integrados**.
7. Será possível visualizar o arquivo recebido, integrado ou rejeitado ao dar duplo clique sobre o registro.

**Obs.:**Para processamento ou visualização do arquivo recebido do serviço **Recebimento de Despesas** ou **Recebimento de NF**, será utilizado*o*mesmo procedimento do serviço **Recebimento de numerário**.
