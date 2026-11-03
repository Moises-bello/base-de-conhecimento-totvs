---
article_id: 360036860353
category: Configurador
content_hash: b8122d70875df69d2403b937f57c9814546da38fdffa75c0ddc5b9428bab5668
fetched_at: '2026-06-28T22:42:18.980639+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Configurar o envio de senha por e-mail quando
  o usuário esqueceu sua senha
type: support-article
updated_at: '2024-05-08T11:38:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036860353-Framework-Linha-Protheus-Configurar-o-envio-de-senha-por-e-mail-quando-o-usu%C3%A1rio-esqueceu-sua-senha
---

**Dúvida**Como configurar o SMTP para envio da senha por e-mail aos usuários?  
   
 **Ambiente**Protheus - Configurador - A partir da versão 11  
   
**Solução**O Protheus possui uma configuração que permite que o usuário receba uma nova **senha** por **e-mail**, caso venha a esquecê-la, clicando em **Esqueceu sua senha?** na tela de login do Protheus. Para o funcionamento desse recurso, é necessário configurar os seguintes passos no Configurador:  
1. Acesse Configurador > Usuário > Senhas > **Política**2. Na aba Política de Segurança, clique na aba **Regras de Violação**3. Em Parâmetros, selecione **Sim** em **Permitir envio de senha por e-mail  
  
![SPE_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048385473)**4. Na aba **Conexões**, em **SMTP**, preencha os dados de SMTP do seu provedor de e-mail  
5. Clique em **Confirmar  
  
![SPE_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047501354)**

|  |
| --- |
| **Obs.**: é necessário que o usuário tenha um e-mail configurado no seu cadastro  SPE_03.png |

6. Com a configuração feita, na tela de login digite o nome de usuário e clique em **Esqueceu sua senha?  
  
![SPE_04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048386493)**7. Na tela **Enviar senha por e-mail** digite o e-mail cadastrado para este usuário e clique em **Finalizar  
  
![SPE_05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048387053)**Se tiver alguma configuração errada, será exibida uma mensagem solicitando entrar em contato com o Administrador. Caso esteja tudo OK, você será redirecionado para a tela de login novamente, e uma **nova senha** será enviada por **e-mail** para o endereço cadastrado do usuário.
