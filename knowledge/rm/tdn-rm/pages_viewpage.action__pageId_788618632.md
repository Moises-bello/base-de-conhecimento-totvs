---
content_hash: 66f1d954e340eeff4087f1cbaa07c3e66a810dd853a1142c5febce75e4c77bcd
fetched_at: '2026-06-29T00:11:39.225173+00:00'
page_id: '788618632'
product: rm
source: tdn-rm
title: '04 - Portal do Processo Seletivo - Matrícula: Termo de Uso de Imagem e Voz'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=788618632
version: 17
---

Será possível visualizar o termo de consentimento do uso de imagem e voz na matrícula do portal do processo seletivo, sendo permitido realizar o aceite ou revogação do mesmo conforme as regras abaixo.

Para que o Termo de Uso seja apresentado na matrícula via central do candidato será necessário os seguintes procedimentos:

* No **TOTVS Educacional,** acesse: "Parâmetros" > "Educacional" > "RM Portal" > "RM Portal - Gerais 16/18" e marque a opção "[Habilitar uso do termo](https://tdn.totvs.com/x/jPpbGQ)".
* No **TOTVS Processo Seletivo**, acesse o cadastro do processo seletivo e marque  a opção "**Usa termo de consentimento de uso de imagem e voz**" disponível  na aba [Parâmetros / Matrícula](https://tdn.totvs.com/pages/viewpage.action?pageId=640537958).

O processamento do Termo pelo portal do processo seletivo utiliza o usuário **RMProcessoSeletivo** para realizar algumas operações, portanto é necessário que este usuário exista e que ele possua todas as permissões pertinentes ao Termo.

Ao executar a matrícula será apresentada uma nova etapa "**Termo de uso de imagem e voz**"

##### **Habilitar somente opção de aceite**

É possível definir nos parâmetros do **TOTVS Educacional** se será habilitada somente a opção "**Aceitar**", com isso não será disponibilizado no termo a opção de "**Revogar**".

É importante ressaltar que se o candidato em algum outro momento já atualizou o status do termo, seja porque ele já era aluno ou aceitou anteriormente ou não concluiu a matrícula, o passo do termo não será exibido novamente durante o processo de matrícula, desde que no **TOTVS Educacional** o parâmetro "**Somente opção de aceite**" esteja ativado (neste caso o aceite já foi executado para o termo em outro momento).

Se no **TOTVS Educacional** o parâmetro "**Somente opção de aceite**" estiver desmarcado, o termo sempre será exibido novamente disponibilizando a opção "**Revogar**", pois a qualquer momento nesta etapa o candidato poderá executar a revogação.

Alteração da versão do termo

Quando a versão do termo nos parâmetros do **TOTVS Educacional** é modificada, e se um candidato em algum outro momento já atualizou o status desse termo, e o termo ao qual ele havia aceitado ou revogado é de uma versão inferior, ao efetuar uma nova matrícula, um novo termo com status pendente será apresentado ao candidato ou ao responsável. Isso permitirá que eles realizem um novo aceite ou revogação de acordo com a versão atualizada do termo.

No portal processo seletivo qualquer usuário com acesso a matrícula do candidato pode aceitar ou revogar o termo, mesmo se esse for menor de idade ou responsável pela inscrição.

Candidato que já é aluno com matricula em outros contextos

Ao concluir a matrícula, caso o candidato já seja um aluno da instituição matriculado em outro contexto, o sistema replicará automaticamente o termo de consentimento assinado para os demais contextos, evitando que o aluno precise realizar um novo aceite.

Essa replicação será realizada apenas para os contextos em que a parametrização do termo de consentimento seja idêntica. Abaixo, estão os parâmetros que devem ser iguais para que a réplica seja aplicada (RM Portal | RM Portal - Geral 16/18):

* "Habilita uso do termo",
* "Habilita somente a opção de aceite",
* "Relatório do termo de consentimento" (mesma coligada e id do relatório),
* "Versão" ,
* "Responsável por aceitar/revogar termo quando o aluno for menor de idade" (ter as mesmas opções marcados);

# 04.01  Token de segurança

É possível parametrizar o **TOTVS Educacional** para que ao realizar o aceite/revogação seja necessário informar o número do **Token** que será enviado para o e-mail do usuário autenticado no portal do aluno.

Para conhecer quais os parâmetros estão relacionados ao **Token** de segurança [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425459706)

Ao clicar em "**Aceitar**" ou "**Revogar**" será apresentada a tela abaixo solicitando o número do **Token** que foi enviado para o e-mail do usuário autenticado no portal.

Para concluir a operação informe o número do **Token** enviado no e-mail e clique em "**Validar**"

* Se o processo seletivo estiver parametrizado para utilizar responsável pela inscrição o **Token** será encaminhado para o e-mail definido no cadastro do responsável pela inscrição, se o processo seletivo não utilizar responsável pela inscrição o **Token**será encaminhado para o e-mail do candidato. É importante destacar que se o cadastro não possuir e-mail informado, será apresentada uma mensagem de erro não sendo permitido seguir com a matricula.

* Conforme definido nos parâmetros o **Token**tem um tempo de validade, portanto o mesmo poderá ficar expirado sendo necessário o reenvio do mesmo.
