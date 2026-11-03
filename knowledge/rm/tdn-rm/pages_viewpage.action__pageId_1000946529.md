---
content_hash: 3a307812559b9d793a672e4f425a7b338853cf0db9babb3feb0b9b9d3e2b93ac
fetched_at: '2026-06-29T00:05:45.008307+00:00'
page_id: '1000946529'
product: rm
source: tdn-rm
title: Conhecimento de Transporte Eletrônico para Outros Serviços (CT-e OS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1000946529
version: 27
---

![](https://tdn.totvs.com/download/attachments/772807458/CT-e.png?version=1&modificationDate=1756293686222&api=v2)
]]>

# Conteúdo

**Conteúdonone**

# 1. Visão Geral

O Conhecimento de Transporte Eletrônico para Outros Serviços (CT-e OS) é o formato eletrônico de Emissão de Documentos Fiscais para prestação de serviços de transporte que substituiu a Nota Fiscal de Serviço de Transporte modelo 7, no que se refere aos serviços que não envolvem o transporte de cargas, a saber:

* Transporte de Pessoas: por agência de viagem ou por transportador, sempre que executar, em veículo próprio ou fretado, serviço de transporte intermunicipal, interestadual ou internacional, de pessoas.
* Excesso de Bagagem: por transportador de passageiro para englobar, no final do período de apuração do imposto, os documentos de excesso de bagagem emitidos durante o mês.

# 2. Parâmetros

Para emissão CT-e OS é necessário configurar alguns parâmetros conforme abaixo.

ParametrosleftParâmetros Gerais

Parâmetros gerais para configuração da emissão do CT-e OS

falsefalseParametrizações Gerais1º Passo

**App para Transmissão**

O CT-e OS pode ser transmitido para a SEFAZ utilizando o APP TSS ou através da integração com o TPF. Acesse Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Importação/Envio de Arquivo XML | Campo Tipo de integração

* **Não Utiliza:** Essa o opção indica que o TSS será o APP utilizado para emissão do CT-e OS
* **TOTVS PROCESSOS FISCAIS (TPF):**Essa opção indica que alguns documentos podem ser emitidos utilizando o CT-e OS, na próxima etapa essa integração será detalhada.

Imagem2º Passo

**Conexão NF-e**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá CT-e OS> | Conexão NF-e. Devem ser configurados os parâmetros **URL do Servidor TOTVS Service** e os **dados de Autenticação.**

ImagemDicas

Instalação do TSS:

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

3º Passo

**Certificado Digital**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá CT-e OS> | Certificado Digital 2/2. Deve ser configurado o certificado Digital para emissão do CT-e OS.

ImagemDicas

Como preparar o certificado digital: [NFE0006\_Preparar\_Certificado\_Digital](https://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital)

Cadastro do certificado digital:

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

4º Passo

**Integração com TPF**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá CT-e OS> | Importação/Envio de Arquivo XML 1/2. Deve ser configurado o campo **Tipo Documento Integração TOTVS Colaboração**.

* **Todos:** Se habilitado, a transmissão do CT-e OS será realizada pelo TPF respeitando a parametrização do 1º passo independente da opção Envio CT-e esta marcada ou não.
* **Envio CT-e:** Se habilitado, a transmissão do CT-e OS será realizada pelo TPF respeitando a parametrização do 1º passo. Caso não esteja habilitado, a transmissão do CT-e será realizada pelo TSS conforme configurações dos 2º e 3º passos

ImagemDicas

Documentação do TPF:

5º Passo

**Ambiente CT-e OS**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá CT-e OS> | Ambiente CT-e. Deve ser configurado os campos abaixo

* **Ambiente e Modalidade:** configurar os campos Ambiente de envio e Modalidade de Operação
* **Versões de Layout Utilizados:** Configurar a versão de emissão do CT-e OS

ImagemParâmetros do Movimento

Parâmetros do Tipo de Movimento para emissão do CT-e.

Dicas

Exemplo de preenchimento de um Movimentos com essas parametrizações:

Parametrizações Tipo MovimentoMov - Emitente/Destinatário

* Mov - Emitente/Destinatário 1/2:  o campo Emitente deve ser igual a Empresa e o campo Destinatário deve ser igual a Cliente.
Mov - Transporte

* Mov - Transporte 1/3: Etapa Movimento - Transporte (Mov - Transporte 1/3): selecionar o parâmetro "Editar Quantidade"
* Mov - Transporte 2/3: marcar o campo "Tipo de Frete" como Edita e marcar os parâmetros "Edita Dados de Cálculo do Frete" e "Editar Dados da Placa do Veiculo".
Mov - Item

* Etapa Item - Identificação 1/2: Campo Tipo dos Itens, selecionar entre serviço, produto ou Ambos.
Fis - Natureza

* Fis - Natureza: selecionar a "Edição da Natureza" com o valor Edita ou Mostra.

Dica

Cadastro da CFOP:

Fis - Escrituração

* Fis - Escrituração 1/2: marcar o campo "Gerar Escrituração" e no campo "Tipo Documento Escrituração", selecionar tipo de documento cujo campo Código do Modelo do Documento = 57.

Dica

Cadastro do Tipo de Documento:

Fis - Tributação - Movimento

* Fis - Tributação - Movimento: marcar o parâmetro "Utilizar Tributação dos Movimentos" cadastrar os tributos envolvidos na operação.

Importante

Para movimentos de CT-e OS, os tributos que irão compor o XML (normalmente ICMS e INSS) devem ser cadastrados no Movimento e não no Item.

Fis - Conhecimento de Transporte

* Fis - Conhecimento de Transporte: É necessário preencher os seguintes campos:
  + "Tipo de Operação de Conhecimento de Transporte" como Emitir CTe OS,
  + Campo "Modal" como Rodoviário.
  + Selecionar qual o "Tipo de CT-e OS" que se deseja: Transporte de Pessoas ou Excesso de Bagagens (o preenchimento deste campo, nos parâmetros do tipo de movimento, não é obrigatório, mas caso seja preenchido, o valor definido no parâmetro deverá ser carregado para o movimento).
  + Informar o relatório default para impressão do DACTE OS e o seu formato nos campos DACTE e Formato de Impressão.

**Observação:** No tipo de movimento há várias outras etapas que podem ser preenchidas de acordo com a regra de negócio da empresa.

Após a parametrização o tipo de movimento está apto para ser utilizado.

Cadastro Veiculo

Foram criados dois novos campos no cadastro de veículos para atender à legislação do CT-e OS: O **TAF - Termo de Autorização de Fretamento** e o **Número de Registro Estadual**.

Esses campos serão habilitados quando o campo **Tipo Prop. Veículo** estiver com o valor **Terceiros.**

ImagemCadastro Filial

No Cadastro da Filial em **Anexos -> Dados Fiscais -> Aba Dados Adicionais,** foram criados dois novos campos para atender à legislação do CT-e OS:

* Termo de Autorização de Fretamento
* Número de Registro Estadual

Imagem

# 3. Conhecimento de Transporte Eletrônico para Outros Serviços (CT-e OS)

A tela para emissão do CT-e OS será acessada através do módulo Gestão de Estoque, Compras e Faturamento, no menu Vendas | Documentos Eletrônicos | Conhecimento de Transporte Eletrônico para Outros Serviços (CT-e OS).

Cada CT-e OS apresentará os dados de identificação, o xml com todas as informações que compões o documento e um status da situação atual do documento

## 3.1 Exemplo de Movimento Ct-e OS(básico)

Exemplo de Movimento Ct-e OS

## 3.2 Histórico (Anexo)

No Anexo de Histórico, teremos um registro de cada alteração ocorrida no CT-e OS. As informações exibidas serão resumidas apenas com a finalidade de demonstrar os processos que foram executados para cada CT-e OS.

Imagem

## 3.3 Processos

Abaixo está apresentado o fluxo correto para os processos relacionados ao CT-e. Para compreender em detalhe o funcionamento de cada etapa, clique no processo desejado para ser direcionado à página do processo.

trueFluxo Proc CT-efalseautohiddentrue11295

# 4. Relatórios DACTE

O Documento Auxiliar do Conhecimento de Transporte Eletrônico (**DACTE**) é a representação gráfica simplificada do CT-e OS, utilizado para acompanhar a carga durante o transporte e facilitar a consulta do documento fiscal eletrônico. Ele não substitui o CT-e OS, mas contém as principais informações da operação e a chave de acesso para verificação junto à SEFAZ. Para detalhes sobre o processo de impressão do DACTE, consulte a [documentação completa aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=1000946529).

mapeamentoCampos\_Cte

Campos\_Cte

**5. Mapeamento de Campos CT-e OS 4.00**

Estão listados abaixo os principais campos do CT-e OS de acordo com o Manual de Orientação do Contribuinte 4.00.

# 5. Atualizações e Notas Técnicas

# 6. Documentos Auxiliares

## 6.1 Instalação do TSS

A transmissão do CT-e OS para o ambiente da SEFAZ é realizada por meio do aplicativo **TSS**. Para orientações de instalação e configuração, consulte a documentação:

## 6.2 Preparar o certificado

A emissão do CT-e OS requer o uso de um **certificado digital modelo A1**, que garante a autenticidade e a validade jurídica do documento. Para realizar a configuração do certificado, siga as instruções disponíveis em: [NFE0006\_Preparar\_Certificado\_Digital](https://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital)

## 6.3 TOTVS Processos Fiscais (TPF)

A transmissão do CT-e OS para a SEFAZ também pode ser realizada através do do TPF. Para saber mais acesse:

## 6.4 Outros Documentos Relacionados

# Informações sobre LGPD

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

Imagens
