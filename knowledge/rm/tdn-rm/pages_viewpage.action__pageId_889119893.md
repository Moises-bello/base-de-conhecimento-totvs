---
content_hash: 3d52b69d5979b6967d86d9043e1f5e3c82600a3737ba40951bf4e15e818f1c16
fetched_at: '2026-06-29T00:12:01.230253+00:00'
page_id: '889119893'
product: rm
source: tdn-rm
title: Registro T - Serviços Tomados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=889119893
version: 28
---

Serão selecionados todos os Lançamentos de Entrada da Filial selecionada na tela da rotina que atendam aos seguintes critérios:

1. Lançamentos cuja data de entrada (conforme o parâmetro especificado no item
2. Lançamentos com status "Normal".

|  |  |  |  |
| --- | --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** | **Observação** |
| 01 | Tipo do Registro | Identificação do registro. Caractere fixo "T". |  |
| 02 | Data de Emissão | Data de Emissão do lançamento fiscal |  |
| 03 | Data Competência | Data de entrada/saída do lançamento fiscal |  |
| 04 | Número de Identificação do Documento Fiscal | Número do Documento Inicial informado no Lançamento Fiscal. |  |
| 05 | Série do Documento | Série informada no Lançamento Fiscal. |  |
| 06 | Modelo do Documento Fiscal | "Modelo ISS" associado ao Tipo de Documento (Espécie) nos parâmetros do TOTVS Gestão Fiscal (Processo 03.02.03 – Apur. ISS por Filial, Etapa 1 – Modelo ISS). Não existindo a relação, será preenchido com o valor do campo "Código Modelo Documento" do Tipo de Documento associado ao Lançamento Fiscal. |  |
| 07 | Tipo do Prestador | Campo preenchido conforme o **País** selecionado no cadastro do [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal.   * **1**=Nacional * **2**=Exterior |  |
| 08 | CNPJ/CPF do Prestador de Serviço | Campo preenchido com o dado no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. | Campo preenchido apenas com números. FCFO.CGC |
| 09 | Documento de identificação do Prestador Exterior | O campo será gerado vazio. |  |
| 10 | Nome Razão social Prestador | Campo preenchido com o dado do nome no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. |  |
| 11 | Código do município do prestador de serviço | Código do município onde o serviço foi prestado (tabela do IBGE), |  |
| 12 | Prestador Optante pelo Simples | Se o campo "**Optante pelo Simples**" estiver marcado ou desmarcado no cadastro do [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. Preencher com  * **S** - Sim / Optante no simples nacional; * **N** - Não / Não Optante no simples nacional; | Caso o prestador enquadrado no MEI preenche com "**N**" |
| 13 | Prestador enquadrado como MEI | Se o campo "**Porte da Empresa**" estiver selecionado ou não como **"MEI - Micro Empreendedor Individual"** no cadastro do [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. Preencher com  * **S** - Sim / Enquadrado como MEI; * **N** - Não / Não enquadrado como MEI. |  |
| 14 | Prestador Estabelecido no Município | Preenche esse campo conforme o **Município** selecionado no cadastro do [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. Preencher com  * **S** - Sim * **N** - Não |  |
| 15 | CEP do Endereço do Prestador | Preencher esse campo com o dado no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. | Informar somente números. |
| 16 | Tipo de Logradouro do Prestador | Preencher esse campo com o dado no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. | **Por exemplo**: Rua, Avenida, Via, etc. |
| 17 | Nome do logradouro do endereço do prestador | Preencher esse campo com o dado no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. |  |
| 18 | Número do endereço do prestador | Preencher esse campo com o dado no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. |  |
| 19 | Complemento do Prestador | Preencher esse campo com o dado no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. |  |
| 20 | Nome do Bairro do  Prestador | Preencher esse campo com o dado no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. |  |
| 21 | UF do Prestador | Preencher esse campo com o dado no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. |  |
| 22 | País do Prestador |  |  |
| 23 | Cidade do Prestador | Preencher esse campo com o dado no cadastro [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786) associado ao Lançamento Fiscal. |  |
| 24 | Código do Serviço Prestado | Buscar do Lançamento Fiscal |  |
| 25 | Código da Atividade CNAE | Busca da aba **Dados Adicionais** da [Filial](https://tdn.totvs.com/pages/viewpage.action?pageId=422545738#1--401241980). |  |
| 26 | Código da obra | O campo será gerado vazio. |  |
| 27 | Local da prestação do serviço | Valor Fixo "**LOC**" |  |
| 28 | Código do Município do Local da Prestação do Serviço | Busca do Lançamento Fiscal |  |
| 29 | UF Prestação do Serviço | Sigla do estado da Prestação do Serviço no Lançamento Fiscal |  |
| 30 | Município Exterior prestação Serviço | O campo será gerado vazio. |  |
| 31 | Estado Exterior Prestação do serviço | O campo será gerado vazio. |  |
| 32 | Pais da Prestação do Serviço | O campo será gerado vazio. |  |
| 33 | Local do Resultado da Prestação do Serviço | Valor Fixo "**BRA**" |  |
| 34 | Código do Município do Local do Resultado da Prestação do Serviço | Preenche esse campo com o dado no Lançamento Fiscal |  |
| 35 | UF do Resultado da Prestação do Serviço | Preenche esse campo com o dado no Lançamento Fiscal |  |
| 36 | Município Exterior do Resultado Prestação do Serviço | O campo será gerado vazio. |  |
| 37 | Estado Exterior do Resultado Prestação do Serviço | O campo será gerado vazio. |  |
| 38 | País do Resultado da Prestação do Serviço | O campo será gerado vazio. |  |
| 39 | Motivo da não Retenção | Busca do campo **Regime de ISS** no cadastro do [Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786)associado ao Lançamento Fiscal. Preencher com Indica o Motivo da não Retenção:   * **A** - Não Incidência no Município * **B** - Não Tributável * **C** - Pago pelo Prestador/Não Incidente * **D** – Imune * **E** – Isento * **F** - Sociedade de Profissionais * **G** - Profissional Autônomo Inscrito * **H** – Estimativa * **I** - Depósito em Juízo * **J** - Medida Liminar/Cautelar * **V** - Valor de Serviços Menor que o Mínimo | Quando não houver, preencher com espaço em branco " ". |
| 40 | Exigibilidade ISS | Busca a Informação do campo **Tipo do Recolhimento** do Tributo ISS Lançado no Item. Preencher com Exigibilidade do ISS   * **1** – Exigível * **2** - Não incidência * **3** – Isenção * **4** – Exportação * **5** – Imunidade * **6** - Exigibilidade Suspensa por Decisão Judicial * **7** – Exigibilidade Suspensa por Processo Administrativo |  |
| 41 | Tipo Recolhimento de Imposto | Busca a Informação do campo **Tipo de Tributação** no Tributo ISS Lançado no Item. Preencher com Responsável pelo recolhimento do imposto:   * **RPP** – A recolher pelo prestador * **RNF** – Retido na fonte * **NAP** - Não se aplica | * Se Tipo de Recolhimento igual a Nenhum então **"NAP"** * Se Tipo de Recolhimento igual a Devido  então **"RPP"** * Se Tipo de Recolhimento igual a Retido  então **"RNF"** * Se Tipo de Recolhimento igual a Dep.Juizo então **"NAP"** * Se Tipo de Recolhimento igual a Retido Deduzido então **"RNF"** * Se Tipo de Recolhimento igual a Isento então **"NAP"** * Se Tipo de Recolhimento igual a Imune  então **"NAP"** |
| 42 | Alíquota de ISS | Busca do campo **Alíquota** informada no Tributo ISS Lançado no Item. | Não informar quando **Exigibilidade ISS** for 3, 4, 5, 6 ou 7. Preencher o campo com zero.  É obrigatório preencher quando Exigibilidade for 1 ou 2 |
| 43 | Valor do Serviço da Nota Fiscal | Preenchido com o valor da nota fiscal |  |
| 44 | Valor das Deduções | Valor das deduções para Redução da Base de Cálculo |  |
| 45 | Desconto Incondicionado | Se o campo Desconto Item for maior que 0,00 e existe Tributo ISS Lançado no Item este campo será preenchido com o valor. |  |
| 46 | Desconto Condicionado |  |  |
| 47 | Base de Cálculo | Valor da Base de Cálculo |  |
| 48 | Valor PIS | Tributo PIS estiver Lançado no Item, este campo será preenchido com o Valor do Tributo. |  |
| 49 | Valor COFINS | Tributo COFINS estiver Lançado no Item, este campo será preenchido com o Valor do Tributo. |  |
| 50 | Valor INSS | Tributo INSS estiver Lançado no Item, este campo será preenchido com o Valor do Tributo. |  |
| 51 | Valor IR | Tributo IRPJ estiver Lançado no Item, este campo será preenchido com o Valor do Tributo. |  |
| 52 | Valor CSLL | Tributo CSLL estiver Lançado no Item, este campo será preenchido com o Valor do Tributo. |  |
| 53 | Outras Retenções | O campo será gerado vazio. |  |
| 54 | Valor do ISS | Tributo ISS estiver Lançado no Item, este campo será preenchido com o Valor do Tributo. |  |
| 55 | Discriminação dos Serviços da Nota Fiscal | Buscar a descrição do serviço no Lançamento Fiscal |  |
