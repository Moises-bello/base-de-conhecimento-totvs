---
content_hash: ade415f5d81b19321eaef65e0eade40a5a823e354837b0ec2c1b746b55d95822
fetched_at: '2026-06-29T00:11:38.335454+00:00'
page_id: '784762186'
product: rm
source: tdn-rm
title: 03 - Portal do Aluno - Termo de Consentimento de Uso de Imagem e Voz
type: documentation
url: https://tdn.totvs.com/display/LRM/03+-+Portal+do+Aluno+-+Termo+de+Consentimento+de+Uso+de+Imagem+e+Voz
version: 50
---

# 03.01 Cadastros Acadêmicos

Será possível acessar o termo de consentimento do uso de imagem e voz no cadastros acadêmicos do aluno, sendo permitido realizar o aceite ou revogação do mesmo conforme as regras abaixo.

Para que o Termo de Uso seja habilitado no Portal do Aluno, é necessário ir em Parâmetros > Educacional > RM Portal > RM Portal - Gerais 16/18 e marcar a opção [Habilitar uso do termo](https://tdn.totvs.com/x/jPpbGQ).

**Portal do Aluno | Cadastro acadêmico > Termo de Uso**

Para saber se aluno ou responsável aceitou ou revogou o termo, basta conferir o campo **"Status"**, sendo possível visualizar a data e responsável que executou a operação do status.

Aluno menor de idade

Quando o aluno for menor de idade,  o aceite ou revogação do termo será permitido somente se o papel do usuário autenticado estiver habilitado nos parâmetros com permissão.

É importante ressaltar que o aluno **menor de idade** poderá visualizar o termo e status, mas não possuirá permissão de aceitar/revogar. Este aluno só poderá aceitar/revogar o termo caso a permissão esteja com a opção "**Próprio Aluno"** marcada .

Aluno maior de idade

A qualquer momento o aluno que é maior de idade poderá realizar o aceite ou revogação do termo.

Caso o usuário autenticado no portal seja algum responsavel do aluno, somente será permitido o aceite ou revogação caso o mesmo possua acesso aos dados acadêmicos. Para saber mais sobre acesso aos dados acadêmicos  [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=754237338).

Aluno matriculado em mais de um contexto no TOTVS Educacional

Caso um mesmo aluno tenha matrícula em mais de um contexto no TOTVS Educacional, e a parametrização dos termos desses contextos estejam com os seguintes parâmetros configurados iguais (da tela Geral 16/18):

* "Habilita uso do termo",
* "Habilita somente a opção de aceite",
* "Relatório do termo de consentimento" (mesma coligada e id do relatório),
* "Versão" ,
* "Responsável por aceitar/revogar termo quando o aluno for menor de idade" (ter os mesmos checkboxes marcados);

a ação que for feita no termo de um dos contextos do aluno pelo portal do aluno (visualizar o termo deixando-o em situação pendente, ou aceitar o termo, ou revogar o termo) será feita também para os demais contextos em que o aluno está matriculado, e o termo que for aceito ou revogado também será replicado para os demais contextos do aluno.

Vale ressaltar também, caso a instituição utilize esse recurso (replicar os termos entre contextos de um mesmo aluno), é interessante utilizar um relatório mais genérico, evitando informações que façam referência ao contexto como nome de coligada, filial ou do nível de ensino.

##### **Habilitar somente opção de aceite**

É possível definir nos parâmetros do TOTVS Educacional se  será habilitada somente a opção "**Aceite**", com isso não será disponibilizado no termo a opção de "**Revogar**".

Alteração da versão do termo

Quando nos parâmetros do TOTVS Educacional a versão do termo for alterada, e o termo que o aluno realizou o aceite ou revogação for de versão inferior será exibido um novo termo com status pendente para que o aluno ou responsavel realize um novo aceite ou revogação.

# 03.02  Token de segurança

É possível parametrizar o **TOTVS Educacional** para que ao realizar o aceite/revogação seja necessário informar o número do **Token** que será enviado para o e-mail do usuário autenticado no portal do aluno.

Para conhecer quais os parâmetros estão relacionados ao **Token** de segurança [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425459706)

Ao clicar em "**Aceitar**" ou "**Revogar**" será apresentada a tela abaixo solicitando o número do **Token** que foi enviado para o e-mail do usuário autenticado no portal.

Para concluir a operação informe o número do **Token** enviado no e-mail e clique em "**Validar**"

* Caso o usuário autenticado não possua e-mail cadastrado, será apresentada uma mensagem de erro não sendo permitido concluir a operação.

O e-mail que será considerado é o e-mail que constar no cadastro da pessoa e não no cadastro do usuário de sistema, no caso de um responsável financeiro será considerado o e-mail do cadastro de cliente do **TOTVS Financeiro**.

* Conforme definido nos parâmetros o **Token**tem um tempo de validade, portanto o mesmo poderá ficar expirado sendo necessário o reenvio do mesmo.

# 03.03 Bloqueio do Portal

Você pode parametrizar o **TOTVS Educacional** de modo que, se um aluno estiver com o termo pendente, o acesso ao portal será bloqueado até que ele efetue o aceite ou a revogação desse termo.

Para conhecer quais os parâmetros estão relacionados ao **bloqueio do portal**

Ao acessar o portal, tendo habilitado o bloqueio do portal, será apresentado a tela abaixo, possibilitando acessar o termo ou sair do ambiente do portal, pois só é possível seguir ao realizar o aceite/revogação do termo.

Ao acessar o termo será possível atualizar o status do mesmo, seguindo todas as parametrizações como disposto nos tópicos anteriores.

Quando o aluno estiver com o termo pendente e o bloqueio do portal não estiver habilitado, sempre ao entrar no portal será exibido a tela abaixo, que possibilita acessar o termo ou deixar o aceite/revogação do termo para depois

É importante ressaltar que se o aluno já possuir um termo aceito ou revogado, e a instituição modifique o termo e altere a versão do mesmo nos parâmetros do **TOTVS Educacional** as telas acima serão apresentadas novamente, pois será necessário que o aluno ou responsavel execute o aceite ou revogação novamente.

É recomendável que a instituição não inclua no relatório do TOTVS Reports, informações relacionadas ao status de aceite ou revoga, pois a geração do termo de consentimento de uso de imagem e voz é feita apenas uma vez por versão do relatório parametrizado, no momento que o aluno ou responsável acessa o Portal do Aluno.  
A partir desse termo criado, o aluno ou responsável pode realizar o aceite ou revoga do mesmo quantas vezes acharem necessário, sem refletir mudanças diretas no termo gerado, apenas no status controlado pelo sistema, que pode ser visto no portal do aluno (Cadastro Acadêmico | Termo de uso) ou pelo sistema (Cadastro de aluno | anexo Termo de consentimento de uso de imagem e voz).
