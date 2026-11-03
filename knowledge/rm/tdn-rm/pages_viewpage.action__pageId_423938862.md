---
content_hash: 3b98c8bbcfbceeb2799bc30363c5d1a14c65fe32f09039889f06459ccb5a639c
fetched_at: '2026-06-29T00:09:29.284101+00:00'
page_id: '423938862'
product: rm
source: tdn-rm
title: Qualificação de Fornecedores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938862
version: 12
---

O processo de Qualificação de Fornecedores avalia os fornecedores conforme critérios específicos e pré-definidos, quanto à capacidade de fornecimento de materiais e/ou prestação dos serviços.

Existem dois critérios de qualificação distintos:

* O primeiro está ligado somente à qualificação do fornecedor, independente do produto/serviço fornecido. Esta qualificação estará relacionada ao cadastro do fornecedor, no qual terão requisitos de qualificação direcionados a apresentação de documentações como:

**-** Contrato social,

**-** Inscrição CNPJ,

**-** Certificação ISO,

**-** Certidão negativa de tributos,

**-** Experiência comprovada,

**-** dentre outros documentos.

* O segundo critério está relacionado à qualificação do fornecedor para fornecimento de determinado produto/serviço. Neste caso os produtos/serviços terão uma indicação da exigência de se comprar com fornecedor qualificado e os requisitos estarão relacionados ao fornecedor e aos fornecimentos do produto/serviço por parte desse fornecedor, como:

**-** Pontualidade nas entregas,

**-** Produtos e serviços de qualidade,

**-** Conformidade na entrega,

**-** dentre outros.

## [Requisitos de Qualificação](https://tdn.totvs.com/pages/viewpage.action?pageId=423938226)

É no cadastro de Requisitos de Qualificação,  que será definido a aplicabilidade seja no "**Fornecedor**" ou "**Produto/Fornecedor**", o tipo de cálculo da pontuação sendo, "**Manual**" ou "**Calculada**", a "**Fórmula de cálculo** **da pontuação**" e o "**Peso**" para o requisito.

Os Requisitos aplicados no **fornecedor**, com tipo de cálculo da pontuação "**manual"**, deverão ser informados manualmente no Anexo do cadastro de fornecedor | Requisitos de Qualificação do Fornecedor. Já os requisitos do tipo "**calculado**" serão carregados neste mesmo anexo de forma automática ao executar do processo "[Análise de Requisitos de Qualificação](https://tdn.totvs.com/pages/viewpage.action?pageId=423938816)".

Os Requisitos aplicados no **produto/fornecedor**, são aqueles analisados em função do relacionamento ou movimentação com o fornecedor, e sua pontuação deverá obrigatoriamente ser calculada com base em uma fórmula. Esses requisitos serão carregados automaticamente no Anexo do cadastro de Produto | Requisitos de Qualificação do Produto/Fornecedor,  após a execução do processo "[Análise de Requisitos de Qualificação](https://tdn.totvs.com/pages/viewpage.action?pageId=423938816)".

Para avaliação dos fornecedores existem dois processos que devem ser executados na seguinte ordem:

**1 -** [Análise de Requisitos de Qualificação](https://tdn.totvs.com/pages/viewpage.action?pageId=423938816)**:**Este processo calcula a pontuação dos requisitos definidos como calculados. O sistema irá executar as fórmulas cadastradas em cada requisito e atualizar seu valor nos respectivos anexos de requisitos para qualificação, seja do Fornecedor ou do Produto/Fornecedor. Ainda no anexo citado, após a execução do processo de analise do requisito, o usuário poderá alterar alguma pontuação que foi calculada caso veja a necessidade de interferir na pontuação. Realizando este procedimento, a pontuação será definida como "**Editada**".

**2 -** [Qualificação de Fornecedores](https://tdn.totvs.com/pages/viewpage.action?pageId=423938819)**:**Este processo define a pontuação da qualificação para o fornecedor, ou seja, define um valor entre 0 e 100 que posteriormente será comparado com o parâmetro de "**Pontuação Mínima para Qualificação**" o que determinará se o mesmo está qualificado para fornecer determinado produto.

Para definir esta pontuação, o sistema executa as fórmulas de qualificação parametrizadas em |04.06 - Gestão de Compras | 04.06.09 - Qualificação de Fornecedores|.

* Se a empresa utilizar o "Controle de Qualidade" por **Fornecedor**, o processo de qualificação verificará somente a fórmula para esse tipo de qualificação. O resultado desta fórmula deverá retornar um valor entre 0 e 100.
* Se a empresa utilizar o "Controle de Qualidade" por **Produto/Fornecedor**, o processo de qualificação verificará somente a fórmula para esse tipo de qualificação. O resultado desta fórmula deverá retornar um valor entre 0 e 100.
* Se a empresa utilizar o "Controle de Qualidade" por **Ambos**, o processo de qualificação verificará as duas fórmulas de forma separada e o valor definido em suas respectivas tabelas (Fornecedor ou Produto/Fornecedor). O resultado destas fórmulas deverá retornar um valor entre 0 e 100.

## Status da Qualificação:

O **Status Qualificação Calculado**, exibido virtualmente no sistema, terá as seguintes opções: "**Qualificado"** ou **"Não Qualificado".**

Após execução do processo de Qualificação, o usuário poderá alterar a pontuação calculada automaticamente pelo sistema, assim o campo "Pontuação Editada" será marcado automaticamente e o **Status Qualificação Editada**, exibido virtualmente pelo sistema, terá as seguintes opções: "**Qualificação Especial**" ou "**Bloqueado**" de acordo com a pontuação definida.

Para editar a Pontuação é obrigatório informar na Observação o motivo da edição. 

A Pontuação calculada será o campo a ser utilizado como referência para definir se o fornecedor foi qualificado.

## Cotação:

No processo de cotação de materiais e/ou serviços que exigem qualificação de fornecedores o sistema irá sugerir os fornecedores que estejam qualificados de acordo com as análises e pontuações calculadas previamente pelos processos da Qualificação de Fornecedores.

Para verificar se serão considerados fornecedores qualificados na cotação, o sistema consulta o parâmetro "**Controle de Qualidade por Fornecedor**" localizado em |04.06 - Gestão de Compras | Etapa 14 - Definições Gerais| se está parametrizado para utilizar qualificação, seja por **Fornecedor**, por **Produto/Fornecedor** ou **Ambos**.

Também será verificado nos parâmetros da cotação por filial | Definições Gerais 3/5 | se o parâmetro " Utiliza Fornecedores Qualificados", está definido para "Utilizar apenas fornecedores qualificados" ou ambos (qualificados e não qualificados).

No Registro do Orçamento do Fornecedor serão apresentados somente os produtos que estão qualificados para o fornecedor e os produtos que não exigem qualificação.

Ao gerar o Quadro Comparativo, da mesma forma como é apresentada a mensagem de que o fornecedor "Não Fornece" o produto, será apresentada uma mensagem referente a qualificação informando o status do fornecedor para cada produto, se o mesmo é "**Não Qualificado**", "**Qualificad**o" ou se "**Produto Não Exige Qualificação**".

No Cálculo do Quadro Comparativo, a qualificação irá entrar como um critério no caso de empate de fornecedores.

Caso o fornecedor que vencer a cotação não esteja qualificado e mesmo assim o usuário deseje gerar a Ordem de Compra para este fornecedor, deverá ficar registrado na cotação a justificativa desta não conformidade.

## Cotação com Central de Compras:

No processo de cotação de materiais e/ou serviços que utiliza Central de Compras e exige qualificação de fornecedores o sistema irá sugerir os fornecedores que estejam qualificados de acordo com as análises e pontuações calculadas previamente pelos processos da Qualificação de Fornecedores.

Para verificar se serão considerados fornecedores qualificados na cotação, o sistema consulta o parâmetro "**Controle de Qualidade por Fornecedor**" localizado em |04.06 - Gestão de Compras | Etapa 14 - Definições Gerais| se está parametrizado para utilizar qualificação, seja por **Fornecedor**, por **Produto/Fornecedor** ou **Ambos**.

Para utilizar a Qualificação de Fornecedores considerando os requisitos de Fornecedor, o 'Controle de Qualidade por Fornecedor' deverá estar configurado com a opção de Fornecedor na coligada centralizadora da Central de Compras. Neste caso somente serão considerados os requisitos de fornecedores analisados pela coligada centralizadora, tratando os fornecedores com uma análise de requisitos de forma global.

## Fórmulas de Qualificação de Fornecedores

A fórmula deve ser parametrizada na etapa Gestão de Compras | Qualificação de fornecedores, podendo ser utilizada na "[Qualificação por Fornecedores](https://tdn.totvs.com/pages/viewpage.action?pageId=423938819)" e na "[Qualificação por Produto/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=423938869)".

## Funções de formula envolvidas:

Estão disponíveis as seguintes funções de fórmula para auxiliar o processo de criação de fórmulas para a análise dos requisitos e qualificação dos fornecedores:

A função de fórmula **TABQUALIFICACAO** é responsável por retornar as seguintes informações:

* Código da Coligada do Fornecedor:  Exemplo de Utilização: **TABQUALIFICACAO('CODCOLCFO', 'N')**

* Código do Fornecedor:   Exemplo de Utilização: **TABQUALIFICACAO('CODCFO', 'S')**

* Coligada do contexto:   Exemplo de Utilização: **TABQUALIFICACAO('CODCOLIGADA', 'N')**

* Identificador do requisito:   Exemplo de Utilização: **TABQUALIFICACAO('IDREQUISITO', 'N')**

* Identificador do produto (No caso de Qualificação por Produto/Fornecedor):   Exemplo de Utilização: **TABQUALIFICACAO('IDPRD', 'N')**

**Exemplo de utilização:**

Esta função pode ser utilizada em uma fórmula que qualifica o fornecedor com base na última entrega dos produtos fornecidos.

Neste contexto, a função **TABQUALIFICACAO** seria utilizada para retornar a **Coligada** e o **Código do Fornecedor.**

Com base nessas informações seria utilizada uma sentença SQL que identifique a última compra e compare a "data de entrega" da mesma com "data de emissão" da Nota Fiscal. Se houve antecipação, o fornecedor será bem qualificado de acordo com a pontuação minima parametrizada, caso contrário terá uma qualificação menos positiva.

Segue abaixo o print das formulas utilizadas nesse contexto:

* **Código da Coligada do Fornecedor:**

* **Código do Fornecedor**

* Consulta SQL passando como parâmetro as formulas criadas para retornar o **Código da coligada do Fornecedor** e o **Código do Fornecedor** (Formulas citadas acima).

* Fórmula utilizada no parâmetro de "Qualificação de Fornecedor" para calcular a pontuação e certificar se o Fornecedor será bem qualificado ou menos qualificado.

## Funções de fórmula aplicáveis ao processo de Analise de Requisitos:

* **PESOREQUISITO** Retorna o Peso do Requisito informado no cadastro do Requisito.

*Sintaxe: PESOREQUISITO*

* **QTDEMOVIMENTOSATENDIDOS** Retorna a quantidade de movimentos, cujo requisito (X) foi atendido.

*Sintaxe: QTDEMOVIMENTOSATENDIDOS (VALOR)**Onde VALOR = número de movimentos (dentre os últimos incluídos) que serão analisados.*

* **QTDEMOVIMENTOSATENDIDOSPORPERIODO** Retorna a quantidade de movimentos, cujo requisito (X) foi atendido, nas movimentações no período 'xx/xx/xxxx' a 'yy/yy/yyyy'.

*Sintaxe: QTDEMOVIMENTOSATENDIDOSPORPERIODO (DATA,DATA )**Onde DATA,DATA = Data Inicial e Data Final de movimentação a analisar.*

* **QTDEMOVIMENTOSCOMREQUISITOPORPERIODO** Retorna a quantidade de movimentos que possuem informações sobre o requisito (X) (seja atendido ou não atendido), no período 'xx/xx/xxxx' a 'yy/yy/yyyy'. *Sintaxe: QTDEMOVIMENTOSCOMREQUISITOPORPERIODO (DATA,DATA ).**Onde DATA,DATA = Data Inicial e Data Final de movimentação a analisar.*

**Importante***:*

O retorno das funções: **QTDEMOVIMENTOSATENDIDOS, QTDEMOVIMENTOSATENDIDOSPORPERIODO** e**QTDEMOVIMENTOSCOMREQUISITOPORPERIODO** não consideram movimentos cancelados.

## Funções de fórmula aplicáveis ao processo de Qualificação de Fornecedores:

* **PONTUACAOTOTALPORFORNECEDOR:**Soma a pontuação dos requisitos cadastrados, cuja aplicação é no fornecedor (por fornecedor).

*Sintaxe: PONTUACAOTOTALPORFORNECEDOR*

* **PONTUACAOTOTALPORPRODUTOFORNECEDOR:**Soma a pontuação dos requisitos cadastrados, cuja aplicação é no produto/fornecedor (por produto/fornecedor).

*Sintaxe: PONTUACAOTOTALPORPRODUTOFORNECEDOR*

* **QTDEREQUISITOSDEFORNECEDOR** Retorna a quantidade de requisitos cadastrados, cuja aplicação é no fornecedor (por fornecedor).

*Sintaxe: QTDEREQUISITOSDEFORNECEDOR*

* **QTDEREQUISITOSDEPRODUTOFORNECEDOR** Retorna a quantidade de requisitos cadastrados, cuja aplicação é no produto/fornecedor (por produto/fornecedor).

*Sintaxe: QTDEREQUISITOSDEPRODUTOFORNECEDOR*
