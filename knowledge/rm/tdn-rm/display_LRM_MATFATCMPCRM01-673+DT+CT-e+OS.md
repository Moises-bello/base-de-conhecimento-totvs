---
content_hash: a7021ca687b71d18d26cace6b299197767d0e779e761e9475d5ef7c0bbc57087
fetched_at: '2026-06-29T00:08:36.310848+00:00'
page_id: '284473216'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-673 DT CT-e OS
type: documentation
url: https://tdn.totvs.com/display/LRM/MATFATCMPCRM01-673+DT+CT-e+OS
version: 128
---

# CT-e OS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Totvs Gestão de Estoque, Compras*.e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *CT-e OS* | *CONHECIMENTO DE TRANSPORTE ELETRÔNICO - OUTROS SERVIÇOS* | |
| **Cadastros Iniciais:** | *Filial e Veíciulos* |
| **Parâmetro(s):** | *Parâmetros Fiscais da Filial e Parâmetros do Tipo de Movimento.* |
| **Ponto de Entrada:** | *-* |
| **Tickets relacionados** | *MATFATCMPCRM01-673* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *MATFATCMPCRM01-673* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server.* |
| **Tabelas Utilizadas:** | *TCTEMOV, TPARFILIAL, TCTEOS.* |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Implementação do Conhecimento de Transporte Eletrônico para Outros Serviços (CT-e OS).

## **Documentação Adicional**

Informações adicionais sobre o funcionamento do CT-e OS podem ser encontrados no Manual do CT-e que pode ser adquirido em <http://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=bx74pJ8hXaM=>

Para informações sobre o **Evento de Prestação em Desacordo**, consultar [MATFATCMPCRM01-2050 DT PRESTAÇÃO DE SERVIÇO EM DESACORDO](http://tdn.totvs.com/pages/viewpage.action?pageId=351017018)

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.18*.

As alterações também foram liberadas nas seguintes versões:

* 12.1.15.191 ou superiores
* 12.1.16.167 ou superiores
* 12.1.17.151 ou superiores

Para versões anteriores à 12.1.18 é necessário executar o script que se encontra na Central de Downloads com o nome de **Pacote CT-e OS.**

## Procedimento para Utilização

Para utilização do CT-e OS será necessário realizar as seguintes parametrizações:

**1) DADOS FISCAIS DA FILIAL**

No Cadastro da Filial em **Anexos -> Dados Fiscais -> Aba Dados Adicionais,** foram criados dois novos campos para atender à legislação do CT-e OS. O ****Termo de Autorização de Fretamento**** e o ****Número de Registro Estadua**l.**

**2) PARAMETRIZAÇÃO DA FILIAL**

No **Totvs Gestão de Estoque, Compras e Faturamento** acessar a opção **Ambiente -> Parâmetros** e selecionar o item  **Gestão de Estoque, Compras e Faturamento.**

Acessar o caminho **Integrações -> Fiscal -> Dados Fiscais** e clicar em **Avançar**. Após isso acessar o item **Parâmetros por Filial** e selecionar a filial que deseja configurar.

Para configurar o Certificado, deve-se configurar a opção Certificação Digital 2/2.

Para configurar as informações de Ambiente, deve-se selecionar o item **Ambiente CT-e OS.**

Essa tela contém três campos:

a) Ambiente de Envio: Indica para qual ambiente da SEFAZ será enviado o CT-e OS (Produção ou Homologação).

b) Modalidade de Operação: indica em qual modalidade o CT-e OS será emitido. As possíveis modalidades são:

* Normal: CT-e OS emitido normal
* Contingência Offline FS-DA: Indica que o CT-e OS foi emitido sem comunicação com a SEFAZ.
* Contingência SVC - RS: Indica que o CT\_e OS será emitido para a SEFAZ Virtual do Rio Grande do Sul
* Contingência SVC - SP: Indica que o CT\_e OS será emitido para a SEFAZ Virtual de São Paulo.

c) Versão do CT-e OS: Indica qual a versão do layout do CT-e OS.  Atualmente conterá valor fixo **3.00**

**3) PARAMETRIZAÇÃO DO TIPO DE MOVIMENTO**

A Parametrização do Tipo de Movimento é realizada conforme os passos abaixo:

Na Etapa **Movimento - Transporte (Mov - Transporte 1/3)**, seleciona o parâmetro "Editar Quantidade"

Na etapa **Movimento - Transporte (Mov - Transporte 2/3)** selecionar o "Tipo de Frete" como **Edita** e marcar os parâmetros "Edita Dados de Cálculo do Frete" e "Editar Dados da Placa do Veiculo"

Na Etapa **Fiscal - Natureza**, Selecionar a "Edição da Natureza" com o valor **Edita**

Na etapa **Fiscal - Tributação - Movimento**, marcar o parâmetro "Utilizar Tributação dos Movimentos" cadastrar os tributos envolvidos na operação.

IMPORTANTE: para movimentos de CT-e OS os tributos que irão compor o XML (normalmente ICMS e INSS) devem ser cadastrados no **Movimento** e não no **Item**

Na Etapa **Fis - Conhecimento de Transporte** é necessário Informar o "Tipo de Operação de Conhecimento de Transporte" como **Emitir CTe OS**. Após isso, deve-se selecionar o Modal desejado para envio.

E depois selecionar qual o "**Tipo do Serviço CT-e OS**" que se deseja.

Este campo agora é um default do campo "Tipo do Serviço do CT-e OS" do movimento (Transporte | Identificação), portanto não é mais obrigatório o seu preenchimento nos parâmetros do tipo de movimento, mas caso seja preenchido, o valor definido no parâmetro deverá ser carregado para o movimento.

**4) CADASTRO DE VEÍCULOS**

Foram criados dois novos campos no cadastro de veículos para atender à legislação do CT-e OS: O **TAF - Termo de Autorização de Fretamento** e o **Número de Registro Estadua**l.

Esse campos serão habilitados quando o campo **Tipo Prop. Veículo** estiver com o valor **Terceiros**

**5) MOVIMENTO**

Durante a criação do movimento de CT-e OS será necessário alterar os seguintes campos:

a) Na aba **Integrações -> Fiscal** informar o **Cod. Natureza de Operação.**

IMPORTANTE. Os CFOPs válidos para CT-e OS podem ser encontrados no ANEXO IX no Manual do CT-e  3.0

b) Na aba **Transporte -> Identificação**, informar o **Tipo de Frete** e o campo **Quantidade**.

No tipo de movimento definido como "**Emitir CT-e OS**", na aba (Transporte | Identificação) será apresentado os campos "**Tipo CT-e OS**" e "**Tipo do Serviço CT-e OS**" com seus respectivos valores:

No tipo de movimento definido como "**Emitir CT-e OS**", na aba (Transporte | Identificação) será apresentado os campos "**Tipo CT-e OS**" e "**Tipo do Serviço CT-e OS**" com seus respectivos valores:

**Consistências:**

* O campo "Tipo do Serviço CT-e OS" é de preenchimento obrigatório.

Em tipos de movimento parametrizados como "**Emitir CT-e OS**" será obrigatório o preenchimento do campo "**Tipo do Serviço CT-e OS**" no movimento e não mais nos parâmetros e caso não seja preenchido, será apresentado a mensagem de consistência abaixo:

c) Na aba **Transporte -> Identificação**, o campo **Cliente/Fornecedor do Tomador** - Informando um Cliente / Fornecedor (tabela FCFO) que é o tomador desse serviço.

d) Na aba **CRTC -> Coleta em Entrega** informar o Estado e Município de início (Coleta) e o Estado e Município de fim (Entrega)

e) Na aba **CTRC -> Outros Dados** informar os valores da **Composição do Frete** (é necessário pelo menos um deles preenchido)

* **Tipo do Serviço CT-e OS igual a "Excesso de Bagagem":**

f) Quando **Tipo do Serviço CT-e OS**igual a "Excesso de Bagagem", em CTRC | CTRC Saída, na tela **Notas Fiscais Conhec. Transporte**, exibir os campos **Data Emissão** (TCTRC.DATAEMISSAO), **Número Nota** (TCTRC.NUMERODOC), **Série** (TCTRC.SERIEDOC), **Sub Série** (TCTRC.SUBSERIEDOC) e **Valor Total** (TCTRC.VALORTOTAL).Caso o campo Tipo de Documento seja informado com um tipo de documento referente a CT-e (FTDO.CODMODDOC igual a 57), não exibir as abas Informações Contingência e Documento Auxiliar Eletrônico

Quando for um movimento de "**CT-e OS**" e o campo ”**Tipo do Serviço CT-e OS**" for definido como "**Excesso de bagagem**", na aba (CTRC | CT-e) não deverá ser apresentado "**Informações de Percurso**". Para os demais tipos de Serviços a aba será apresentada normalmente.

g) Na aba **CTRC -> CT-e -> Seguro de Carga**, incluir as informações do **Seguro do Transporte.**

h) Na aba **CTRC -> CT-e -> Informações de Percurso**, incluir as informações dos estados contidos no Percurso entre as UF de Origem e a UF de Destino. É necessário informar também qual a ordem em que cada estado será parte do percurso. Quando **Tipo do Serviço CT-e OS** forigual a "**Excesso de Bagagem**", em CTRC | CT-e, não será exibido a aba **Informações de Percurso** conforme visto no item "**F**" deste documento.

* **Tipo do Serviço CT-e OS igual a "Transporte de Pessoas":**

Quando for um movimento de "**CT-e OS**" e o campo ”**Tipo do Serviço CT-e OS**" for definido como "**Transporte de Pessoas**", será apresentado o campo "**Tipo do Fretamento de Pessoas**" com duas opções: **Contínuo** e **Eventual**.

**OBS**: O campo "**Tipo do Fretamento de Pessoas**" é de preenchimento obrigatório e será consistido caso tente salvar o movimento sem preencher um valor para o campo.

Quando o tipo do fretamento for definido como "**Eventual**" será exibido um novo campo na tela "**Data e Hora da Viagem**" e o seu preenchimento é opcional.

**Consistências:**

* O campo "Tipo do Fretamento de Pessoas" é de preenchimento obrigatório.

Em tipos de movimento parametrizados como "**Emitir CT-e OS**" onde o  campo "**Tipo do Serviço CT-e OS**" esteja preenchido como "**Transporte de Pessoas**", o campo "**Tipo do Fretamento de Pessoas**" será de preenchimento obrigatório e caso não seja preenchido, será apresentado a mensagem de consistência abaixo:

**Tabelas Utilizadas**

Para a implementação, foi criado o campo na base na tabela citada abaixo:

* TMOVTRANSP.TIPOFRETAMENTOPESSOAS - Tipo do Fretamento de Pessoas (CTeOS - Transporte de Pessoas).
* TMOVTRANSP.DATAHORAVIAGEM - Data e hora da viagem (CTeOS - Transporte de Pessoas).

**6) ENVIO DO CT-E OS**

Para realizar o envio do CT-e OS é necessário acessar a visão de CT-e OS no caminho **Faturamento → Conhecimento de Transporte - Outros Serviços (CT-e OS).**

Na visão, acessar **Processos → Enviar CT-e.** É necessário preencher a **Filial**, o **Tipo de Movimento**. o Intervalo de **Datas de Emissão** e também o Intervalo de **Número de Movimentos**que se deseja enviar.

Um registro enviado, caso esteja tudo certo, será aprovado o que será indicado pelo status igual a **Autorizado.**

IMPORTANTE: Diferente dos processos de NF-e, MDF-e e CT-e, o CT-e OS não possui processo de consulta. Isso ocorre porque a SEFAZ definiu o processo de envio do CT-e OS como síncrono e portanto o próprio processo de envio já autoriza o registro. 

**7) IMPRESSÃO DO CT-E OS**

Para a impressão do Documento Auxiliar do Conhecimento de Transporte Eletrônico (DACTE) deve acessar **Processos → Impressão do Relatório CT-e .Net (RM Reports)**e selecionar o relatório.

**8) CANCELAR O CT-E OS**

Para a realizar o cancelamento do CT-e OS, deve-se selecionar um registro com o status igual a **Autorizado** e acessar **Processos → Enviar Evento,**selecionar o "Tipo de Evento" igual a **Cancelamento**e informar a justificativa

IMPORTANTE: A Justificativa deve ter pelo menos 15 caracteres.

Após o envio, o status do registro irá ser alterado para **Evento pendente.**

Deve-se então, executar o processo de consulta do evento em **Processos → Consultar Evento**e, caso autorizado, o status do registro será alterado para **Cancelado**

**9) CARTA DE CORREÇÃO DO CT-E OS**

Para enviar uma Carta de Correção para  o CT-e OS, deve-se selecionar um registro com o status igual a **Autorizado** e acessar **Processos → Enviar Evento,**selecionar o "Tipo de Evento" igual a **Carta de Correção (CC-e).** Então, deve clicar no botão **Incluir**.

Deve-se então selecionar os seguintes itens:

* **Grupo da Alteração** - Indica a qual grupo do XML o campo pertence.
* **Campo** - O Campo que precisa ser alterado
* **Valor Alteração** - O valor que se deseja ser corrigido.

É possível incluir quantos campos forem  necessários antes do envio.

Após o envio, o status do registro irá ser alterado para **Evento pendente.**

Deve-se então, executar o processo de consulta do evento em **Processos → Consultar Evento.**O registro voltará a ter o status **Autorizado**.

IMPORTANTE: As alterações realizadas na carta de correção NÃO afetam o movimento, assim como não alteram o XML original na SEFAZ.

**10) ENVIO DE CONTINGÊNCIA NO CT-E OS**

Caso seja necessário o envio de um CT-e OS em contingência deve-se primeiro parametrizar a filial para essa operação.

No **Totvs Gestão de Estoque, Compras e Faturamento** acessar a opção **Ambiente -> Parâmetros** e selecionar o item **Gestão de Estoque, Compras e Faturamento.**

Acessar o caminho **Integrações -> Fiscal -> Dados Fiscais** e clicar em **Avançar**. Após isso acessar o item **Parâmetros por Filial** e selecionar a filial que deseja configurar.

Ir na aba **Ambiente CT-e OS** e selecionar a Modalidade de Operação como **Contingência Offline FS-DA**

Para enviar é necessário acessar a visão de CT-e OS no caminho **Faturamento → Conhecimento de Transporte - Outros Serviços (CT-e OS).**

Então, deve-se acessar ****Processos → Gerar DACTE em Contingência.****

É necessário preencher a **Filial**, o**Tipo de Movimento**. o Intervalo de **Datas de Emissão** e também o Intervalo de **Números de Movimento** que se deseja enviar. 

Após o envio, o registro será salvo com o status de **Contingência**.

Esse registro deve-se ser posteriormente enviado à SEFAZ. Para isso, selecione o registro com status igual a Contingência e selecione **Processos → Enviar CT-e.**

Informar a **Data de Início da Contingência** e a **Justificativa** da contingência

Após esse Envio, o registro ficará com Status ****Autorizado.****

******11) CT-E OS COMPLEMENTAR******

Para enviar um CT-e OS do tipo Complemento de Valores, é necessário configurar um novo Tipo de Movimento com o Motivo de Referência → **6 - NF Complementar / Retificadora.**

Esse Motivo de Referência é configurado na etapa **Mov - Outros Dados**

Assim, deve-se gerar uma cópia por referência nesse novo Tipo de Movimento selecionando como movimento base o movimento do CT-e OS a que se deseja complementar.

Nesse Movimento, deve-se selecionar na etapa **Transporte → Identificação** e selecionar o **Tipo CT-e OS** como "**Complemento de Valores**"

Após isso, o envio do CT-e OS complementar é igual ao de um CT-e OS normal, detalhado no item 6 deste documento.

divs
