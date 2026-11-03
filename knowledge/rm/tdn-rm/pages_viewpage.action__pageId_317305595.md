---
content_hash: 88c0e9d80e8bb0674fe56ad2327f77fb13a235b18e87e4b781c428cae2c82518
fetched_at: '2026-06-29T00:08:46.588249+00:00'
page_id: '317305595'
product: rm
source: tdn-rm
title: DT Revitalização da Personalização Plano de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317305595
version: 24
---

# Personalização do Plano de Pagamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Personalização do Plano de Pagamento | Personalização do Plano de Pagamento |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Plano de Pagamento* | *Plano de Pagamento* | |  |  | |
| **Cadastros Iniciais:** | *Definir na parametrização por curso o plano modelo de personalização* |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Tickets relacionados** |  |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** |  |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |

## Descrição

Realizada a revitalização do processo de personalização do plano de pagamento que é disponibilizado no contrato do aluno.

Esta revitalização tem como objetivo proporcionar melhor usabilidade ao usuário, facilitando e flexibilizando a forma de personalizar o plano de pagamento de forma rápida e prática.

## Importante

As regras já existentes na personalização do plano de pagamento não foram alteradas, tais como:

* Não será permitida a personalização se já existirem lançamentos gerados para o contrato
* As parcelas já cadastradas para o contrato serão substituídas pelas parcelas da personalização
* Serviços definidos como obrigatórios no plano de pagamento modelo não poderão ser removidos na personalização.

## Procedimento para Utilização

Abaixo apresentamos as mudanças e descreveremos as funcionalidades disponíveis na personalização.

Ao acionar a personalização o sistema vai carregar as informações conforme o plano modelo informado no cadastro de Parametrização por curso, veja o exemplo da imagem abaixo.

**>>>Adicionar / Excluir **Serviço****

Conforme a imagem acima será possível adicionar na personalização um novo serviço, ou excluir serviços já adicionados. Quando o serviço estiver parametrizado como obrigatório no plano de pagamento modelo a exclusão não será permitida.

**>>> Linha Serviço**

**Botão Novo:**Adiciona uma nova parcela para personalização ao serviço selecionado.

Regra:

* A nova parcela respeitará as informações da última parcela já adicionada dando sequência aos dados, por exemplo, se a última parcela for a de Nº 5 a nova parcela será a de Nº 6, a mesma regra se aplica ao campo "Vencimento", "Competência".

**Botão **Excluir**:**Exclui as parcelas selecionadas para o serviço corrente.

Regra:

* Serviços parametrizados como obrigatório no plano modelo não poderão ser removidos

**Qtd Parcela:** Indica a quantidade de parcelas que irão compor o serviço.

Regra:

* Campo editável
* Ao informar a quantidade de parcela o sistema automaticamente criará as parcelas para serem personalizadas.
* O valor da parcela será calculado / distribuído conforme o valor informado na coluna "Valor personalizado"

**Parcela inicial:** Indica o número da primeira parcela

Regra:

* Campo editável
* Ao informar a parcela inicial o sistema atualizará automaticamente o número das parcelas já adicionadas para o serviço

**Vencimento inicial:** Indica a data de vencimento da primeira parcela

Regra:

* Campo editável
* Ao informar o vencimento inicial o sistema atualizará automaticamente as datas de vencimento das parcelas já adicionadas

**Competência inicial:** Indica a competência da primeira parcela

Regra:

* Campo editável
* Ao informar competência inicial o sistema atualizará automaticamente as competências das parcelas já adicionadas

**Valor base:** Indica o valor total original do serviço no plano de pagamento modelo, este valor é composto do somatório das parcelas cadastradas para o serviço no plano modelo.

Regra:

* Não pode editar

**Valor personalizado:** Indica o valor que o usuário está personalizando, ou seja, é valor total do serviço que será considerado na personalização.

Regra:

* Campo editável
* Ao preencher o valor personalizado o sistema irá realizar o cálculo do valor da parcela conforme as parcelas já adicionadas no serviço, e questiona ao usuário se deseja que o sistema atualize as parcelas já adicionadas.

**Total da (s) parcela (s):** Mostra o somatório das parcelas já adicionadas para o serviço

Regra:

* Não pode editar

**Obrigatório:** Indica se o serviço está parametrizado no plano modelo como obrigatório, se sim, o mesmo não poderá ser removido.

**Origem:** Indica se o serviço foi carregado do plano modelo ou se  foi adicionado manualmente na personalização.

Regra:

Quando um serviço for adicionado na personalização, ou seja, não foi carregado pelo plano modelo o sistema mostrará a informação conforme a imagem abaixo:

**>>> Linha Parcelas (Detalhe da linha de Serviço)**

Os detalhamentos das parcelas serão listados conforme a personalização informada na linha de serviço, podendo o usuário personalizar também o detalhamento da parcela que por sua vez irá refletir automaticamente na linha do serviço.

**Nº:** Número da parcela do serviço

Regra:

* Campo editável/ Obrigatório

**Valor:** Valor da parcela

Regra:

* Campo editável/ Obrigatório quando o valor não é por crédito, coluna "Valor por crédito"
* Ao preencher atualiza automaticamente o campo "Total da (s) parcela (s)" da linha de serviço.

**Vencimento:**Data de vencimento da parcela

Regra:

* Campo editável/ Obrigatório

**Competência:** Mês e ano da competência da parcela.

Regra:

* Campo editável/ Não obrigatório

**Tipo Desconto:** Tipo de desconto, valor ou percentual.

Regra:

* Campo editável

**Desconto:** Desconto da parcela

Regra:

* Campo editável/ Não obrigatório

**Valor por crédito:** Indica se o valor da parcela será calculado por crédito

Regra:

* Campo editável
* Se a parcela for calculada por crédito, o valor não será obrigatório, e não vai fazer parte dos totalizadores da tela.

**>>> Resumo da Personalização**

O resumo da personalização apresenta os totais de toda a personalização, agrupando os totalizadores conforme a origem do serviço e obrigatoriedade, apresentando as diferenças de valores entre o plano modelo e a personalização.

Caso na personalização só tenham parcelas que serão calculadas por crédito o resumo não será apresentado.

**Origem do (s) serviço (s):** Indica qual origem do serviço está sendo totalizada

**Serviço (s) obrigatório:** Indica se o totalizador é referente ao serviço obrigatório ou não.

**Total do valor base do plano:** Somatório do valor dos serviços cadastrados no plano modelo.

**Total do valor personalizado:** Somatório do valor dos serviços personalizado pelo usuário

**Diferença (Total do valor base do plano X valor personalizado):** Quando o valor personalizado for diferente do valor base do plano modelo o sistema apresentará o valor da diferença.

Esta diferença será (-) quando o valor personalizado do contrato estiver *menor* que o valor base, indicando que ainda há valores para ser aplicado no contrato ou ao contrário, será (+), indicando que o valor personalizado do contrato está *maior* que o valor base do plano modelo.

**Aplicar valor na (s) parcela (s) selecionada (s):**Quando houver diferença entre os valores, o usuário poderá optar por realizar a distribuição desta diferença entre parcelas que deverão estar previamente selecionadas, acionando o respectivo botão. Então, se o valor parametrizado for *maior*, a diferença será (+), assim este valor será rateado e removido do valor das parcelas selecionadas eliminando a diferença.  Se o valor parametrizado for *menor*, a diferença será (-), este valor será rateado e adicionado ao valor das parcelas selecionadas eliminando a diferença.

Exemplo:

Para este exemplo temos uma diferença de -1000, neste caso podemos optar em aplicar esta diferença entre uma ou várias parcelas do contrato, para serviços obrigatório e originados do plano modelo.

Veja:

Conforme a imagem abaixo, selecionamos as parcelas de 1 a 3 para receber o ajuste da diferença.

Ao acionar o botão "Aplicar valor" o sistema apresentará a mensagem abaixo

Apos confirmação o sistema realiza a distribuição dos valore e atualizará o resumo da personalização.

**>>> Execução do processo**

Regras que restringem a execução do processo

* Nenhum serviço adicionado
* Serviços que não tenha parcelas adicionadas
* Parcelas com valores zerados
* Se no cadastro do plano de pagamento modelo o campo "Bloqueia alteração do valor base do plano de pagamento para serviços obrigatórios."" estiver marcado e existirem diferenças de valor para serviço obrigatório (apresentados no resumo), porem o usuário poderá executar o processo mesmo tendo diferenças de valores desde que marque a permissão "Permite alteração do valor base do contrato bloqueado no plano de pagamento" dos parâmetros educacionais do perfil do usuário.   
  Para maiores informações consulte o documento: [Bloqueia alteração valor base - plano de pagamento modelo](http://tdn.totvs.com/pages/viewpage.action?pageId=317306543)

## Vídeo

**Parte 1**

**Parte 2**

**Parte 2**
