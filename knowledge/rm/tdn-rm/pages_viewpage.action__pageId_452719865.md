---
content_hash: 4b4b6b5615575590e0bcf5bd62ad650a81a925ba1e15ff596145f0d809e84a0c
fetched_at: '2026-06-29T00:10:10.528891+00:00'
page_id: '452719865'
product: rm
source: tdn-rm
title: Pasta Pareceres - Requisição de Substituição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719865
version: 2
---

**Pasta Pareceres - Requisição de Substituição**

Os pareceres tem como objetivo registrar as alterações realizadas na requisição de Substituição. Cada parecer estará sempre vinculado a uma única requisição, porém, uma requisição poderá ter diversos pareceres. Para acessar o parecer de um requisição de Substituição o usuário deverá acessar a requisição desejada, Anexos | Parecer de Substituição.

**Pasta Identificação - Parecer da Requisição de Substituição**

Na pasta Identificação os seguinte dados devem ser informados:

**Emitido em -** Este campo exibirá a data e hora da emissão do parecer e não poderá ser alterado.

**Status -** Exibirá o status que a requisição assumiu conforme definição do fluxo de aprovações, porém, se a requisição não tiver sido incluída no fluxo, ou seja, quando o controle estiver sendo feito manualmente, este campo poderá ser alterado. Esta alteração será possível apenas no Totvs Gestão de Pessoas.

**Parecer emitido -** Deve conter o texto do parecer emitido pelo usuário.

**Responsável -** Somente podem ser selecionados chefes das seções da coligada na qual o usuário está logado. Para informações relacionadas aos chefes das seções verifique o cadastro de chefes e supervisores.

**Filial/Função e E-mail -** Após preenchimento do campo "Responsável" os dados relacionados a estes campos serão exibidos automaticamente. O campo "Filial/Função" deve exibir o nome da filial seguido do nome da função de lotação do funcionário selecionado no campo "Responsável". Em caso de alteração do nome do responsável, o conteúdo desde campo deverá ser automaticamente atualizado. A informação do campo "E-mail" deverá ser automaticamente atualizada com o e-mail que constar no cadastro do responsável indicado. Para confirmar esta informação acesse Acompanhamento | Pessoas | Pasta Identificação. 

**Pasta Dados da Requisição - Substituição**

Na pasta Dados da requisição podem ser visualizados/alterados os seguintes dados:

**Substituição de -** Exibirá o nome do funcionário ou ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Previsão -** Exibirá a mesma data prevista da requisição pai que está vinculada à requisição de substituição. Este campo poderá ser alterado ao criar um novo parecer para a requisição.

**Filial -** Exibirá a mesma filial da lotação do funcionário ou do ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Seção -** Exibirá a mesma seção da lotação do funcionário ou do ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Função -** Exibirá a mesma função do funcionário ou do ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Este campo não é editável.

**Tabela -** Caso esteja configurada a utilização das tabelas salariais será exibido o nome da tabela associada à seção e função, previamente selecionadas. Para verificar esta configuração acesse: Opções | Parâmetros | RM Vitae | Pasta "Geral" | Pasta "Validações".

**Nível e Faixa -** Após o preenchimento dos campos "Seção" e "Função" e se o parâmetro "Considerar os salários das tabelas salariais" estiver marcado, serão apresentados o nível e a faixa salarial do funcionário ou do ex-funcionário existente na requisição pai que está vinculada à requisição de substituição. Estes campos poderão ser alterados ao criar um novo parecer para a requisição. Para saber como funciona a vinculação de tabelas salariais acesse: Gerência de RH | Cargos e Salários | Tabelas Salariais | Vinculação.

**Salário -** Com a utilização de tabela salarial, o salário proposto será automaticamente preenchido com base na faixa salarial selecionada. O campo salário será habilitado se a empresa não trabalhar com tabelas salariais e, neste caso, o valor do salário deverá ser informado diretamente neste campo, ou, caso seja parametrizada a utilização das tabelas salariais, o parâmetro "Não permitir alterar diretamente o salário" deverá estar desmarcado, para que este campo permita alterações. Este campo poderá ser alterado ao criar um novo parecer para a requisição. Se houver alteração do nível salarial ou da faixa salarial este campo também sofrerá alterações, o conteúdo deste campo assume o valor refente à tabela salarial.
