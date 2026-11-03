---
content_hash: 9f033fd995e923941cb969e0ed81bb76706e9e0561d9653f63ab69b0894585d0
fetched_at: '2026-06-29T00:10:16.439784+00:00'
page_id: '469446949'
product: rm
source: tdn-rm
title: Utilização em smartphone
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469446949
version: 11
---

Atenção

Essa funcionalidade está disponível a partir da release 12.1.24.

Conforme descrito na documentação, o novo portal do aluno foi desenvolvido para ser responsivo até o nível de tablets para oferecer a melhor experiência ao usuário. Para smartphones recomendamos a utilização de nossa solução [TOTVS eduCONNECT/Educa Mobile](http://tdn.totvs.com/display/public/LRM/TOTVS+eduCONNECT).

Portanto para uma melhor experiência do aluno, é possível emitir uma mensagem alertando e dando opção de redirecionamento para as soluções voltadas para mobilidade (EduMobile e/ou Educonnect), sempre que o aluno acessar de um smartphone.

Para isso basta definir os links para o redirecionamento, no arquivo **edu-constantes.global.config.js** que fica localizado dentro da pasta **.../PortalEducacional/js**

**Educa Mobile**

Se você possui o **Educa Mobile** preencha o valor da constante EDU\_CONST\_URL\_EDUCAMOBILE com o link do seu EducaMobile, conforme print abaixo:

Com isso o aluno será alertado e terá a opção de com um click ser direcionado para o EducaMobile.

**eduCONNECT**

Se você possui o **eduCONNECT** preencha os valores das constantes EDU\_CONST\_URL\_EDUCONNECT\_IOS e EDU\_CONST\_URL\_EDUCONNECT\_ANDROID com os links da loja de aplicativos, conforme print abaixo:

Com isso o aluno será alertado e terá a opção de com um click ser direcionado para a loja de aplicativos para baixar o app.

ATENÇÃO

Caso você não possua o TOTVS Educa Mobile ou o TOTVS eduCONNECT ou ainda, caso não queira emitir a mensagem de alerta citada nessa documentação, basta deixar os valores das constantes EDU\_CONST\_URL\_EDUCAMOBILE, EDU\_CONST\_URL\_EDUCONNECT\_IOS e EDU\_CONST\_URL\_EDUCONNECT\_ANDROID vazios conforme é mostrado a seguir:

Obs. os links do EduConnect padrão estão abaixo, porém se você possui uma versão customizada acesse as lojas e coloque os links da versão customizada.

IOS → <https://itunes.apple.com/br/app/totvs-educonnect/id1255287155?mt=8>

Android → [https://play.google.com/store/apps/details?id=com.educonnect.totvs&hl=pt\_B](https://play.google.com/store/apps/details?id=com.educonnect.totvs&hl=pt_BR)

Aviso!

As URL's das lojas possuem prioridade referente a URL do EducaMobile, ou seja, se forem definidas todas as URL's os alunos serão redirecionados para a loja.

Recomendamos que para quem possuir o EduConnect preencha todas as URL's garantindo um melhor funcionamento da funcionalidade.

**Resultado no smartphone do aluno**
