---
article_id: 360044236953
category: LOGIN
content_hash: 1eb3d47e4b704bec939f8e2f10e87e5fa6ac039c9f0827b5ffdfcb59ff16623f
fetched_at: '2026-06-28T22:44:40.661810+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como “Iniciar usuário” e “Gerar Senhas” para
  o primeiro acesso ao MEU RH
type: support-article
updated_at: '2026-06-19T17:02:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044236953-RH-Linha-Protheus-MEU-RH-Como-Iniciar-usu%C3%A1rio-e-Gerar-Senhas-para-o-primeiro-acesso-ao-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27269844718743) Tempo aproximado para leitura: 00:02:00 min****Dúvida**Como “Iniciar usuário” e “Gerar Senhas” para o primeiro acesso ao MEU RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**1. O Login e Senha utilizados para acesso ao MEU RH depende desse procedimento, sendo assim, para “Iniciar usuário” e “Gerar Senhas” do **Usuário do Portal,** acesse no Protheus o módulo "**18 - SIGATCF**",  
![hPxMd19zka.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414496320407)  
  
2. No Menu acesse as opções: **> Atualizações > Configurações > Usuários > Manutenção**:  
  
Na rotina acesse **> Outras Ações > Gerenciar Usuários**:  
![baGc8Xktl1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414503215639)  
  
3. Nesta rotina deverá rodar primeiro a opção “Inicia usuário” para que sejam inicializados os Usuários que serão utilizados no MEU RH e, em seguida, rodar com a opção “Gerar Senhas”, para que sejam inicializado as senhas que serão utilizados no MEU RH.  
![wFVg08p2F7.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414503261079)  
  
**Importante:** O Login e Senha utilizados para acesso ao MEU RH dependem do procedimento acima.   
  
Com relação a Senha, o seu padrão é: DOIS DÍGITOS DO ANO DE NASCIMENTO DO FUNCIONÁRIO + DIA DE ADMISSÃO + DÍGITO DO CPF  
  
Com relação ao Login:

1. O campo **RD0\_LOGIN** é preenchido somente no primeiro login do funcionário no portal Gestão Capital Humano - GCH, mais informações [PSIGAPGCH0011- Login Unificado Portal Gestão Capital Humano](https://tdn.totvs.com/pages/viewpage.action?pageId=334340793). Quando não se utiliza o portal GCH não será possível efetuar o preenchimento do campo **RD0\_LOGIN.**
2. Caso o campo **RD0\_LOGIN** esteja em branco, o acesso será feito pelo CPF do funcionário (**RD0\_CIC**). Para isso, será necessário deixar o parâmetro MV\_ACESSPP conforme exemplo abaixo:  

   MV\_ACESSPP = qualquer outro código ou em branco →  o usuário será o CPF (RD0\_CIC).

   MV\_ACESSPP = 1 → o usuário será o e-mail (RD0\_EMAIL).

Para saber mais sobre o parâmetro MV\_ACESSPP acesse: [Login Meu RH Protheus](https://tdn.totvs.com/display/NPR/Login+Meu+RH+Protheus)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
