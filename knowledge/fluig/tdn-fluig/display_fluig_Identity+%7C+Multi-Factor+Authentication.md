---
content_hash: b43c6364ef95b19b4570c0f6f614dccebb9a588556450a1eade2fe8ad1d1ef35
fetched_at: '2026-06-28T21:35:25.850800+00:00'
page_id: '317297191'
product: fluig
source: tdn-fluig
title: Identity | Multi-Factor Authentication
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Multi-Factor+Authentication
version: 39
---

75%

5.\*ndice

25%

trueIdioma

# Falando de Multi-Factor Authentication...

---

A autenticação multifator (do inglês *Multi-factor authentication* ou MFA) oferece uma camada adicional de segurança no acesso ao TOTVS Identity através da exigência de um código (chave eletrônica) gerado no aplicativo  ou outro aplicativo autenticador de sua preferência. O My Safe ID é a única aplicação que damos suporte, por esse motivo, o usuário pode usar outro aplicativo, mas não é homologado pela TOTVS.

O código gerado no aplicativo deve ser informado pelo usuário na página de login do Identity para liberar o acesso à conta, após a autenticação via e-mail e senha. Assumindo que apenas a pessoa tem acesso ao aparelho - e portanto ao código - agentes maliciosos serão barrados, mesmo que saibam qual é a senha, pois não dispõe do código gerado pelo aplicativo autenticador. Além disso, para impedir a reutilização, o código é substituído automaticamente a cada 30 segundos.

A autenticação multifator no Identity é definida por grupos: pode ser configurada como obrigatória para os grupos desejados. Ao torná-la obrigatória, os usuários desses grupos deverão configurar a autenticação multifator no próximo acesso. A configuração de MFA será opcional para os demais grupos.

ATENÇÃO!

A autenticação multifator, mesmo habilitada para o grupo, não é exigida nas seguintes situações:

* A  está habilitada na empresa do Identity.
* A autenticação for realizada pelo aplicativo  em uma instalação do TOTVS Fluig Plataforma com mais de uma empresa cadastrada.
IMPORTANTE!

Ao habilitar a autenticação multifator (do inglês ***Multi-factor authentication*** ou **MFA**) obrigatóriona empresa, todas as pessoas precisarão autenticar-se via interface. Se houver alguma integração que esteja fazendo login via API, esse recurso não será suportado e a integração irá parar de funcionar.

## Gerenciar a autenticação multifator nos grupos

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Multi-factor Authentication**.

**03.** Localize o grupo que deseja visualizar a configuração de MFA.

**04.** Na linha correspondente ao grupo, acione **Habilitar**  ou **Desativar**localizados na coluna **Autenticação multifator obrigatória?** para alterar sua configuração.

#f2f2f2#f2f2f2

Ao informar **Sim**, a autenticação multifator será obrigatória para o acesso dos usuários desse grupo. Ao informar **Não**, a autenticação será opcional, cada usuário do grupo pode optar pela utilização de MFA para autenticar-se na empresa no Identity.

**05.** Caso esteja habilitando o MFA como obrigatório, insira sua senha na mensagem de confirmação. Caso esteja desabilitando, além da senha é necessário informar uma justificativa.

#f2f2f2#f2f2f2

Após a ativação do recurso nas configurações do grupo, os usuários devem configurar o MFA em suas contas através da opção .

Ao habilitar a autenticação multifator como um recurso obrigatório, será solicitado a todos os usuários do grupo que ainda não possuam MFA configurado, que realizem a configuração, por isso as instruções de ativação serão apresentadas em tela no próximo acesso ao sistema.

Tanto a ativação quanto a desativação do recurso MFA do grupo é registrada em histórico e pode ser consultada no relatório de .

### Buscar grupo

---

**01**. No campo de pesquisa, informe o nome do grupo que deseja buscar.

#f2f2f2#f2f2f2

A busca por meio desse campo é automática: durante a digitação, apenas os grupos que tiverem o texto informado serão mantidos na listagem.

### Filtrar grupos

---

**01**. No filtro, selecione os grupos que deseja visualizar.

#f2f2f2#f2f2f2

Por padrão, são trazidos todos os grupos, mas é possível filtrar apenas pelos definidos como MFA obrigatório ou MFA opcional.

]]>

## Documentações relacionadas

---

* [Identity | Multi-Factor Authentication](https://tdn.totvs.com/display/fluig/Identity+%7C+Multi-Factor+Authentication)
* [Fazer login com autenticação multifator (MFA)](https://tdn.totvs.com/display/fluig/Identity+%7C+Login#Identity|Login-Fazerlogincomautentica%C3%A7%C3%A3omultifator(MFA))
* [Identity | Configuração e Uso do MFA por e-mail](https://tdn.totvs.com/pages/viewpage.action?pageId=1048505459)
* [Identity | Validação do MFA desvinculado do Login](https://tdn.totvs.com/pages/viewpage.action?pageId=1048504602)
* Identity | API de validação de MFA
