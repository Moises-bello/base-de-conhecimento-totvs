---
content_hash: 8ddf68168796c63921fd43a57e27ac5a3a18a510778779c0aeb6b695c8961ee7
fetched_at: '2026-06-29T00:09:17.790938+00:00'
page_id: '421388651'
product: rm
source: tdn-rm
title: Cubos - Ferramentas de Análise
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388651
version: 4
---

**FINCUB0001 - Recebíveis\_Pagáveis.TotvsCube - Valores Recebíveis/Pagáveis na data vigente pelo vlr. Líquido**

O Cubo "Valores Recebíveis/Pagáveis na data vigente pelo vlr. Líquido" foi criado para visualizar os lançamentos em aberto e parcialmente baixado de um determinado período definido pelo usuário baseado na data de vencimento. Ao gerar o relatório o usuário tem flexibilidade para alterar as linhas e colunas conforme necessidade da empresa.

Para importar o relatório é necessário acessar o módulo Inteligência de Negócios | Cadastro |Cubo clicar em processo "Importação de Cubos". Após a importação o cubo estará disponível na visão. Para executá-lo selecione o mesmo, clique duas vezes e preencha os parâmetros.

O Cubo também está disponível para execução no módulo Gestão Financeira | Gestão | Ferramentas de Análise | Cubos.

**Parâmetros do cubo:**

Pagar/Receber

Para gerar o relatório com os lançamentos a receber deve ser informado "R", para os lançamentos a pagar deve ser informado "P", se desejar gerar o cubo para lançamentos a pagar e a receber deve-se informar "PR".

Data Vencimento Inicial

Informe a data de vencimento inicial que deseja realizar o filtro para o cálculo dos valores no cubo.

Data Vencimento Final

Informe a data de vencimento final que deseja realizar o filtro para o cálculo dos valores no cubo.

Coligada

Informe a(s) coligada(s) desejada(s) separando as mesmas por vírgula, por exemplo: 1,2,3

Considera Valor de Cheque Emitido

Informe "V" se deseja considerar o valor do cheque emitido no cálculo do valor líquido e "F" se não deseja considerar o valor do cheque emitido no cálculo do valor líquido.

**Exemplo**:

Um lançamento a Receber com valor do líquido de R$1.200,00, para este lançamento existe um cheque no valor de R$1.000,00.  
 Se o parâmetro informado for:

* **V** - O valor do cheque emitido será considerado e para este lançamento o valor líquido ficará R$200,00, ou seja, considerando o cheque emitido o valor a receber é R$200,00.
* **F** - O valor do cheque emitido não será considerado, ou seja, o valor líquido ficará R$1.200,00.

Se o cheque emitido for igual ao valor total não terá impacto no cálculo do valor líquido.  
 Exemplo: Se no exemplo acima o cheque fosse de R$1.200,00 o valor líquido seria apresentado R$1.200,00.  
 Após informar os parâmetros, se desejado clique na opção para salvar os mesmos, e em seguida executar, os valores do cubo serão atualizados conforme parâmetros informados.   
 Na barra de menus do cubo "Valores Recebíveis/Pagáveis na data vigente pelo vlr. Líquido" tem disponível os seguintes ícones:

"Atualizar"

Será apresentada a tela com os parâmetros para poder modifica-los.

"Exportar"

Será possível exportar o relatório gerado.

**FINCUB0002 - Valores Previstos x Realizados**

Este cubo tem como objetivo visualizar valores previstos e realizados em um período determinado, sem apresentar a obrigatoriedade de utilizar uma natureza orçamentária financeira e o centro de custo, possibilitando uma visualização mais simples mediante alguns parâmetros. Este cubo segue o mesmo padrão do primeiro cubo, porém com os campos abaixo:

* Valor Previsto na data atual (considerando o valor líquido na data atual);
* Valor Previsto no vencimento (considerando o valor líquido na data de vencimento);
* Valor Realizado (considera os valores parciais ou totalmente baixados).

**Observação**

O campo "Valor Previsto Vencimento" apresentará o valor do cálculo na data do vencimento do lançamento;  O campo "Valor Data Previsto" apresentará o valor na data informada na tela.
