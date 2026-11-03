---
content_hash: 6750cf3d83c338742900e296ab353f5bd1a925bc4f0a44a49ab070302258ff10
fetched_at: '2026-06-28T21:35:18.763275+00:00'
page_id: '185732379'
product: fluig
source: tdn-fluig
title: Personalização da URL para redirecionamento mobile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185732379
version: 14
---

# Índice

*true.\*ndicenone*

# Objetivo

---

Conforme informado na , o TOTVS Fluig Plataforma não é homologado para acesso pelo navegador mobile, apenas pelo aplicativo My fluig. Quando é realizado o acesso via navegador mobile, a plataforma apresenta uma tela sugerindo o download do aplicativo . O campo URL para redirecionamento mobile configura a URL para qual o usuário será direcionado ao acionar o link "continuar mesmo assim".

## Alteração da URL para redirecionamento mobile

Para alterar a URL da página de redirecionamento *mobile*, realize os seguintes passos:

1. Efetue o *login* na plataforma utilizando o usuário **wcmadmin**, e então acesse **Painel de Controle  ► WCM ► Configurações do Sistema**.
2. Na tela de configurações do sistema, acesse a aba **Personalização**.
3. Informe a URL da página no campo **URL para redirecionamento *mobile***.Pode ser informada uma URL padrão da plataforma ou algo específico (por exemplo, pode ser uma comunidade ou uma página customizada).
4. Clique no botão **Salvar**.

Após salvar essa configuração, quando os usuários forem acessar a plataforma via navegador mobile e acionarem o link "continuar mesmo assim" (da tela de sugestão do download do aplicativo), a plataforma irá redirecionar para a URL informada.

## Como montar a URL de redirecionamento

Quando requisita a página de redirecionamento, a plataforma envia dois parâmetros que podem ser utilizados na lógica desta página de redirecionamento:

* **cssClass:** sistema operacional utilizado quando acessada a página de redirecionamento. Seu valor pode ser **ios** ou **android.**
* **urlMobile:** URL requisitada originalmente pelo usuário.

Teste sua URL!

É importante testar a configuração dessa URL, pois caso sejam informados dados inválidos neste campo e a URL for construída incorretamente, a plataforma pode entrar em um loop infinito e redirecionar novamente para a tela de login após a autenticação.

* Exemplo para redirecionar para uma página customizada: <https://suaempresa.fluig.com/portal/p/1/acompanhamentoprojeto>
* Exemplo de URL incorreta: <https://suaempresa.fluig.com/nkwidget/index.html?urlMobile=https://suaempresa.fluig.com:443/portal/home?redir=true&cssClass=android>

Nos casos onde o usuário configurar a URL [https://URLFLUIG/portal](https://urlfluig/portal "Follow link") por exemplo, e ainda assim desejar acessar a plataforma pelo navegador mobile, deve ser implementado o login personalizado conforme descrito nas páginas [Personalização da página de login no tema Clássico](https://tdn.totvs.com/x/DwFlDw) e [Personalização da página de login no tema Snowflake](https://tdn.totvs.com/x/zE90GQ).
