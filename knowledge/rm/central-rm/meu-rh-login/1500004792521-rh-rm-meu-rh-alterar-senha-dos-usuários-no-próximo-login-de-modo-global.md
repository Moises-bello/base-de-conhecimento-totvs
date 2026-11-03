---
article_id: 1500004792521
category: Meu RH - Login
content_hash: 35a4f333a5616524ef3ca0a57f948392723900a603fa8072dc82ab352fbc5a22
fetched_at: '2026-06-28T22:47:27.315287+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Alterar Senha dos Usuários no Próximo Login de Modo Global
type: support-article
updated_at: '2026-01-16T15:29:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004792521-RH-RM-Meu-RH-Alterar-Senha-dos-Usu%C3%A1rios-no-Pr%C3%B3ximo-Login-de-Modo-Global
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24078509948055) Tempo aproximado para leitura: 00:02:45 min**  
  
**Dúvida**  
Como alterar a senha dos usuários de forma global?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - 12.1  
  
**Solução**

**1º -** Acesse o módulo **Serviços Globais**;

**2º -** Na aba Segurança, acesse o menu **Usuários**;

**3º -** Selecione os usuários desejados;

**4º -** Em Processos, selecione **Atualização de múltiplos Registros de Usuário**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006464922)

**5º -**Selecione Alterar senha no Próximo Login com valor T (True = verdadeiro);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24078509965207)

**6º -** Clique em executar. Aguarde a finalização do processo;

**7º -** Ao logar no Meu RH, será solicitada troca de senha para todos os usuários selecionados no processo;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006624361)

**Importante**  
O processo será executado para os registros selecionados na visão de usuários. Por padrão, as telas dos sistema carregam 1000 registros por questão de performance (desempenho). Caso seja necessário realizar o processo para mais de 1000 usuários, deverá aumentar a quantidade de registros da visão de usuários para o valor desejado, por exemplo, 3000, criando um servidor de aplicação para a action GlbUsusarioAction. Detalhes seguem no link abaixo:  
  
[RM - Frame - Aumentar quantidade de registros na visão (Servidores de Aplicação )](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016013767-RM-Frame-Aumentar-quantidade-de-registros-na-vis%C3%A3o-Servidores-de-Aplica%C3%A7%C3%A3o-)  
  
Após configurar e carregar a visão de usuários com todos os registros, neste exemplo, os 3000, selecione os registros desejados e execute o processo de atualização de múltiplos registros.
