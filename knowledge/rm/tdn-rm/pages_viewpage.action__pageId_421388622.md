---
content_hash: 4801b86dfd13fd13a3a2add3efec7425edb16980f31088a549583e126fd734ca
fetched_at: '2026-06-29T00:09:17.710778+00:00'
page_id: '421388622'
product: rm
source: tdn-rm
title: Relatório de Fluxo de Caixa 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388622
version: 6
---

O Fluxo de Caixa é o instrumento de projeção que possibilita determinar as necessidades financeiras, a curto, médio e longo prazo da empresa, permitindo de forma transparente e eficaz visualizar os momentos em que ocorrerão as diversas entradas e saídas de caixa. Permite que o administrador planeje, organize, coordene, dirija e controle os recursos financeiros de sua empresa.  
 O fluxo de caixa permite a avaliação das alternativas de investimentos e das razões que provocam as mudanças da situação financeira da empresa, as formas de aplicação do lucro gerado pelas operações e os motivos das eventuais variações do capital de giro. Por isso, as informações do fluxo de caixa de uma empresa são úteis para proporcionar aos usuários das demonstrações financeiras uma base para avaliar a capacidade de a empresa gerar caixa.

**Dica**

A permissão para visualização de informações ou realização de processos deste módulo pode ser configurada por Usuário ou por Perfis, no menu Segurança dos Serviços Globais.

**Pré-requisitos para o Fluxo de Caixa**

Para a utilização do Fluxo de caixa deve-se possuir natureza Orçamentária Financeira cadastrada na base de dados e o sistema parametrizado para permitir rateio por Centro de Custo/Natureza Orçamentária/Financeira:  
 A Natureza Orçamentária Financeira define a origem do capital em questão, se ele é um recebimento ou se é uma cobrança. Ela é quem define quais são as entradas e saídas do Fluxo de Caixa, é utilizada no rateio de lançamentos financeiros e no extrato de caixa. Pode ser definida como default em Aplicações Financeiras no Cliente/Fornecedor.  
 O código dessa tabela é definido através de máscara, criando-se uma estrutura hierárquica. É possível definir defaults contábeis. Possui Controle de último nível, ou seja, critério de sintético e analítico para definir quais itens poderão receber lançamentos.

**Classificação de tipos para definir Receita / Despesa.**

Exemplo de cadastro de Natureza:  
 Código = 01; Descrição = Receitas; Natureza = A Receber; Sintético/Analítico = Sintético;  
 Código = 01.001; Descrição = Receitas; Natureza = A Receber; Sintético/Analítico = Analítico;

**Observação**

Ao incluir um lançamento e informar um rateio por centro de custo e Natureza Orçamentária Financeira, o sistema exibirá somente as naturezas Analíticas e que possuírem natureza igual a do lançamento (A pagar/A Receber).

**Mudança de comportamento relacionado ao campo Previsto.**

Com a alteração na exibição dos valores no fluxo de caixa, o saldo Inicial só será preenchido com valores que não são apresentados nas linhas, ou seja, dentro do período selecionado.  Os valores previstos de linha, das naturezas que estão dentro do período selecionado, não serão repassados para o saldo inicial, dos próximos períodos, facilitando assim o discernimento de valores na apresentação da planilha.

**Exemplo:**

Criado lançamento a receber de valor 100,00 no dia 12/09/2018. Criado um lançamento a receber de valor 100,00 no dia 13/09/2018. Baixado um lançamento a receber no valor 100,66 no dia 14/08/2018.  
A partir dessas informações perceba que ao gerar o relatório, no período do dia 12/09/2018 até 16/09/2018,  poderemos visualiza-lo da seguinte forma:

* O valor 100,00 constará de uma operação do dia 12/09/2018 e que resulta então, no saldo final de 100,00, para este dia.
* O saldo final do dia 12/09, não será repassado para o saldo inicial do dia 13/09. O valor de 200,00 já contará em seu valor previsto.
* O valor de 100,66 será representado de forma diferente dos valores previstos, no exemplo acima, por constar somente o saldo realizado daquela data em questão, no dia 14/09/2018. Desta forma, o valor final é sempre reexibido no saldo inicial do próximo dia, 15/09/2018.

**Parametrização do Fluxo de Caixa**

A parametrização do Fluxo de caixa é relacionada ao parâmetro que define a utilização do rateio por Centro de Custo/Natureza Orçamentária Financeira. Deve-se definir a forma como o sistema irá utilizar o rateio e sua obrigatoriedade.  
 Ambiente | Parâmetros | Gestão Financeira | Contas a Pagar | Manutenção de Lançamentos | Lançamento | Recursos Adicionais - Rateio por Centro de Custo/Natureza Orçamentária Financeira.

Rateio por Centro de Custo/Natureza Orçamentária Financeira

Define o uso do rateio por Centro de Custo/Natureza Orçamentária Financeira. Permite as opções:

* Não Usar Rateio;
* Natureza;
* Centro de Custo;
* Ambos.

Obrigatoriedade

Define a forma de obrigatoriedade dos rateios definidos nos parâmetros anteriores. Permite as opções de obrigatoriedade:

* Não Obrigatório;
* Obrigatório sempre;
* Obrigatório a Receber;
* Obrigatório a Pagar.

**Visão do Fluxo de Caixa**

A visão do Fluxo de Caixa é baseada no modelo clássico de Fluxos de Caixa utilizando planilhas eletrônicas. O Gestão Financeira, integrado ao Microsoft Excel, exibem uma planilha diretamente relacionada aos Lançamentos Financeiros e Extratos de Caixa, sendo possível salvar como Excel através do ícone disponível na interface.

Para visualizar o relatório de Fluxo de Caixa basta acessar o menu Gestão Financeira | Relatórios | Fluxo de Caixa e preencher os dados para sua geração.

Veja Também

Informações Complementares

* [Procedimento para gerar o Fluxo de Caixa](http://tdn.totvs.com/x/hGxJ)
