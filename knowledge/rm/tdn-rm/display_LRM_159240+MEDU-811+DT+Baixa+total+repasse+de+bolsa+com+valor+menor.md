---
content_hash: c9bc0bfd476a328095dda8e0968c936dc91dfbf92fbf79a1e312579572ec8e5e
fetched_at: '2026-06-29T00:08:27.829639+00:00'
page_id: '271646978'
product: rm
source: tdn-rm
title: 159240 MEDU-811 DT Baixa total repasse de bolsa com valor menor
type: documentation
url: https://tdn.totvs.com/display/LRM/159240+MEDU-811+DT+Baixa+total+repasse+de+bolsa+com+valor+menor
version: 114
---

# Repasse de Bolsa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Repasse de Bolsa* | *Repasse de Bolsa* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | |  |  | |  |  | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Tickets relacionados** | *159240* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** | Todos |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |

## Descrição

O processo do Repasse de Bolsa tem como objetivo identificar os repasses cadastrados realizando as baixas automaticamente dos lançamentos do sacado, e conforme os valores dos repasse o sistema vai gerar novos lançamentos a pagar ou a receber para o responsável financeiro do aluno.

**Cenário:**

Identificamos um cenário em que foi cadastrado um repasse com valor inferior ao valor da bolsa do aluno.

Exemplo:

Valor da mensalidade: R$500,00

Valor da bolsa: R$ 50,00 (10%)

Valor do repasse: R$ 25,00

O comportamento normal do processo de repasse é baixar o lançamento do sacado e caso o valor do repasse seja inferior ao valor da bolsa o sistema deverá gerar uma parcela extra, e consequentemente um lançamento financeiro a pagar para o responsável financeiro do aluno.

Porem para o cenário acima o sistema não poderá baixar o valor total do lançamento do sacado, o correto será o sistema baixar o lançamento conforme o valor do repasse e lançar a diferença em outro campo no lançamento financeiro.

**Melhoria:**

Para contemplar o cenário acima realizamos uma melhoria no processo do Repasse de Bolsa do módulo TOTVS Gestão Educacional  para que o lançamento baixado seja baixado com o valor do repasse, e a diferença do valor do repasse entre o valor da bolsa vai ser controlada em um campo especifico no lançamento financeiro.

Para esta demanda iremos utilizar o recurso do “Valor de integração” disponível no módulo TOTVS Gestão Financeira.

O “Valor de integração” é um campo totalmente parametrizável pelo usuário em que definimos qual o comportamento do mesmo em relação ao lançamento financeiro (acrescenta ou desconta).

**Parametrização:**

Nos parâmetros do  Educacional  >> Integração >> Financeiro >> Fin – Geral 4/4:

Será necessário identificar o campo “Valor de integração” que  será responsável em realizará o controle do valor quando houver um repasse de bolsa a menor.

Regras:

* O campo valor de integração dever ser do tipo “Desconta” e não poderá ser calculado por fórmula, pois a responsabilidade de controle do valor é do processo.

Observação:

* Atualmente o cadastro de valores de integração não está disponível nos menus do sistema TOTVS Gestão Financeira, portando o usuário deverá realizar o cadastro pelo próprio loookup de seleção disponível nos parâmetros do Educacional . Ao acionar pesquisa clique no ícone “Novo” e cadastre um novo campo.  
    
  Para realizar este cadastro é necessário que o usuário tenha permissão de manutenção neste cadastro (confira as permissões do perfil).
* Após parametrizar este item se houver alguma baixa do lançamento financeiro utilizando este campo não será possível alterar a parametrização.

**Processo – Repasse de Bolsa**

O processo de repasse foi evoluído somente em dois pontos:

1)      Quando o valor do repasse for menor que o valor da bolsa

Quando o valor do repasse for menor que o valor da bolsa, o sistema vai baixar o lançamento do sacado conforme o valor do repasse, e a diferença entre o valor da bolsa e o valor repasse será lançado no campo do valor de integração (conforme parametrizado) do item de baixa do lançamento financeiro.

2)      Opção “Não calcular juros e multas ao baixar o lançamento”

**Opção “Marcada”:**

Será considerado como data da baixa a data de vencimento do lançamento, desta forma o lançamento será baixado conforme a data do vencimento.

**Opção “Desmarcada”**

Será considerado como data da baixa e data base para os cálculos a data de repasse informada no processo.

As demais funcionalidades e comportamento deste processo não foram alteradas.

## Importante

* Se existir o cenário em que o valor do repasse for menor que o valor da bolsa, será obrigatório a parametrização identificando o campo valor de integração que irá controlar o repasse de bolsa a menor.
* Caso o módulo TOTVS Gestão Financeira esteja parametrizado para realizar os cálculos da baixa por proporção o sistema não permitirá está parametrização no Educacional, pois os serviços não foram evoluídos para tratar este cenário. Caso tenhamos este cenário os procedimentos deverão ser realizados manualmente e deverá ser acionado o suporte para que seja aberto uma solicitação de melhoria.

## Procedimento para Utilização

**Parametrização:**

Nos parâmetros do  Educacional  >> Integração >> Financeiro >> Fin – Geral 4/4:

Antes de cadastrar o valor de integração é necessário acessar o perfil do usuário e habilitar as permissões para manutenção no cadastro.

Cadastrando "Valor de integração"

Exemplo:

Vamos realizar o processo de repasse conforme as informações abaixo:

Valor da mensalidade: R$500,00

Valor da bolsa: R$ 50,00 (10%)

Repasse: R$ 25,00

Apos a execução do repasse veja como ficou a baixa do lançamento do sacado:

divs
