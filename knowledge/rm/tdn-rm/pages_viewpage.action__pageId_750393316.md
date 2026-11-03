---
content_hash: c575bdb9eda30c0874e798295c0c208e37f6dbdffc71c9cbe318789211d5f8bc
fetched_at: '2026-06-29T00:11:32.848773+00:00'
page_id: '750393316'
product: rm
source: tdn-rm
title: Etapa de Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=750393316
version: 48
---

Para o correto funcionamento da rotina de *"Inclusão de Movimento Através do XML - NF-e"* será necessário algumas definições, como:

* Definir o diretório de importação
* Definir o parceiro para recebimento dos arquivos XML
* Definir os documentos que serão importados
* Avaliar se o processo poderá ser 100% automatizado

A seguir, detalhamos toda a parametrização referente a esta etapa.

---

Etapas da ParametrizaçãoEtapasdaParametrizacaoParâmetros por Coligada

Em*“Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Integrações > Fiscal > Importação/Envio de Arquivos XML”,* deverá ser preenchido por filial o “Tipo de Integração”  e o diretório onde serão salvos os arquivos XML.

**Obs**: Esta parametrização é realizada apenas 1 vez, para cada coligada.

Tipo de Integração:

* TOTVS Colaboração 2.00 - indica que é utilizado a integração com a Neogrid.
* TOTVS Colaboração 1.00 - indica utilização do TSS
* TOTVS Processos Fiscais - indica que está utilizando o TPF (TOTVS Processos Fiscais)
* TOTVS Transmite – indica que está utilizando o TOTVS Transmite
* Não Utiliza - indica que não utiliza nenhum dos parceiros disponíveis

**Realizar Importação de XML de NF-e e CT-e (sem integração com parceiros)**: marque apenas se não houver contratação de parceiro para disponibilizar os arquivos XML automaticamente na pasta *Client EDI*.

**Diretório Padrão para Importação dos Arquivos XML:** informe o diretório escolhido para a integração (diretório onde os arquivos XML serão salvos), que deverá conter as subpastas IN e RM.

A partir da release 12.1.2402 será possível utilizar este cadastro em ambientes multi-tenant. Para estes ambientes o diretório deverá ser informado manualmente (não será possível selecionar). Isso se faz necessário, pois o diretório escolhido será uma subpasta do **FileServerpath****,** (para mais informações acesse: ).  Dessa forma, não deverá ser informado um caminho com uma raiz (exemplo: C:\pasta), será definida apenas a subpasta para ser utilizada no **FileServerpath.** Conforme exemplo abaixo:

Esta configuração para ambiente Multi Tenant está disponível a partir da versão 12.1.2402

Atenção!

O diretório deverá estar compartilhado em rede com todos os usuários, permitindo leitura e gravação.

Parâmetros por Filial

Em*“Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Integrações > Fiscal > Parâmetros por Filial > Importação/Envio de Arquivos XML 1/2”,* deverá ser definido qual o tipo de documento fiscal será recebido pelo processo de importação de arquivos XML.

**Obs**: Estas parametrizações deverão ser realizadas para cada filial que desejar utilizar o processo de importação de arquivo XML.

Na segunda etapa, em*“Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Integrações > Fiscal > Parâmetros por Filial > Importação/Envio de Arquivos XML 2/2”,* deverão ser definidos:

1 – O  tipo de recebimento de NF-e - O campo "Tipo de Recebimento de NF-e" define a forma como o sistema irá realizar o processo de recebimento automático das NF-e. Esta informação é parametrizável por Filial e/ou por Fornecedor.

Para mais informações sobre o tipo de recebimento, acesse a aba .

2 – A Fórmula Tipo Mov. p/Recebimento NF-e – Poderá ser definido uma fórmula com regras especificas para entrada automática das NF-e’s.

Para mais informações sobre o tipo de recebimento, acesse a aba

3 – Recebimento de CT-e -  definir um tipo de movimento default para o recebimento do CT-e

obs.: as formulas parametrizadas no campo 'Fórmula Tipo Mov. Para Recebimento de NF-e' devem ser da aplicação = 'T' (Gestão de estoque, compras e faturamento)

TipoRecebimentoTipo de Recebimento

Esta etapa deverá ser parametrizada apenas se o processo de inclusão de documentos a partir de arquivos XML for ocorrer de forma totalmente automatizada. Para isto, devera ser avaliado se há necessidade de interferência do usuário no momento da inclusão do movimento (se durante o processo de inclusão do movimento for necessário preenchimento ou conferência de campos, a inclusão de documentos a partir de arquivos XML  não poderá ser totalmente automatizada, sendo desnecessário o preenchimento dos parâmetros abaixo).

O campo "Tipo de Recebimento de NF-e" define a forma como o sistema irá realizar o processo de recebimento automático das NF-e. Esta informação é parametrizável por Fornecedor  e/ou porFilial. Assim, quando do recebimento automático de uma NF-e, caso o emitente da mesma conste na tabela de definições do Cli/For para importação de XML (*"Cadastros > Tabelas Auxiliares > Definições de Cli/For – Importação de Arquivo XML"*), essa informação prevalecerá sobre o parâmetro definido por filial.  Ou seja, para determinados fornecedores poderá ser definido um Tipo de Recebimento diferente do que é praticado geralmente.

Caso a filial não vá utilizar a rotina de recebimento automático da NF-e, o campo "Tipo de Recebimento de NF-e" deverá permanecer em branco.

 Tipo de Recebimento por Filial

Para evitar erro no momento do recebimento, é imprescindível que o parâmetro da filial esteja sempre preenchido indicando como o sistema deve proceder para os fornecedores cujo Tipo de Recebimento não foi informado.

Acesse "*Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Dados Fiscais | Parâmetros por Filial | Importação/Envio de Arquivo XML 1/2"* e informe o Tipo de Recebimento que será utilizado na empresa.

Tipo de Recebimento por Fornecedor

Lembre-se que, caso para alguns fornecedores o tipo de recebimento seja diferente do que foi definido para a filial, você deve fornecer esta informação em *"Cadastros > Tabelas Auxiliares > Definições de Cli/For –Importação de Arquivo XML".*

TipoRecebimento

FormulaTipoMovtoFórmula Tipo Movto Recebimento NF-e

Esta etapa deverá ser parametrizada apenas se o processo de inclusão de documentos a partir de arquivos XML for ocorrer de forma totalmente automatizada. Para isto, devera ser avaliado se há necessidade de interferência do usuário no momento da inclusão do movimento (se durante o processo de inclusão do movimento for necessário preenchimento ou conferência de campos, a inclusão de documentos a partir de arquivos XML não poderá ser totalmente automatizada, sendo desnecessário o preenchimento dos parâmetros abaixo).

Em*“Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Integrações > Fiscal > Parâmetros por Filial > Importação/Envio de Arquivos XML 2/2”>”,* deverá ser preenchido por filial o campo "Fórmula Tipo Mov. p/Recebimento NF-e**"**.

Este parâmetro é do tipo fórmula, e assim, através do mesmo, o usuário poderá implementar uma regra específica para buscar o tipo de movimento que será utilizado tanto no recebimento automático como no recebimento manual das NF-e de cada filial.

Essa fórmula será executada para cada XML a ser recebido.

Foram criadas quatro novas funções de fórmula para auxiliar na criação dessa regra, são elas:

* TABXMLCOLAB - Retorna o valor de um campo da tabela de XMLs do Totvs Colaboração (TNFEENTRADA);
* DADOSXMLCOLAB - Retorna o valor de uma TAG de um XML;
* QTDTAGSXMLCOLAB - Retorna o número de vezes que uma determinada Tag aparece no XML;
* TABPRDCOLAB - Retorna o conteúdo de um campo do cadastro dos produtos vinculados aos itens constantes do XML.

Explicaremos a seguir a sintaxe de cada uma dessas funções bem como daremos exemplos de utilização de todas elas.

TABXMLCOLAB - Retorna o valor de um campo da tabela de XMLs do Totvs Colaboração (TNFEENTRADA)Sintaxe

* TABXMLCOLAB ('NomeCampo', 'TipoRetorno') onde:
* NomeCampo = Nome do Campo da Tabela TNFEENTRADA. Podemos citar como campos dessa tabela o código da coligada (CODCOLIGADA), o código da filial (CODFILIAL), o código da coligada do fornecedor (CODCOLCFO), o código do fornecedor (CODCFO), a data de emissão (DATAEMISSAO), etc.;
* TipoRetorno = Informa o tipo de retorno relativo ao campo informado em NomeCampo, se S (string), V (valor), D (data) ou I (inteiro).
Exemplo de fórmula de seleção do tipo de movimento utilizando a função TABXMLCOLAB

Neste exemplo o sistema irá verificar na tabela TNFEENTRADA (tabela que contém os XML importados) o registro gerado pelo XML e caso o código do fornecedor seja F00017 o movimento será gerado com o tipo 1.2.27, caso contrário o tipo do movimento será 1.2.20.

DADOSXMLCOLAB - Retorna o valor de uma TAG de um XMLSintaxe

* DADOSXMLCOLAB ('CaminhoTAG', 'NamespaceXML') onde:
* CaminhoTAG = Caminho da TAG desejada, separado por barra ( / ). Exemplo: '/nfeProc/NFe/infNFe/det/prod/CFOP' para o CFOP do produto do XML;
* IMPORTANTE: O Caminho da Tag deve ser informado exatamente como consta no XML, esta pesquisa considera letras maiúsculas e minúsculas (Case Sensitive).
* NamespaceXML = <http://www.portalfiscal.inf.br/nfe>
Exemplo de fórmula de seleção do tipo de movimento utilizando a função DADOSXMLCOLAB

Quando a tag possuir índice, basta informá-lo o entre colchetes ([ ]).

No exemplo acima o sistema irá retornar a informação da TAG CFOP do primeiro item da NFe, já que não informamos nenhum índice.

Veja abaixo um exemplo da mesma fórmula retornando o CFOP do 2º item da NFe:

QTDTAGSXMLCOLAB - Retorna o número de vezes que uma determinada Tag aparece no XMLSintaxe

* QTDTAGSXMLCOLAB ('CaminhoTAG', 'NamespaceXML') onde:
* CaminhoTAG = Caminho da TAG desejada, separado por barra ( / ). Exemplo: '/nfeProc/NFe/infNFe/det' para o produto do XML;
* NamespaceXML = <http://www.portalfiscal.inf.br/nfe>
Exemplo de fórmula de seleção do tipo de movimento utilizando as funções QTDTAGSXMLCOLAB

No exemplo acima através da função QTDTAGSXMLCOLAB o sistema irá identificar o número de itens constantes do XML. Após isso, através da função DADOSXMLCOLAB, irá percorrer todos os itens do XML e caso o último CFOP seja 5.405 o tipo de movimento gerado será o 1.2.02. Senão, o tipo de movimento gerado será 1.2.01.

Assim, utilizando em uma mesma fórmula estas duas funções (QTDTAGSXMLCOLAB e DADOSXMLCOLAB), o sistema irá verificar determinado dado de todos os itens constantes de um XML.

Esta mesma fórmula também poderia ser escrita desta maneira:

TABPRDCOLAB - Retorna o conteúdo de um campo do cadastro dos produtos vinculados aos itens constantes do XMLSintaxe

* TABPRDCOLAB ('CodigoProdutoColab', 'NomeCampo', 'TipoRetorno') onde:
* CódigoProdutoColab = Código do Produto na tabela "Produtos TOTVS Colaboração";
* NomeCampo = Nome do campo da tabela de Produtos;
* TipoRetorno = Informa o tipo de retorno relativo ao campo informado em NomeCampo, se S (string), V (valor), D (data) ou I (inteiro).
Exemplo de fórmula de seleção do tipo de movimento utilizando a função TABPRDCOLAB

Neste exemplo, em primeiro lugar o sistema utilizará a função QTDTAGSXMLCOLAB para identificar o número de itens constantes do XML, logo depois, através da função DADOSXMLCOLAB irá percorrer todos os itens do XML e através da função TABPRDCOLAB irá identificar na tabela Produtos TOTVS Colaboração quais são os produtos vinculados aos itens do XML. Após verificar sua tabela de produtos e irá analisar se algum deles possui a Tabela de Classificação 1 preenchida com 05. Em caso afirmativo o sistema irá gerar o movimento com o tipo 1.2.12, caso contrário o movimento será do tipo 1.2.11.

Assim, utilizando em uma mesma fórmula estas três funções (QTDTAGSXMLCOLAB, DADOSXMLCOLAB e TABPRDCOLAB), o sistema irá verificar determinado dado de todos os itens constantes de um XML e ainda irá compará-lo com determinado campo do seu cadastro de Produtos. Caso, para algum XML, através da fórmula não seja possível definir o seu tipo de movimento, o XML será criado na base de dados com o status 'Inconsistente' e poderá ser recebido manualmente.

TipoMovto
