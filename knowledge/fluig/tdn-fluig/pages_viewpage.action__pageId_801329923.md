---
content_hash: 5a6492334cf7bffa046591f472b06b5dfbbe0452aa8749346427f46cfffb4661
fetched_at: '2026-06-28T21:35:29.992590+00:00'
page_id: '801329923'
product: fluig
source: tdn-fluig
title: Identity | Política de senha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=801329923
version: 19
---

# Falando de política de senha...

---

Nessa tela é realizada a configuração da complexidade de senha exigida para os usuários da empresa no Identity. O administrador pode escolher se os usuários devem configurar suas senhas usando os requisitos de senha padrão, ou se uma política de senha específica deve ser definida, e nessa política podem ser configurados requisitos como a quantidade de caracteres, tempo de expiração, senhas proibidas, entre outras configurações.

## Acessar política de senha

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Política de senha**.

#f2f2f2#f2f2f2

É possível escolher se deve ser aplicada a política de senha padrão ou uma política personalizada.

Importante

Por padrão, a senha precisa atender aos seguintes requisitos:

* ser composta por no mínimo **8** caracteres;
* conter pelo menos uma letra minúscula (**a-z**);
* conter pelo menos uma letra maiúscula (**A-Z**);
* conter pelo menos um número (**0-9**);
* conter pelo menos um caractere especial (**! @ # &** etc.).

### Personalizar a política de senha

---

**01**. Na tela de Política de senha, marque a opção **Personalizado**.

#f2f2f2#f2f2f2

Ao fazer isso, os campos das abas **Complexidade de senha** e **Senhas proibidas** são automaticamente habilitados. Conforme as opções de tela forem modificadas, o indicativo de classificação da senha também se modifica, desde a senha muito fraca até a muito forte.

**02.** Configure os requisitos de senha na aba **Complexidade de senha**.

#f2f2f2#f2f2f2

**Tamanho mínimo da senha**  
Indica o número mínimo de caracteres exigidos para a senha. É possível informar um número entre 8 a 99 como valor mínimo de caracteres a ser preenchido.

**Requisitos de senha**  
Indica os caracteres que devem ser informados para que a senha seja considerada válida. As opções a serem configuradas na política são:

* Conter pelo menos um número
* Conter pelo menos um caractere especial
* Conter pelo menos uma letra maiúscula
* Conter pelo menos uma letra minúscula

**Segurança de senha**  
São oferecidas algumas configurações de senha para segurança adicional, sendo elas:

* **Prazo de validade para senha**: Quando habilitado, os usuários devem redefinir a senha no prazo de dias determinado pelo administrador. Por padrão, a cada 90 dias.
* **Disparar e-mail de notificação aos usuários:** Quando habilitado, com 5 dias de antecedência os usuários recebem um e-mail de notificação sobre a expiração da senha.
* **Reutilização de senhas**: Quando habilitado, os usuários só podem utilizar a mesma senha após a quantidade determinada de trocas ser efetuada.
* **Tentativas de acesso**: Quando esse parâmetro estiver habilitado, os usuários que ultrapassem a quantidade estabelecida de tentativas de login são bloqueados, até serem novamente ativados por um usuário administrador. Para mais detalhes, consulte a documentação de .

Dica:

É possível customizar os e-mails enviados nos casos de expiração de senha e bloqueio de usuário. Para mais detalhes, consulte a documentação de .

**03.** Configure as combinações que não podem ser informadas como senha na aba **Senhas proibidas**.

#f2f2f2#f2f2f2

**Verificar se a senha**  
São oferecidas algumas opções de bloqueio de combinação de caracteres. São elas:

* **Contém mais de 3 números sequenciais:** Quando habilitado, não deixa com que o usuário crie senhas com mais de três números consecutivos (em sequência crescente ou decrescente).
* **Contém mais de 3 letras sequenciais:** Quando habilitado, não deixa com que o usuário crie senhas com mais de três letras consecutivas em sequência.
* **Contém o nome do usuário**: Quando habilitado, não permite que o usuário crie sua senha com o próprio nome de usuário.
* **Contém o e-mail do usuário**: Quando habilitado, não permite que o usuário crie sua senha com o próprio e-mail.

**Listagem de senhas proibidas**Quando habilitado, os usuários não podem utilizar as senhas indicadas como proibidas. Podem ser incluídas quantas senhas forem necessárias, utilizando o separador "," (vírgula).

As senhas proibidas são apresentadas em uma listagem ao final da tela. Para excluir as combinações, utilize o botão **Excluir** .

Importante!

A complexidade de senha é definida por empresa, mas a senha pessoal é única para cada usuário. Quando o usuário for resetar sua senha, precisa definir uma senha que atenda aos critérios de todas as empresas onde está cadastrado.

A cada tentativa de autenticação realizada pelos usuários, o Identity verifica se a senha atual está atendendo a todos os critérios estabelecidos, e caso não esteja, o usuário é direcionado para a alteração de senha.

### Restaurar a política de senha padrão

---

**01**. Na tela de Política de senha, marque a opção **Política de senha padrão Identity**.

**02**. Na mensagem de confirmação, acione **Descartar**.

#f2f2f2#f2f2f2

Ao realizar essa ação, as políticas de senha da empresa são alteradas para o padrão do Identity, e todas as configurações personalizadas serão descartadas.

]]>
