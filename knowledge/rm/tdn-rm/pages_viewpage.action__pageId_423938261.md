---
content_hash: a3e723fd0390b4deadd8417c0d3a44917ae36dc4ed1f2f11615191cfecd211d0
fetched_at: '2026-06-29T00:09:26.105690+00:00'
page_id: '423938261'
product: rm
source: tdn-rm
title: Clientes/Fornecedores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938261
version: 14
---

Nesse anexo é possível relacionar Clientes/Fornecedores ao produto, os dados informados podem ser utilizados como default para inclusão de movimento com o Cliente/Fornecedor relacionado e que possua o produto em questão como item de movimento. Os Clientes/Fornecedores relacionados também podem ser usados na Cotação ao utilizar o parâmetro "[Somente Cotar Produtos Fornecidos](http://tdn.totvs.com/display/LRM/ER_Importar_Cotacoes_via_Planilha_Excel)" através dos parâmetros do TOTVS Gestão de Estoque, Compras e Faturamento | Gestão de Compras | Cotação | Definições Gerais 2/5.

**Cód. Cliente/Fornecedor**: Deve ser informado o código do cliente/fornecedor relacionado ao produto.

**Cód. no Cliente/Fornecedor**:\* Esse campo é opcional, pode ser informado para identificar o Código do Produto no Cliente/Fornecedor. O Código do Produto no Cliente/Fornecedor é único para cada Cliente/Fornecedor, exemplo:

1
incomplete
Um produto possui o "Fornecedor A" relacionado em seu anexo de Cliente/Fornecedor, neste fornecedor o "Cód. no Cliente/Fornecedor" é "001", nesse caso, para um outro produto que também possua o "Fornecedor A" relacionado,  não é permitido cadastrar no campo "Cód. no Cliente/Fornecedor" o código{\*} "{\*}001".

**Ativo**: Ao fazer uma Cotação para o produto, somente são sugeridos os fornecedores ativos para aquele produto. Quando selecionado mais de um produto para fazer a Cotação, se o fornecedor estiver ativo para um dos produtos selecionados, ele será apresentado como sugerido. Entretanto, ao calcular o Quadro Comparativo, o Fornecedor será apresentado como Inativo para os para os produtos que não estão com a flag "Ativo" marcada para aquele Fornecedor.

**Prioritário para Cotação**: Quando um Fornecedor está definido como prioritário para a Cotação, o mesmo é apresentado prioritariamente na etapa de Escolha de Fornecedores no Assistente de Inclusão de Cotação. Para que essa consistência seja realizada, o parâmetro "Usar Fornecedor Prioritário" \[Parâmetros | Gestão de Estoque, Compras e Faturamento| Gestão de Compras | Cotação | Fornecedores 2/5\] deve estar marcado.

**Fornecimento %**: Campo informativo para controle do percentual de fornecimento do Fornecedor para o Produto, podem ser informados valores entre 0 e 100. Pode ser utilizado, por exemplo, para guardar quanto cada Fornecedor fornece do produto.

**Fator de Embalagem**: Este fator representa a quantidade mínima do produto a ser comprada no fornecedor, exemplo:

2
incomplete
Se a quantidade mínima de um produto para compra no Fornecedor for caixa com 100 unidades, 100 seria o fator da embalagem.

**Data de Validade**: Se refere a data de validade do preço do Fornecedor para o produto. Ao informar e salvar uma data é salvo na aba Histórico o Valor e o Número do Contrato referente à aquela data. A cada alteração da data de validade, o sistema guardará na aba Histórico o valor anterior, caso queira retornar para o cliente um valor com data de validade anterior, pode-se utilizar o processo "Produtos - Restaurar Preços de Cli/For" acessado pelo menu Utilitários | Mais...

**Moeda do Cliente/Fornecedor**: Quando informada uma moeda nesse campo, ao incluir uma movimentação com o Cliente/Fornecedor em questão é realizada a conversão do Valor conforme a Cotação da Moeda informada, exemplo:

3
incomplete
No dia 20/08 a moeda "US$ - Dólar" tem a cotação 4,00 e no campo valor está informado 5,00. Se na inclusão do movimento o preço do item for o preço buscado no cliente/fornecedor, ao salvar o movimento o preço unitário do produto será R$ 20,00.

**Valor**: Pode ser informado o preço unitário do produto no cliente/fornecedor. Este valor pode ser utilizado no preço do item movimento, para isto, nos parâmetros do tipo de movimento, pasta Item | Preços, deve-se indicar no campo "Buscar Preço em" a opção "Cliente/fornecedor". Assim, sempre que incluir um movimento para este Cliente/Fornecedor e indicar este produto como item do movimento, o sistema buscará como preço unitário do item o valor indicado neste campo valor.

**Desconto %**: Ao informar o percentual de desconto, o percentual de desconto é aplicado no item do movimento sempre que incluído o produto para esse Cliente/Fornecedor, para isto, nos parâmetros do tipo de movimento, pasta Item | Valores Financeiros 1/2, deve estar habilitada a opção "Utilizar Desconto".

**Número Contrato**: Caso este produto neste cliente ou fornecedor tenha um vínculo através de um contrato, indique se desejar o número do mesmo. Essa informação será associada ao Fornecedor juntamente com o Valor e Data de Validade, e o registro será salvo na aba Histórico. Esse Número do Contrato é independente do Módulo de Contratos do sistema (Menu Contratos | Manutenção de Contratos)

**Caminho da Imagem**: Se existir um arquivo de imagem do produto no cliente/fornecedor, informe neste campo o caminho, ou seja, onde se encontra o arquivo e o nome do mesmo. Este campo é apenas informativo, portanto, não é possível buscar esta imagem diretamente pelo sistema.

**Campo Livre**: O campo livre pode ser utilizado para informar dados adicionais para o Cliente/Fornecedor. É um campo somente informativo.

**IRRF / INSS**: Os dados abaixo são utilizados nas rotinas fiscais e geração de impostos para o Financeiro.

**Código de Receita**: Informe neste campo o código do IRRF no produto para o cliente/fornecedor.

**Base IRRF %**: Informe neste campo o percentual a ser utilizado como Base do IRRF.

**Código de Receita no INSS**: Informe neste campo o código do INSS no produto para o cliente/fornecedor.

***Observação***: Os códigos da receita devem ter sido previamente cadastrados no menu Cadastros | Fiscais | Mais... | IRRF e Cadastros | Fiscais | Mais... | INSS/PJ. Estes códigos deverão ser informados seguindo as normas da Receita Federal.
