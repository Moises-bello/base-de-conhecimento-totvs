---
article_id: 37278303032087
category: Meu RH - Login
content_hash: 464afde2bf580e0e2ce593bebeef35628046a2051ef571147dc272ed1e017e06
fetched_at: '2026-06-28T22:47:27.227916+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Erro de usuário ou senha incorreto para vários colaboradores
  no Meu RH
type: support-article
updated_at: '2026-06-17T20:00:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37278303032087-RH-RM-Meu-RH-Erro-de-usu%C3%A1rio-ou-senha-incorreto-para-v%C3%A1rios-colaboradores-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37278303019927) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Ao tentar realizar login no Meu RH, por que um usuário que acessava normalmente passou a receber o erro "Usuário ou senha incorretos"?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**  
O erro acontece quando há a execução da rotina de **"Inclusão de usuários para o RM Portal"** sem realizar um filtro na visão de funcionários ou não selecionando nenhuma caixa de seleção, resultando na execução do reset de senha para todas ou várias chapas (inclusive quem já possui usuário criado) com e flag **"Atualiza permissões para usuário existente"**.  
  
Ao executar a rotina sem utilizar a caixa de seleção dos funcionários é retornada a mensagem de aviso que será executada para todos os registros da visão:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37278285929495)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37278285930263)  
  
O erro também ocorre quando o funcionário responsável pelo cadastro de novos usuários seleciona alguns funcionários cadastrados e executa o processo de inclusão de usuários no RM Portal.

Caso a opção **"Utiliza Seleção de Funcionários"** permaneça marcada, o processo utilizará a seleção de funcionários exibida no lado direito da tela, onde uma nova seleção deve ser realizada. Para que sejam considerados apenas os funcionários selecionados anteriormente, é necessário desmarcar essa opção antes da execução do processo. Caso esta Flag não seja desmarcada pode ocorrer de atualizar todos os cadastros de usuários do RM.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41303828463895)

Geralmente o usuário utiliza o CPF como **"Senha Default"** e também necessita de **"Alterar senha no próximo login"**, mas quando se marca a flag "**Atualiza permissões para usuário existente"** os usuários já existentes que, já haviam alterado sua senha para outra diferente do CPF, acatam as novas configurações dessa execução voltando novamente a senha para o CPF e necessitando alterar no próximo login. (Caso a flag "**Definir CPF como senha default" não** seja marcada, osistema utilizará o **último nome** do usuário como senha.)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37278303022999)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37278303023383)

Nesse caso, o usuário do Meu RH deve testar o acesso novamente utilizando sua senha como CPF ou o último nome e, caso tenha ocorrido a situação descrita, ele irá acessar novamente o Meu RH e imediatamente alterar sua senha (caso tenha sido marcada a flag **"Usuário deve alterar senha no próximo login"** nessa execução que foi realizada sem filtros.)  
  
**Importante**  
O uso incorreto dessa rotina também pode causar a mensagem ["**Usuário desabilitado"**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7226452453271-RH-RM-Meu-RH-Usu%C3%A1rio-desativado-na-base-de-dados-da-Linha-RM). Isso acontece porque o colaborador continua tentando acessar com a senha antiga e, após exceder o número de tentativas inválidas configuradas no sistema, o usuário é bloqueado automaticamente.

O parâmetro de bloqueio está disponível em: **Ambiente > Parâmetros > Parâmetros Globais > Gerais**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40558790806039)

**Observação:**

É possível rastrear se esta rotina foi executada com o parâmetro  "**Atualiza permissões para usuário existente"** marcado. Para isto, acesse no RM a aba **Ambiente** > **Gerenciamento de Jobs**. Filtre os jobs pela **Classe do processo** = *'FopInclusaoUsuarioProc'.* Nesta tela será possível consultar o usuário que executou a rotina e também o horário de execução.

Para obter os detalhes dos parâmetros de execução do job, clique para **edita-lo**, vá em **Anexos** e selecione **XML de Parâmetros de Jobs**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40716008615575)

Será aberta uma nova janela contendo o XML completo da execução. Localize a tag: <`AtualizarPermissoesUsuario>true</AtualizarPermissoesUsuario>`.

Caso o valor da tag esteja como `true`, significa que o parâmetro foi marcado durante a execução da rotina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40716018284183)

**Saiba mais**  
[Framework - Linha RM - Frame - Como configurar bloqueio de usuário por erros em tentativa de login no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410818139799-Framework-Linha-RM-Frame-Como-configurar-bloqueio-de-usu%C3%A1rio-por-erros-em-tentativa-de-login-no-sistema)
