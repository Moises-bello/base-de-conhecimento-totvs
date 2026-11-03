---
content_hash: adf96bd340957c77cacce6b85508a3b3b33951e473b5cb80d4d9abef9b668877
fetched_at: '2026-06-29T00:09:12.129157+00:00'
page_id: '415715038'
product: rm
source: tdn-rm
title: RMPES00003_Como Fazer - Lançamento de benefícios na folha de pagamento do funcionário.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415715038
version: 3
---

# Lançamento de Benefícios.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Gestão de Pessoas |
| **Módulo:** | Gestão de Pessoas |
| **Função:** | Valorização | Benefícios e Remuneração Variável. |

Cadastrar Benefício

Totvs Gestão de Pessoas.

Valorização | Benefícios e Remuneração Variável.

Cadastrar um benefício, informando os campos necessários para o cálculo do valor.

Aba Identificação:

Para o correto cálculo dos valores, além dos campos de identificação, os seguintes campos devem ser preenchidos: Periodicidade, Data Início da Vigência, Tipo de Benefício, Objetivo do Benefício e Categoria do Benefício. Quando o benefício for de natureza monetária é necessário que a *flag* esteja marcada.

No caso de benefícios monetários, é necessário preencher as informações da aba parâmetros de cálculo.

* Origem Valor: Informar um valor ou fórmula para o cálculo do Benefício;
* Gerar Ficha Financeira: Permite que o benefício seja lançado na folha de pagamento;
  + Tipo de Lançamento: Selecionar o tipo de lançamento para o benefício. Em qual tipo de lançamento o benefício será lançado. Para gerar o cálculo do benefício no Totvs Folha de Pagamento, o tipo de lançamento deverá ser igual ao tipo informado neste cadastro;
  + Evento Funcionário: Informar um evento do tipo Provento ou Desconto que será lançado na folha do funcionário;
  + Evento Empresa: Informar um evento do tipo base de cálculo que corresponda ao valor de contribuição da empresa. Quando o evento do Funcionário for tipo Provento não é necessário preencher o evento empresa. Somente se fará necessário quando o evento do funcionário for de Desconto e desejar demonstrar no contracheque do funcionário a base de cálculo (valor pago pela empresa);
* Fórmula percentual do valor para Evento Funcionário: Esta formula deverá ser informada quando o evento do funcionário e o evento da empresa forem informados. O valor retornado pela fórmula será o percentual do benefício descontado no evento do funcionário. O restante do valor será demonstrado no evento da empresa.
  + Ex.: Fórmula retorna 30 30% do benefício será descontado do funcionário e 70% do benefício a empresa irá subsidiar. (Quando nenhuma fórmula é informada, todo o valor do benefício irá para o evento do funcionário mesmo que o benefício possua evento da empresa e do funcionário);
* Benefício Extensivo a dependentes: Caso o benefício seja extensivo a dependentes, a opção “Extensivo a dependentes” deverá ser marcada. E através de fórmulas é possível validar os dependentes que receberão o benefício e o percentual do valor benefício que o dependente receberá.
  + O campo Fórmula Percentual do Valor Dependente tem o mesmo funcionamento do campo Fórmula percentual do valor para Evento Funcionário, porém o percentual incide sobre o benefício lançado para o dependente.

Observação: Todas as informações relacionadas aos benefícios do dependente são redirecionadas à folha do funcionário.

Vinculação do benefício.

Após parametrizar o benefício é necessário realizar a vinculação desse benefício. A vinculação pode ser feita por Seção, Cargo/Função ou Funcionário/Dependente.

Acesse Valorização | Vinculação de benefícios.

Um assistente será executado para realiza a vinculação.

Ao vincular o benefício, o usuário tem a opção de de marcá-lo como obrigatório, o que significa que o mesmo deverá ser lançado obrigatoriamente na folha do funcionário.

Lançamento de Benefícios.

No Assistente de Lançamento de Benefícios os benefícios serão lançados para o funcionário/dependente. Informações como valor e data de lançamento deverão ser informados. Os benefícios poderão ser lançados para a competência atual e competências futuras, lançamentos anteriores a competência atual não podem ser inseridos nem modificados.

Acesse Valorização | Vinculação de benefícios.

O lançamento **não leva os valores para a folha de pagamento**, somente faz a integração entre o Totvs Gestão de Pessoas e o Totvs Folha de Pagamento. Após o lançamento do benefício é necessário acessar o Totvs Folha de Pagamento e realizar o cálculo do benefício.

Cálculo de Benefícios

Totvs Folha de Pagamento.

Folha Mensal | Lançamentos | Cálculo de Lançamentos de Benefício.

Neste processo os benefícios a serem lançados devem ser calculados para o funcionário. A Data Limite corresponde à data referência a ser verificada no lançamento do benefício, ou seja, se para a data limite informada não existir nenhum lançamento o benefício não será calculado.

Após a realização da rotina de cálculo, os valores dos eventos recuperados a partir dos lançamentos dos benefícios para os Funcionários selecionados poderão ser recalculados enquanto não forem lançados para o envelope através do Grupo de Eventos.

Observação: Somente benefícios monetários serão exibidos no cálculo de benefícios.

Lançamento Eventos de Integração

Folha Mensal | Lançamentos | Grupo de Eventos.

No Grupo de Evento a opção “Lançar Eventos da Integração com Outros Aplicativos” deve ser marcada e é preciso informar o comportamento: A (Adicionar), I (Ignorar) ou S (Substituir) e selecionado o(s) funcionário(s) cujo benefício foi calculado.

Na Aba “Integração com Outros Aplicativos” o tipo de lançamento informado no cadastro do benefício – Aba “Parâmetros de Cálculo” deve ser igual para que o benefício seja lançado na folha do funcionário.

Ao realizar o lançamento do evento os benefícios calculados para o funcionário serão lançados em sua folha com os respectivos eventos relacionados ao benefício.
