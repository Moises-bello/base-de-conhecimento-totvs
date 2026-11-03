---
content_hash: 09161e988770a7f54366c3a122330acfce552594541cc87b3bf2261b114058a8
fetched_at: '2026-06-29T00:09:32.640407+00:00'
page_id: '425458894'
product: rm
source: tdn-rm
title: Associar Descontos por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458894
version: 14
---

---

Desconto por Antecipação é um recurso disponível no sistema que permite à Instituição de Ensino cadastrar uma modalidade específica de desconto, válido para determinado período de vigência, composto por uma série de itens (ou faixas) de descontos, com regras específicas de valores e datas para serem concedidos aos alunos que quitarem antecipadamente os boletos referentes às suas mensalidades. Os descontos por antecipação são cadastrados no produto TOTVS Educacional, no menu *'Financeiro / Contábil | Geração | Financeiro | Desconto por Antecipação'*.

Após cadastrá-los é necessário associá-los aos locais onde o sistema irá procurá-los para os devidos cálculos. Os locais são: Matriz aplicada, campus/polo da matriz ou contratos. Lembrando que o sistema sempre fará a busca pelos descontos por antecipação partindo do local mais específico (contrato) para o local mais abrangente (matriz aplicada), sempre nesta ordem de prioridade.

Associação de Descontos por Antecipação à Contratos

Para realizar a associação dos descontos por antecipação aos **Contratos**, primeiramente é necessário que o usuário tenha permissão para esta ação no cadastro de Contratos. Confira as permissões no cadastro do Perfil do usuário (*Perfil Educacional-Tags: Financeiro/Contábil | Contratos | Desconto por Antecipação por contrato | Incluir | Excluir | Editar devem estar habilitadas*).

Feito isto, selecione o contrato do aluno e acesse *Anexos | Desconto por antecipação por contrato* e utilizando o botão *'Incluir'*, associe os descontos por antecipação desejados. Neste momento, serão feitas validação de vigência entre os descontos por antecipação associados a este contrato, não sendo permitida a inclusão/alteração de descontos por antecipação cujo período de validade coincida com outro desconto já associado ao mesmo contrato.

**Desconto por antecipação associado ao contrato do aluno:** Será disponibilizado o anexo "Desconto por antecipação por contrato" na cadastro de contratos e permissões conforme telas abaixo:

Associação de Descontos por Antecipação à Campus/Polo da Matriz aplicada

Para realizar a associação dos descontos por antecipação aos **Campus/Polo da Matriz aplicada**, primeiramente é necessário que o usuário tenha permissão para esta ação no cadastro de Campus/Polo da Matriz aplicada. Confira as permissões no cadastro do Perfil do usuário (Perfil Educacional-Tags: Currículo e Oferta | Estrutura Curricular | Matrizes Curriculares | Matrizes Aplicadas | Campus da Matriz Aplicada | Desconto por antecipação por campus/polo da matriz aplicada | Incluir|Excluir|Editar devem estar habilitadas).

Feito isto, selecione o campus/polo da matriz aplicada e acesse Anexos | Desconto por antecipação por campus/polo da matriz aplicada e utilizando o botão 'Incluir', associe os descontos por antecipação desejados. Neste momento, serão feitas validação de vigência entre os descontos por antecipação associados a este campus/polo da matriz aplicada, não sendo permitida a inclusão/alteração de descontos por antecipação cujo período de validade coincida com outro desconto já associado ao mesmo campus/polo da matriz aplicada.

**Desconto por antecipação associado ao campus/polo da matriz aplicada somente no ensino superior:** Será disponibilizado o anexo "Desconto por antecipação por campus/polo da matriz aplicada" (**válido somente para o ensino superior**) no cadastro de campus/polo da matriz aplicada e permissões conforme telas abaixo:

O campus/polo a ser considerado para cálculo do valor do desconto por antecipação será o campus/polo "Ativo" vinculado ao curso do aluno (Cursos/Habilitações)

Associação de Descontos por Antecipação à Matriz aplicada

Para realizar a associação dos descontos por antecipação à **Matriz aplicada**, primeiramente é necessário que o usuário tenha permissão para esta ação no cadastro de Matriz aplicada. Confira as permissões no cadastro do Perfil do usuário (Perfil Educacional-Tags: Currículo e Oferta | Estrutura curricular | Matrizes curriculares | Matrizes aplicadas | Desconto por Antecipação por matriz aplicada | Incluir | Excluir | Editar devem estar habilitadas).

Feito isto, selecione a matriz aplicada e acesse Anexos | Desconto por antecipação por matriz aplicada e utilizando o botão 'Incluir', associe os descontos por antecipação desejados. Neste momento, serão feitas validação de vigência entre os descontos por antecipação associados a esta matriz aplicada, não sendo permitida a inclusão/alteração de descontos por antecipação cujo período de validade coincida com outro desconto já associado à esta matriz aplicada.

**Desconto por antecipação associado à matriz aplicada:** Será disponibilizado o anexo "Desconto por antecipação por matriz aplicada" na matriz aplicada e permissões conforme telas abaixo:

Associação em Lote de Descontos por Antecipação a Matriz Aplicada ou Campus/Polo

Este processo permite associar de forma dinâmica um ou vários Descontos por Antecipação simultaneamente a várias Matrizes Aplicadas ou Campus/Polo.

O processo está disponível no TOTVS Educacional, no menu 'Currículo e Oferta / Matrizes Curriculares | Processos | Associar descontos por antecipação para Matrizes Aplicadas ou Campus/Polo'.

**Associar descontos por antecipação em:**

Esta opção identifica a qual informação o sistema irá associar o Desconto por Antecipação.

* *Matriz Aplicada*: se selecionada esta opção, serão apresentadas as Matrizes Aplicadas selecionadas anteriormente na visão de dados.
* *Campus/Polo da Matriz Aplicada*: se selecionada esta opção, serão apresentados os Campus/Polo das Matrizes Aplicadas selecionadas anteriormente na visão de dados.

Caso na listagem apresentada exista alguma informação para a qual não deseja que a associação seja realizada, selecione a mesma e clique no botão '*Remover*'.

**Desconto por Antecipação:**

Serão apresentados todos os Descontos por Antecipação cadastrados no TOTVS Educacional.

Se desejar selecionar os Descontos por Antecipação através de filtros específicos, clique no botão com ícone do Filtro e selecione-o conforme necessitar.

Caso na listagem apresentada exista alguma informação para a qual não deseja que a associação seja realizada, selecione a mesma e clique no botão '*Remover*'.

**Sobresser vínculos existentes**

Essa opção é para informar se eventuais vínculos pré-existentes serão sobrescritos ou não.

Ao clicar em '*Executar'*, o sistema realizará automaticamente a associação entre a Matriz Aplicada / Campus/Polo e o (s) Desconto (s) por Antecipação apresentados na tela, e ao final será exibido um log informativo, onde consta quais e quantos vínculos foram feitos e quais e quantos não foram e os motivos da eventual não associação

Pronto, feitas as devidas associações dos Descontos por Antecipação nos locais desejados, no momento da geração dos lançamentos e também da baixa dos boletos referentes aos serviços prestados, os Descontos por

Antecipação serão calculados conforme características e regras de cada um.

Segue abaixo exemplo da utilização do processo:

(Permissão no perfil do usuário)

Assim como na associação direta nos cadastros a associação de desconto por antecipação via processo também validará inclusões de descontos por antecipações com vigências sobrepostas.

Cada associação de desconto por antecipação a algum item: matriz aplicada, campus/polo ou contrato do aluno, validará a vigência do desconto por antecipação que está sendo associado. Não serão permitidas inclusões de descontos por antecipações com vigências sobrepostas.

Exemplo:

       (Associação inválida  - Vigências sobrepostas em 01/2017)

* Campus 9
* Associação 1: Desconto por antecipação de   a
* Associação 2: Desconto por antecipação de   a

       (Associação válida  - Vigências não sobrepostas)

* Campus 9
* Associação 1: Desconto por antecipação de   a
* Associação 2: Desconto por antecipação de   a

Essa validação impedirá que Descontos por Antecipação com conflito de vigência sejam associados a uma mesma matriz aplicada ou a um campus/polo de uma matriz aplicada.

 Veja Também

---
