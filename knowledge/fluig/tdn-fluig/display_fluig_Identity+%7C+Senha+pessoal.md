---
content_hash: 1c56c383b5bc14bf2687bccea683b6eb2ea3586c85b90ad8ecd7d59ebdbb3e1d
fetched_at: '2026-06-28T21:35:25.115230+00:00'
page_id: '274828593'
product: fluig
source: tdn-fluig
title: Identity | Senha pessoal
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Senha+pessoal
version: 15
---

# Falando de senha pessoal...

---

A senha pessoal é uma senha própria do TOTVS Identity que os usuários são orientados a criar ao aceitarem o [convite](https://tdn.totvs.com/pages/viewpage.action?pageId=312150740) para o contexto. Ela é fundamental em ambientes que não são integrados ao Active Directory e serve como uma forma alternativa de autenticação em ambientes que possuem essa integração, mas o Active Directory está indisponível.

## Senha pessoal x senha de rede

---

Em ambientes integrados ao Active Directory, os usuários podem autenticar-se utilizando a senha de rede ao invés da senha pessoal e, se preferir, o administrador pode [desabilitar totalmente](https://tdn.totvs.com/x/sZJvI) o uso da senha pessoal como forma de autenticação no contexto da empresa.

Um administrador corporativo sempre poderá autenticar-se no contexto utilizando sua senha pessoal, mesmo que essa opção tenha sido desabilitada.

Usuários importados do AD não recebem o convite por e-mail para entrar no contexto, pois são automaticamente ativados após serem  pelo administrador, portanto não são obrigados a realizar o cadastro da senha pessoal.

Nos contextos em que a senha pessoal não foi desativada pelo administrador, os usuários podem cadastrá-la através da página [Meu perfil](https://tdn.totvs.com/x/gNq7E) ou pela opção Esqueceu Sua Senha na página de [login](https://tdn.totvs.com/x/bZpUE).

## Habilitar/Desabilitar senha pessoal

---

O administrador poderá habilitar ou desabilitar o uso da senha pessoal para o acesso à empresa no Identity. Nesse caso, os usuários poderão acessar o Identity apenas com a senha do Active Directory / Open LDAP. Confira o passo a passo para habilitar ou desabilitar o uso da senha pessoal na documentação de [Credenciais do usuário](https://tdn.totvs.com/x/sZJvI).

O recurso de , em que os usuários cadastram-se manualmente na empresa no Identity através de um *link* na página de login será bloqueado se o uso da senha pessoal estiver desabilitado.

Fique atento

Um administrador corporativo sempre poderá autenticar-se no contexto utilizando sua senha pessoal, mesmo que essa opção tenha sido desabilitada nas configurações de segurança da empresa. Esta regra também se aplica ao recurso de troca de contextos.

## Troca de contextos

---

Caso o usuário possua [cadastro em mais de uma empresa](https://tdn.totvs.com/x/9K6cEw) e tenha utilizado a senha pessoal para autenticar-se no Identity, ao tentar fazer a troca para uma empresa que não permita o login via senha pessoal o acesso será negado. O usuário deverá autenticar-se utilizando as credenciais de Active Directory da empresa que deseja acessar.

## Requisitos da senha pessoal

---

A senha pessoal precisa atender a alguns requisitos de segurança, que podem ser padrão do TOTVS Identity ou uma política de senhas personalizada para a empresa. Para mais detalhes, consulte a documentação de .

]]>
