---
content_hash: 0c1f2209f79b1c1c1a36169e09d364f4e3e99c73c09e5aa35f5efe57e5f86312
fetched_at: '2026-06-29T00:11:48.547032+00:00'
page_id: '82477740'
product: rm
source: tdn-rm
title: RMFIS00003_Como gerar DOT\ES
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=82477740
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | Rotina Estaduais - DOT\ES |
| **Subprocesso** | **:** | Parametrização - Declaração Operações Tributáveis |
| **Data da publicação** | **:** | 24/09/2013 |

**Introdução**

1.       Passos para implantação da Rotina DOT\ES

O arquivo ***IMPORTAR\_DOTS.XML*** será gerado com o formato e layout pré-estabelecido pela Secretaria do Estado do Espírito Santo, O arquivo a ser carregado, deverá ser do tipo ***XML***, versão 1.0, ISO-8859-1.  Somente serão considerados para a seleção dos registros na geração do arquivo, os lançamentos cuja Natureza Fiscal esteja com o campo Natureza com ICMS / IPI habilitado e que o status seja diferente de CANCELADO e ou ESTORNADO.

Quadro B – Valores a serem detalhados

Este registro será com o somatório da Prestação de Serviços com incidência de ICMS. Neste caso, será somado o Valor Contábil dos lançamentos de saída para o estado do ES, assim serão levadas em consideração naturezas fiscais de saída com Origem/Destino igual a Dentro do Estado. Além disso, devem ser notas de prestação de serviços de Transporte, Comunicação ou Energia Elétrica.

Este somatório deverá ser por código de município do lançamento fiscal. Será selecionado Lançamentos de Saída Internos e com as seguintes considerações:

Energia Elétrica: Será considerados os Lançamentos Fiscais de Saída com os seguintes **CFOP**: “5153; 5207; 5251; 5252; 5253; 5254; 5255; 5256; 5257; 5258; 5305; 5355.” 

Comunicação: Consideramos os Lançamentos Fiscais de Saída com o Tipo de Documento igual à 21

 Transporte: Consideramos os Lançamentos Fiscais de Saída com o Tipo de Documento igual à 07, 08, 8B, 09, 10,11 e 57

Água Canalizada: Consideramos os Lançamentos Fiscais de Saída com o Tipo de Documento igual à 29

Outras Atividades: Consideramos os Lançamentos Fiscais de Saída com o Tipo de Documento igual à 28

**1.1****Geração da Rotina**

A Rotina será gerada pela nova MDI.

Tela de geração da Rotina

Filial: Informar a Filial a qual se deseja gerar o arquivo

Período: Informar o Período que será gerado o arquivo.

 Tipo de Documento: A Sefaz disponibiliza os seguintes códigos:

√  Normal, no prazo regulamentar

√  Normal, fora do prazo regulamentar

√  Por retificação

√  Por pedido de baixa de inscrição

√  Por transferência de município

**Outros Dados**

Estoque Inicial: Informar o valor do estoque inicial que obrigatoriamente deverá ser igual ao estoque final do período anterior.

Estoque Final: Informar o valor do estoque final.

Classificação de Município: Informe a Classificação de Municípios que será utilizada na geração da rotina. A Classificação de Município é cadastrada em**Cadastros | Tabelas Auxiliares | Classificação de Município**. É necessário utilizar a Classificação do Município determinado pela SEFAZ, pois conforme o manual.

Valor Serviço de Transporte: Correspondente aos serviços de transporte contratados de pessoas físicas (transportadores autônomos) ou de empresas de transportes estabelecidas em outras unidades da federação, nos quais o contribuinte contratante assume a responsabilidade pelo recolhimento do imposto devido.

Executando a Geração da Rotina

Após gerar a Rotina é solicitado o caminho onde será salvo o arquivo do DOT.

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
