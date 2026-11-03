---
content_hash: d864381ea02e68951b9214c638b36894ba8d541227119a8707fa5eac30b9fbf5
fetched_at: '2026-06-29T00:11:32.762816+00:00'
page_id: '748060890'
product: rm
source: tdn-rm
title: Integração para Laboratórios Apoiados - XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=748060890
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Configurações Gerais**
3. **Importação de Pedidos**
4. **Exportação de Resultados**
5. **Arquivos de Exemplo**

ItensVisão Geral

## **01. VISÃO GERAL**

Essa funcionalidade tem como objetivo permitir que laboratórios apoiados integrem seus pedidos de exames e retorno de resultados desses exames sendo a instituição que utiliza o TOTVS Saúde Hospitais e Clínicas o laboratório apoiador. Essa funcionalidade é composta por dois processos, sendo um de recebimento, via arquivo XML, dos pedidos de exames e outro processo de exportação de resultados dos exames, também, via arquivo XML.

Configurações Gerais

## **02. CONFIGURAÇÕES GERAIS**

Para utilizar essa integração, algumas configurações são necessárias para que o processo esteja pronto para o reconhecimento do laboratório apoiado para realizar a análise do exame e sua emissão de resultados, bem como realizar a cobrança do laboratório pelo serviço executado.

**2.1 Cadastros do Laboratório Apoiado para realizar o faturamento do serviço prestado**

Caminho: TOTVS RM => Saúde => Hospitais e Clínicas => Cadastros => Uso Geral => Convênio

O laboratório apoiado deverá ser cadastrado como um convênio para que os atendimentos / pedidos de exames importados sejam registrado nesse convênio para futura cobrança do serviço prestado.

A indicação de preenchimento dos campos "Grupo de Convênios" e "Padrão de Informação" são, respectivamente, "1 - ABRAMGE" e "1 - FATMED.BR", para os demais campos preencha da maneira que melhor reflete o contrato de prestação de serviço celebrado.

2.1.1 Planos de Convênio

Um plano para esse convênio também deve ser criado. Esse será utilizado no momento da abertura do atendimento pela integração.

**2.2 Cadastros do Laboratório Apoiado para a execução do Exame**

Caminho: TOTVS RM => Saúde => Hospitais e Clínicas => Cadastros => Uso Geral => Prestador

Cadastre o laboratório apoiado no cadastro do prestador com seus respectivos dados e na aba Tipo Prestador insira a Classe "14 - Laboratório Apoiado"

AVISO

Ao finalizar o cadastro do prestador ou do convênio, dependendo da ordem de cadastro, pelo CNPJ utilizado ser o mesmo para ambos, o sistema irá sugerir associar o Cliente/Fornecedor já existente, criado no primeiro cadastro. Confirme essa associação para que os cadastros se mantenham ligados ao Cliente/Fornecedor correto no Backoffice.

2.2.1 Em Anexo => "Configuração de integração do prestador" insira um novo registro e preencha os campos destacados em negrito de acordo com as informações utilizadas nos arquivos de integração enviado pelo laboratório e arquivo de  resultado a ser enviado para o laboratório.

Os campos de Especialidade e Convênio são utilizados para a abertura do registro de atendimento onde será inserido o pedido de exames.

**2.3 Cadastros do Laboratório Apoiado para a execução do Exame**

Caminho: TOTVS RM => Saúde => Hospitais e Clínicas => Cadastros => Unidades de Diagnóstico => Unidades de Diagnóstico => Locais de Execução Externa

É necesário configurar o laboratório apoiado no cadastro de locais de execução externa para configurar alguns dados referentes ao prestador responsável pelo atendimento a ser aberto no sistema.

**2.4 Cadastros dos Exames a serem realizados**

Caminho: TOTVS RM => Saúde => Hospitais e Clínicas => Cadastros => Unidades de Diagnóstico => Unidades de Diagnóstico => Exames e Serviços => Aba Laboratórios de Execução Externa

Nos exames que serão integrados deverá ser informado o código referente ao exame para o laboratório apoiador no campo "Cód. Exame Local".

**2.5 Cadastro de Unidade de Atendimento**

Caminho: TOTVS RM => Saúde => Hospitais e Clínicas => Cadastros => Uso Geral => Unidade de Atendimento

A unidade de atendimento utilizada para registrar os atendimentos importados do arquivo de pedidos de exame precisa ser informada ao sistema através do campo "Unidade apoiadora de exames esternos" localizada no cadastro de unidade de atendimento, aba Outros Dados.

Importação de Pedidos

## **03. IMPORTAÇÃO DE PEDIDOS**

3.0 - Caminho: TOTVS RM => Saúde => Hospitais e Clínicas => Utilitários => Integrações => Laboratório Apoioado => Importação de Pedidos

* O processo de importação de pedidos exibirá uma tela de processo na qual será exibido o diretorio onde deve ser incluido o(s) arquivo(s) a ser importado. Por padrão é utilizado a pasta configurada no servidor e subpasta \Saude\Coligada\_?\Filial\_0\LaboratorioCustomizado (? = código da coligada).
* O arquivo é referente ao laboratório que o enviou, ou seja, os pedidos são pertencentes a um único laboratório apoiado.
* O sistema busca o laboratório na qual estão sendo importados os pedidos pelo código enviado na tag CodLab do arquivo XML e que deverá ser configurado na tela descrita no item acima 2.2.1.
* O sistema verifica se o arquivo já foi processado antes de iniciar a importação através do número do lote enviado pelo laboratório (tabela SZLOTEPEDIDOS)
* Sistema verifica se o paciente já está cadastrado na base (tenta localizá-lo pelo CPF, caso o arquivo não venha com a Tag de CPF preenchida utiliza o código do paciente no laboratório apoiado - tag CodPacLab precedida do código do laboratório: Ex.: 9999.0043239060  e gravado no campo SZPACIENTE.CHAVEIMPORT). Se o paciente não foi encontrado nessas condições, então ele é cadastrado no sistema.
* Se o arquivo for importado com sucesso, o mesmo é copiado para pasta  ...\Saude\Coligada\_?\Filial\_0\LaboratorioCustomizado\Processado (? = código da coligada) com a inclusão de data e hora no final do nome do arquivo e extensão pok. Exemplo: Arquivo original: Pedido123.xml, Arquivo Processado: Pedido123\_20250424\_075134.pok;
* Se o arquivo não for importado gerando erro, o mesmo é copiado para pasta  ...\Saude\Coligada\_?\Filial\_0\LaboratorioCustomizado\Processado (? = código da coligada) com a inclusão de data e hora no final do nome do arquivo e extensão err. Exemplo: Arquivo original: Pedido123.xml, Arquivo Processado: Pedido123\_20250424\_075134.err;

AVISO

A partir da versão 12.1.2310 o caminho a ser utilizado deixa de ser um caminho absoluto selecionavel e passa a ser um caminho fixo em uma subpasta no servidor. Mais informações <https://tdn.totvs.com.br/pages/viewpage.action?pageId=423929512>. 

3.1 - Abertura do registro de atendimento

Para abrir o atendimento referente ao pedido de exames a ser importado o sistema busca a especialidade do laboratório, prestador e convênio cadastrados no RM referente ao laboratório apoiado, informações localizadas no item 2.2.1. Se já houver um atendimento aberto (com status “Em elaboração” aberto na mesma data do pedido) para esse laboratório, o sistema utiliza esse atendimento, senão abre um novo.

Tratamentos específicos de preenchimento de campos do registro de Atendimento:

* + CODPLANO: Busca o primeiro plano ativo encontrado para o convênio;
  + CODSUBPLANO: Mantém esse campo NULO;
  + CODTIPOATENDIMENTO: Valor fixo  "31 - Exames de Laboratório";
  + DATAENTRADA: Data do pedido de exames;
  + HORAENTRADA: Hora do pedido de exames (se vier no arquivo, se não vier considera a hora da importação);
  + DATASAIDA = DATAENTRADA;
  + HORASAIDA = HORAENTRADA;
  + TIPOPACIENTE: Valor Fixo "E" (Externo);
  + CLASSEATENDIMENTO: Valor fixo "E" (Eletivo);
  + DOCCOMPLETO: Valor fixo "T" (Sim);
  + CODNOTA: Valor fixo "02" (GSP / SADT);
  + OCUPALEITO: Valor fixo "F" (Não);
  + STATUSATENDIMENTO: TerminoRegistroAtendimento;

3.2 - Inserção do Pedido de Exames

 O sistema verifica se já existe um pedido para esse paciente/atendimento que não esteja cancelado e que já tenha sido enviado no arquivo (TAG: CodPedLab, Campo: SZPEDEXAME.NUMPEDSEC). Informações dos pedidos consistidos na tabela SZLOTEPEDIDOITENS.

Tratamentos específicos de preenchimento de campos do pedido de exames:

* + EXAMELEITO: Valor fixo "F" (Não);
  + DATAEXAME e HORAEXAME: Data/Hora do pedido de exames;
  + NUMPEDSEC: Número do pedido de exames do laboratório apoiado (Tag: CodPedLab);
  + INFCLINICAS: Taag OBS;
  + TIPOMEDSOLIC: Valor fixo "M" (Médico);
  + CANCELADO: Valor fixo "F" (Não);
  + SENHAINTERNET: Gera a senha de internet conforme lógica do próprio sistema
  + CODSETOR: Setor do exame;
  + IDUNIDATEND: Unidade de atendimento do pedido, mesma unidade de configuração dos exames;

3.3 - Inserção dos Exames no pedido

Todos os exames utilizados na integração precisam ter seu código de integração (DE-PARA) configurados no cadastro de exames (Item 2.4)

Tratamentos específicos de preenchimento de campos dos exames:

* + TIPOEXAME: Valor fixo "N" (Normal);
  + MATPENDENTE: Valor fixo "F" (Não);
  + DATACOLETA: Data da coleta enviada no XML (Tag: DataColeta);
  + STATUS: Valor fixo "I" (Inicial);
  + CANCELADO: Valor fixo "F" (Não);
  + LANCAITEMDEBCONTA: Busca no cadastro do exame se ele é faturado ou não;

### IMPORTANTE: Sobre a utilização da tag de <Medico> no XML de importação:

           A tag de médico no XML de importação se refere ao prestador do pedido e contém as seguintes informações:

* + SIGLACONSELHO: Valor com a sigla do conselho do profissional;
  + UFCONSELHO: Unidade Federativa do conselho;
  + NUMEROCONSELHO: Número do conselho do profissional;
  + NOME: Nome do profissional;
  + SEQMED: Sequencial do médico. Esse campo é **obrigatório** quando eu tiver um ou mais médicos no meu XML;

          Quando eu tiver um médico no meu XML, identificar sempre na tag <idMedicoSolicitante> dentro da tag de Exame o valor correspondente ao meu prestador. Esse número será igual ao sequencial do médico.

Exportação de Resultados

## **04. EXPORTAÇÃO DE RESULTADOS**

Caminho: TOTVS RM => Saúde => Hospitais e Clínicas => Utilitários => Integrações => Laboratório Apoioado => Exportação de Resultados

O processo de exportação de resultados solicita ao usuário algumas informações necessárias para a execução do processo como:

* + Diretório de Integração: Usuário deverá informar qual diretório que o sistema irá gravar os arquivos de exportação dos resultados de exames
  + Data Inicial e Data Final: Intervalo de datas de liberação do resultado na qual o sistema irá considerar os exames para exportação de seus resultados
  + Unidade de Faturamento: Usuário deverá selecionar uma unidade de faturamento específica para que a informação do laboratório apoiador seja enviado como identificação no arquivo (TAG Emissor)

É gerado um arquivo para cada laboratório apoiado.

Para a exportação dos resultados são selecionados todos os exames laboratoriais do laboratório apoiado em questão que possuem intervalo de liberação dos resultado dentro da faixa informado pelo usuário na tela do processo, que não estejam cancelados, que não tenha sido enviados anteriormente na integração (Campo SZPEDEXAMEITEM.IDPEP2 = NULL ou 0) e estejam, no momento da geração, com um dos seguintes status:

* + Liberado (L)
  + Emitido (E)
  + Entregue (F)
  + Liberado pela Recepção (O)

Mapeamento das TAGs ao gerar o XML de resultados:

* + Protocolo: Valor fixo “1”
  + ID: Data e hora de geração no formato yyyyMMddHHmmss
  + Emissor: Nome da Unidade de Faturamento selecionada para gerar o arquivo
  + DataEmissao: Data do sistema no momento da execução do processo
  + HoraEmissao: Hora do sistema no momento da execução do processo
  + Período: Período (Data Início e Fim) informado na tela de execução do processo de exportação
  + CodLab: Código cadastrado no RM referente ao laboratório apoiado, informação localizada na tela 2.2.1
  + CodPedApoio: Número do Pedido do TOTVS Saúde Hospitais e Clínicas
  + CodPedLab: Número do Pedido do Laboratório Apoiado (SZPEDEXAME.NUMPEDSEC)
  + Nome: Nome do Paciente
  + MaterialNome: Descrição do material biológico do exame
  + ExameNome: Nome do Exame
  + CodExmApoio: Código do exame do laboratório apoiado (SZEXAMELOCALEXTERNO.CODEXAMELABEXT)
  + CodExmLab: Código do exame do laboratório apoiado (SZEXAMELOCALEXTERNO.CODEXAMELABEXT)
  + CodigoFormato: Valor Fixo “1”
  + Metodo: Descrição do método utilizado
  + idExame: Sequencial do Exame no arquivo
  + Nome: Nome do Exame
  + Resultado - idItemDeExame: Valor Fixo 1
  + Resultado - Nome: Nome do Parâmetro do Exame
  + Valor: Valor do resultado do parâmetro (Campo SZPEDEXAMERESULT.RESULTADO)

Além dos resultados estruturados para os exames laboratoriais é possível gerar o resultado de exames da seguinte forma:

* + Exame Laboratoriais:
    - Base 64 : É possível exportar em Base64 o relatório configurado no sistema para que esse seja enviado no formato PDF dentro do XML
  + Exames de Imagem:
    - Base 64 : É possível exportar em Base64 o relatório configurado no sistema para que esse seja enviado no formato PDF dentro do XML
    - Laudo Texto: Para exportação de exames de imagem, o resultado padrão da integração é, na TAG de resultados, enviar o Texto do Laudo do exame dentro de uma estrutura CDATA do arquivo XML.

Informação

Para habilitar o envio do PDF no XML (Base64) é necessário habilitar o respectivo parâmetro que fica localizada na tela 2.2.1

Arquivos de Exemplo

## **05. ARQUIVOS DE EXEMPLO**

Abaixo dois exemplo de arquivos utilizados na integração:

* + Exemplo Exportação Resultados.xml : Arquivo que contém resultados de exames exportado pelo TOTVS Saúde Hospitais e Clínicas para envio ao laboratório apoiado
  + Exemplo Importação Pedidos.xml : Arquivo que contém os pedidos de exames enviado pelo laboratório apoiado a serem importados no TOTVS Saúde Hospitais e Clínicas

250250
