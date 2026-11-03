---
content_hash: d27299d8ae4a33d337e113883446fc8f12ba7b38ea481a5582b769b67abc284e
fetched_at: '2026-06-29T00:05:57.323090+00:00'
page_id: '172297423'
product: rm
source: tdn-rm
title: COMO FAZER - Geração de Arquivo NIS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=172297423
version: 6
---

Produto

**RMLabore**

**Processo:** **Processo de Geração de Arquivo NIS - Cadastramento de Trabalhador em Lote**

**Versão: 11.8X ou superiores**

1. Acesse o menu Folha Mensal -> Relatórios da Folha -> Cadastro NIS

Clique para visualizar imagem

2. Insira as informações conforme os campos

Clique para visualizar imagem

**Layout Gerador de Saídas – NIS em Arquivo**: Selecionar o layout do NIS importado no Gerador de Saídas (FOPLAY0001 - Relatório Cadastro NIS v13.2.TotvsGen).

**Para ver como importar o layout clique no [link.](http://tdn.totvs.com/pages/viewpage.action?pageId=152800283)**

**Conceito de Classificação para Tipo de Logradouro (Tipo de Rua)**: Foi disponibilizado uma funcionalidade para atender o e-Social.

Esta classificação tem o objetivo de realizar um “De/Para” associando o tipo de logradouro à um código ou sigla.

Detalhes de como realizar esta classificação para tipo de logradouro está no Anexo I deste arquivo.

**Localização do(s) Arquivo(s)**: Local onde será gravado o arquivo gerado.

**CPF do responsável pelo cadastro**: Campo é utilizado para informação em um registro do arquivo

**Formato Nome do Arquivo**: Opção para definir o formato do nome do arquivo gerado. Na versão 13 do layout o formato para o nome foi alterado, contudo o exemplo de arquivo gerado continua com o nome da versão 12. Acreditamos que o formato da versão 13 seja o correto, mas existe a opção de utilizar o formato da versão anterior.

3. Na próxima tela, preencha conforme os campos

Clique para visualizar imagem

**Seleção de Funcionários**: Filtro global, que define quais serão os filtros para funcionários que terão registros informados caso não seja marcado o parâmetro “Usa Parâmetros Específicos” no passo posterior.

**Tipo de Arquivo**:

*Simplificado* - usado para os casos de envio de arquivo diretamente pela Empresa, com o

seguinte conjunto de registros lógicos:

* Header Geral
* n Registros Detalhe, onde n varia de zero a 99999999999
* Trailer Geral

*Completo*: usado para os casos de envio de arquivo por Empresa com os dados

segregados por filial ou Escritório de Contabilidade com dados de várias empresas distintas,

contendo um conjunto de registros lógicos com a seguinte estrutura:

* Header Geral
* Header Parcial
* n Registros Detalhe, onde n varia de zero a 99999999999
* Trailer Parcial
* Trailer Geral

Neste caso, a sequência “Header Parcial, Registros Detalhe e Trailer Parcial”, doravante

denominada Lote, poderá ocorrer várias vezes no arquivo e corresponderá aos dados de

uma empresa.

**Tipo de Remessa**: Informação de arquivo Original ou Retificação do mesmo

**Tipo de Geração Arquivo Completo**: Parâmetro usado somente no caso de arquivo completo, podendo gerar um arquivo unificado, ou um arquivo por coligada, ambos agrupando os funcionários por filiais da coligada.

**Versão do Arquivo**: Conforme o próprio texto informativo do campo, uma nova versão de arquivo significa informação de novos dados. Poderá ser informada a mesma versão de arquivo anteriormente postado nos casos de retificação. Sempre inicia por 0 (limite 99).

Caso seja utilizada a opção de gerar vários arquivos (um arquivo por coligada) o número da versão é incrementado a cada coligada a partir do valor inicial informado.

Ex: Informada a versão 00 e gerado três arquivos. Logo será gerado a versão 00, 01, 02, respectivamente na ordem das coligadas geradas.

***Obs. Cabe ao usuário o gerenciamento da versão do arquivo conforme descrito acima.***

4. Selecione as coligadas que deseja gerar, podendo ser gerado um arquivo por coligada (nos casos de simplificado ou completo por coligada) ou gerar um único arquivo (completo unificado) agrupando por filiais das coligadas selecionadas.

Clique para visualizar imagem

**Coligada**: Somente utilizado para geração dos registros para o arquivo Completo, informação da coligada que contemplará o Header Geral dos arquivos (Empresa que está enviando os arquivos).

Clique para visualizar imagem

**Usa Parâmetros Específicos:** Habilita o uso dos parâmetros específicos para cada coligada. Utilizando esta opção, os Filtros Globais, do Passo 1 são descartados.

Anexo I – Classificação Tipo de Logradouro

Cria-se uma classificação:

O nome desta classificação é livre, ficando a critério do usuário:

Após a criação de uma classificação, faz-se a associação conforme necessidade:

Existem alguns Tipos de Logradouros pré-cadastrados na Base:

Neste Exemplo, faremos a associação do tipo logradouro “RUA” à uma sigla conforme layout do NIS:

Adicionamos uma nova Codificação do Tipo de Logradouro (Tipo Rua), selecionamos a categoria que pertencerá

Agora, o tipo de logradouro “RUA” para a categoria criada NIS, terá a sigla (código) “R” que será usado na geração do arquivo

Abaixo, segue a tabela de tipo de logradouro do layout do NIS disponibilizado pela Caixa Econômica Federal que contempla todas as siglas usadas no arquivo:
