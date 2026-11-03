---
article_id: 40248401518615
category: SIGAACD - Automação e Coleta de Dados
content_hash: 8c1324bfab811a438a713a5fdf7ff2db5ab202bfadb87283e97e50efe00712fe
fetched_at: '2026-06-28T22:39:13.889538+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Wizard de Impressão
  de Etiqueta apresenta a mensagem NODRIVER
type: support-article
updated_at: '2026-05-05T18:01:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40248401518615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Wizard-de-Impress%C3%A3o-de-Etiqueta-apresenta-a-mensagem-NODRIVER
---

A mensagem "NODRIVER" na rotina de Wizard de Impressão do TOTVS Protheus ocorre por ausência do driver correto. Para corrigir, descompacte os arquivos .drv na pasta system conforme o sistema operacional do servidor, confirme os caminhos no appserver.ini, configure o parâmetro MV\_DRIVER como EPSON no Configurador, ajuste as configurações de impressão no cadastro do usuário e no grupo vinculado. Verifique se o erro persiste após essas ações.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40248401495575) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Na rotina de Wizard de Impressão apresenta a mensagem "NODRIVER" como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Para a mensagem **NODRIVER**, segue arquivos .drv em anexo, descompacte dentro da pasta system **de acordo com o sistema operacional do servidor.**  
   
1. Verifique se esta aplicando os arquivos .DRV na pasta system correta, valide pela chave **RootPath** e **StartPath** no appserver.ini.

**Após, efetue:**

 2. Acesse o Configurador (SIGACFG) e configure o parâmetro MV\_DRIVER como EPSON nas 3 linhas.

3. No cadastro do usuário valide se na Aba Parametrização e Sub Aba Impressão está conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40248377597591)

4. Verifique se o usuário esta vinculado a um Grupo, na Aba Grupo, Sub Aba Impressão, deixe conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40248401499287)

5.  Após valide se a mensagem **NODRIVER** persiste por gentileza.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
