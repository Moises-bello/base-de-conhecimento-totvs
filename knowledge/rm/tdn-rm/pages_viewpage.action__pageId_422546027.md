---
content_hash: f5ee302f6afbbf3ce36572f01e19e19a9e2515b066ad507f5b0c435678d8818f
fetched_at: '2026-06-29T00:09:22.777852+00:00'
page_id: '422546027'
product: rm
source: tdn-rm
title: Nota Fiscal Eletrônica de Serviços (NFS-e) 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546027
version: 50
---

![](https://tdn.totvs.com/download/attachments/422546027/NFS-e.png?version=1&modificationDate=1738592213230&api=v2)
]]>

# Conteúdo

**Conteúdonone**

# 1. Visão Geral

A **Nota Fiscal de Serviço Eletrônica (NFS-e)** é um documento fiscal exclusivamente digital, emitido e armazenado eletronicamente pela prefeitura ou por entidade responsável pela administração tributária municipal. Ela tem como finalidade **registrar as operações de prestação de serviços**, substituindo documentos em papel e padronizando o processo de escrituração.

A responsabilidade pelo envio correto das informações e pelo cumprimento da obrigação acessória é inteiramente do contribuinte. Por isso, é essencial que os dados cadastrais, fiscais e operacionais estejam consistentes, garantindo a emissão adequada da NFS-e e evitando rejeições, inconsistências ou questionamentos dos órgãos competentes.

# 2. Parâmetros

Para emissão da NFS-e é necessário configurar alguns parâmetros conforme abaixo.

ParametrosleftParâmetros Gerais

Parâmetros gerais para configuração da emissão da NFS-e

falsefalseParametrizações GeraisImportação/Envio de Arquivo XML

**App para Transmissão**

A NFS-e pode ser transmitida para a prefeitura utilizando o APP TSS ou através da integração com o TPF. Acesse Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Importação/Envio de Arquivo XML | Campo Tipo de integração

* **Não Utiliza:** Essa o opção indica que o TSS será o APP utilizado para emissão da NFS-e
* **TOTVS PROCESSOS FISCAIS (TPF):**Essa opção indica que alguns documentos podem ser emitidos utilizando o TPF, na próxima etapa essa integração será detalhada e a NFS-e será configurada para emitir pelo TPF.

ImagemImportação/Envio de Arquivo XML 1/2

**Integração com TPF**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá NFS-e> | Importação/Envio de Arquivo XML 1/2. Deve ser configurado o campo **Tipo Documento Integração TOTVS Colaboração**.

* **Todos:** Se habilitado, a transmissão da NFS-e será realizada pelo TPF respeitando a parametrização do 1º passo independente da opção Envio NFS-e estar marcada ou não.
* **Envio NFS-e:** Se habilitado, a transmissão da NFS-e será realizada pelo TPF respeitando a parametrização do 1º passo. Caso não esteja habilitado, a transmissão da NFS-e será realizada pelo TSS conforme configurações dos próximos passos

ImagemDicas

Documentação do TPF:

Conexão NF-e

**Conexão NF-e**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá NFS-e> | Conexão NF-e. Devem ser configurados os parâmetros **URL do Servidor TOTVS Service** e os **dados de Autenticação.**

ImagemDicas

Instalação do TSS: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/18590720143639>

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

Certificado Digital 1/2

**Certificado Digital**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá NFCom> | Certificado Digital 1/2. Deve ser configurado o certificado Digital para emissão da NFCom

ImagemDicas

Como preparar o certificado digital: [NFE0006\_Preparar\_Certificado\_Digital](https://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital)

Cadastro do certificado digital:

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

Ambiente NF-e

**Ambiente NF-e**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá NFS-e> | Ambiente NF-e. Devem ser configurados os campos abaixo

Configuração Obrigatórias:

* **Ambiente de envio:** Homologação ou Produção. Obs.: Não é recomendado emitir notas de teste (homologação) na base de produção.
* **Classificação de município:** Deverá ser avaliado qual a classificação de município é utilizado pela layout da prefeitura (na maioria dos casos será IBGE)

Configurações opcionais conforme regras das prefeituras

* **Número Máximo de NFS-e por Lote:** Configuração especifica para limitar a quantidade de notas por lote conforme definido por algumas prefeituras
* **CNPJ Assinatura Lote NF-e:** Permite indicar um CNPJ para assinatura do Lote da NFS-e, deverá ser configurado quando solicitado pela prefeitura.
* **Tipo FTP:** É utilizado para definir o modelo de integração para municípios com nota txt
* **Classificação de País:** Deverá ser informado quando a prefeitura utilizar uma codificação de país especifica em seu Layout

Outras configurações

* **Retirar Acentuações e Texto para Sanitização do Doc-e:** Estes parâmetros têm o objetivo de ajustar os textos do xml da NFS-e.  
  Para mais detalhes consulte a documentação do layout:

DicasNFS-e Nacional

Parâmetros para configuração da emissão da NFS-e Modelo Nacional

falsefalseParametrizações GeraisAmbiente NF-e

NFS-e Nacional

* **Layout Nacional:** Este campo deve ser marcado para indicar que a prefeitura adotou o modelo nacional como layout para emissão de notas

Imagem

**Classificação de País**

Para a NFS-e Nacional é necessário definir a classificação de Países ISO 3166, para isso acesse: Parâmetros | Gestão de Estoque Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | selecione a Filial | Ambiente NF-e | Campo **Classificação de País**

ImagemDicas

Essa classificação deverá ser definida no cadastro de cada **País** | Anexo **Codificação de País**conforme a tabela ISO 3166

Documentação especifica:

#### Lista oficial com os municípios que aderiram a NFS-e Nacional (gov)

<https://www.gov.br/nfse/pt-br/municipios/municipios-aderentes/municipios-aderentes>

#### Apoio da consultoria de segmentos

<https://espacolegislacao.totvs.com/nfs-e-nacional/>

#### Perguntas frequentes (gov)

<https://www.gov.br/nfse/pt-br/biblioteca/copy_of_perguntas-frequentes/copy_of_faq-nfs-e>

Parâmetros do Movimento

Parâmetros do Tipo de Movimento para emissão da NFCom

Parametrizações Tipo MovimentoMov - Faturamento 1/6

* Mov - Faturamento 1/6:  O Tipo de Movimento deve gerar Faturamento, o grupo de fatura será obrigatório na NFcom.

  Imagem
Fis - Escrituração

* Fis - Escrituração 1/2: marcar o campo "Gerar Escrituração" e no campo "Tipo Documento Escrituração", selecionar tipo de documento cujo campo Código do Modelo do Documento = 62.

  Imagem

Dica

Cadastro do Tipo de Documento:

Fis - NF-e

* Fis - NF-e: Informar campo "NFCom" como Integrado.

  Imagem

# 3. Notas Fiscal de Serviço Eletrônica (NFS-e)

A tela para emissão da NFS-e será acessada através do módulo Gestão de Estoque, Compras e Faturamento, no menu Vendas | Documentos Eletrônicos | Nota Fiscal de Serviço eletrônica (NFS-e).

Cada NFS-e apresentará os dados de identificação, o xml com todas as informações que compõe o documento e um status da situação atual do documento

Imagem - Identificação

## 3.1 Histórico (Anexo)

No Anexo de Histórico, teremos um registro de cada alteração ocorrida na NFS-e. As informações exibidas serão resumidas apenas com a finalidade de demonstrar os processos que foram executados para cada NFS-e.

Imagem

## 3.2 Processos

Abaixo está apresentado o fluxo correto para os processos relacionados à NFS-e. Para compreender em detalhe o funcionamento de cada etapa, clique no processo desejado para ser direcionado à página do processo.

trueFluxo NFS-efalseautohiddentrue9982

# 4. Modelos de xml gerados pelo RM

O processo de emissão da NFS-e possibilita a geração de diferentes modelos de XML, de acordo com as configurações definidas para o município e o aplicativo utilizado para a transmissão (TSS ou TPF).

Na página a seguir, está disponível o mapeamento completo de todos os campos gerados no XML da NFS-e em cada Layout.

## 4.1 Mapeamento de Campos (NFS-e)

Clique e veja o mapeamento de camposhttps://tdn.totvs.com/pages/viewpage.action?pageId=422546168

## 4.2 Atualizações dos Layouts

# 5. DANFSe

O **DANFSe** é a representação gráfica simplificada da **NFS-e**. Ele funciona como um documento auxiliar da NFS-e impresso em papel com os objetivos de:

* Facilitar a consulta resumida dos dados da NFS-e, provendo a necessidade de  
  representações impressas previstas na legislação;
* Auxiliar os processos administrativos e financeiros do destinatário não credenciado  
  como emissor de NFS-e.

Para detalhes técnicos e orientações completas sobre o DANFSe, consulte a documentação específica:



# 6. Documentos Auxiliares

## 6.1 Instalação do TSS

A transmissão da NFS-e para o ambiente da prefeitura é realizada por meio do aplicativo **TSS**. Para orientações de instalação e configuração, consulte a documentação: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/18590720143639>

## 6.2 Preparar o certificado

A emissão da NFS-e requer o uso de um **certificado digital modelo A1**, que garante a autenticidade e a validade jurídica do documento. Para realizar a configuração do certificado, siga as instruções disponíveis em: [NFE0006\_Preparar\_Certificado\_Digital](https://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital)

## 6.3 TOTVS Processos Fiscais (TPF)

A transmissão da NFS-e também pode ser realizada através do do TPF. Para saber mais acesse: [TOTVS Processos Fiscais](https://tdn.totvs.com/display/PFV/TOTVS+Processos+Fiscais)

## 6.4 Outros Documentos Relacionados



# 7. Informações sobre LGPD

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

Imagens
