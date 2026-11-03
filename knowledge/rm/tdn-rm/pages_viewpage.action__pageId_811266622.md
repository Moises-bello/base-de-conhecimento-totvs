---
content_hash: cf9172283b3c80cb1a9c0774eeb3d1f24bcfe52301332b2b526575ed8ae49b3b
fetched_at: '2026-06-29T00:11:44.229944+00:00'
page_id: '811266622'
product: rm
source: tdn-rm
title: 06 - Preenchimento da Ficha Médica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=811266622
version: 48
---

# Sumário

---

Sumário

# Ficha médica

---

A ficha médica poderá ser preenchida pelo aluno ou seu responsável através do portal do aluno acessando os dados acadêmicos, durante a matrícula (conforme parametrização) ou pelo candidato através do **TOTVS Processo Seletivo.**

Além disso, será permitido conforme as devidas permissões, a visualização da mesma através do **RM** no anexo do cadastro do aluno ou através do **Portal Gestão Educacional (PGE).**

Modelo da ficha médica

A ficha que será apresentada em todos os locais do **RM** ou **Portal** será correspondente ao modelo que estiver ativo no contexto que estiver autenticado, lembrando que é permitido somente um único modelo ativo por contexto.

Caso seja necessário no futuro reestruturar a ficha médica gerando um novo modelo, é possível modificar o modelo existente ou gerar uma cópia do modelo, realizar a modificação, inativar o modelo antigo e ativar o modelo alterado.

Os campos do modelo antigo que já foram preenchi

através do portal do aluno.

# Portal do Aluno - Dados Acadêmicos

---

# Portal do Aluno - Matricula

---

A ficha médica apresentada será conforme o modelo de ficha médica ativo para o contexto do aluno.  E será registrado o horário, data e por quem foi feita a alteração na ficha.

# Portal do Processo Seletivo - Matricula

---

A ficha médica apresentada será conforme o modelo de ficha médica ativo para o contexto do candidato e será registrado o horário, data da alteração na ficha.

É importante ressaltar que para habilitar o passo "**Ficha Médica**" é necessário sinalizar que o processo seletivo utiliza a ficha médica flexível na confirmação da matrícula, que ela esteja habilitada nos parâmetros e que haja modelo cadastrado e ativo.

Ponto de atenção

Podemos enfrentar um cenário em que um candidato, que já é aluno e possui uma ficha médica preenchida, e tem um cadastro de usuário no TOTVS Processo Seletivo que ainda não está vinculado ao cadastro de Pessoa/Aluno. Nesse caso, durante o preenchimento da ficha médica, não será possível carregar os dados da ficha médica já preenchida para o aluno, pois o sistema não consegue identificar a vinculação entre o cadastro de usuário e o cadastro de aluno. Portanto, o candidato precisará preencher a ficha médica novamente.

No entanto, ao concluir a matrícula na Central do Candidato, o sistema fará o vínculo entre o cadastro do usuário e o cadastro da pessoa. Em seguida, realizará a fusão das fichas médicas. A ficha médica preenchida durante a matrícula será mesclada com a ficha médica previamente vinculada ao aluno, com prioridade para os campos preenchidos na ficha médica da matrícula efetivada na Central do Candidato.

Todas alterações de ficha médica pelo portal do processo seletivo será registrada de forma integrada do usuário autenticado na Central do Candidato a partir do usuário **RMProcessoSeletivo**, portanto é necessário que este usuário exista nos cadastros de usuário do RM e que ele possua todas as permissões de preenchimento da ficha médica.

Outro ponto importante, a ficha médica é uma funcionalidade nativa do Portal Gestão Educacional que é integrada ao portal do Processo Seletivo, como a integração ocorre através do usuário de serviço é necessário que  exista no cadastro de usuário um usuário "**RM**" (não precisa de nenhuma permissão especifica, apenas o cadastro e que ele esteja **ativo**).

# Portal Gestão Educacional (PGE)

---

É importante ressaltar que para habilitar a aba "**Ficha Médica**" será necessário habilitar a permissão no perfil associado ao usuário

No **Portal Gestão Educacional (PGE)** a ficha médica flexível estará presente no Painel do Aluno.

A ficha médica apresentada será conforme o modelo de ficha médica ativo para o contexto do aluno (para conhecer mais sobre modelo [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=801997666))

Será permitido que o usuário do **Portal Gestão Educacional (PGE)**apenas adicione observações à ficha médica, para os demais campos, será permitido apenas a consulta.

Lembrando que para qualquer observação adicionada, será encaminhado um e-mail de notificação de alteração para o e-mail [parametrizado](https://tdn.totvs.com/pages/viewpage.action?pageId=790645108).

* Caso a ficha médica flexível não esteja habilitada na parametrização, o **Portal Gestão Educacional (PGE)** mostrará o menu correspondente ao modelo antigo da [Ficha médica do aluno](https://tdn.totvs.com/pages/viewpage.action?pageId=425459696).
* O nome apresentado na aba "Ficha Médica" poderá ser configurado nas parametrizações (verificar [parametrização](https://tdn.totvs.com/pages/viewpage.action?pageId=790645086)).
Modelo da ficha médica

dos pelo aluno e que foram mantidos no modelo copiado, não terão o seu preenchimento perdido, pois temos o conceito de campo global, desta forma se o aluno já preencheu esse campo, em toda ficha médica que o campo for adicionado será exibida a informação já preenchida, da mesma forma se o aluno alterar essa informação, em toda ficha médica que possuir esses campos a informação já será mostrada alterada.

Para mais informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=801997666)

Aproveitamento de preenchimento 

Quando uma matrícula não chega a ser finalizada por algum motivo, e a etapa da ficha médica tiver sido realizada, as informações da ficha ficarão armazenadas e poderão ser alteradas quando o processo de matrícula for retomado.

Quando um aluno é desmatriculado, os campos da ficha médica que foram preenchidos anteriormente, não serão mais aproveitados em possíveis matrículas futuras.

Permissão de preenchimento

As permissões de preenchimento da ficha médica são as seguintes:

* Aluno maior de idade não tem restrição
* Aluno menor de idade será permitido somente se estiver habilitado na [parametrização](https://tdn.totvs.com/pages/viewpage.action?pageId=790645086)
* Para os responsáveis do aluno menor de idade será permitido conforme a [parametrização](https://tdn.totvs.com/pages/viewpage.action?pageId=790645086)
* Para os responsáveis do aluno maior de idade, o responsável acadêmico não tem restrição, pai e mãe serão permitidos somente se no cadastro do aluno os mesmos possuírem acesso aos dados acadêmicos
Notificação de alteração

Quando houver alguma modificação na ficha médica através do portal do aluno, será enviado um e-mail para o responsável pela alteração e também um e-mail de notificação para o e-mail parametrizado para receber as notificações de alteração da ficha médica do contexto, para mais informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=790645108).

O e-mail enviado será formatado conforme o corpo de e-mail [parametrizado](https://tdn.totvs.com/pages/viewpage.action?pageId=790645108).

O responsável pela alteração será notificado com um e-mail, somente quando a alteração estiver sendo realizada por algum responsável do aluno ou próprio aluno, se o mesmo possuir e-mail cadastrado no RM. Já a instituição será notificada sempre no e-mail [parametrizado](https://tdn.totvs.com/pages/viewpage.action?pageId=790645108).

Dicas de instalação

É importante ressaltar que a **ficha médica flexível**disponibilizada no portal do aluno é a mesma ficha médica que é disponibilizada no **Portal Gestão Educacional (PGE)**, portanto neste caso, há integração entre os dois portais de forma transparente, sendo necessário que ambos portais estejam instalados dentro da pasta **FRAMEHTML** (caminho padrão do instalador ). 

Exemplo:

Caso o Portal Gestão Educacional esteja criado apartado da pasta **FRAMEHTML,** será necessário modificar o arquivo **totvs-app.global.config.js**da pasta **FrameHTML/Web/js**  e adicionar a TAG "**CONST\_GLOBAL\_URL\_PGE** " com o caminho base da URL do Portal Gestão Educacional.

Exemplo:

A URL do portal gestão educacional é [http://{dominio}**/PortalGestaoEducaciona**](http://localhost/FRAMEHTML)l,

A configuração deverá ser:

**CONST\_GLOBAL\_URL\_PGE = "/PortalGestaoEducacional"**

Importante: o Portal Gestão Educacional deve estar hospedados no mesmo domínio.

Ambientes TCLOUD

Para clientes que são TCLOUD é necessário realizar uma configuração adicional no [RM.exe.config](https://tdn.totvs.com/pages/releaseview.action?pageId=516194871) adicionando novas TAGS com as informações abaixo.

* api\_baseUrl: Configuração a ser definida no RM.exe.config contendo o endereço base para consumo das APIs no RM.Host. Esse valor é utilizado pelo Interceptor da Lib [Common-Api](https://npm.totvs.io/-/web/detail/@totvs/common-api) para acessar o endpoint de autorização para renovar o Token de Acesso injetado na abertura da tela.
* http\_baseUrl: Configuração a ser definida nas configurações do RM contendo o endereço base para consumo das serviços via HTTP como SOAP. Esse valor é pode ser interceptado pelo [Common-Api](https://npm.totvs.io/-/web/detail/@totvs/common-api).
* productLine: Utilizado para indicar qual linha de produto está embarcando o App PO UI. Valores: RM, Protheus, etc...

# Campo de observações

---

Agrupador padrão da ficha médica, que permite a inclusão de novas observações, com o limite de até 1000 caracteres. Após o registro, essas observações tornam-se permanentes e inalteráveis, assegurando a integridade do histórico médico do aluno ou candidato. Nessa mesma seção é possível visualizar os seis registros mais recentes associados ao aluno ou candidato. Além disso, oferecemos a conveniência de realizar o download do histórico completo, proporcionando uma ferramenta abrangente para revisões detalhadas.

Ao acessar a ficha médica através do anexo do cadastro do aluno ou pelo **Portal Gestão Educacional (PGE)**, será permitido somente adicionar uma nova observação, não sendo possível modificar nenhuma outra informação da ficha. As demais informações poderão ser modificadas somente pelo próprio aluno ou seu respectivo responsável

# Log

---

Toda alteração realizada pelo aluno ou responsável em algum campo da sua respectiva ficha médica será registrado no Log (tabela SLOGFICHAMEDICA).

Será possível consultar o log através do recurso do log de movimentação do aluno disponível no menu principal de acesso ao cadastro do aluno.

O campo observação não será registrado no Log, pois o preenchimento do campo de observações é acumulativo, sendo possível visualizar todo histórico diretamente na tela de preenchimento da ficha médica (tabela: SFICHAMEDICAPESSOAOBSERVACOES).
