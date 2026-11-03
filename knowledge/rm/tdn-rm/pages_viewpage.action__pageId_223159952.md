---
content_hash: 9e622dd7ae5aba84cd17efdbdea57ec5cac238437e7801ce2b785ac620e76dff
fetched_at: '2026-06-29T00:06:21.007536+00:00'
page_id: '223159952'
product: rm
source: tdn-rm
title: TSRMCN ER Recebimento Automático de NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223159952
version: 141
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Compras / Recebimento de Materiais |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado** | TSRMCN | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   

## Objetivo

O objetivo dessa implementação é permitir a importação automática das notas fiscais eletrônicas, através do processo do TOTVS Colaboração 2.0.

O atual processo responsável pelo recebimento da NF-e, exige a intervenção manual do usuário para resolver alguns conflitos, tais como, tradução dos produtos, seleção da natureza de operação, entre outros. A fim de simplificar este processo, está sendo implementado o recebimento automático da NF-e, o qual será capaz de solucionar todas estas questões, mediante uma prévia configuração, sendo que todas as validações/consistências executadas na criação manual do movimento serão também executadas no recebimento e criação automática da NF-e.

O Recebimento Automático da NF-e está disponível apenas para o TOTVS Colaboração 2.0, mas as melhorias de performance e de usabilidade das telas também estão disponíveis para o TOTVS Colaboração 1.0.

É importante salientar que para a utilização do TOTVS Colaboração é indispensável a contratação dos serviços da NeoGrid que é a responsável pelo processamento da leitura dos arquivos XML, pela comunicação com os webservices da SEFAZ e pelo retorno às consultas destes documentos. Estes, por sua vez, serão lidos e interpretados através da execução de JOBs específicos pelo TOTVS Gestão de Estoque, Compras e Faturamento para a devida atualização dos dados no sistema.

## Definição da Regra de Negócio

### 1. Parametrização

Para o correto funcionamento da rotina de Recebimento Automático das NF-e é necessário que sejam executadas algumas parametrizações. São elas:

### 1.1. Tipo de Recebimento de NF-e

O campo "Tipo de Recebimento de NF-e" define a forma como o sistema irá realizar o processo de recebimento automático das NF-e. Esta informação é parametrizável por Fornecedor do TOTVS Colaboração e/ou porFilial.

Assim, quando do recebimento automático de uma NF-e, caso o emitente da mesma conste na tabela de definições do Cli/For para o TOTVS Colaboração (*"Cadastros > Mais > Tabelas Auxiliares > Definições de Cli/For – TOTVS Colaboração"*), essa informação prevalecerá e assim, para determinados fornecedores poderá ser definido um Tipo de Recebimento diferente do que é praticado geralmente.

Para o preenchimento deste campo é importante avaliar quais os fornecedores enviam o nº do Pedido de Compra no XML.

Caso no momento do recebimento automático de uma NF-e o emitente da mesma não conste na tabela de*"Definições de Cli/For para o TOTVS Colaboração"*, o sistema obedecerá ao que foi parametrizado para a filial de destino da NF-e em *"Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > 04.03  - Integrações > 04.03.03 - Fiscal > 04.03.03.01 - Dados Fiscais > Parâmetros por Filial > Informações TOTVS Colaboração"*.

Assim, para evitar erro no momento do recebimento, é imprescindível que o parâmetro da filial esteja sempre preenchido indicando como o sistema deve proceder para os fornecedores cujo Tipo de Recebimento não foi informado.

Os Tipos de Recebimento possíveis são:

* Inclusão Direta:O sistema não considera o código do pedido no XML e realiza a inclusão direta do movimentode NF-e com base nos dados existentes no XML. O movimento será criado acatando a todas as parametrizações do seu tipo de movimento, ou seja, efetuando todas as integrações parametrizadas. O status do movimento será 'Normal' ou 'A Pagar' conforme a parametrização do seu tipo de movimento;
* Inclusão Direta - Status Não Processado:O sistema não considera o código do pedido no XML e realiza a inclusão direta do movimento com base nos dados existentes no XML, só que com o status “Não Processado”.  Um movimento criado com status 'Não Processado' existirá apenas como documentação, sem qualquer efeito sobre o sistema, ou seja, estes movimentos serão criados sem a geração de suas possíveis integrações com a Contabilidade, Financeiro e Aprovações e não irão gerar movimentação no estoque, lançamentos financeiros, lançamentos contábeis, workflows de aprovação, etc. Para que estes movimentos passem a ter efeito os mesmos deverão ser processados (vide item 4 deste documento);
* Recebimento de Pedido:O sistema utiliza o código do pedido contido no XML para buscar o movimento correspondente e realizar o faturamento do mesmo, sendo que se o pedido não for encontrado na base de dados o novo movimento não será criado, pois o sistema abortará o processo, informando o motivo através do log de execução;
* Recebimento de Pedido ou Inclusão Direta:Através do conteúdo do XML, o sistema tentará identificar o respectivo pedido, e caso seja bem-sucedido, será realizado o faturamento do mesmo. Se o sistema não conseguir identificar nenhum pedido, a inclusão do movimento será feita através dos dados constantes do XML e sem nenhum relacionamento com qualquer outro movimento já existente na base de dados, ou seja, o movimento será criado acatando a todas às parametrizações do seu tipo de movimento, efetuando todas as integrações parametrizadas. O novo movimento terá o status 'Normal' ou 'A Pagar' conforme a parametrização do seu tipo de movimento;
* Recebimento de Pedido ou Inclusão Direta - Status Não Processado:Através do conteúdo do XML, o sistema tentará identificar o respectivo pedido, e caso seja bem-sucedido, será realizado o faturamento do mesmo.  Se o sistema não conseguir identificar nenhum pedido, a inclusão do movimento será feita através dos dados constantes do XML e sem nenhum relacionamento com qualquer outro movimento já existente na base de dados, ou seja, o movimento será criado acatando às parametrizações do seu tipo de movimento, exceto as de integração, pois o movimento será criado com o status "Não Processado".  Um movimento criado com status 'Não Processado' existirá apenas como documentação, sem qualquer efeito sobre o sistema, ou seja, estes movimentos serão criados sem a geração de suas possíveis integrações com a Contabilidade, Financeiro e Aprovações e não irão gerar movimentação no estoque, lançamentos financeiros, lançamentos contábeis, workflows de aprovação, etc. Para que estes movimentos passem a ter efeito os mesmos deverão ser processados (vide item 4 deste documento).

Lembre-se que, caso para alguns fornecedores o tipo de recebimento seja diferente do que foi definido para a filial, você deve fornecer esta informação em *"Cadastros > Mais > Tabelas Auxiliares > Definições de Cli/For – TOTVS Colaboração".*

Caso a filial não vá utilizar a rotina de recebimento automático da NF-e, o campo "Tipo de Recebimento de NF-e" deverá permanecer em branco. 

### 1.2. Fórmula do Tipo de Movimento para Recebimento de NF-e

Em*“Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Integrações > Fiscal > Parâmetros por Filial > Informações TOTVS Colaboração”,* deverá ser preenchido por filial o campo "Fórmula Tipo Mov. p/Recebimento NF-e**"**.

Este novo parâmetro é do tipo fórmula, e assim, através do mesmo, o usuário poderá implementar uma regra específica para buscar o tipo de movimento que será utilizado tanto no recebimento automático como no recebimento manual das NF-e de cada filial.

Essa fórmula será executada para cada XML a ser recebido.

Foram criadas quatro novas funções de fórmula para auxiliar na criação dessa regra, são elas:

* TABXMLCOLAB - Retorna o valor de um campo da tabela de XMLs do Totvs Colaboração (TNFEENTRADA);
* DADOSXMLCOLAB - Retorna o valor de uma TAG de um XML;
* QTDTAGSXMLCOLAB - Retorna o número de vezes que uma determinada Tag aparece no XML;
* TABPRDCOLAB - Retorna o conteúdo de um campo do cadastro dos produtos vinculados aos itens constantes do XML.

Explicaremos a seguir a sintaxe de cada uma dessas funções bem como daremos exemplos de utilização de todas elas.

* TABXMLCOLAB ('NomeCampo', 'TipoRetorno') onde:
  + NomeCampo = Nome do Campo da Tabela TNFEENTRADA. Podemos citar como campos dessa tabela o código da coligada (CODCOLIGADA), o código da filial (CODFILIAL), o código da coligada do fornecedor (CODCOLCFO), o código do fornecedor (CODCFO), a data de emissão (DATAEMISSAO), etc.;
  + TipoRetorno = Informa o tipo de retorno relativo ao campo informado em NomeCampo, se S (string), V (valor), D (data) ou I (inteiro).

Exemplo de fórmula de seleção do tipo de movimento utilizando a função TABXMLCOLAB:

Neste exemplo o sistema irá verificar na tabela TNFEENTRADA (tabela que contém os XML importados) o registro gerado pelo XML e caso o código do fornecedor seja F00017 o movimento será gerado com o tipo 1.2.27, caso contrário o tipo do movimento será 1.2.20.

* DADOSXMLCOLAB ('CaminhoTAG', 'NamespaceXML') onde:
  + CaminhoTAG = Caminho da TAG desejada, separado por barra ( / ). Exemplo: '/nfeProc/NFe/infNFe/det/prod/CFOP' para o CFOP do produto do XML;
  + NamespaceXML = <http://www.portalfiscal.inf.br/nfe>

Exemplo de fórmula de seleção do tipo de movimento utilizando a função DADOSXMLCOLAB:

Quando a tag possuir índice, basta informá-lo o entre colchetes ([ ]).

No exemplo acima o sistema irá retornar a informação da TAG CFOP do primeiro item da NFe, já que não informamos nenhum índice.

Veja abaixo um exemplo da mesma fórmula retornando o CFOP do 2º item da NFe:

* QTDTAGSXMLCOLAB ('CaminhoTAG', 'NamespaceXML') onde:
  + CaminhoTAG = Caminho da TAG desejada, separado por barra ( / ). Exemplo: '/nfeProc/NFe/infNFe/det' para o produto do XML;
  + NamespaceXML = <http://www.portalfiscal.inf.br/nfe>

Veja abaixo um exemplo de fórmula de seleção do tipo de movimento utilizando as funções QTDTAGSXMLCOLAB e DADOSXMLCOLAB:

No exemplo acima através da função QTDTAGSXMLCOLAB o sistema irá identificar o número de itens constantes do XML. Após isso, através da função DADOSXMLCOLAB, irá percorrer todos os itens do XML e caso exista algum cujo CFOP seja 5.102 o tipo de movimento gerado será o 1.2.12.

Assim, utilizando em uma mesma fórmula estas duas funções (QTDTAGSXMLCOLAB e DADOSXMLCOLAB), o sistema irá verificar determinado dado de todos os itens constantes de um XML.

* TABPRDCOLAB ('CodigoProdutoColab', 'NomeCampo', 'TipoRetorno') onde:
  + CódigoProdutoColab = Código do Produto na tabela "Produtos TOTVS Colaboração";
  + NomeCampo = Nome do campo da tabela de Produtos;
  + TipoRetorno = Informa o tipo de retorno relativo ao campo informado em NomeCampo, se S (string), V (valor), D (data) ou I (inteiro).

Veja abaixo um exemplo de fórmula de seleção do tipo de movimento utilizando as funções QTDTAGSXMLCOLAB, DADOSXMLCOLAB e TABPRDCOLAB:

Neste exemplo, em primeiro lugar o sistema utilizará a função QTDTAGSXMLCOLAB para identificar o número de itens constantes do XML, logo depois, através da função DADOSXMLCOLAB irá percorrer todos os itens do XML e através da função TABPRDCOLAB irá identificar na tabela Produtos TOTVS Colaboração quais são os produtos vinculados aos itens do XML. Após verificar sua tabela de produtos e através  e irá analisar se algum deles possui a Tabela de Classificação 1 preenchida com 05. Em caso afirmativo o sistema irá gerar o movimento com o tipo 1.2.12, caso contrário o movimento será do tipo 1.2.11.

Assim, utilizando em uma mesma fórmula estas três funções (QTDTAGSXMLCOLAB, DADOSXMLCOLAB e TABPRDCOLAB), o sistema irá verificar determinado dado de todos os itens constantes de um XML e ainda irá compará-lo com determinado campo do seu cadastro de Produtos.

Caso para algum XML através da fórmula não seja possível definir o seu tipo de movimento, o XML será criado na base de dados com o status 'Inconsistente' e poderá ser recebido manualmente.

Este novo parâmetro somente será habilitado quando, no quadro “Tipo Documento Integração TOTVS Colaboração” pelo menos uma das opções, 'Todos' ou 'Recebimento de NFe' estiver marcada.

O recebimento manual do XML consta do documento [TSRMCN\_ER\_Inclusão\_de\_Movimento\_através\_de\_XML\_TOTVS\_Colaboração](http://tdn.totvs.com/pages/viewpage.action?pageId=224106789).  Acesse-o para maiores informações sobre este procedimento.

### 1.3. Parametrização de Local de Estoque e Condição de Pagamento

A informação do Local de Estoque é obrigatória na geração de qualquer movimento e a informação da Condição de Pagamento é obrigatória na geração de todos os movimentos que possuem Integração Financeira.

Para os movimentos gerados automaticamente através do recebimento de um pedido estes campos já virão automaticamente preenchidos mas para aqueles onde a inclusão da NF-e não possui nenhum vínculo com outro movimento,  torna-se necessário fornecer estas informações para o sistema.

Caso a sua empresa possua apenas um Local de Estoque, basta preenchê-lo na parametrização dos tipos de movimento. Para isso vá em *"Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > 04.06 - Gestão Compras > 04.06.05 - Recebimentos de Materiais"*e no tipo de movimento desejado forneça esta informação em*"Mov - Emitente/Destinatário"*. Veja abaixo:

O mesmo se aplica à Condição de Pagamento, ou seja, caso a sua empresa adquira produtos com apenas uma condição de pagamento basta parametrizá-la no tipo de movimento. Para isso vá em *"Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > 04.06 - Gestão Compras > 04.06.05 - Recebimentos de Materiais"*e no tipo de movimento desejado forneça esta informação em*"Fin - Condições de Pagamento"*. Veja abaixo:

Nos casos acima caso a edição do Local de Estoque e da Condição de Pagamento estejam como "Edita", mesmo assim o sistema ainda criará o movimento de NF-e com a informação do Local de Estoque e da Condição de Pagamento informados como "Default" nestas telas de parâmetros.

Sabemos que essa realidade não se aplica a grande parte das empresas que, em sua maioria, possuem vários Locais de Estoque e trabalham com inúmeras Condição de Pagamento, por isso para que sua empresa possa definir no sistema suas próprias regras de negócio quanto a estas informações poderão ser utilizadas "Fórmulas Visuais".

Assim, caso sua empresa  possua mais de um Local de Estoque e utilize mais de uma Condição de Pagamento, no tipo de movimento informe que estes dados deverão ser editados e não preencha a informação default, conforme demonstramos nas telas a seguir:

Após isso vá em *"Gestão > Fórmula Visual > Fórmula Visual"*.

Clique no botão "Novo" e insira sua Fórmula Visual a ser utilizada no Recebimento Automático de NF-e.

Na aba*"Gatilhos"*em "Assinantes" selecione o gatilho "Antes de validar o contexto" e clique no ícone "Adicionar Objetos".

Foram criados 2 novos objetos relativos ao processo de Recebimento Automático da NF-e do TOTVS Colaboração;

* TOTVS Colaboração / Assinante de Inclusão de Movimento por Faturamento;
* TOTVS Colaboração / Assinante de Inclusão de Movimento.

No campo localizar digite "TOTVS" para que o sistema apresente as mesmas na tela:

 

Clique no primeiro objeto e o sistema automaticamente o levará para a tela dos Gatilhos. Repita o mesmo com o segundo objeto e clique em OK para gravar o registro.

 

O sistema retornará à visão das Fórmulas Visuais. Dê duplo clique na Fórmula Visual criada para o Recebimento Automático de NF-e.

 

Clique na aba "Atividades", desça até "RM Movimento" e você terá acesso às atividades a serem utilizadas em sua fórmula visual que são:

* Atribuir valor no contexto do Assinante/Movimento;
* Consulta valor no contexto do Movimento (Assinante).

A partir da agora, já de posse das informações relativas às implementações que efetuamos nas Fórmulas Visuais você poderá criar aquelas que se adequarão à sua empresa.

Neste documento citamos os campos Local de Estoque e Condição de Pagamento mas as fórmulas visuais poderão ser utilizadas para atribuir o conteúdo de outros campos do movimento ou ítens de movimento de Recebimento Automático, conforme a necessidade da sua empresa.

 

### 2. Cadastros

Para o correto funcionamento da rotina de Recebimento Automático das NF-e devemos ficar atentos ao preenchimento de alguns cadastros. São eles:

 

### 2.1. Natureza Fiscal (CFOP)

Quando uma nota fiscal eletrônica é enviada por um fornecedor, ela contém, para cada um dos seus itens, uma natureza fiscal (CFOP) de saída, que caracteriza a operação desse fornecedor. Para a empresa que recebe esse documento entretanto, devemos encontrar a natureza fiscal (CFOP) de entrada correspondente. Essa ‘Natureza Inversa’ é indispensável para a criação automática de um movimento de NF-e.

Para definir a Natureza Inversa na geração automática do movimento de entrada, o TOTVS Gestão de Estoque, Compras e Faturamento utilizará os seguintes recursos:

### 2.1.1. Regra de Seleção da Natureza (RSN)

Para cada movimento de NF-e a ser incluído, o sistema irá encontrar a Natureza Inversa do CFOP constante do arquivo XML. Para isso, é necessário saber, através das parametrizações vigentes do tipo de movimento, se o movimento a ser criado seleciona a Natureza de Operação somente para o movimento, ou se deve ser selecionada também uma Natureza para o item de movimento. Para ambos os casos, será utilizada em primeiro lugar a Regra de Seleção da Natureza (RSN), rotina hoje já existente e que tem a finalidade de encontrar a Natureza de Operação baseada nas informações do movimento e parametrizações de várias tabelas tais como: Parâmetros do Tipo de Movimento, Produto, Classificação de Produto, Naturezas Fiscais, Regras de ICMS, Regras de IPI, etc..

Para verificar como está a parametrização da sua empresa vá na etapa *"Fis - Natureza"* dos Parâmetros dos Tipos de Movimento que serão utilizados no Recebimento Automático da NF-e e verifique o preenchimento do campo 'Seleção Automática da Natureza'.

Detalharemos a seguir como o sistema procederá conforme o tipo de Seleção Automática da Natureza definido para o tipo de movimento.

### 2.1.1.1. Seleção Automática da Natureza por Movimento

Neste caso, deverá ser encontrada obrigatoriamente uma Natureza de Operação analítica para o movimento.

Através dos dados do XML e das parametrizações e cadastros do sistema**,** a Regra de Seleçao da Natureza irá encontrar a(s) natureza(s) possível(eis), de forma que:

* Se a RSN encontrar apenas uma Natureza de Operação (CFOP) possível, o movimento de NF-e será incluído com o CFOP encontrado;
* Se a RSN encontrar mais de uma Natureza de Operação (CFOP) possível, o sistema irá verificar as opções cadastradas como Natureza Inversa da CFOP extraída do XML.

No item 2.1.2 deste documento iremos detalhar como será o comportamento do sistema caso seja necessário utilizar o cadastro de Natureza Inversa do CFOP.

### 2.1.1.2. Seleção Automática da Natureza por Item de Movimento

Nesta situação, será realizado o mesmo procedimento já explicado anteriormente para encontrar a Natureza de Operação do movimento, com a diferença desta poder ser analítica ou sintética.

Se for encontrada uma Natureza analítica, sua ‘Raiz’ (Natureza Sintética) deve ser extraída e considerada como a Natureza do movimento enquanto que a Natureza analítica será atribuída ao item.

Caso sejam encontradas 2 naturezas sintéticas possíveis, os campos natureza 1 e natureza 2 do movimento (TMOV.IDNAT, TMOV.IDNAT2) serão preenchidos caso ambos estejam parametrizados para o tipo de movimento, mas se existirem mais de 2 naturezas sintéticas possíveis, o sistema não será capaz de solucionar o conflito e, neste caso a natureza não será identificada, sendo preenchida a natureza do movimento com um CFOP de primeiro nível, ou seja, 1 ou 2 conforme a UF de origem da NF-e.

Caso seja encontrada apenas a Natureza sintética, ela será atribuída ao movimento, e o procedimento de busca será realizado novamente para selecionar a Natureza do item. Para o item, a Regra de Seleção da Natureza irá considerar os dados do movimento e das demais tabelas citadas anteriormente (Parâmetros do Tipo de Movimento, Produto, Classificação de Produto, Naturezas Fiscais, Regras de ICMS, Regras de IPI, etc.).

Conforme já informado o sistema primeiramente executará as Regras de Seleção da Natureza, e caso as mesmas retornem mais de uma opção de CFOP para os itens do movimento, o sistema utilizará o cadastro das Naturezas Inversas que detalharemos a seguir:

### 2.1.2. Natureza Inversa

No cadastro de Natureza de Operação (CFOP), de responsabilidade do sistema TOTVS Gestão Fiscal, foi criado o anexo *"Natureza Inversa TOTVS Colaboração"* (TNATUREZACOLAB) onde deverão ser cadastradas as possíveis naturezas de operação inversas para uma determinada natureza sintética.

Uma natureza de operação sintética, poderá ter a ela vinculada, várias naturezas de operação inversas, sejam elas sintéticas ou analíticas.

Entre as naturezas inversas cadastradas, o usuário poderá definir "Defaults", ou seja, registros que devem ser considerados prioritários caso existam várias naturezas possíveis para um determinado movimento.

Este cadastro será utilizado apenas caso através da aplicação das Regras de Seleção da Natureza tenha sido encontrada mais de uma natureza inversa possível para o item. Neste caso o sistema procederá da seguinte forma:

* Se apenas uma das naturezas selecionadas  estiver cadastrada como "Default", ela será utilizada para a criação de movimento;
* Se mais de uma das naturezas selecionadas estiver cadastrada como "Default", o sistema não saberá qual Natureza Inversa escolher e o movimento será criado com o Status do TOTVS Colaboração como 'Natureza Incompleta';
* Se apenas uma das naturezas selecionadas estiver cadastrada como Natureza Inversa, mesmo não sendo como "Default", ela será utilizada para a criação do movimento;
* Se mais de uma das naturezas selecionadas estiver cadastrada como Natureza Inversa mas nenhuma delas é "Default", o sistema não saberá qual Natureza Inversa escolher e o movimento será criado com o Status do TOTVS Colaboração como ‘Natureza Incompleta';
* Se nenhuma das naturezas selecionadas estiver no cadastro de Natureza inversa, o movimento será criado com o Status do TOTVS Colaboração como ‘Natureza Incompleta'.

É importante salientar que o Status TOTVS Colaboração 'Natureza Incompleta' não influencia no status do movimento que será criado conforme o Tipo de Recebimento utilizado e os parâmetros do Tipo de Movimento gerado, ou seja, mesmo estando com esse Status TOTVS Colaboração o movimento poderá gerar todas as demais integrações (financeira, contábil, estoque e de aprovações) se assim estiver parametrizado.

Os movimentos gerados com o Status TOTVS Colaboração 'Natureza Incompleta' deverão ter seus CFOP informados através de edição manual.

Uma natureza default pode ser sintética ou analítica, entretanto, poderá haver somente uma natureza analítica default de cada 'raiz' para uma mesma natureza sintética.

Exemplo:

No nosso exemplo acima a natureza 1.102.04 não pode ser default para a natureza 5.101 já que outra natureza que possui a sintética idêntica (1.102.03) já foi definida como default para a mesma.

No TOTVS Gestão de Estoque, Compras e Faturamento, o cadastro das naturezas inversas***,***está disponível em *“Cadastros > Fiscais > Natureza Fiscal > Anexos > Natureza Inversa TOTVS Colaboração”*.

Você poderá acessar este Anexo a partir da visão de Naturezas ou a partir da tela de edição de uma Natureza específica.

Acesso a partir da visão de Naturezas

Acesso a partir da tela de edição da Natureza:

O sistema irá verificar a Natureza Inversa do CFOP constante da NF-e, ou seja as Naturezas Inversas devem estar cadastradas nas naturezas sintéticas de Saída. Assim, selecione o CFOP sintético para o qual você irá cadastrar as Naturezas Inversas e clique em *"Anexos > Natureza Inversa TOTVS Colaboração"*.

Será apresentada a tela onde você poderá cadastrar as Naturezas Inversas a serem vinculadas à natureza sintética selecionada.

Informe a Natureza Inversa correspondente, marque o campo caso a mesma vá ser uma natureza 'Default' para esta natureza sintética e clique em 'Inserir'.

O sistema apresentará na tela a correspondência entre as naturezas inseridas, permitindo que as demais Naturezas Inversas dessa Sintética sejam incluídas, caso existam.

Informe todas as naturezas inversas de cada natureza sintética de saída e clique em 'OK' ou 'Salvar' para que o sistema as grave.

### 2.2. Produtos

Para efetuar o recebimento automático é necessário que esteja cadastrada a correlação entre os produtos constantes dos XML e os produtos constantes da sua base de dados, ou seja, dos produtos do fornecedor com os produtos do seu estoque.

A tradução dos produtos contidos no XML, que anteriormente era feita com base nas informações da tabela Produtos por Fornecedor (TPRDCFO), a partir de agora será feita através da tabela Produtos TOTVS Colaboração (TPRDCFOCOLAB).

Nesta nova estrutura, o usuário poderá definir um relacionamento de 1 x N, conforme exemplificamos abaixo:

Note que para o produto 100524 podemos ter N produtos vinculados como por exemplo os produtos Caneta Esferográfica Azul e Caneta Esferográfica Preta do fornecedor, correspondem a um só produto no estoque, Caneta Esferográfica.

As informações atualmente existentes na tabela Produtos (TPRDCFO) serão automaticamente inseridas na tabela  Produtos TOTVS Colaboração (TPRDCFOCOLAB) através do atualizador da versão.

Para incluir novos produtos na tabela acesse *“Cadastros > Produtos > Anexos > Produtos TOTVS Colaboração”.*

Como todos os demais Anexos do sistema, você poderá acessá-lo a partir da visão de Produtos ou a partir da tela de edição de determinado Produto.

Acesso através da visão de Produtos.

Acesso a partir da tela de edição do produto:

Informe o 'Código do Fornecedor', o 'Código do Produto no Fornecedor' e se este for o único produto correspondente para este fornecedor, clique em 'Salvar" ou "OK" para efetuar a gravação do registro ou no ícone "Incluir" caso queira gravar o registro e em seguida informar um novo fornecedor e código de produto correspondente para este produto.

Caso o produto possua mais de um produto correspondente no mesmo fornecedor, informe um deles no 'Cód. do Produto no Fornecedor' e clique em "Inserir Múltiplos" para utilizar esse recurso facilitador que permitirá que você inclua vários registros na mesma tela e grave-os de uma só vez.

No campo 'Código do Produto' informe o código do produto no fornecedor e em seguida clique em "Inserir", e assim sucessivamente até que todos os códigos no fornecedor tenham sido informados.

Após informar os códigos de todos os produtos correspondentes nesse fornecedor clique em "Salvar" ou "OK" para efetuar a gravação do registro ou no botão "Incluir" caso queira gravar o registro e em seguida informar um novo fornecedor e produto correspondente para este produto.

Após finalizar a inserção dos Registros Múltiplos, caso opte por "Salvar" o sistema lhe apresentará em tela a mensagem informando os registros que foram gravados.

Para encerrar a informação dos fornecedores e produtos correspondentes a este produto tecle "OK" e o sistema automaticamente sairá da tela de cadastro e exibirá a visão  dos Produtos TOTVS Colaboração cadastrados para o seu produto.

Vale salientar que caso tenha(m) havido inclusão(ões) a partir da inserção de múltiplos registros será necessário clicar no botão "Atualizar Informações" para que os mesmos sejam apresentados.

Conforme informamos, no Recebimento Automático da NF-e é imprescindível que todos os produtos constantes de cada XML já tenham sido vinculados com o respectivo produto da sua base de dados, caso contrário o movimento não será criado e sua entrada terá que ser efetuada manualmente.

 

### 2.3. Unidades

Da mesma forma que com os produtos, para efetuar o recebimento automático é necessário que esteja cadastrada a correlação entre as unidades de medida dos produtos constantes dos XML, ou seja das unidades do fornecedor com as unidades utilizadas na sua empresa.

O sistema realizará a tradução do campo Unidade de Medida ‘CODUND’ através da tabela ‘TUNDCFOCOLAB’, onde será possível cadastrar o código da unidade no fornecedor, e informar a unidade correspondente no sistema, evitando assim, a intervenção manual do usuário durante o processo de recebimento.

Para informar a correlação entre as unidades vá em *“Cadastros > Mais... > Tabelas Auxiliares > Unidade > Anexos > Unidades TOTVS Colaboração”.*

Você poderá acessar este Anexo exclusivamente da visão de Unidades.

O sistema abrirá o Anexo do lado direito da tela de visão das Unidades.

Clique no botão "Incluir" para inserir as Unidades dos Fornecedores que correspondem à sua Unidade selecionada.

Informe ou selecione o 'Fornecedor' (código ou nome), informe o  'Código da Unidade no Fornecedor' e se esta for a única correspondência para esta unidade, clique em "Salvar" ou "OK" para efetuar a gravação do registro. Caso existam outros fornecedores para o qual essa unidade será utilizada clique no ícone "Incluir" para gravar o registro e em seguida informar um novo fornecedor e código de unidade correspondente para esta unidade.

Para encerrar a informação dos fornecedores e unidades correspondentes a esta unidade tecle "OK" e o sistema automaticamente sairá da tela de cadastro e exibirá a visão  das Unidades TOTVS Colaboração cadastradas.

É importante salientar que caso o sistema não localize a unidade correspondente durante o recebimento automático, o movimento não será gerado.

Agora que já falamos sobre todos as parametrizações e cadastros necessários, vamos falar sobre o processo de Recebimento Automático da NF-e em si.

### 3. Recebimento Automático da NF-e

Conforme já dito o Recebimento Automático somente está disponível para o TOTVS Colaboração 2.0 portanto antes de ativá-lo sugerimos a verificação das parametrizações necessárias para a  atualização desta versão do TOTVS Colaboração.

Acesse o manual  [TOTVS Colaboração 2.00](http://tdn.totvs.com/pages/viewpage.action?pageId=219696881) para instruções acerca da parametrização necessária.

No processo de Recebimento Automático de NF-e o TOTVS Colaboração irá executar os seguintes procedimentos:

### 3.1. Importação de Arquivos - TOTVS Colaboração

Esse Job  é um Job Global, responsável por buscar os documentos enviados pela ClientEDI Neogrid e distribuí-los por coligada. Neste momento, nenhuma validação é feita. Após a execução desse Job, os documentos lidos são exibidos no *“Monitor de Arquivos TOTVS Colaboração”* com o status **‘**Pendente’,  aguardando a ação do segundo Job.

O ideal é que a execução deste job seja agendada, assim, periodicamente o mesmo será executado de forma automática, buscando os XML disponibilizados.

Informamos que somente serão importados os XML que obedeçam totalmente a todos os requisitos do schema definido pela SEFAZ.

Para maiores detalhes acesse [http://tdn.TOTVS.com/display/public/LRM/CLB\_0002\_Jobs](http://tdn.totvs.com/display/public/LRM/CLB_0002_Jobs)

### 3.2. Serviço TOTVS Colaboração Consulta

Esse Job é responsável por validar o arquivo XML do documento enviado, de acordo com o tipo de documento em questão (CT-e, NF-e, NFS-e, etc.), através da chamada do serviço especifico para cada um deles. Serão verificados todos os documentos lidos pelo 1º Job. Caso o documento esteja válido, o registro do arquivo é excluído do monitor, e passa a ser exibido na tela do movimento conforme o tipo de movimento utilizado, indicando que o mesmo foi incluído no sistema com sucesso.

O ideal é que a execução deste job seja agendada, assim periodicamente o mesmo será executado de forma automática.

Para validar e incluir o movimento o sistema irá em primeiro lugar executar a 'Fórmula do Tipo de Movimento para Recebimento Automático de NF-e" comparando-a com os dados do XML para verificar qual o tipo de movimento a ser utilizado na entrada automática da NF-e.

Após encontrar o tipo de movimento a ser incluído o sistema passará à Tradução dos Dados do Arquivo XML.

Caso através da fórmula  definida para a o tipo de movimento no Recebimento Automático (vide item 1.1 deste documento) para algum XML não seja possível definir o seu tipo de movimento esse XML será criado na base de dados com o status 'Inconsistente'. Para verificar o erro ocorrido, basta um duplo clique no registro para que seja exibido o seu Log onde o problema será demonstrado. Quando o arquivo está Inconsistente, é necessário corrigir a causa do erro para poder tentar incluí-lo no sistema. Após a correção do erro basta alterar o seu status para 'Pendente', através do processo *“Alterar status do arquivo TOTVS Colaboração”*e o Job tentará recebê-lo automaticamente novamente em sua próxima execução. Caso opte por não acertar o erro e receber o XML manualmente o registro 'Inconsistente' deverá ser excluído da tela do*"Monitor de Arquivos TOTVS Colaboração"*.

### 3.2.1. Tradução dos Dados do Arquivo XML

Tendo identificado o tipo de movimento a ser utilizado, o sistema efetuará a tradução do XML utilizando-se dos dados dos cadastros que já descrevemos anteriormente:

#### 3.2.1.1. Identificação dos Produtos

A identificação de cada produto será efetuada com base nos registros da tabela Produtos TOTVS Colaboração (TPRDCFOCOLAB).

Para cada produto no XML, o sistema verificará qual é o produto correspondente no seu cadastro, utilizando-o na inserção do item de movimento.

Caso no XML seja encontrado algum produto sem correspondência o processo de Recebimento Automático será abortado mas o XML será criado na base de dados  com o status  'Inconsistente'. Para verificar o erro ocorrido, basta um duplo clique no registro para que seja exibido o seu Log onde o problema será demonstrado. Quando o arquivo está Inconsistente, é necessário corrigir a causa do erro para poder tentar incluí-lo no sistema. Após a correção do erro basta alterar o seu status para 'Pendente', através do processo *“Alterar status do arquivo TOTVS Colaboração”*e o Job tentará recebê-lo automaticamente novamente em sua próxima execução. Caso opte por não acertar o erro e receber o XML manualmente o registro 'Inconsistente' deverá ser excluído da tela do*"Monitor de Arquivos TOTVS Colaboração"*.

#### 3.2.1.2. Identificação das Unidades de Medida

Assim como na identificação dos produtos, ao localizar o código da unidade de medida de cada item no arquivo XML, o sistema verificará na tabela Unidades TOTVS Colaboração (TUNDCFOCOLAB) qual é o código da Unidade correspondente e o mesmo será utilizado na inserção do item de movimento.

Caso no XML seja encontrada alguma unidade sem correspondência o processo de Recebimento Automático será abortado mas o XML será criado na base de dados com o status 'Inconsistente'. Para verificar o erro ocorrido, basta um duplo clique no registro para que seja exibido o seu Log onde o problema será demonstrado. Quando o arquivo está Inconsistente, é necessário corrigir a causa do erro para poder tentar incluí-lo no sistema. Após a correção do erro basta alterar o seu status para 'Pendente', através do processo *“Alterar status do arquivo TOTVS Colaboração”*e o Job tentará recebê-lo automaticamente novamente em sua próxima execução. Caso opte por não acertar o erro e receber o XML manualmente o registro 'Inconsistente' deverá ser manualmente excluído da tela do**"Monitor de Arquivos TOTVS Colaboração"**.

#### 3.2.1.3. Identificação dos CFOP

Vide item 2.1. deste documento onde são explicados os critérios para seleção das Naturezas Fiscais.

Durante o recebimento da nota fiscal eletrônica, caso o sistema não seja capaz de identificar a natureza de operação, o movimento será gerado normalmente, no entanto, será atribuído ao mesmo o Status TOTVS Colaboração “Natureza Incompleta’.

O Status TOTVS Colaboração 'Natureza Incompleta' não influencia no status do movimento que será criado conforme o Tipo de Recebimento utilizado e os parâmetros do Tipo de Movimento gerado, ou seja, mesmo estando com esse Status TOTVS Colaboração o movimento poderá gerar todas as integrações (financeira, contábil, estoque e de aprovações) parametrizadas.

Os movimentos gerados com o Status TOTVS Colaboração 'Natureza Incompleta' deverão ter seus CFOP informados através da edição manual dos mesmos.

### 3.2.2. Identificação do Pedido de Compra

Após efetuar a tradução dos dados do XML o sistema irá verificar se consta do mesmo a informação do Número do Pedido no Fornecedor. Assim, caso a tag xPed (Número do Pedido no Fornecedor)do XML esteja preenchida e exista na base de dados um pedido correspondente, o mesmo será selecionado, caso contrário, o sistema buscará por um pedido de compra com status pendente, emitido para o CNPJ do fornecedor e que seja um ‘espelho’ da NF-e em questão, ou seja, o movimento deve possuir os mesmos produtos com as mesmas quantidades constantes do XML.

Se,  de acordo com a regra acima, o sistema identificar mais de um registro, nenhum pedido será selecionado.

### 3.2.3. Identificação do Tipo de Recebimento NF-e

Após verificar se o Número do Pedido no Fornecedor consta do XML o sistema irá identificar o Tipo de Recebimento a ser praticado para cada NF-e. Para isso o sistema irá verificar se o emitente da mesma consta na tabela Definições de Cli/For - TOTVS Colaboração e em caso positivo será utilizado o tipo de recebimento ali definido. Caso o emitente não conste dessa tabela o sistema irá utilizar o Tipo de Recebimento definido para a filial para a qual a NF-e foi emitida.

Conforme o Tipo de Recebimento utilizado, o comportamento do sistema será:

#### 3.2.3.1. Inclusão de Movimento Através do Pedido:

Caso o Tipo de Recebimento seja 'Recebimento de Pedido', a inclusão do movimento relativo à NF-e será efetuada através do processo de Recebimento/Faturamento do pedido.

Neste Tipo de Recebimento, se o sistema não conseguir localizar o pedido informado na NF-e, o processo será abortado e o motivo será informado no log de execução.

#### 3.2.3.2. Inclusão de Movimento Sem Pedido:

Caso o Tipo de Recebimento seja 'Inclusão Direta' o sistema não irá considerar o código do pedido no XML e fará a inclusão direta do movimento com base nos dados do XML.

Assim, após a tradução, o registro correspondente à NF-e será gerado e não possuirá relacionamento com nenhum movimento de origem.

O movimento será criado, acatando a todas as parametrizações do seu tipo de movimento, ou seja, efetuando todas as integrações parametrizadas. O status do movimento será 'Normal' ou 'A Pagar' conforme sua parametrização.

#### 3.2.3.3. Inclusão de Movimento Com ou Sem Pedido:

Caso o Tipo de Recebimento seja 'Recebimento de Pedido ou Inclusão Direta' o sistema, em primeiro lugar tenta identificar o pedido, e caso obtenha sucesso, efetuará o seu recebimento. Já caso não tenha sido identificado um pedido correspondente, o sistema incluirá o movimento através dos dados constantes do XML e sem nenhum relacionamento com qualquer outro movimento já existente na base de dados.

#### 3.2.3.4. Inclusão de Movimento Com Status Não Processado:

* Caso o Tipo de Recebimento seja 'Inclusão Direta - Status Não Processado' o sistema não irá considerar o código do pedido no XML e fará a inclusão direta do movimento com base nos dados do XML., mas com o status “Não Processado”;
* Caso o Tipo de Recebimento seja 'Recebimento de Pedido ou Inclusão Direta - Status Não Processado' o sistema, em primeiro lugar tenta identificar o pedido, e caso obtenha sucesso, efetuará o seu recebimento. Neste caso o status do movimento será  'Normal' ou 'A Pagar' conforme sua parametrização. Já caso não tenha sido identificado um pedido correspondente, o sistema incluirá o movimento através dos dados constantes do XML e sem nenhum relacionamento com qualquer outro movimento já existente na base de dados, sendo que, neste caso o movimento será incluído com o status  "Não Processado".

Um movimento criado com status 'Não Processado' existirá apenas como documentação, sem qualquer efeito sobre o sistema, ou seja, estes movimentos serão criados sem a geração de suas possíveis integrações com a Contabilidade, Financeiro e não irão gerar movimentação no estoque, lançamentos financeiros, lançamentos contábeis, workflows de aprovação, etc. Para que estes movimentos passem a ter efeito os mesmos deverão ser processados.

Após finalizar sua execução o *"Serviço TOTVS Colaboração Consulta"* irá apresentar no Bloco de Notas do Log de Execução os dados de todos os movimentos que foram automaticamente gerados, conforme exemplo a seguir:

 

### 4. Processar Movimento - TOTVS Colaboração

Os movimentos criados com o status "Não Processado" deverão ser processados para que passem a ter efeito no sistema.

Para processar um movimento você deve, na visão de movimentos em *"Compras" > "Recebimento de Mercadorias",*informar o tipo de movimento e a filial, selecionar o movimento e executar o processo*"Processar Movimento - TOTVS Colaboração"*.

Ao processar um movimento você terá acesso à tela de tradução do respectivo XML, sendo possível selecionar vários XMLs para realizar suas devidas traduções. Para selecionar vários movimentos a serem processados, basta marcá-los na visão de movimentos ou, dentro da tela de tradução clicar no botão 'Adicionar Movimento'. 

Ao clicar neste botão o sistema abrirá uma tela de filtro para que você possa informar seus critérios de seleção e em seguida definir os movimentos que serão incluídos na rotina "*"Processar Movimento - TOTVS Colaboração"*.

Os movimentos selecionados serão apresentados em ordem de código do Tipo de Movimento e Número do Movimento e em formato de lista.

Ao navegar entre os registros, o sistema atualizará automaticamente as informações contidas nas abas *“Identificação”, “Tradução de Itens”*e*“Tributação”.*

Caso queira excluir algum movimento do processo, basta selecioná-lo e clicar no botão 'Remover Movimento'.

Veremos a seguir o conteúdo do processo *"Processar Movimento - TOTVS Colaboração"*.

A aba *“Identificação”*, apresentará as informações gerais do movimento selecionado.

Serão apresentados os seguintes dados:

Id. Movimento – Identificador (número interno gerado automaticamente pelo sistema) do movimento;

* Destinatário / Filial – Filial do movimento;
* Emitente / Fornecedor – Fornecedor dos produtos;
* Chave de Acesso da NF-e;
* Série da NF-e;
* Número do Documento - Número da NF-e;
* Data de Emissão da NF-e;
* Tipo de Movimento no qual a NF-e foi inserida.

Estes dados são importados do XML e por isso não poderão ser alterados.

Caso o sistema não tenha vinculado o XML a um pedido, por estar assim definido no Tipo de Recebimento, ou porque o número do pedido não constava do XML e o mesmo não era espelho da NF-e, o sistema permitirá que você vincule um ou mais Pedidos ao movimento que está sendo processado, bastando para isso que você marque o campo 'Receber Pedido' e clique no ícone 'Incluir' para informar o(s) pedido(s) que será(ão) recebido(s) para este movimento de NF-e.

O sistema apresentará uma tela de filtros para que você selecione o(s) pedido(s) a ser(em) vinculado(s) ao movimento, sendo que o sistema filtrará apenas os pedidos que geram movimentos do tipo de movimento que está sendo processado.

No nosso caso, como o movimento que está sendo processado é do tipo 1.2.12, somente os pedidos que podem ser faturados para este tipo de movimento estarão disponíveis para realizar o vínculo.

Ao ser(em) informado(s) o(s) pedido(s), o sistema imediatamente efetuará o vínculo entre a NF-e e o(s) mesmo(s), caso as informações de ambos sejam correspondentes.

Outros pedidos de compras poderão ser adicionados a qualquer momento.

Na aba *"Tradução de Itens"* serão apresentados os dados relativos aos itens da NF-e.

Caso o movimento de NF-e não esteja vinculado a um pedido será permitida apenas a visualização dos seus dados, ou seja, não será permitida nenhuma alteração.

Caso o movimento de NF-e esteja vinculado a um pedido você poderá alterar o pedido que foi informado para o produto, bastando para isso, selecionar o produto cujo pedido deseja alterar, clicar no campo 'Produto no Pedido' e clicar na seta da lista de opções para que o produto do pedido seja apresentado.

Clique então no botão do lookup do produto.

O lookup exibirá o(s) pedido(s) de compra vinculado(s) ao XML, e que ainda possuem produtos com saldo a receber para que você selecione um deles.

Outro recurso disponível na aba *"Tradução de Itens"*é o botão "Múltiplos".

O botão Múltiplos poderá ser utilizado quando o pedido selecionado pelo sistema não possuir quantidade suficiente para realizar a tradução do produto.

Assim, ao clicar no botão "Múltiplos", será criada uma réplica da linha selecionada para que o produto possa ser associado a outro registro.

Vamos considerar o nosso exemplo, onde o produto '6.0.0.01.8373'  no XML tem a quantidade 1,00, tendo sido 0,50 solicitada no pedido 26790 e mais 0,50 solicitada no pedido 111111 sendo que ambos os pedidos foram vinculados ao XML através da rotina *"Processar Movimento - TOTVS Colaboração".*

Na tela de *"Tradução de Itens"*o sistema relacionará o item sempre ao primeiro pedido vinculado ao movimento.

Poderemos informar então que a quantidade restante no XML foi consumida no pedido 111111.

Para isso selecione o produto e clique no botão "Múltiplos".

No registro já existente o sistema irá alterar a quantidade recebida para o produto, informando a quantidade total do pedido vinculado ao item, e irá inserir um novo registro com o produto e sua quantidade restante.

A partir daí você irá proceder da mesma forma que na alteração do pedido, ou seja, clique no campo 'Produto no Pedido' e clique na seta da lista de opções.

Clique então no ícone do lookup do produto.

O lookup exibirá o(s) pedido(s) de compra vinculado(s) ao XML, e que ainda possuem produtos com saldo a receber para que você selecione um deles.

Ao ser selecionado o pedido, seus dados automaticamente irão para a aba *"Tradução de Itens".*

Na aba *“Tributação de Itens”* serão exibidos todos os tributos parametrizados no tipo de movimento do movimento que está sendo processado.

Na parte superior da tela, em *“Tributação da Nota”* serão carregadas as informações relativas aos tributos do movimento.

Na parte inferior da tela a visão contida no grupo*“Tributação dos Produtos”*será responsável por exibir os impostos dos produtos (itens de movimento).

O preenchimento dos valores relativos aos tributos (base de cálculo, alíquota e valor) será efetuado obedecendo à configuração do campo 'Busca Valores TOTVS Colab' do respectivo tipo de movimento.

Para verificar a sua configuração vá em*"Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > 04.06 - Gestão Compras > 04.06.05 - Recebimentos de Materiais"*e no tipo de movimento desejado consulte este campo em*"Fis - Tributação - Item" e 'Fis - Tributação - Movimento"*. Veja abaixo:

O sistema informará os valores conforme o preenchimento do campo 'Busca Valores TOTVS Colab' com uma das opções a seguir:

* XML: Esta opção deverá ser selecionada caso o usuário deseje que os valores do tributo sejam aqueles recebidos do arquivo XML da NF-e, sem a necessidade de comparação com o tipo de movimento;
* Tipo de Movimento - Não comparar com XML: Esta opção deve ser selecionada caso o usuário deseje que todas as informações do tributo sejam calculadas/buscadas pelo sistema conforme a parametrização do tipo de movimento, sem a necessidade de comparação com os valores advindos do arquivo XML;
* Tipo de Movimento - Comparar com XML: Esta opção deve ser selecionada caso o usuário deseje que todas as informações do tributo sejam calculadas/buscadas pelo sistema, mas elas devem ser comparadas com as informações advindas do XML. No caso do Recebimento Automático, o sistema não apresentará em tela a diferença dos valores encontrados e os valores recebidos do XML, caso exista. Neste caso o usuário deverá selecionar o movimento e verificar se houve diferença indo em *"Anexos > Log de Comparação de Impostos do TOTVS Colaboração".*  
    
    
  Caso não existam diferenças entre os valores calculados pelo sistema e os constantes do XML, será apresentada a seguinte mensagem:  
    
    
    
  Caso existam diferenças o sistema apresentará a tela com as mesmas para que possa ser verificado e o usuário Edite o movimento alterando os valores caso necessário.

Para finalizar a execução da rotina *"Processar Movimento - TOTVS Colaboração"* basta em qualquer uma das telas do processo clicar no botão 'Executar'.

Após a execução o sistema apresentará a tela onde poderá ser verificado o status de conclusão do processo:

A rotina *"Processar Movimento - TOTVS Colaboração"* será responsável por:

* Gerar as integrações (Financeira, Contábil, Aprovação via Workflow, etc.) do movimento;
* Realizar o vínculo do pedido selecionado com o movimento;
* Baixar o(s) Pedido(s) de Compra selecionado(s);
* Alterar o Status do movimento.

Em caso de posterior exclusão do movimento de NF-e criado, o XML em questão será desvinculado do movimento e, voltará ao status anterior à inclusão, para que seja possível vincular um novo movimento ao mesmo.

Neste caso a inclusão do movimento se dará de forma manual através do processo *"Inclusão de Movimento através de XML - TOTVS Colaboração"*. Este processo foi remodelado e maiores esclarecimentos sobre o mesmo encontram-se no documento [TSRMCN\_ER\_Inclusão\_de\_Movimento\_através\_de\_XML\_TOTVS\_Colaboração](http://tdn.totvs.com/pages/viewpage.action?pageId=224106789)

É importante salientar que nesse primeiro momento o Recebimento Automático possui algumas restrições, não sendo permitida ainda a geração automática de movimentos de entrada que são gerados através do processo "Cópia por Referência" (devoluções, retornos, etc.) ou de movimentos que possuem controle de lote e/ou número de série.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Serviço TOTVS Colaboração Consulta | Alteração | Integrações > Monitor de Arquivos TOTVS Colaboração > Processos > Serviço TOTVS Colaboração Consulta | Conforme definições constantes deste documento |
| Criação de Fórmulas | Alteração | Serviços Globais > Fórmulas > TOTVS Gestão de Estoque, Compras e Faturamento | Conforme definições constantes deste documento |
| Definições de Cli/For - TOTVS Colaboração | Criação | Cadastros > Mais... > Tabelas Auxiliares > Definições de Cli/For - TOTVS Colaboração | Conforme definições constantes deste documento |
| Natureza Inversa TOTVS Colaboração | Criação | Cadastros > Natureza Fiscal > Anexos > Natureza Inversa TOTVS Colaboração | Conforme definições constantes deste documento |
| Parâmetros por Filial | Alteração | Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Integrações > Fiscal > Dados Fiscais > Parâmetros por Filial | Conforme definições constantes deste documento |
| Processar Movimento - TOTVS Colaboração | Criação | Compras > Recebimento de Materiais > Processos > Processar Movimento - TOTVS Colaboração | Conforme definições constantes deste documento |
| Produtos TOTVS Colaboração | Criação | Cadastros > Produtos > Anexos > Produtos TOTVS Colaboração | Conforme definições constantes deste documento |
| Unidades TOTVS Colaboração | Criação | Cadastros > Mais... > Tabelas Auxiliares > Unidade > Anexos > Unidades TOTVS Colaboração | Conforme definições constantes deste documento |

## Tabelas Utilizadas:

* DCFOP - Naturezas Fiscais (CFOP);
* DREGRAICMS - Regras de ICMS;
* DREGRAIPI - Regras de IPI;
* GFORMULA - Fórmulas;
* TDEFINICOESCFOCOLAB - Definições de Cli/For - TOTVS Colaboração;
* TITMMOV - Itens de Movimento;
* TLOGCOMPIMPOSTOCOLAB - Diferenças de Tributos Calculados x Tributos XML;
* TMOV - Movimentos;
* TNATUREZACOLAB - Naturezas Inversas TOTVS Colaboração;
* TNFEENTRADA - Notas Fiscais (NF-e) Recebidas;
* TPARFILIAL - Parâmetros da Filial;
* TPRDCFOCOLAB - Produtos TOTVS Colaboração;
* TTRBMOV - Tributos do Movimento;
* TUNDCFOCOLAB - Unidades TOTVS Colaboração;
* TXMOCOLAB - XML Recebidos pelo TOTVS Colaboração.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
