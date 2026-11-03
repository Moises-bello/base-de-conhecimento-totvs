---
content_hash: d8a1271197e12a73305c3b11a55a7fa723d8b5486287cd7fe4e1989ae827e52a
fetched_at: '2026-06-29T00:11:13.457876+00:00'
page_id: '66126257'
product: rm
source: tdn-rm
title: NF-e - Verificar cadastros para emissão de NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66126257
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***apartir 11.40* |
| **Processo** | **:** | Verificar cadastros para emissão de NF-e |
| **Subprocesso** | **:** | Verificar cadastros para emissão de NF-e |
| **Data da publicação** | **:** | 09/07/2013 |

**Introdução:**

Este documento tem como objetivo orientar os cadastros que devem ser realizados/revisados para correta de emissão de NF-e.

**Procedimentos:** 

**Tipo de Documento**

Acesse o RM Nucleus no seguinte menu: Cadastros | Tabelas Auxiliares | Tipo de Documento.

Clique em “Incluir”  | Na nova tela, aba “Identificação” Preencha os campos “Código” e “Descrição”, na aba “Dados Adicionais” campo “Código do Modelo do Documento” deve ser preenchido “55”, Salve o cadastro.

**Serie**

Para Emissão de NF-e obrigatoriamente deve ser utilizada uma serie numérica de 0 a 999, sendo que da serie 900 a 999 o uso é exclusivo para Emissão em Modalidade SCAN e da serie 890 a 899 o uso é exclusivo para a emissão de NF-e Avulsa.

Acesse o RM Nucleus no seguinte menu: Opções | Parâmetros | RM Nucleus | 04.01 – Parâmetros Gerais | 04.01.03 Numeração do Movimento | 04.01.03.01 Numero Principal | 04.01.03.01.01 Numeração Geral | Etapa “Numeração Geral” | Campo “Série”, clique em  | na tela que irá aparecer clique em “Incluir”  | na nova tela preencha a Serie a Descrição Salve o cadastro.

**Cliente/Fornecedor**

Acesse o RM Nucleus no seguinte menu: Cadastros | Clientes/Fornecedores.

Para cada cliente que estará envolvido em alguma NF-e devem ser verificados os seguinte campos: Aba Identificação | campo Inscrição Estadual: pode ser preenchida normalmente com ou sem mascará, no caso de Isento a Palavra deve ser escrita em Maiúsculo “ISENTO”.

Campo Nome e Nome Fantasia: devem ser preenchidos com mais de um caracter.

Aba Endereço | Campo CEP: este campo não é obrigatório, mas no caso de ser preenchido ele deve conter 8 numero mesmo se o cliente for do exterior.

Campos Rua e Bairro: estes campos são obrigatórios e devem ser preenchidos com mais de um caracter.

Campo Número: é obrigatório, não aceita o valor “0” (zero), deve ser preenchido apenas com números ou S/N (Maiúsculo).

Campos Rua, Bairro, País, Estado e Município: Estes campos devem ser preenchidos obrigatoriamente.

Campo email: Este campo não é obrigatório, mas se não for preenchido com um email valido não será possível enviar o XML por email para o cliente após a autorização.

**Filial**

Acesse o RM Nucleus no seguinte menu: Cadastros | Filiais.

Para a Filial emissora de NF-e deverá ser verificado os seguinte campos:

Aba Identificação | Campo Nome: deve ser preenchido obrigatoriamente com mais de um caracter.

Aba Endereço | Campo CEP: este campo não é obrigatório, mas no caso de ser preenchido ele deve conter 8 numero.

Campos Rua e Bairro: estes campos são obrigatórios e devem ser preenchidos com mais de um caracter.

Campo Número: é obrigatório, não aceita o valor “0” (zero), deve ser preenchido apenas com números ou S/N (Maiúsculo).

Campos Rua, Bairro, País, Estado e Município: Estes campos devem ser preenchidos obrigatoriamente.

Campo email: Este campo não é obrigatório, mas se não for preenchido com um email valido não será possível enviar o XML por email após a autorização (Quando a Filial estiver em homologação os emails com os XML serão enviados para este email).

Aba Dados Adicionais | campo Inscrição Estadual: é obrigatório e pode ser preenchido normalmente com ou sem mascará.

Campos IM e CNAE: Não são obrigatórios e podem ser preenchidos com ou sem Mascará.

**País**

Para cada País cadastrado no sistema deverá ser informada a tabela de classificação BACEN com o código referente a cada país.

Acesse o RM Nucleus no seguinte menu: Cadastros | Países | Anexos | Codificação de País.

Para Cada País clique em “Incluir”  | na tela que aparecerá o campo “Classificação” deve ser preenchido com a classificação BACEN e o campo “Código País” deve ser preenchido com o código referente ao país conforme [Tabela online do BACEN](http://www.bcb.gov.br/rex/Censo2000/port/manual/pais.asp?idpai=censo2000inf).

**Municípios**

Para cada município envolvido na emissão de NF-e deve ser preenchido a classificação de município IBGE com o código IBGE referente a cada município.

Acesse o RM Nucleus no seguinte menu: Cadastros | Tabelas Auxiliares | Municípios | Anexos | Codificação de Municípios.

Para Cada município clique em “Incluir”  | na tela que aparecerá, o campo “Classificação” deve ser preenchido com a classificação IBGE e o campo “Código” deve ser preenchido com o código referente ao município conforme [tabela online do IBGE.](http://www.ibge.gov.br/home/geociencias/areaterritorial/area.shtm)

**Produto**

Todos os Produtos que serão utilizados na Emissão da NF-e devem ter estes campos verificados.

Acesse o RM Nucleus no seguinte menu: Cadastros | Produtos e Serviços.

Em cada produto | Aba Identificação | Campos Nome Fantasia, Código do Produto e Tipo: são obrigatórios.

Os campos “Código do Fabricante” e “Número do Produto no Fabricante” são obrigatórios na NF-e de Importação.

Aba Detalhes | Descrição | Campo “Descrição”: Ele será considerado no lugar do campo Nome fantasia quando a parametrização dos movimentos estiver para Considerar a Descrição no Lugar do Nome.

Detalhes | Outros dados | Campo NCM: é obrigatório e deve ser preenchido com 8 ou 2 números de acordo com as regras do manual de integração 4.01.

Campo Procedência | “Ref. (0-99)”: é obrigatório e deve ser preenchido com os valores 0 - Nacional ou 1 – Estrangeira adquirida via importação direta ou 2 – Estrangeira adquirida no Mercado interno.

Aba Código de Barras: Aqui deve ser preenchido o código de barras do produto para ser levado no XML da NF-e,  para maiores detalhes.

Acesse anexos | “Dados Fiscais por UF” | na próxima tela clique em “Incluir” , deve ser incluído um registro para cada estado que será emitida NF-e com os campos “Modalidade de Determinação da BC do ICMS:” e “Modalidade de Determinação da BC do ICMSST” preenchidos.

Acesse Anexos | Dados Fiscais do Produto | campo “Classe Enquadramento IPI” e “Código Selo de Controle IPI” Devem ser informados no caso de bebidas e cigarros. Deve ser utilizada a codificação prevista nos atos normativos editados pela Receita Federal.

Campo “Código ANP” Deve ser informado quando se tratar de produtos regulados pela ANP – Agência Nacional do Petróleo.

Campo “Código CODIF” Deve ser informado no caso de derivados de petróleo. Informar apenas quando a UF utilizar CODIF (Sistema de Controle do Diferimento do Imposto nas Operações com AEAC – Álcool Etílico Anidro).

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
