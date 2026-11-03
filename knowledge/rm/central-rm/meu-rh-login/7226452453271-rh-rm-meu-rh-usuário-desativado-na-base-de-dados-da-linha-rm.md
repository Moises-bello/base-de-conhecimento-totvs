---
article_id: 7226452453271
category: Meu RH - Login
content_hash: 6b326274b32c7e8d245fb793bbb4e268c25820c69b758fd9db52b9138cb2a053
fetched_at: '2026-06-28T22:47:27.262121+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Usuário desativado na base de dados da Linha RM
type: support-article
updated_at: '2026-04-06T11:02:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7226452453271-RH-RM-Meu-RH-Usu%C3%A1rio-desativado-na-base-de-dados-da-Linha-RM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24074886043287) Tempo aproximado para leitura: **00:02:10min**  
  
**Ocorrência**  
Ao acessar o Meu RH e tentar realizar o login, é apresentada a seguinte mensagem:

> *"Usuário desativado! O usuário informado encontra-se desativado na base de dados da Linha RM. Entre em contato com o supervisor para regularizar a situação."*

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas Versões  
  
**Causa**  
Esse comportamento pode ocorrer devido a alguns cenários:

* O usuário pode ter excedido o número de tentativas de login com senha incorreta, ocasionando o bloqueio automático por segurança (caso essa regra esteja parametrizada);
* O usuário pode estar inativo no RM devido ao prazo de expiração atingido;
* A senha pode ter sido alterada indevidamente, possivelmente relacionada à execução da rotina de inclusão de acesso:   
  [RH - RM - Meu RH - Erro de usuário ou senha incorreto para vários colaboradores no Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37278303032087-RH-RM-Meu-RH-Erro-de-usu%C3%A1rio-ou-senha-incorreto-para-v%C3%A1rios-colaboradores-no-Meu-RH)

**Solução**  
Para verificar a quantidade de tentativas de login permitidas e o tempo de bloqueio, acesse **Ambiente → Parâmetros → Parâmetros Globais → Gerais**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39540108727447)

Para reativar o acesso do funcionário ao Meu RH, acesse o cadastro do funcionário, vá até a aba **Identificação**, clique sobre o nome do usuário, marque a opção **Ativo** e verifique a validade do acesso, garantindo que esteja dentro da data atual, com a opção **Sempre válido** marcada ou com a **data de expiração** corretamente configurada.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7226197048855)

Para ativar vários usuários em lote, consulte: [Framework - Linha RM - Frame - Como desativar ou ativar vários usuários de uma vez](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37278183609751-Framework-Linha-RM-Frame-Como-desativar-ou-ativar-v%C3%A1rios-usu%C3%A1rios-de-uma-vez)  
  
Para alteração de senha Global no próximo login, consulte: [RH - RM - Meu RH - Alterar Senha dos Usuários no Próximo Login de Modo Global)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004792521-RH-RM-Meu-RH-Alterar-Senha-dos-Usu%C3%A1rios-no-Pr%C3%B3ximo-Login-de-Modo-Global)
