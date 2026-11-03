---
content_hash: 662cf5019270591303b5b652f2ed30328c01b38d253fe02003e72a10280a32e3
fetched_at: '2026-06-29T00:09:33.211505+00:00'
page_id: '425458938'
product: rm
source: tdn-rm
title: Cursos/Habilitações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458938
version: 30
---

Nesta tela, cadastra-se o Curso/Habilitação que o aluno optou em fazer na instituição.

As informações relativas a este cadastro, estão divididas em: Identificação, Ingresso, Diploma, Transferência, Observações e Histórico.

Na aba referente à diplomação, deve-se atentar com os campos de diplomação. Caso o processo de [geração de diplomação](https://tdn.totvs.com/x/JfxbGQ) tenha sido executado, gerando um **diploma** ou **certificado**, os campos abaixo serão bloqueados, sendo apenas possível alterá-las através do processo de [Atualização de dados do Certificado e Registro do Livro](https://tdn.totvs.com/x/X-xbGQ). Caso nenhum processo tenha sido executado, os campos estarão disponíveis para edição.

Importante lembra que na geração de certificado (e no cadastro do certificado) existe as [opções](https://tdn.totvs.com/download/attachments/425459142/image2020-5-4_14-7-45.png?version=1&modificationDate=1588612065680&api=v2) referente a atualização destes campos. Caso esteja marcado as opções **Só atualiza se não houver diploma gerado** ou **Atualiza** os campos abaixo continuarão bloqueados, caso contrário será possível alterar os campos.

Campos que serão bloqueados conforme descrito acima:

* Datas de conclusão do curso
* Data de colação de grau
* Registro de conclusão
* Livro de registro
* Página de registro
* Nº do processo do registro do diploma
* Instituição registradora do diploma (a partir da versão **12.1.2310**, passa a ter um comportamento diferente, conforme mencionado abaixo)
* Data de emissão do diploma
* Data de registro do diploma
* Data de emissão do histórico final (a partir da versão **12.1.2502**)

A partir da versão **12.1.2310**na aba **Diploma** o campo **Instituição registradora do diploma** passa a ter um comportamento diferente conforme abaixo.

Se for inserir um registro novo este campo é condicionado ao campo de **registro em outra IES**na , ou seja, se for registrado em outra IES o campo **instituição registradora do diploma** ficará disponível para seleção das . Se não for registrado em outra IES, este campo ficará disponível para seleção apenas da **Instituição do MEC**, que é definida nos parâmetros da [secretaria](https://tdn.totvs.com/display/LRM/Secretaria#Secretaria-Secretaria7/7:Par%C3%A2metrosGerais).  
Se for editar este campo também irá seguir a regra acima caso o campo da instituição registradora do diploma estiver vazio, se o mesmo já tiver sido preenchido por uma  nada mudará para este campo. Porém esta aba poderá ter sido preenchida automaticamente por um diploma ou certificado, caso isso aconteça antes desta implementação nada mudará para este campo, porém certificados gerados posterior a esta implementação, o campo instituição registradora do diploma sempre será a instituição do MEC, entretanto para diplomas gerados, este campo é condicional ao campo **registro em outra IES**na , regra já mencionada acima.

O intuito desta implementação é unificar as instituições registradora e emissora nos certificados e diplomas, não sendo necessário ter a instituição do MEC e instituição de ensino com os mesmos valores. Vale ressaltar que instituição emissora sempre é a própria instituição, que chamamos de instituição do MEC e instituição registradora para certificados também é a própria instituição (instituição do MEC) e para diplomas irá depender do campo **registro em outra IES**na , se não for registrado também é a própria instituição (instituição do MEC), se for registrado em outra IES será um outra instituição que é cadastrada em .

Até a versão 12.1.2310, o campo da instituição do MEC não era persistido no banco de dados, e era carregado automaticamente no lugar do campo da [instituição de ensino](https://tdn.totvs.com/pages/viewpage.action?pageId=425458695).

A partir das versões mais recentes, esse campo passou a ser persistido em banco, sendo efetivamente gravado na aba de diplomação do curso/habilitação do aluno, de acordo com a regra acima mencionada.

A instituição do MEC está disponível em Atividades Acadêmicas | Censo | Instituição do MEC.

Informações Complementares

---

[Atividades de Extensão](https://tdn.totvs.com/x/PTbuJg)

[Análise Curricular](https://tdn.totvs.com/x/RbSGHw)

Como Fazer

---

[Relatório utilizando provedor de dados Análise Curricular](http://tdn.totvs.com.br/pages/viewpage.action?pageId=273312406)
