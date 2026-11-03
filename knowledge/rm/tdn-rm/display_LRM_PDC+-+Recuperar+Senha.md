---
content_hash: c93bca88cfd09ce7fa7eaac58f8d923048eb6477c190e86c5cd97c5c0e3934df
fetched_at: '2026-06-29T00:11:39.774699+00:00'
page_id: '789410830'
product: rm
source: tdn-rm
title: PDC - Recuperar Senha
type: documentation
url: https://tdn.totvs.com/display/LRM/PDC+-+Recuperar+Senha
version: 7
---

Ao clicar na opção ***Esqueci a minha senha*** na tela de login do *Portal do Cliente*, o sistema apresenta a opção para que o usuário possa recuperar senha.

Ao acessar esta opção, o sistema apresenta uma tela com as opções abaixo

* **Digite seu Usuário:** Informe o nome de usuário utilizado no login do PDC. O sistema verificará se o usuário está vinculado ao Cliente/Fornecedor do Comprador que está solicitando o acesso;
* **Digite seu e-mail:** Insira o endereço de e-mail associado ao usuário ou ao Cliente que está solicitando o acesso.

Importante!

Ao alterar o e-mail associado ao [*Cliente/Fornecedor*](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786), é necessário atualizá-lo também no cadastro do [*Usuário*](https://tdn.totvs.com/pages/viewpage.action?pageId=244425754) de acesso deste Cliente. Se um endereço diferente do registrado no sistema for informado no campo de recuperação de senha, será exibida uma mensagem informando que o e-mail digitado não foi encontrado na base de dados.

Após preencher essas informações e clicar no botão **Enviar**, caso os dados fornecidos sejam válidos nos cadastros do RM, o sistema enviará a senha de acesso para o e-mail correspondente.

*Senha enviada para o e-mail cadastrado.*

Caso as informações não sejam válidas o sistema apresentará uma exceção no formato abaixo, por exemplo:

*E-mail informado do **usuário** não encontrado.*

Nesta tela também é exibido o botão **Voltar**, que irá redirecionar o usuário para a tela de ***login***.

Importante!

**Dica de Segurança:**

Verifique se o seu PDC está com a tag de segurança configurada corretamente:
