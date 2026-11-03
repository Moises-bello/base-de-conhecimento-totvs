---
article_id: 360001079247
category: Configurador
content_hash: 934e7ec31eeea3e4785eb198218a7a14455f2244c2618ec0c0721cd332e99fce
fetched_at: '2026-06-28T22:42:18.989353+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Configurar regras de senha
type: support-article
updated_at: '2024-05-08T11:39:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001079247-Framework-Linha-Protheus-Configurar-regras-de-senha
---

**Dúvida**  
Como configurar uma regra de violação de senha?  
  
**Ambiente**  
Protheus - Configurador - A partir da versão 11.8  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse Configurador > Usuários > Senhas > **Política;**  
2. Na aba **Regras de violação**, em **Regras para bloqueio** é possível configurar a quantidade de vezes que o usuário pode tentar digitar uma senha antes que seu acesso seja bloqueado, o intervalo de espera em minutos entre uma tentativa e outra, além de quanto tempo o usuário permanecerá bloqueado até que a quantidade de tentativas tenha se esgotado;  
3. No campo **Bloquear usuário após n tentativas**, digitar a quantidade de tentativas que usuário terá até ser bloqueado;  
4. No campo **Intervalo entre tentativas (minutos)**, digitar quanto tempo de intervalo deve ser respeitado entre uma tentativa e outra;  
5. No campo **Desbloquear usuário após n minutos**, definir quanto tempo usuário terá que esperar após ter sido bloqueado;  
6. Em **Parâmetros** é possível configurar para que o administrador seja notificado quando o usuário fizer tentativas incorretas de *login*. Além da possibilidade de configurar o envio de senha por e-mail em caso de esquecimento;  
7. No campo **Notificar administrador sobre bloqueio**, selecionar a opção **Sim**, caso queira que o administrador seja notificado sobre usuários bloqueados;  
8. No campo **Notificar sobre a tentativa de violação**, selecionar a opção **Sim**, caso queira que o administrador seja notificado quando houver uma tentativa de acesso por parte de um usuário bloqueado;  
9. No campo **Permitir envio de senha por e-mail**, selecionar a opção **Sim**, caso queira permitir que usuário possa receber uma nova senha no e-mail quando selecionada opção **Esqueci minha senha**;  
10. Em **Múltiplos terminais** é possível configurar para que um único usuário posso acessar diversos terminais ao mesmo tempo;  
11. No campo **Inibir acesso a mais de um terminal**, caso seja selecionada a opção **Não**, o usuário poderá acessar diversos terminais com o mesmo usuário;  
12. No campo **Bloquear usuário ao acessar outro terminal**, caso seja selecionada a opção **Sim** e o usuário não possuir permissão para acessar múltiplos terminais, quando houver a tentativa de acessar um segundo terminal, esse usuário será bloqueado.  
  
![Regra_Senha_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001820368)
