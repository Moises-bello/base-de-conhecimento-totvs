---
content_hash: 6bf55e1e2e0eff906f6b2f3dfc441d7c023aa470abf88b71c1b8196486656c37
fetched_at: '2026-06-29T00:11:16.483103+00:00'
page_id: '668642781'
product: rm
source: tdn-rm
title: PER/DCOMP (Pedido Eletrônico de Restituição, Ressarcimento ou Reembolso e Declaração
  de Compensação)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=668642781
version: 45
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Com o objetivo de proporcionar uma melhor experiência e alinhamento às atualizações mais recentes dos nossos produtos, informamos que a geração da obrigação **PER/DCOMP (Pedido Eletrônico de Restituição, Ressarcimento ou Reembolso e Declaração de Compensação)****,** já disponível no Módulo Gestão Fiscal, não será mais suportado no produto **RM Liber.exe** a partir da **versão 12.1.2502**

Reforçamos que essa alteração faz parte do nosso processo de evolução tecnológica, com a descontinuidade gradual de funcionalidades no **RM** **Liber.exe**. Para garantir a continuidade do uso e acesso à geração da obrigação **PER/DCOMP** recomendamos que a geração seja feita diretamente no **Módulo Gestão Fiscal**.

# Conteúdo

Conteúdo

# 01. Sobre

O **PER/DCOMP (Pedido Eletrônico de Restituição, Ressarcimento ou Reembolso e Declaração de Compensação)** é uma ferramenta eletrônica da Receita Federal que facilita a solicitação de devolução ou compensação de tributos pagos indevidamente, sendo essencial para empresas, especialmente indústrias exportadoras, que têm direito ao **Crédito Presumido do IPI**. Esse crédito, regulamentado pela Lei nº 9.363/1996, permite a recuperação tributária sobre operações de exportação, incentivando o setor. No módulo fiscal, o PER/DCOMP utiliza os [Lançamento Fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=427041477) para gerar arquivos específicos, com base na [Natureza de Operação](https://tdn.totvs.com/pages/viewpage.action?pageId=422545982#1-4), que devem ser enviados à Receita.

A correta parametrização dos lançamentos é fundamental para assegurar que os dados sejam processados adequadamente, gerando arquivos e relatórios fiscais que garantam conformidade com a legislação. Assim, o PER/DCOMP melhora a eficiência fiscal das empresas ao permitir a recuperação de tributos, otimizar o fluxo de caixa e garantir um controle fiscal mais ágil e preciso.

# 02. Geração do arquivo

A geração da PER/COMP deve ser acessada através do processo Gestão Fiscal | Obrigações Acessórias | Federais | PER/DCOMP. Nesta tela, o usuário deve selecionar o layout da **PER/DCOMP** e preencher as demais informações necessárias para a execução do processo.

A PRE/DCOMP utiliza o **FISLAY0028 - PERDCOMP.TotvsGen** do [Gerador de Saídas](https://tdn.totvs.com/pages/viewpage.action?pageId=237383341) que esta disponível no [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816).

Importante

Lançamentos fiscais que possuem o status **“Cancelado”** não serão incluídos nos arquivos da rotina.

# 03. Registros/Arquivos gerados

ArquivosleftVisaoGeralDosArquivosVisão geral dos arquivosVisão geral dos arquivos

Os quatro primeiros arquivos seguem o padrão de nomenclatura "**DCPaatAn.txt**", em que "**aa**" corresponde aos últimos dois dígitos do ano informado na geração da rotina, "**t**" equivale ao trimestre da data informada e "**n**" corresponde ao número do registro do arquivo.  
As informações sobre os registros estão dentro da aba de seu arquivo correspondente. **DCPaatA1.txt** - Notas Fiscais de Exportação Direta (Registro A1);

**DCPaatA2.txt** - Exportação Direta (Registro A2);

**DCPaatA3.txt** - Notas Fiscais de Venda para Empresa Comercial Exportadora (Registro A3);

**DCPaatA4.txt** - Notas Fiscais de Transferência de Crédito (Registro A4);

**ARQIPIA\_BB.txt** - Documento para Restituição de Valores de IPI para Notas Fiscais de Entrada (Ficha 11) e Saída (Ficha 12);

**Entradas.txt** - Notas Fiscais de Entrada/Aquisição (Registro R13);

**Perdcomp.txt** - Relatório de acompanhamento dos arquivos gerados.

DCPaatA1.txtDCPaatA1.txtNotas fiscais de exportação diretaA1ParametrizaçãoParametrização

Arquivo contendo os dados das Notas Fiscais de Exportação Direta, contendo um ou mais Registros A1.   
Serão selecionados os **Lançamentos Fiscais de Saída**, do grupo de **CFOP 7** (Natureza de Operação de Exportação), cujo parâmetro "**Usa Crédito Presumido"** esteja marcado e classificado como "**Outros**".

CamposRegistroA1Campos Registro A1

Para este registro, todos os campos tem origem dos dados com base nas informações preenchidas nos Lançamentos Fiscais.

| ORDEM | NOME | OBSERVAÇÃO | ORIGEM DOS DADOS |
| --- | --- | --- | --- |
| 01 | CNPJ | CNPJ do Estabelecimento Emitente, sem máscara | CNPJ do Cliente/Fornecedor do Lançamento Fiscal |
| 02 | Ano e Mês | Ano e Mês a que se referem a Exportação Direta, no formato AAAAMM | Data de Despacho Exterior do Lançamento Fiscal |
| 03 | Número Nota Fiscal | Número da Nota Fiscal de Exportação Direta | Número do Documento Fiscal do Lançamento Fiscal |
| 04 | Série Nota Fiscal | Série da Nota Fiscal de Exportação Direta | Número de Série do Lançamento Fiscal |
| 05 | Data Emissão Nota Fiscal | Data de Emissão da Nota Fiscal de Exportação Direta, no formato DD/MM/AAAA | Data de Emissão do Lançamento Fiscal |
| 06 | Valor Nota Fiscal | Valor em Reais da Nota Fiscal de Exportação Direta correspondente ao Registro de Exportação | Soma total dos itens do Lançamento Fiscal (Quantidade x preço + IPI + Seguro + Frete - Desconto) |
| 07 | Número Registro Exportação | Número do Registro de Exportação constante do SISCOMEX, com 12 dígitos | Número de Registro de Exportação do item informado no Lançamento Fiscal |

As situações tributárias devidamente parametrizadas para a geração dos registros, cujos itens possuírem o mesmo Número de Registro de Exportação dentro do mesmo Lançamento Fiscal de Saída, terão seus valores agrupados em um único registro dentro do arquivo.  
Em suma: Duas situações tributárias com CFOPs do grupo 7 (sejam a mesma, como 7.101.01, ou diferentes, como 7.101.01 e 7.105.02) dentro de um mesmo Lançamento Fiscal (número do documento 000001, por exemplo), que utilizem Crédito Presumido do IPI e estejam classificadas como Outras, cujos itens possuam o mesmo Número de Registro de Exportação (123456789101), serão geradas em uma única linha, com seus valores somados.  
Caso o Número de Registro de Exportação esteja vazio, o lançamento não será considerado no arquivo e um alerta será exibido no log do gerador de saídas, contendo o número do documento (DLAF.DOCINI) relacionado.

DCPaatA2.txtDCPaatA2.txtExportação diretaParametrizacao\_A2Parametrizacao\_A2\_cardParametrização

Arquivo contendo informações sobre a Exportação direta, contendo um ou mais Registros A2.   
Os dados deste arquivo são relacionados aos dados do arquivo anterior, portanto, a parametrização é a mesma necessária para o Registro A1.

Origem\_Campos\_A2\_cardCampos Registro A2

| ORDEM | NOME | OBSERVAÇÃO | ORIGEM DOS DADOS |
| --- | --- | --- | --- |
| 01 | CNPJ Estabelecimento | CNPJ do Estabelecimento ao qual se refere a exportação direta, sem máscara | CNPJ da Filial do contexto (GFILIAL.CGC) |
| 02 | Número do Registro de Exportação | Número do Registro de Exportação constante no SISCOMEX, com 12 dígitos | Número de Registro informado no item do Lançamento Fiscal (DITEM.NUMERORE) |
| 03 | Ano e Mês | Ano e Mês a que se referem a exportação direta, no formato AAAAMM | Mês e Ano da Data de Emissão do Lançamento Fiscal (DLAF.DATAEMISSAO) |
| 04 | Destinatário | Destinatário da exportação direta | Nome do Cliente/Fornecedor  (FCFO.NOME) |
| 05 | Código do País de destino | Código do país de destino, conforme constante no SISCOMEX | Três primeiros dígitos do código do país, de acordo com tabela informada na geração da rotina (DPAIS.CODPAIS) |
| 06 | Número de Despacho | Número de despacho da exportação constante no SISCOMEX, com 11 dígitos | Número de despacho informado no Lançamento Fiscal, na aba de exportação (DLAFEXTERIOR.NUMDESPACHO) |
| 07 | Data de Embarque | Data de embarque, no formado DD/MM/AAAA | Data de saída da tela de Lançamento Fiscal |
| 08 | Valor Despacho | Valor total do despacho na moeda negociada | Valor de despacho informado na aba de Exportação do Lançamento Fiscal (DLAFEXTERIOR.VALORDESPACHO) |
| 09 | Código Moeda | Código da moeda negociada, conforme tabela constante no SISCOMEX, com 3 dígitos | Moeda informada na aba Exterior do Lançamento Fiscal, de acordo com a tabela informada na geração da rotina (DMOEDA.CODMOEDA) |

Como este arquivo é um complemento do arquivo anterior, as condições de agrupamento se mantém (vide parágrafo abaixo da tabela em DCPaatA1.txt > Campos Registro A1).

DCPaatA3.txtDCPaatA3.txtNotas fiscais de venda para empresa comercial exportadoraParametrizacao\_A3Parametrizacao\_Registro\_A3Parametrização

Arquivo contendo informações sobre Venda para Empresa Comercial Exportadora, contendo um ou mais Registros A3.  
Serão selecionados os **Lançamentos Fiscais de Saída**, do grupo de **CFOP 5 e 6**, cujo parâmetro "**Usa Crédito Presumido"** esteja marcado e classificado como "**Venda Comercial Exportadora**".

Campos\_Registro\_A3Campos A3

| ORDEM | NOME | OBSERVAÇÃO | ORIGEM DOS DADOS |
| --- | --- | --- | --- |
| 01 | CNPJ Estabelecimento Emitente | CNPJ do Estabelecimento ao qual se refere a exportação direta, sem máscara | CNPJ da Filial do contexto atual (GFILIAL.CGC) |
| 02 | CNPJ Comercial Exp | CNPJ da empresa comercial exportadora | CNPJ do Emitente informado no Lançamento Fiscal (FCFO.CGCCFO caso Cliente/Fornecedor, GFILIAL.CGC caso Empresa) |
| 03 | Ano e Mês | Ano e Mês a que se referem a exportação direta, no formato AAAAMM | Campo formatado a partir do ano e mês informados na Data de Emissão (DLAF.DATAEMISSAO) |
| 04 | Número Documento | Número da nota fiscal de venda para a empresa comercial exportadora | Número do documento informado no Lançamento Fiscal (DLAF.DOCINI) |
| 05 | Série Documento | Série da nota fiscal de venda para a empresa comercial exportadora | Série selecionada no Lançamento Fiscal (DLAF.SERIEDOC) |
| 06 | Data de Emissão | Data de emissão da nota fiscal, no formado DD/MM/AAAA | Data de Emissão informada no Lançamento Fiscal (DLAF.DATAEMISSAO) |
| 07 | Valor Nota Fiscal | Valor em reais da nota fiscal de venda para a empresa comercial exportadora | Soma total dos itens do Lançamento Fiscal (Quantidade x preço + IPI + Seguro + Frete - Desconto) |

DCPaatA4.txtDCPaatA4.txtNotas fiscais de transferência de créditoRegistro\_A4Parametrizacao\_Registro\_A4Parametrização

Arquivo contendo informações sobre Notas Fiscais de Transferência de Crédito, contendo um ou mais Registros A4.  
Serão selecionados os **Lançamentos Fiscais de Saída**, do grupo de **CFOP 5 e 6**, cujo parâmetro "**Usa Crédito Presumido"** esteja marcado e classificado como "**Transferência Crédito**".

Campos\_A4Campos Registro A4

| ORDEM | NOME | OBSERVAÇÃO | ORIGEM DOS DADOS |
| --- | --- | --- | --- |
| 01 | CNPJ Estabelecimento Beneficiado | CNPJ do Estabelecimento que será beneficiado com o crédito | CNPJ do Cli/For ou Emitente do Lançamentos Fiscal (FCFO.CGCCFO ou GFILIAL.CGC) |
| 02 | Ano e Mês | Ano e Mês do trimestre da transferência de crédito, no formato AAAAMM | Campo formatado a partir do ano e mês informados na Data de Emissão (DLAF.DATAEMISSAO) |
| 03 | Número Nota Fiscal | Número do documento | Número do documento informado no Lançamento Fiscal (DLAF.DOCINI) |
| 04 | Série Nota Fiscal | Série da nota fiscal | Série selecionada no Lançamento Fiscal (DLAF.SERIEDOC) |
| 05 | Data de Emissão | Data de emissão da nota fiscal, no formado DD/MM/AAAA | Data de Emissão informada no Lançamento Fiscal (DLAF.DATAEMISSAO) |
| 06 | Valor Nota Fiscal | Valor em reais da nota fiscal da transferência de crédito | Soma total dos itens do Lançamento Fiscal (Quantidade x preço + IPI + Seguro + Frete - Desconto) |

IPIA\_BB.txtARQIPIA\_BB.txtCredito IPIDescricaoIPIDescricaoIPI

Arquivo é gerado para cada trimestre escolhido, onde a letra A significa o número do Trimestre , e as letras BB o mês referente aquele trimestre (Exemplo IPI1\_01.txt - Primeiro Trimestre, mês de Janeiro).

As informações contidas no arquivo são de Notas fiscais de Entrada, Ficha 11 (R11), e Saída, Ficha 12 (R12), podendo ter um ou mais registros. Os registros serão agrupados por CFOP.

Arquivo IPIFicha11Ficha11

| ORDEM | NOME | OBSERVAÇÃO | ORIGEM DOS DADOS |
| --- | --- | --- | --- |
| 01 | Tipo | Tipo da Ficha | Texto "R11" |
| 02 | CNPJ do Declarante | CNPJ do Declarante | CNPJ da Filial Matriz |
| 03 | CNPJ da Sucedida | CNPJ da sucedida informado na Ficha Novo Documento | Campo não é gerado |
| 04 | CNPJ do Estabelecimento Detentor de Crédito | CNPJ do estabelecimento detentor de crédito informado na Ficha Novo Documento | Filial do Contexto - GFILIAL.CGC |
| 05 | Ano Período de Apuração | Ano da emissão do Lançamento Fiscal contido no Período de Apuração | Quatro dígitos do Ano de Emissão do Lançamento Fiscal |
| 06 | Mês Período de Apuração | Mês da emissão do Lançamento Fiscal contido no Período de Apuração | Dois dígitos do Mês de Emissão do Lançamento Fiscal |
| 07 | Decêndio / Quinzena / Mensal |  |  |
| 08 | CFOP | Natureza Fiscal informada no Lançamento Fiscal - Sub Pasta Situação Tributária | Gerado com o Natureza Fiscal associada ao Lançamento Fiscal - Sub Pasta Situação Tributaria DCFOP.CODNAT |
| 09 | Operações com Crédito do Imposto - Base de Cálculo | Valor do Campo Base de Cálculo do IPI informado no Lançamento Fiscal | Gerado com Valor do campo Base de Calculo do IPI - Situação Tributaria - Sub Pasta ICMS\IPI  DLAF.BASEIPI |
| 10 | Operações com Crédito do Imposto - IPI Creditado | Valor do Campo IPI Tributado informado no Lançamento Fiscal | Gerado com Valor do campo IPI - Situação Tributaria - Sub Pasta ICMS\IPI  DLAF.VALORIPI |
| 11 | Operações com Crédito do Imposto - Isentas ou Não Tributadas | Valor do Campo Isento do IPI informado no Lançamento Fiscal | Gerado com Valor do campo Isento do IPI - Situação Tributaria - Sub Pasta ICMS\IPI  DLAF.ISENTOIPI |
| 12 | Operações com Crédito do Imposto - Outras | Valor do Campo Outros do IPI informado no Lançamento Fiscal | Gerado com Valor do campo Outros do IPI - Situação Tributaria - Sub Pasta ICMS\IPI  DLAF.OUTROSIPI |
| 13 | Delimitador |  |  |

Ficha12Ficha12

| ORDEM | NOME | OBSERVAÇÃO | ORIGEM DOS DADOS |
| --- | --- | --- | --- |
| 01 | Tipo | Tipo da Ficha | Texto "R12" |
| 02 | CNPJ do Declarante | CNPJ do Declarante | CNPJ da Filial Matriz |
| 03 | CNPJ da Sucedida | CNPJ da sucedida informado na Ficha Novo Documento |  |
| 04 | CNPJ do Estabelecimento Detentor de Crédito | CNPJ do estabelecimento detentor de crédito informado na Ficha Novo Documento | Filial do Contexto - GFILIAL.CGC |
| 05 | Ano Período de Apuração | Ano da emissão do Lançamento Fiscal contido no Período de Apuração | Quatro dígitos do Ano de Emissão do Lançamento Fiscal |
| 06 | Mês Período de Apuração | Mês da emissão do Lançamento Fiscal contido no Período de Apuração | Dois dígitos do Mês de Emissão do Lançamento Fiscal |
| 07 | Decêndio / Quinzena / Mensal |  |  |
| 08 | CFOP | Natureza Fiscal informada no Lançamento Fiscal - Sub Pasta Situação Tributária | Gerado com o Natureza Fiscal associada ao Lançamento Fiscal - Sub Pasta Situação Tributaria DCFOP.CODNAT |
| 09 | Operações com Crédito do Imposto - Base de Cálculo | Valor do Campo Base de Cálculo do IPI informado no Lançamento Fiscal | Gerado com Valor do campo Base de Calculo do IPI - Situação Tributaria - Sub Pasta ICMS\IPI  DLAF.BASEIPI |
| 10 | Operações com Crédito do Imposto - IPI Creditado | Valor do Campo IPI Tributado informado no Lançamento Fiscal | Gerado com Valor do campo IPI - Situação Tributaria - Sub Pasta ICMS\IPI  DLAF.VALORIPI |
| 11 | Operações com Crédito do Imposto - Isentas ou Não Tributadas | Valor do Campo Isento do IPI informado no Lançamento Fiscal | Gerado com Valor do campo Isento do IPI - Situação Tributaria - Sub Pasta ICMS\IPI  DLAF.ISENTOIPI |
| 12 | Operações com Crédito do Imposto - Outras | Valor do Campo Outros do IPI informado no Lançamento Fiscal | Gerado com Valor do campo Outros do IPI - Situação Tributaria - Sub Pasta ICMS\IPI  DLAF.OUTROSIPI |
| 13 | Delimitador |  |  |

Entradas.txtEntradas.txtNotas fiscais de entrada/aquisiçãoArquivo de EntradasParametrizacao\_R13Parametrização R13

Arquivo contendo informações sobre Notas Fiscais de Aquisição/Entrada, contendo um ou mais Registros R13.  
Serão selecionados os **Lançamentos Fiscais de Entrada**, do grupo de **CFOP 1, 2 e 3**, cuja **Regra de IPI** seja do tipo "**Tributado**" ou "**Tributado 50%**".

Campos\_Registro\_R13Campos Registro R13

| ORDEM | NOME | OBSERVAÇÃO | ORIGEM DOS DADOS |
| --- | --- | --- | --- |
| 01 | Tipo | Tipo da Ficha | Texto "R13" |
| 02 | CNPJ do Declarante | CNPJ do Declarante | CNPJ da Filial Matriz |
| 03 | CNPJ da Sucedida | CNPJ da sucedida informado na Ficha Novo Documento |  |
| 04 | CNPJ do Estabelecimento Detentor de Crédito | CNPJ do estabelecimento detentor de crédito informado na Ficha Novo Documento | Filial do Contexto - GFILIAL.CGC |
| 05 | CNPJ do Emitente | CNPJ do emitente da nota fiscal de aquisição | SE Tipo Emitente for Cli/For ENTÃO FCFO.CGCCFO SENÃO SE Tipo Emitente for Empresa ENTÃO GFILIAL.CGC (Filial selecionada no Lançamento Fiscal) |
| 06 | Número Nota Fiscal | Número da Nota Fiscal | DLAF.DOCINI |
| 07 | Série Nota Fiscal | Série da Nota Fiscal | DLAF.SERIEDOC |
| 08 | Data de Emissão | Data de Emissão da nota fiscal, no formato DDMMAAAA | DLAF.DATAEMISSAO |
| 09 | Data de Entrada | Data válida, compreendida no Trimestre-Calendário/Ano de apuração do crédito informado na Ficha Novo Documento. Data de Entrada no Estabelecimento Detentor do Crédito >= Data de Emissão (campo 08) | DLAF.DATAES |
| 10 | CFOP | CFOP atribuído ao Lançamento Fiscal | DCFOP.CODNAT |
| 11 | Valor\* | Valor total das entradas, incluindo valor do IPI | Soma total dos itens do Lançamento Fiscal (Quantidade x preço + IPI + Seguro + Frete - Desconto) |
| 12 | Valor IPI Destacado\* | Valor total do IPI destacado na nota fiscal de aquisição | DLAF.VALORIPI ou DLAF.VALORIPISEMCREDITO |
| 13 | Valor IPI Livro RAIPI\* | Valor total do IPI creditado no Livro RAIPI relativo à nota fiscal informada, mesmo que não haja valor | DLAF.VALORIPI ou DLAF.VALORIPISEMCREDITO |

Esse arquivo requer uma linha em branco entre os registros quando há mais de um Registro R13 criado. Para atender a essa especificação, foi criado um registro vazio, dentro do Registro R13, gerando apenas um caractere de espaço para deixar a linha em branco. Essa solução não afeta o tamanho do registro e o arquivo pode ser importado normalmente no programa da PER/DCOMP.  
  
\*O arquivo é gerado somente com letras e números, portanto, não há vírgula nos valores. Esses três campos são gerados considerando duas casas decimais. Logo, caso o valor informado em algum desses campos seja 10,35 (dez inteiros e trinta e cinco décimos), por exemplo, o registro será gerado no formato "00000000001035".

Perdcomp.txtPerdcomp.txtRelatório de acompanhamento dos arquivos geradosArquivo de EntradasRelatorioArquivo de relatório

Arquivo contendo informações sobre os arquivos DCPaatA1.txt, DCPaatA2.txt, DCPaatA3.txt e DCPaatA4.txt. Pode ser considerado como um totalizador de cada arquivo, para mostrar um resumo de tudo o que foi coletado durante a geração da rotina que seja relativo ao crédito presumido do IPI.

Campos\_RelatorioCampos Relatório

| ORDEM | NOME | OBSERVAÇÃO | ORIGEM DOS DADOS |
| --- | --- | --- | --- |
| 01 | Nome | Nome do arquivo | "DCP" + ano (últimos dois dígitos) + trimestre (um dígito) + "A" + número do arquivo (um dígito) + ".txt" |
| 02 | Data | Data de geração do relatório | Data que o relatório foi gerado |
| 03 | Registros | Quantidade de registros de cada arquivo | Quantidade de linhas lidas de cada arquivo |
| 04 | Totalizador | Totalizador dos valores de cada arquivo | Soma dos valores decimais de cada arquivo |

# 04. Vídeos How To

648432
