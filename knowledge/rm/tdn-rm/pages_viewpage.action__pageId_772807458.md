---
content_hash: be141d2d03aec732ce98c13506a9ee6615977ceab687cff235a5c2def7f4a0e3
fetched_at: '2026-06-29T00:11:36.482811+00:00'
page_id: '772807458'
product: rm
source: tdn-rm
title: Conhecimento de Transporte Eletrônico (CT-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772807458
version: 87
---

![](https://tdn.totvs.com/download/attachments/772807458/CT-e.png?version=1&modificationDate=1756293686222&api=v2)
]]>

# Conteúdo

**Conteúdonone**

# 1. Visão Geral

O Conhecimento de Transporte Eletrônico (CT-e), modelo 57, é um documento fiscal digital que tem por objetivo documentar e validar, de forma eletrônica, a prestação de serviços de transporte de cargas em todo o território nacional. Sua utilização substitui os documentos fiscais em papel, como o Conhecimento de Transporte Rodoviário, Ferroviário, Aéreo, Aquaviário e Dutoviário, trazendo maior padronização, segurança jurídica e agilidade no processo de fiscalização. Além de garantir o cumprimento das obrigações acessórias junto ao Fisco, o CT-e possibilita melhor integração entre empresas e órgãos reguladores, reduzindo custos operacionais e aumentando a eficiência no gerenciamento das operações logísticas.

# 2. Parâmetros

Para emissão do CT-e é necessário configurar alguns parâmetros conforme abaixo.

ParametrosleftParâmetros Gerais

Parâmetros gerais para configuração da emissão do CT-e

falsefalseParametrizações GeraisImportação/Envio de Arquivo XML

**App para Transmissão**

O CT-e pode ser transmitido para a SEFAZ utilizando o APP TSS ou através da integração com o TPF. Acesse Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Importação/Envio de Arquivo XML | Campo Tipo de integração

* **Não Utiliza:** Essa o opção indica que o TSS será o APP utilizado para emissão do CT-e
* **TOTVS PROCESSOS FISCAIS (TPF):**Essa opção indica que alguns documentos podem ser emitidos utilizando o TPF, na próxima etapa essa integração será detalhada.

ImagemConexão NF-e

**Conexão NF-e**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá CT-e> | Conexão NF-e. Devem ser configurados os parâmetros **URL do Servidor TOTVS Service** e os **dados de Autenticação.**

ImagemDicas

Instalação do TSS: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/18590720143639>

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

Certificado Digital 2/2

**Certificado Digital**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá CT-e> | Certificado Digital 2/2. Deve ser configurado o certificado Digital para emissão do CT-e

ImagemDicas

Como preparar o certificado digital: [NFE0006\_Preparar\_Certificado\_Digital](https://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital)

Cadastro do certificado digital:

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

Importação/Envio de Arquivo XML 1/2

**Integração com TPF**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá CT-e> | Importação/Envio de Arquivo XML 1/2. Deve ser configurado o campo **Tipo Documento Integração TOTVS Colaboração**.

* **Todos:** Se habilitado, a transmissão do CT-e será realizada pelo TPF respeitando a parametrização do 1º passo independente da opção Envio CT-e estar marcada ou não.
* **Envio CT-e:** Se habilitado, a transmissão do CT-e será realizada pelo TPF respeitando a parametrização do 1º passo. Caso não esteja habilitado, a transmissão do CT-e será realizada pelo TSS conforme configurações dos 2º e 3º passos

ImagemDicas

Documentação do TPF:

Ambiente CT-e

**Ambiente CT-e**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá CT-e> | Ambiente CT-e. Devem ser configurados os campos abaixo

* **Ambiente e Modalidade:** configurar os campos Ambiente de envio e Modalidade de Operação
* **Versões de Layout Utilizados:** Configurar a versão de emissão do CT-e

ImagemParâmetros do Movimento

Parâmetros do Tipo de Movimento para emissão do CT-e.

Dicas

Exemplo de preenchimento de um Movimentos com essas parametrizações:

Parametrizações Tipo MovimentoMov - Emitente/Destinatário

* Mov - Emitente/Destinatário 1/2:  o campo Emitente deve ser igual a Empresa e o campo Destinatário deve ser igual a Cliente.
Mov - Transporte

* Mov - Transporte 1/3: habilitar os opções "Editar Transportadora", "Editar Quantidade", "Editar Marca", "Editar Via de Transporte" e "Editar Espécie";
* Mov - Transporte 2/3: marcar o campo "Tipo de Frete" como Edita e marcar os parâmetros "Edita Dados de Cálculo do Frete" e "Editar Dados da Placa do Veiculo".
* Mov - Transporte 3/3: habilitar os campos "Editar Peso Bruto" e "Editar Peso Líquido".
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

Para movimentos de CT-e, os tributos que irão compor o XML (normalmente ICMS e INSS) devem ser cadastrados no Movimento e não no Item.

Fis - Conhecimento de Transporte

* Fis - Conhecimento de Transporte: informar o "Tipo de Operação de Conhecimento de Transporte" como "Emitir CTe" e no campo "Modal" selecionar o tipo do modal que será utilizado. Se necessário, informar o relatório default para impressão do DACTE.

# 3. Conhecimento de Transporte Eletrônico (CT-e)

A tela para emissão do CT-e será acessada através do módulo Gestão de Estoque, Compras e Faturamento, no menu Vendas | Documentos Eletrônicos | Conhecimento de Transporte Eletrônico (CT-e).

Cada CT-e apresentará os dados de identificação, o xml com todas as informações que compões o documento e um status da situação atual do documento

## 3.1 Histórico (Anexo)

No Anexo de Histórico, teremos um registro de cada alteração ocorrida no CT-e. As informações exibidas serão resumidas apenas com a finalidade de demonstrar os processos que foram executados para cada CT-e.

Imagem

## 3.2 Processos

Abaixo está apresentado o fluxo correto para os processos relacionados ao CT-e. Para compreender em detalhe o funcionamento de cada etapa, clique no processo desejado para ser direcionado à página do processo.

trueFluxo Proc CT-efalseautohiddentrue112910

# 4. Relatórios DACTE

O Documento Auxiliar do Conhecimento de Transporte Eletrônico (**DACTE**) é a representação gráfica simplificada do CT-e, utilizado para acompanhar a carga durante o transporte e facilitar a consulta do documento fiscal eletrônico. Ele não substitui o CT-e, mas contém as principais informações da operação e a chave de acesso para verificação junto à SEFAZ. Para detalhes sobre o processo de impressão do DACTE, consulte a [documentação completa aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=830947801).

# 5. Atualizações e Notas Técnicas

# 6. Documentos Auxiliares

## 6.1 Instalação do TSS

A transmissão do CT-e para o ambiente da SEFAZ é realizada por meio do aplicativo **TSS**. Para orientações de instalação e configuração, consulte a documentação: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/18590720143639>

## 6.2 Preparar o certificado

A emissão do CT-e requer o uso de um **certificado digital modelo A1**, que garante a autenticidade e a validade jurídica do documento. Para realizar a configuração do certificado, siga as instruções disponíveis em: [NFE0006\_Preparar\_Certificado\_Digital](https://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital)

## 6.3 TOTVS Processos Fiscais (TPF)

A transmissão do CT-e para a SEFAZ também pode ser realizada através do do TPF. Para saber mais acesse:

## 6.4 Outros Documentos Relacionados

# Informações sobre LGPD

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

Imagens
