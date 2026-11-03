---
content_hash: b9d46e8f22a9856d2c7b3f7bce10bb2def184bf964650d3df5a4daa28326f514
fetched_at: '2026-06-29T00:09:32.404280+00:00'
page_id: '425458841'
product: rm
source: tdn-rm
title: Cadastrar Descontos por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458841
version: 19
---

---

Para realizar o cadastro de 'Desconto por Antecipação', primeiramente é necessário que o usuário tenha permissão para manutenção neste cadastro. Confira as permissões no cadastro do Perfil do usuário (Perfil Educacional-Tags: Financeiro/Contábil | Geração | Financeiro | Desconto por Antecipação | Incluir | Excluir | Editar devem estar habilitadas).

Cadastro do Desconto por Antecipação

Inicialmente cadastra-se o Desconto por Antecipação que servirá como um agrupador de vários itens (ou faixas) de desconto que posteriormente deverão ser cadastrados.

Para cadastrá-los no TOTVS Educacional, acesse o menu '*Financeiro / Contábil | Geração | Financeiro | Desconto por Antecipação*', o desconto por antecipação tem os seguintes campos:

* **Código**: Informa o código do desconto por antecipação que é inserido automaticamente pelo sistema.
* **Descrição**: Informa a descrição do desconto por antecipação.
* **Período de Vigência**: Informa o período de vigência do desconto por antecipação, porém esse período é opcional.   
  Pode ser informada somente a data de início ou a data final de vigência. Caso não seja informado, o desconto por antecipação sempre será válido.  
  + **Data Início de Vigência**: Informa a data inicial de vigência do desconto por antecipação.
  + **Data Final de Vigência**: Informa a data final de vigência do desconto por antecipação.

Desconto por Antecipação com período de vigência.

Desconto por Antecipação sem período de vigência.

- O sistema permite o cadastro de vários Descontos por Antecipação com vários períodos de vigência sem fazer neste momento validações entre os períodos. A validação dos períodos de vigência será feita no momento da associação dos descontos nos contratos, nos campus/polos das matrizes ou nas matrizes aplicadas, não permitindo que sejam feitas associações de descontos com vigências que coincidam ou sejam sobrepostas.

Cadastro do Item do Desconto por Antecipação

Após o cadastro do Desconto por Antecipação é necessário cadastrar os Itens (ou Faixas) de descontos, contendo cada um, definições específicas das regras para aplicação dos Descontos por Antecipação, para isto acesse o menu '*Financeiro / Contábil | Geração | Financeiro | Desconto por Antecipação | Anexos | Item do Desconto por Antecipação'* e cadastre os vários itens que irão compor cada Desconto por Antecipação.

O item do desconto por antecipação tem os seguintes campos:

* **Código**: Informa o código do item do desconto por antecipação, e é inserido automaticamente pelo sistema.
* **Desconto** por Antecipação: Informa o desconto por antecipação ao qual o item pertence, e é inserido automaticamente pelo sistema.
* **Descrição**: Informa a descrição do item do desconto por antecipação.
* **Tipo de Desconto**: Informa se o desconto será um valor ou um percentual sobre o valor original do lançamento.
* **Tipo Limite Desconto**: Informa o tipo de limite de aplicação do desconto. O tipo limite pode ser:
  + **Dia Fixo**:  Informa o dia fixo de limite que será utilizado para calcular a data limite do item de desconto que considerará esse dia limite / mês da data de vencimento / ano da data de vencimento. Se o dia fixo for maior do que o último dia do mês, esse último dia do mês é que será considerado.
  + **Dia Útil**: Informa o dia útil do mês da data de vencimento que será utilizado para calcular a data limite do item de desconto. A data calculada será <dia útil calculado> / <mês da data de vencimento> / <ano da data de vencimento>. Se o dia útil calculado for maior do que o último dia do mês, esse último dia do mês é que será considerado. O sistema considerará o calendário selecionado na Filial do lançamento. Caso não exista calendário selecionado na Filial, o sistema irá verificar o calendário nos parâmetros do TOTVS Gestão Financeira parâmetro: "Calendário Oficial → Calendário Oficial".
* **Valor do Desconto**: Informa o valor ou percentual do desconto por antecipação a ser aplicado conforme configuração no campo "*Tipo de Desconto*".
* **Dia Útil/Dia Fixo**: Informa a quantidade de dias fixos ou dias úteis a ser aplicada no desconto conforme configuração do campo "*Tipo Limite Desconto*".

**Importante:**- Após cadastrarem os Descontos por Antecipação e os seus respectivos Itens (ou Faixas) do Desconto por Antecipação é necessário associá-los à matriz aplicada ou campus/polo da matriz ou ainda aos contratos dos alunos.

- Para flexibilizar ainda mais a aplicação dos Descontos por Antecipação, eles somente serão aplicados aos boletos cujos *serviços* tiverem a opção '**Considera desconto por antecipação**' marcada, portanto verifiquem se esta opção está devidamente marcada nos cadastros dos respectivos  para os quais desejam que este benefício seja concedido.

Veja Também

---
