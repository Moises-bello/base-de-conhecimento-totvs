---
article_id: 4402319952151
category: Meu RH - Login
content_hash: 6d4f1e358a8ece5a98852963f2dc5aca33967b47bd0958be3f57499980a4b6b4
fetched_at: '2026-06-28T22:47:27.311757+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Erro ao logar a chapa do funcionário não foi identificada
type: support-article
updated_at: '2026-01-16T15:28:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402319952151-RH-RM-Meu-RH-Erro-ao-logar-a-chapa-do-funcion%C3%A1rio-n%C3%A3o-foi-identificada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19150022181015) Tempo aproximado para leitura: 00:04:20 min**  
  
**Ocorrência**  
Ao acessar o Meu RH é apresentada a mensagem de erro  "**A chapa do funcionário não foi identificada. Por favor, entre em contato com o suporte**".  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões do sistema RM  
  
**Solução**  
Esse erro acontece quando o usuário que está acessando o portal não possui nenhum perfil vinculado ao modulo Folha de Pagamento.

**Importante:**  
Se o funcionário estiver vinculado a mais de uma Coligada, deverá avaliar se em todas Coligadas envolvidas foram vinculadas um Perfil do Folha de Pagamento.  
  
Para incluir um usuário do Meu RH para um funcionário, basta acessar:  
**| Folha de Pagamento | Funcionários | Selecionar o Funcionário | Processos | Inclusão de Usuário para Acesso ao RM Portal.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402312838039)

Ao avançar no processo, será apresentado a tela onde deve ser informado o "Código de acesso ao banco" e a qual perfil este funcionário irá utilizar, este Perfil define quais permissões ele possui. Para maiores informações sobre permissões acesse o link. [Personalizar permissões Perfil Meu RH](https://tdn.totvs.com/pages/viewpage.action?pageId=287067720)

Defina a **Data inicial** da validade do usuário, a **Data Final** caso fique em branco determina que o prazo é indeterminado para o acesso ao Meu RH.

**Observação:** O período de validade deve estar dentro do período atual, caso contrario irá impedir o acesso ao Meu RH.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402312889623)

Na tela seguinte, deve ser informado o **Código do Grupo**, também chamado de Grupo de Quiosque.  
Em **Parâmetros** são opcionais marcar ou não as Flags, mas caso a Flag **Definir CPF como senha default** não seja marcada, deve ser informado uma senha manualmente para o usuário.![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402321086103)

Após executar com sucesso, o cadastro do funcionário será preenchido com os dados do usuário.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402321119895)

Caso apresente a mensagem de alerta " **Usuário XXXX já possui permissão para a coligada XXX !** " demonstra que ele foi já possui alguma permissão neste modulo, caso apresente esta mensagem verifique acessando o modulo de Serviços Globais.

Na aba Segurança, abra os cadastros de usuários, selecione o Sistema de Folha de pagamento, então abra o cadastro do usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19150022195223)

No cadastro do usuário valide se esta com um perfil associado a ele.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19150022200343)

**Importante**

Caso o funcionário receba e-mails como, aviso de férias, recibo de férias e outras notificações, deve ser informado um e-mail valido em seu cadastro de usuário.  
  
**Saiba mais**

Para mais informações sobre cadastro de usuários acesse [Cadastro de usuários na MDI](https://tdn.totvs.com/pages/releaseview.action?pageId=244425754)
