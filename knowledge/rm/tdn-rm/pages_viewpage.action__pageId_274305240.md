---
content_hash: 6804b21b2475510ee03a9e35dbf47fa827741e7031444d37b1f4828270a64847
fetched_at: '2026-06-29T00:08:33.158164+00:00'
page_id: '274305240'
product: rm
source: tdn-rm
title: ER RMD - Registro de Materiais Dedutíveis - São Paulo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274305240
version: 21
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Fiscal |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | RMD - Registro de Materiais Dedutíveis | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.17 | **Réplica** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>* | | |

## Objetivo

Implementação do Registro de materiais dedutíveis em Lote - RMD

Legislação:

<http://nfpaulistana.prefeitura.sp.gov.br/Nfe/empresas/informacoes-gerais/manuais>

Para se beneficiar das deduções previstas no art. 31, inciso I, alínea “a” do Decreto 53.151/2012, o prestador de serviços de

construção civil deverá inicialmente registrar os documentos fiscais que comprovem as deduções de materiais incorporados ao imóvel,

com a identificação do número de inscrição no Cadastro de Obras de Construção Civil.

**Definição da Regra de Negócio**

**Parametrização**

Parametrizar a Filial para Emitir Livro de Construção Civil.

**Seleção dos Dados** 

Selecionar somente os Lançamentos de Entrada cuja a Natureza (CFOP) associado, esteja com o Campo "Classificação Operações Construção Civil" - na Pasta "Dados C.Civil", parametrizado.

Selecionar somente Lançamentos Fiscais que tenho Projeto associado "Situação Tributária – Sub Pasta Prestação de Serviço".

**Geração da rotina:**

Importar Layout RMD no Gerador de Saídas do Gestão Fiscal (Liber)

Após a importação do Layout acesse a Tela de geração da rotina e preencha os dados.

O arquivo vai ser gerado na pasta Saídas.

Exemplo: C:\totvs\CorporeRM\RM.Net\Saídas

****Arquivo - Layout Gerador de Saídas****

**REGISTRO TIPO 1 – CABEÇALHO**

| Campo | Posição Inicial | Posição Final | Tamanho | Obrigatório | Formato | Descrição | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo de Registro | 1 | 1 | 1 | Sim | Numérico | Deve ser preenchido com valor "1", indicando linha de cabeçalho. | Fixo "1" |
| Versão do Arquivo | 2 | 4 | 3 | Sim | Numérico | Indica a versão do layout a ser utilizada. Deve ser preenchido com o número da versão atual. A versão deste layout é a 001. | Campo Versão da Tela de Parametrização da Geração do Arquivo |
| Inscrição Municipal | 5 | 12 | 8 | Sim | Numérico | Inscrição municipal do prestador de serviços de construção civil a que se refere o arquivo. | Campo Inscrição Municipal da Filial informada na Tela da Parametrização  da Geração do Arquivo |
| Data de Início | 13 | 20 | 8 | Sim | AAAAMMDD | O arquivo de transferência deverá conter todos os documentos referentes a um período. Informe neste campo a Data INICIAL desse período no formato AAAAMMDD. | Campo Data inicial da Tela de Parametrização da Geração do Arquivo |
| Data de Fim | 21 | 28 | 8 | Sim | AAAAMMDD | O arquivo de transferência deverá conter todos os documentos referentes a um período. Informe neste campo a Data FINAL desse período no formato AAAAMMDD. | Campo Data Final Tela de Parametrização da Geração do Arquivo |
| Caractere Fim de Linha | 29 | 30 | 2 | Sim | ASCII(13) + ASCII(10) | Caractere de Fim de Linha (Chr(13) + Chr(10)). | O Gerador de Saídas já quebra a linha automaticamente. |

****REGISTRO TIPO 7 – DETALHE****

| Campo | Posição Inicial | Posição Final | Tamanho | Obrigatório | Formato | Descrição | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo de Registro | 1 | 1 | 1 | Sim | Numérico | Deve ser preenchido com valor "7", indicando linha de cabeçalho. | Fixo "7" |
| Situação do documento Fiscal | 2 | 2 | 1 | Sim | Numérico | 1 – Normal; 2 – Para cancelar registro do documento fiscal. | Campo StatusLf Lançamento Fiscal |
| Modelo do Documento Fiscal | 3 | 7 | 5 | Não | Texto | Informe o modelo do documento fiscal com 5 posições. | Campo CodModDoc Lançamento Fiscal |
| Número do Documento Fiscal | 8 | 16 | 9 | Sim | Numérico | Informe o Número do documento fiscal com 9 posições. | Campo DocIni Lançamento Fiscal |
| Série do Documento Fiscal | 17 | 25 | 9 | Não | Texto | Informe a Série do documento com 9 posições. | Campo Série do Lançamento Fiscal |
| Chave de Acesso | 26 | 69 | 44 | Não | Numérico | Informe a chave de acesso da Nota Fiscal Eletrônica - NF-e com 44 números. | Campo Chave de Acesso do Lançamento Fiscal |
| Valor Total dos Produtos | 70 | 84 | 15 | Sim | Numérico | Informe o Valor total dos produtos com 15 posições. Exemplo: R$ 500,85 – 000000000050085 R$ 500,00 – 000000000050000 | Somatório do ValorCont de Todas as Parcelas do Lançamento Fiscal |
| Valor a ser alocado para Deduções | 85 | 99 | 15 | Sim | Numérico | Informe o valor a ser alocado para deduções de materiais incorporados ao imóvel. Poderá ser menor ou igual ao valor total da nota | ValorCont do Lançamento Fiscal |
| CNPJ do Fornecedor | 100 | 113 | 14 | Sim | Numérico | Informe o CNPJ do fornecedor dos materiais dedutíveis com 14 posições. | CNPJ do Fornecedor vinculado ao Lançamento Fiscal |
| Razão Social do Fornecedor | 114 | 188 | 75 | Não | Texto | Informe a Razão Social do fornecedor dos materiais dedutíveis. | Razão Social do Fornecedor vinculado ao Lançamento Fiscal |
| UF do Fornecedor | 189 | 190 | 2 | Sim | Texto | Informe a unidade da federação (sigla do Estado onde o fornecedor está estabelecido) com 2 posições. | UF do Fornecedor vinculado ao Lançamento Fiscal |
| Data de Emissão do Documento Fiscal | 191 | 198 | 8 | Sim | AAAAMMDD | Informe a data de emissão do documento fiscal de materiais incorporados ao imóvel no formato AAAAMMDD. | Data Emissão do Lançamento Fiscal |
| Código Fiscal de Operações e Prestações - CFOP | 199 | 202 | 4 | Não | Numérico | Informe o Código Fiscal de Operações e Prestações – CFOP com 4 posições. | Natureza vinculada ao Lançamento Fiscal |
| Número de Inscrição da obra | 203 | 214 | 12 | Sim | Numérico | Informe o número de inscrição do Cadastro de Obras de Construção Civil. | Código do Projeto vinculado ao Lançamento Fiscal |
| Campo Reservado | 215 | 314 | 100 | Não |  | Campo reservado. Deverá ser preenchido com espaços em branco à direita até completar seu tamanho máximo. | Campo gerado em Branco |
| Caractere Fim de Linha | 315 | 316 | 2 | Sim | ASCII(13) + ASCII(10) | Caractere de Fim de Linha (Chr(13) + Chr(10)). | O Gerador de Saídas já quebra a linha automaticamente. |

****REGISTRO TIPO 9 – RODAPÉ****

| Campo | Posição Inicial | Posição Final | Tamanho | Obrigatório | Formato | Descrição | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo de Registro | 1 | 1 | 1 | Sim | Numérico | Deve ser preenchido com valor "9", indicando linha de cabeçalho. | Fixo "9" |
| Número de linhas Detalhe do Arquivo | 2 | 8 | 7 | Sim | Numérico | Número de linhas de detalhe (Tipo 7) contidas no arquivo. | Número Total de Linhas do Registro 7 - Detalhe |
| Somatória do Valor Total das Notas contidas no Arquivo | 9 | 23 | 15 | Sim | Numérico | Informe a soma dos valores das notas das linhas de detalhe (Tipo 7) contidas no arquivo. | Somatório do campo "Valor Total dos Produtos Registro 7 - Detalhe" |
| Somatória do Valor Total alocado para Deduções | 24 | 38 | 15 | Sim | Numérico | Informe a soma dos valores dos serviços das linhas de detalhe (Tipo 7) contidas no arquivo. | Somatório do campo "Valor a ser alocado para Deduções Registro 7 - Detalhe" |
| Caractere Fim de Linha | 39 | 40 | 2 | Sim | ASCII(13) + ASCII(10) | Caractere de Fim de Linha (Chr(13) + Chr(10)). | Gerada uma Linha em Branco no Final do Arquivo gerando a quebra de Linha |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
