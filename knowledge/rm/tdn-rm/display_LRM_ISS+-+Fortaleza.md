---
content_hash: f480195f0eaac889f6b00546904edf0fc6a59e9898c21bf175beaffade0f7994
fetched_at: '2026-06-29T00:09:19.523373+00:00'
page_id: '422545600'
product: rm
source: tdn-rm
title: ISS - Fortaleza
type: documentation
url: https://tdn.totvs.com/display/LRM/ISS+-+Fortaleza
version: 6
---

**Estrutura do Arquivo**  
  
O arquivo deve ser gerado em formato texto (.txt) com campos separados por ";" , separados um Arquivo para os Serviços Tomados e outro arquivo para Cliente\Fornecedor (.csv).  
  
**Seleção de Lançamentos**  
  
A seleção dos Lançamentos Fiscais de Entrada  será feita de acordo com os parâmetros informados nos parâmetros do  TOTVS Gestão Fiscal em Assistente | Parâmetros | TOTVS Gestão Fiscal | 03.02 - Apuração de Tributos | 03.02.03 - Etapa "Apur. ISS por Filial" - Datas Apuração do ISS). As opções são:   

* Data de Emissão;
* Data de Entrada/Saída;
* Data de Pagamento/Vencimento.

Utilizando a opção "**Data de Pagamento/Vencimento**", o sistema se comportará da seguinte forma:  
a) Se existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cujo Lançamento Financeiro associado esteja baixado no período informado na tela da rotina (Data de Baixa);  
b) Se não existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cuja Data de Vencimento (aba "**Dados Financeiros**") esteja dentro do período informado na tela da rotina.  
  
***Importante!***  
Se a Filial estiver parametrizada para utilizar município por item, as informações de Alíquota, Tipo de Recolhimento, Base de Cálculo e Valor do Imposto serão preenchidos de acordo com os dados informados na aba "**Outros Tributos**" dos Itens do Lançamento Fiscal.  
Se a Filial for parametrizada para **não** usar o município por item, esses campos serão preenchidos de acordo com os dados informados na aba "**Outros Tributos**" do Lançamento Fiscal.  
  
**Tela de Geração da Rotina (Gerador de Saídas)**

Informe os seguintes dados:

* Código Filial
* Período
* Versão Layout
* Classificação Município
* Classificação Pais
* Órgão Público

Se a Filial selecionada for órgão público, marcar a opção "Órgão Público". O preenchimento deste campo impacta na geração dos campos 47(Valor Bruto dos Serviços) e 48 (Data do Pagamento). Caso o parâmetro "Órgão Público" não for marcado os campos não serão gerados pela rotina.  
  
**Origem dos Dados**

Serão selecionados todos os Lançamentos de Entrada da Filial selecionada na tela da rotina que atendam aos seguintes critérios:  
a)        Lançamentos cuja data de entrada (de acordo com o parâmetro especificado no item 1) estejam dentro do período informado na tela da rotina;  
b)        Lançamentos com status "**Normal**" ou "**Cancelado"**;  
c)        Lançamentos que possuam em uma de suas parcelas pelo menos um item tributado pelo ISS   
d)        O item deve ser tributado pelo ISS (Acessar cadastro do Produto, menu Anexos > Dados Fiscais do Produto > Tipo Tributação = ISS).  
  
 **Layout para Importação da Escrituração**

|  |  |  |  |
| --- | --- | --- | --- |
| Código | Campo | **Descrição** | **Origem dos Dados** |
| 1 | Indicador da Versão do Layout | Valor fixo: "2.0" | Gerado conforme campo "Versão" informado na Tela da Rotina |
| 2 | Tipo da Prestação de Serviço | Valor fixo: 2 - Serviço tomado. | Valor Fixo "2" |
| 3 | Tipo de Pessoa Referente ao Prestador | 1 - Pessoa Física; 2 - Pessoa Jurídica; 3 - Estrangeiro | Se País do Cliente Fornecedor for diferente de Brasil  Então "3"  Senão Se Tipo Pessoa for Física Então "1" Senão "2" |
| 4 | CPF ou CNPJ do Prestador | Informar CPF com tamanho 11 ou CNPJ com tamanho 14 preenchendo com 0 (zero) à esquerda. | Campo FCFO.CGCCFO do Cadastro do Cliente\Fornecedor |
| 5 | Nome ou Razão Social do Prestador |  | FCFO.NOME |
| 6 | Inscrição Municipal do Prestador de Fortaleza | Inscrição municipal de Fortaleza com o dígito. Não é necessário colocar zero à esquerda. | Se Município do Prestador igual a Fortaleza  Então FCFO.INSCRMUNICIPAL  Senão Vazio |
| 7 | Código do País do Prestador | Conforme Anexo I - Países (disponível no site do ISS Fortaleza - [{+}](http://iss.fortaleza.ce.gov.br/)<http://iss.fortaleza.ce.gov.br+> - em "Layouts e Documentos"). | FCFO.IDPAIS  Observação: Será observado a Codificação de país parametrizada ao gerar a rotina. |
| 8 | Código da Unidade de Federação do Prestador | Conforme Anexo II - Unidades da Federação (disponível no site do ISS Fortaleza - [{+}](http://iss.fortaleza.ce.gov.br/)<http://iss.fortaleza.ce.gov.br+> - em "Layouts e Documentos"). | Se Pais do Cliente Fornecedor igual a Brasil  Então FCFO.CODETD  Senão Vazio |
| 9 | Código da Cidade do Prestador | Conforme Anexo III - Cidades IBGE (disponível no site do ISS Fortaleza - [{+}](http://iss.fortaleza.ce.gov.br/)<http://iss.fortaleza.ce.gov.br+> - em "Layouts e Documentos"). | Se Pais do Cliente Fornecedor igual a Brasil  Então FCFO.CODMUNICIPIO  Senão Vazio  Observação: Será observado a Codificação do Município parametrizado ao gerar a rotina. |
| 10 | CEP do Prestador | Numero do CEP | FCFO.CEP |
| 11 | Nome do Logradouro do Prestador | Nome do Logradouro | FCFO.RUA |
| 12 | Número do Endereço do Prestador | Número do Endereço | FCFO.NUMERO |
| 13 | Complemento do Endereço do Prestador | Complemento | FCFO.COMPLEMENTO |
| 14 | Bairro do Prestador | Bairro | FCFO.BAIRRO |
| 15 | Telefone do Prestador | Telefone | FCFO.TELEFONE |
| 16 | E-mail do Prestador | e-mail | FCFO.EMAIL |
| 17 | Tipo do Documento Digitado | Conforme Anexo IV - Tipo de Documento Digitado, disponível no final do arquivo. | "Modelo ISS" associado ao Tipo de Documento (Espécie) nos parâmetros do TOTVS Gestão Fiscal (Processo 03.02.03 – Apur. ISS por Filial, Etapa 1 – Modelo ISS).  Não existindo a relação, preencher com o valor do campo "Código Modelo Documento" do Tipo de Documento associado ao Lançamento Fiscal. |
| 18 | Número do Documento | Valor não pode ser zero. | DLAF.DOCINI |
| 19 | Série do Documento | Série | DLAF.SERIE |
| 20 | Data da Emissão do Documento | Formato DD/MM/YYYY. | DLAF.DATAEMISSAO |
| 21 | Situação do Documento | 1 - Normal 2 - Cancelado | Se Status do Lançamento igual a "Normal"  Então "1" Senão "2" |
| 22 | Mês de Competência do Documento | Data de Entrada do Serviço | MÊS(DLAF.DATAES) |
| 23 | Ano de Competência do Documento | Data de Entrada do Serviço | ANO(DLAF.DATAES) |
| 24 | CNAE (Código da Classificação Nacional de Atividades Econômicas versão 2.1) da Atividade | Conforme Anexo VI - Tabela CNAE Fortaleza. | GFILIAL.CODATIVFED |
| 25 | Alíquota |  | Se Tributo ISS Então  DTRBLAF.ALIQTRB ou DTRBITEM.ALIQTRB  Senão 0  É observado se a Filial está parametrizada para utilizar município por item. |
| 26 | Descrição do Serviço |  | TPRODUTO.NOMEFANTASIA |
| 27 | Código do País Onde Ocorreu a Prestação do Serviço | Conforme Anexo I - Países (disponível no site do ISS Fortaleza - [{+}](http://iss.fortaleza.ce.gov.br/)<http://iss.fortaleza.ce.gov.br+> - em "Layouts e Documentos"). | Se "Utilizar município por item"  Então CODIGOPAIS(DITEM.UFMUNICIPIOSERV)  Senão CODIGOPAIS(DLAF.UFMUNICIPIOSERV) |
| 28 | Código da Unidade de Federação Onde Ocorreu a Prestação do Serviço | Conforme Anexo II - Unidades da Federação (disponível no site do ISS Fortaleza - [{+}](http://iss.fortaleza.ce.gov.br/)<http://iss.fortaleza.ce.gov.br+> - em "Layouts e Documentos"). | Se País diferente de Brasil  então Vazio  Senão  Se "Utilizar município por item"  Então DITEM.UFMUNICIPIOSERV  Senão DLAF.UFMUNICIPIOSERV |
| 29 | Código da Cidade Onde Ocorreu a Prestação do Serviço | Conforme Anexo III - Cidades IBGE (disponível no site do ISS Fortaleza – [{+}](http://iss.fortaleza.ce.gov.br/)<http://iss.fortaleza.ce.gov.br+> – em "Layouts e Documentos"). | Se País diferente de Brasil  Então Vazio  Senão Se "Utilizar município por item"  Então DITEM.CODMUNICIPIOSERV  Senão DLAF.CODMUNICIPIOSERV |
| 30 | Código da Natureza da Operação | Conforme Anexo V - Natureza da Operação, disponível no final do arquivo. | Se Tributo ISS igual a Isento  Então "3"  Senão Se Tributo ISS igual a Deposito em Juízo  Então "5"  Senão Se Tributo ISS igual a Imune  Então "4"  Se Município Prestação do Serviço Igual a Fortaleza  Então "1" Senão "2" |
| 31 | Código ART | Apenas para Construção Civil. | Projeto ART |
| 32 | Código da Obra | Apenas para Construção Civil. | Projeto Código da Obra |
| 33 | Valor do Serviço Prestado |  | Se a Filial estiver parametrizada para usar município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS dos Itens do Lançamento Fiscal, considerando somente os itens cujo município informado é igual ao município da Filial.  Se a Filial estiver parametrizada para não usar o município por item, esse campo será preenchido com somatório das Bases de Cálculo do Tributo ISS do lançamento fiscal. |
| 34 | Valor das Deduções |  | Não Gerado |
| 35 | Descontos Incondicionados |  | Não Gerado |
| 36 | Descontos Condicionados |  | Não Gerado |
| 37 | Outras Retenções |  | Não Gerado |
| 38 | Valor IR |  | Valor do Tributo IRRF ou IRRFPJ informado no Item ou no lançamento. |
| 39 | Valor PIS |  | Valor do Tributo PIS RF informado no Item ou no lançamento.  Ou  CSRF pegar 0,65% da Base do tributo no Item ou no Lançamento |
| 40 | Valor COFINS |  | Valor do Tributo COFINS RF informado no Item ou no lançamento.  Ou  CSRF pegar 3% da Base do tributo no Item ou no Lançamento |
| 41 | Valor CSLL |  | Valor do Tributo CSLL RF informado no Item ou no lançamento.  Ou  CSRF pegar 1% da Base do tributo no Item ou no Lançamento |
| 42 | Valor INSS |  | Valor do Tributo INSS informado no Item ou no lançamento. |
| 43 | Número do Empenho |  | Não Gerado |
| 44 | Indicador de ISS Retido | 0 - Não; 1 – Sim | Se o Tipo de Recolhimento do ISS for "**Retido na Fonte**" ou "**Retido na Fonte Deduzido**" então preencher com "**1**". Caso contrário preencher com "0". |
| 45 | Tipo de Tributação do Tomador |  | Não Gerado |
| 46 | Inscrição Municipal de Fortaleza do Contribuinte que está escriturando | Inscrição municipal sem dígito. Não é necessário colocar zero à esquerda. Referente ao contribuinte que está importando a escrituração. | GFILIAL.INSCMUN |
| 47 | Valor Bruto do Serviço\* |  | Este campo é preenchido com o somatório dos valores (quantidade x preço) de todos os itens do Lançamento Fiscal, considerando todas as suas parcelas.  Para lançamentos com status "Cancelado", é preenchido com o valor zero. |
| 48 | Data do Pagamento\* | Formato **DD/MM/YYYY**. | Se Integrado com Financeiro  Então FLAN.DATABAIXA Senão  DLAF.VENCIMENTO |

Os campos com  serão gerados se o Parâmetro "Órgão Público" da Rotina estive marcado.  
   
**Layout para Importação de Clientes/Fornecedores**

O formato do arquivo é do tipo .csv, com campos separados por ",".

| **Código** | **Campo** | **Descrição** | **Origem dos Dados** |
| --- | --- | --- | --- |
| 1 | Tipo de Cliente/Fornecedor | 1 - Pessoa Física; 2 - Pessoa Jurídica; 3 -Estrangeiro. | Se País do Cliente Fornecedor for diferente de Brasil  Então "3"  Senão Se Tipo Pessoa for Física Então "1" Senão "2" |
| 2 | CPF/CNPJ |  | Campo FCFO.CGCCFO do Cadastro do Cliente\Fornecedor |
| 3 | Nome ou Razão Social |  | FCFO.NOME |
| 4 | Inscrição Municipal de Fortaleza |  | Se Município do Prestador igual a Fortaleza  Então FCFO.INSCRMUNICIPAL  Senão Vazio |
| 5 | Código do País |  | FCFO.IDPAIS  Observação: Será observado a Codificação de país parametrizada ao gerar a rotina. |
| 6 | Sigla da Unidade de Federação |  | Se Pais do Cliente Fornecedor igual a Brasil  Então FCFO.CODETD  Senão Vazio |
| 7 | Código da Cidade |  | Se Pais do Cliente Fornecedor igual a Brasil  Então FCFO.CODMUNICIPIO  Senão Vazio  Observação: Será observado a Codificação do Município parametrizado ao gerar a rotina. |
| 8 | CEP/Código Postal |  | FCFO.CEP |
| 9 | Logradouro |  | FCFO.RUA |
| 10 | Número do Endereço |  | FCFO.NUMERO |
| 11 | Complemento |  | FCFO.COMPLEMENTO |
| 12 | Bairro |  | FCFO.BAIRRO |
| 13 | Telefone |  | FCFO.TELEFONE |
| 14 | E-mail |  | FCFO.EMAIL |
