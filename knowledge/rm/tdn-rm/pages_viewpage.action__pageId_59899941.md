---
content_hash: be88de28b1e817ad8e09069266fb949be4c4aea647a8275bc2a7786079909e55
fetched_at: '2026-06-29T00:10:57.216506+00:00'
page_id: '59899941'
product: rm
source: tdn-rm
title: Integração TOTVS COLABORAÇÃO - ERP LINHA RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=59899941
version: 10
---

**1.**  **Conceito: TOTVS Colaboração**

A oferta TOTVS Colaboração compreende toda integração entre os ERP’s TOTVS com a solução Neogrid.

A responsabilidade do TSS no TOTVS Colaboração é de integrar os ERP’s com a Neogrid, provendo serviços que possibilitam a comunicação e transmissão de documentos entre as partes, conforme figura abaixo.

**O TOTVS Colaboração tem como premissas:**

* Solução de integração simples e padronizada para todos os tipos de documentos e ERPs, sempre utilizando TSS ou um middleware TOTVS para comunicação com a NeoGrid;
* Utilização dos mesmos layouts (NF-e e CT-e) e protocolos de comunicação (WebServices) existentes atualmente com o TSS;
* Menor impacto possível para ERPs (Microsiga, Datasul, Logocenter e RM), TSS e NeoGrid;

**2.** **RM x TOTVS Colaboração**

Na linha **RM** o TOTVS Colaboração compreende integração dos seguintes processos:

* Recebimento de NF-e
* Recebimento de CT-e
* Emissão de NF-e
* Emissão de NFS-e
* Emissão de CT-e

O módulo RM que contem a integração com o TOTVS Colaboração é o **TOTVS Gestão de Estoque, Compras e Faturamento**. Os processos e sub processos envolvidos são:

**Compras**

* Recebimento de Materiais
* Importação
* Aquisição de Serviços
* Devolução de Compras

**Vendas**

* Faturamento
* Exportação
* Devolução de Venda

**Estoque**

* Transferência

Veja no quadro abaixo a relação entre processos RM e processos TOTVS Colaboração:

|  |  |  |
| --- | --- | --- |
| **Processos RM** | **Sub Processos RM** | **Processos TOTVS Colaboração** |
| **Compras** | Recebimento de Materiais | Recebimento de NF-e |
| Importação | Recebimento de NF-e |
| Aquisição de Serviços | Recebimento de CT-e |
| Devolução de Compras | Emissão de NF-e |
| **Vendas** | Faturamento | Emissão de NF-e  Emissão de NFS-e  Emissão de CT-e |
| Exportação | Emissão de NF-e |
| Devolução de Venda | Emissão de NF-e  Recebimento de NF-e |
| **Estoque** | Transferência | Emissão de NF-e  Recebimento de NF-e |

**3.**  **Pré- requisitos Instalação / Implantação / Utilização:**

Os pré-requisitos (técnicos ou de negócios) necessários para a utilização dos processos do TOTVS Colaboração na linha RM são:

**Técnicos:** Versões **mínimas** do produto:

* BibliotecaRM: **11.40.50 / 11.52 / 11.82** – Recebimento de NF-e
* BibliotecaRM: **11.52.56.102** **/ 11.82.26** – Recebimento de CT-e
* BibliotecaRM: **11.52 / 11.82** – Emissão de NF-e
* BibliotecaRM: **11.52.56/ 11.82.26**  – Emissão de NFS-e
* BibliotecaRM: **11.52 / 11.82** – Emissão de CT-e
* TSS versão 2.08 – configurado com os serviços a serem utilizados no TOTVS Colaboração

**Instruções para baixar as últimas versões:**

1. Acesse: [www.totvs.com/suporte](http://www.totvs.com/suporte)
2. Faça login, com seu e-mail e senha
3. Clique em Download através da barra do menu do Portal do Cliente
4. Aplica-se o filtro: [Linha = RM e Amb/Vers = versão desejada] preencha demais campos conforme necessidade e clique em pesquisar.

**Negócios:**

* Contratação oferta TOTVS Colaboração (TSS / Neogrid). Converse com seu EAR para maiores informações sobre esse serviço;
* Acesso ao EDI da Neogrid (URL, usuários e senhas)

**4.**  **Parametrizações Comuns a todos os processos:**

**a)**      Instação do TSS (TOTVS Service SPED) versão 2.08 ou superior (de preferência sempre a última versão). Observar os serviços a serem instalados de acordo com a oferta TOTVS Colaboração contratada pelo cliente.

Obs.: Não faz parte do escopo desse documento detalhar a instalação do TSS no ambiente. Para tal, favor utilizar manual específico de instalação do TSS.

**b)**      **Atenção**: Clientes que estão implantando o processo do TOTVS Colaboração em versões inferiores a versão 12.0

Execução de Script específico - Para a correta parametrização da integração com o TC, é necessário executar um script para criação dos campos de integração do RM com o TOTVS Colaboração. Esse script deve ser solicitado a equipe de Help Desk da linha RM.

c)        Parametrizar módulo TOTVS Gestão de Estoque, Compras e Faturamento para Integração com Neogrid.

**Acessar:**

*MDI .Net* - Ambiente | Parâmetros Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Parâmetros por Filial | **Conexão NF-e**

* Informar: URL do Servidor TOTVS Services

**Acessar:**

*MDI .Net* - Ambiente | Parâmetros Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Parâmetros por Filial | **Certificação Digital**

* Informar: Tipo de Certificado, localização física e senha

**Acessar:**

*MDI .Net* - Ambiente | Parâmetros Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Parâmetros por Filial | **Informações do Neogrid**

* Informar: Usuário e Senha de acesso ao Neogrid:

O usuário deverá ser informado no seguinte formato: **CNPJ#Usuário** (CNPJ da empresa sem os separados, o caracter sustenido (#) e o usuário fornecido pela Neogrid).

**Exemplo:**

CNPJ: 17.810.358/0001-20

Usuário fornecido pela Neogrid: TOTVS

Informar no RM: Usuário Neogrid = **17810358000120#TOTVS**

* Informar: Ambiente de integração com o Neogrid para o Recebimento (caso tenha contratado algum processo de Recebimento).

Produção

Homologação

* Informar: Tipos de Documentos que serão tratados na Integração com o Neogrid

Todos

**Envio de NF-e**

**Envio de CT-e**

**Envio de NFS-e**

**Recebimento de NF-e**

**Recebimento de CT-e**

**Atenção**:

* Essa parametrização deverá ser realizada para todas as filiais que irão trabalhar com os processos integrados ao TOTVS Colaboração.
* Marcar somente as opções que a empresa contratou para a solução TOTVS Colaboração.
* Os clientes que já implantaram algum processo do TOTVS Colaboração, devem acessar essa parametrização e verificar se os campos Ambientes e Tipo Documento Integração Neogrid estão parametrizados corretamente.

Essa parametrização será repassada para a configuração do TSS (tabelas SPE000 e SPE001)     
  
  
**5**. **Modelo Operacional - Recebimento**

O Recebimento de NF-e e CT-e na linha RM consiste na inclusão de movimentos de entrada, seja de produtos ou serviços, através da importação de um arquivo XML (NF-e ou CT-e).

Esse processo, foi dividido em duas etapas:

* **Cadastro de XML** à consiste no cadastramento do arquivo XML no banco de dados do ERP.

* **Inclusão do Movimento de Entrada** à trata-se do processo de inclusão de movimento de nota fiscal de entrada, porém utilizando a importação de um arquivo XML.

A seguir descreveremos cada processo.

**6.****Cadastro XML**

Acessar:

*MDI .Net* **- Compras | TOTVS Colaboração – Cadastro XML**

Esse cadastro é específico para os processos de Recebimento de NF-e e Recebimento de CT-e.

Ele irá armazenar os XML recebidos pelo ERP RM, seja do fornecedor ou da Neogrid, para que sejam utilizados na inclusão de movimentos de entrada.

**Atenção**:

* Para a correta utilização desse cadastro é necessário que as parametrizações comuns, citadas anteriormente tenham sido executadas.
* Será necessário também que o serviço do TSS esteja ativo.

A Estrutura de Dados desse cadastro é composta por duas tabelas:

* **TNFEENTRADA** à tabela para armazenar os arquivos XML.
* **TNFEENTRADAHIST** à tabela para armazenar o histórico dos processos executados em cada XML.

Uma informação importante no cadastro do XML é o campo de ‘**Status**’ do XML, que pode indicar:

* Pendente (P) à para os arquivos cadastrados e ainda não enviados para validação;
* Enviado para Validação (E) à para os arquivos que foram enviados para validação de sua autenticidade;
* **Válido (V)** **à** **para os arquivos cuja autenticidade foi comprovada junto a SEFAZ. Somente os arquivos com este status poderão ser utilizados para inclusão de movimentos;**
* Inconsistentes (I) à para os arquivos, que por algum motivo, ocorreram erros na transação e devem ser processados novamente, seja enviados ou consultados);
* Rejeitados (R) à para os arquivos cuja autenticidade não foi comprovada junto a SEFAZ.

Neste cadastro, será possível executar os seguintes processos:

* Incluir Arquivo XML (COM ou SEM o arquivo físico do XML);
* Incluir Múltiplos XML
* Inclusão de XML por Data
* Enviar Arquivo XML para Validação
* Consultar Validação Arquivo XML
* Buscar XML já Validado
* Exclusão de Arquivo XML

**6.1**  **Incluir Arquivo XML (COM ou SEM o arquivo físico do XML)** **- Clicar no botão ‘Incluir’**

Este processo deve ser utilizado para cadastrar os arquivos XML quando se tem fisicamente o arquivo XML ou quando não tem o arquivo físico, mas possui o número da chave de acesso.

Possuindo o arquivo XML, o usuário deve indicar sua localização e confirmar a operação. O XML será cadastrado.

Se o usuário não possuir fisicamente o arquivo XML, o sistema abrirá uma tela para que seja informada a filial na qual será importado o XML, o fornecedor, a chave de acesso e o tipo do XML (NF-e ou CT-e). Posteriormente estes dados serão utilizados para buscar o arquivo XML junto à solução TOTVS Colaboração. Os XML incluídos nessa opção, terão habilitado o campo ‘Importado TOTVS Colaboração’.

O arquivo XML incluído por esta opção será salvo com status = ‘**P** – Pendente’.

**6.2**  **Incluir Múltiplos XML**

Este processo deve ser utilizado para cadastrar simultaneamente vários XML, mas somente quando se tem o arquivo físico.

Por esta opção será possível selecionar/marcar vários arquivos XML de uma determinada pasta, para serem incluídos automaticamente. No final do processo, o sistema irá exibir um log informando a situação de cada arquivo selecionado (se foi incluído ou não).

O arquivo XML incluído por esta opção será salvo com status = ‘P – Pendente’.

**6.3**  **Inclusão de XML por Data**

Este processo deve ser utilizado para cadastrar os XML disponibilizados pelo TC automaticamente por data de processamento do TSS. Por essa opção, o usuário **não** necessitará informar a chave de acesso. O TSS irá controlar os XML já exportados para o ERP.

A execução desse processo poderá ser **agendada** [[1]](file:///C:/Documents%20and%20Settings/felipe.patricio/Configura%C3%A7%C3%B5es%20locais/Temporary%20Internet%20Files/Content.Outlook/90VTFXUY/TOTVS%20Colabora%C3%A7%C3%A3o%20x%20ERP%20RM.docx#_ftn1)  de forma recorrente, tornando assim o cadastro de XML automatizado.

Esse processo irá carregar os XML (NF-e / CT-e) processados e autorizados junto a SEFAZ, que não tenham sido exportados para o ERP, em um determinado intervalo de data. Os XML serão carregados no RM com status ‘Validos’, ficando assim disponíveis para a inclusão de movimentos de entrada.

O default desse processo é carregar os XML com data de processamento no TSS no intervalo de (hoje – 1) até hoje. O número de dias inicial do intervalo é parametrizável na execução do processo.

Agendamento:

Caberá ao gerenciador do banco de dados da empresa, avaliar o tempo viável de recorrência do job, considerando ambiente e volume de registros processos pelo Neogrid.

Pontos de Atenção:

Todos os XML carregados por esse processo serão atualizados no TSS como exportados para o ERP. Se sua empresa utiliza este processo para carregar os XML, informamos que esse processo **não** recarrega XML excluído no ERP. Caso a exclusão tenha ocorrido indevidamente, a reinclusão do arquivo XML somente será possível manualmente, ou seja, através do processo ‘Incluir XML’ com a informação da chave de acesso.

Funcionalidade disponível à partir das Bibliotecas RM: 11.52.56.102 e 11.82.26.

**6.4**  **Enviar Arquivo XML para Validação**

Este processo deve ser utilizado para enviar o arquivo XML para validação de sua autenticidade.

Somente os XML com status de ‘P – Pendente’ , ‘I – Inconsistentes’ e ‘R – Rejeitados’, que foram incluídos informando que existia a arquvio físico, devem ser selecionados para a execução desse processo. Após sua execução, os XML selecionados terão o status alterado para ‘E – Enviado’.

**6.5**  **Consultar Validação** **Arquivo XML**

Este processo deve ser utilizado para confirmar a autenticidade / validação dos XML enviados no processo anterior: ‘Enviar Arquivo XML para validação’.

Somente os XML com status de ‘E – Enviado’ devem ser selecionados para a execução desse processo. Após a execução, os XML autorizados junto a SEFAZ terão o status alterado para ‘V – Válidos’, ficando assim disponíveis para a inclusão de movimentos de entrada.

**6.6**  **Busca** **XML já validado**

Este processo deve ser utilizado para buscar os XML cujo cadastro foi realizado somente com a chave de acesso, sem o arquivo físico.

Somente os XML com status de ‘P – Pendente’, ‘I – Inconsistentes’ e ‘R – Rejeitados’, que possuem o campo ‘Importado TOTVS Colaboração’ habilitado, devem ser selecionados para a execução desse processo. Após a execução, os XML selecionados terão o status alterado para ‘V - Válido’.

**6.7**  **Exclusão de XML**

Este processo pode ser executado quando desejar excluir algum arquivo XML cadastrado no ERP.

Somente arquivos XML não vinculados a inclusão de movimentos podem ser excluídos. O sistema faz consistência nesse sentido.

**7.Inclusão do Movimento de Entrada**

Para cada tipo de operação de entrada, existe no RM, um ou  ‘n’ tipos de movimentos específicos. Além disso, os processos internos do RM podem ser diferenciados de acordo com a operação de entrada.

A seguir, descreveremos separadamente os processos de **Recebimento de NF-e** e **Recebimento de CT-e**.

 

 **8. Recebimento de NF-e**

A inclusão de movimentos de entrada referente a compra de mercadorias pode ser realizada, utilizando um arquivo XML de NF-e das seguintes maneiras:

* Através da Inclusão Direta de um movimento, ou seja, que não tem pedido;
* Através do Recebimeto de Pedido(s);
* Através de Cópia por Referência, para as movimentações de Devolução

**8.1**  **Parametrizações – Tipo Movimento – Recebimento de NF-e**

Acessar:

*MDI.Net:* Ambiente | Parâmetros Gestão de Estoque, Compras e Faturamento | Processo (\*) | Tipo de Movimento

*(\*) Identificamos que a funcionalidade de Inclusão de Movimento a partir da Importação de um Arquivo XML de NF-e está associada aos processos / sub processos de negócio:*

*Compras* */ Recebimento de Materiais**(são incluídos os movimentos de compra de materiais)*

*Vendas* */ Devolução de Venda**(são incluídos os movimentos de entrada por devolução de venda)*

*Estoque / Transferências* *(são incluídos os movimentos de entrada por transferência entre filiais)*

* **Etapa: TOTVS Colaboração**

Integração Neogrid: Informar o tipo de documento que o tipo de movimento em questão irá tratar.

Opções válidas:

* Não Utiliza
* Envio NF-e / NFS-e
* Envio CT-e
* **Recebimento NF-e**
* Recebimento CT-e

**Atenção**: Parametrização alterada à partir da versão 11.52.56. Em versões anteriores, essa opção era indicada na Etapa |Outros Dados|.

* Busca PIS/COFINS em: Informar se o cálculo do PIS/COFINS no tipo de movimento em questão, quando utilizado um XML para sua inclusão, deve considerar os valores desses tributos informado no XML ou calculados de acordo com a parametrização do tipo de movimento.

Opções válidas:

* Tipo de Movimento
* XML (default do sistema)

* **Etapa Fis – Natureza**

Seleção Automática da Natureza: Seleciona por Item, pois no arquivo XML esta informação está associada à TAG de Produtos e Serviços.

* **Etapa Fis – Tributação - Item**

Os tributos: ICMS. ICMSST, IPI, ISS, PIS e COFINS s/Faturamento devem ser parametrizados por ITEM DE MOVIMENTO. Isto porque de acordo com o layout do XML de NF-e, esses tributos estão vinculados a TAG de produtos e serviços.

Para esses tributos serão levados para a tributação do item de movimento: os valores de base de cálculo, alíquota e o valor do imposto, quando informados no XML.

* **Etapa Fis – Tributação - Movimento**

Os tributos: PIS-RF, COFINS-RF, CSLL-RF (retidos), IR-RF e INSS (valor da previdência social) devem estar parametrizados no movimento. Isto porque de acordo com o layout do XML de NF-e, esses tributos constam somente na TAG de valores totais, não estando associados aos produtos e serviços.

Para os tributos PIS, COFINS e CSLL RETIDO será levado para a tributação do movimento somente o valor do imposto. Para o IR Retido e o INSS serão levados os valores de Base de Cálculo e o valor do imposto, quando os mesmos forem informados no XML.

**Observações**:

* É obrigatório que os tipos de movimentos utilizados para inclusão de NF-e de entrada tenham parametrizados os tributos ICMS, ICMS ST e IPI, mesmo que a empresa não tenha crédito desses impostos na entrada. Essa parametrização é necessária devido ao arquivo XML conter informações sobre esses impostos independente da CST. A correta escrituração dos movimentos estará vinculada ao código de CFOP informado no movimento de entrada.

* As naturezas fiscais de entrada com ICMS ST, que serão utilizadas na importação de arquivo XML, devem ter o parâmetro: ‘*ICMS ST não considera ICMS próprio*’ **marcado**, isto porque o valor do ICMS ST será carregado do XML e seu valor não deve ser recalculado pelo sistema.

* A parametrização dos tributos PIS e COFINS não é obrigatória no tipo de movimento. Se a empresa não possuir crédito desses impostos na entrada, os mesmo não devem ser parametrizados. Ao importar um XML com valores para PIS e COFINS, se o movimento não tiver esses tributos parametrizados, o sistema irá apresentar uma mensagem alertando dessa divergência e o movimento será incluído normalmente, sendo esses valores desprezados.

* Quanto aos tributos PIS e COFINS, se a empresa possuir crédito com alíquotas e valores diferentes dos valores contidos no XML, o parâmetro ‘*Buscar PIS/COFINS em’*: deve estar indicado ‘*Tipo de Movimento*’ e o cálculo desse tributos definidos conforme parametrização do tipo de movimento.

* Quando os valores dos tributos forem carregados para o movimento conforme as informações do arquivo XML, o sistema irá considerar que a tributação foi editada, deixando esta informação registrada na grid de tributação. Importante citar que uma vez carregado os tributos para o movimento, o sistema não irá realizar recalculo dos valores dos tributos se o código da natureza de operação for alterado.

* Sugerimos também verificar o tamanho do *Número do Movimento*, pois o tamanho definido para a NF-e é de até 9 dígitos, isto, para que seja possível carregar para o movimento o número que consta no arquivo XML da NF-e sem inconsistência.

* Sugerimos também verificar o tamanho do *Número do Documento Financeiro* *e do Documento Contábil*, que deverá ser alterado, tendo seu tamanho aumentado proporcionalmente ao tamanho do número do movimento.

**8.2**  **Inclusão de Movimento de Entrada de Mercadoria** **– Recebimento de NF-e**

**a)** **Inclusão Direta – sem Pedido de Compra**

Na visão de movimento, clicar no ícone ‘*Inclusão de Movimento com Arquivo XML*’.

Será aberto um wizard de ‘*Tradução de arquivo XML*’.

Neste wizard deve-se selecionar o arquivo XML que será utilizado para incluir o movimento. Serão apresentados somente os arquivos XML com status de ‘Válido’,cadastrados na filial selecionada no filtro de movimento cujo Tipo de XML corresponda ao Tipo de Documento TC parametrizado no Tipo de Movimento.

Os dados do arquivo XML serão carregados na visão.

Na sequencia, deve-se vincular cada item do arquivo XML a um produto cadastrado no ERP.

**Observação:** Os itens do arquivo XML poderão ser **identificados automaticamente** durante a execução do wizard de tradução. Para tal é necessário que os produtos tenham cadastrado o código no respectivo cliente/fornecedor. São as informações da tabela TPRDCFO.

Quando o usuário vincular manualmente um produto ao item do arquivo XML, o sistema criará o vinculo do produto ao fornecedor, incluindo automaticamente um registro na tabela TPRDCFO. Esta informação servirá para que nas próximas compras desse mesmo fornecedor, o produto seja identificado automaticamente.

Ao finalizar o wizard, será aberta a edição do movimento. O mesmo terá as informações contidas no XML traduzidas para o ERP. As informações gerenciais do movimento, como local de estoque, tabelas de classificação, condição de pagamento, dentre outras, deverão ser informadas pelo usuário, se o tipo de movimento não possuir default.

**Observação**: O código da natureza de operação da entrada será preenchido automaticamente, se o tipo de movimento tratar regras de seleção automática. Caso contrário, o usuário deverá informar a natureza de operação manualmente. O tratamento é o mesmo adotado para a inclusão de movimento, quando não se utiliza um arquivo XML.

A correta escrituração dos movimentos, bem como a geração do SPED  estará vinculada ao código de CFOP informado no movimento de entrada.

**b)** **Recebimento de Pedido(s) de Compra**

Na visão de Pedido(s) de Compra, selecionar os movimentos que serão recebidos e clicar no ícone ‘*Receber*’ (processo padrão do sistema, quando se deseja receber um movimento).

Será aberto o wizard de ‘*Recebimento / Faturamento de Movimento*’. Selecionar as opções conforme necessidades do processo.

Na sequencia, estando o movimento destino parametrizado para integração com o TOTVS Colaboração/Neogrid, o sistema abrirá o wizard de ‘*Tradução do arquivo XML*’.

Neste wizard deve-se selecionar o arquivo XML que será utilizado para incluir o movimento. Serão apresentados somente os arquivos XML com status de ‘Válido’ e cadastrados na filial selecionada no filtro de movimento.

Os dados do arquivo XML serão carregados na visão.

Na sequencia, deve-se vincular cada item do arquivo XML a um item do Pedido(s) de Compra selecionado para recebimento ou a um produto cadastrado no ERP.

**Observação**: Os itens do arquivo XML poderão ser identificados e vinculados automaticamente aos itens dos pedidos selecionados por duas maneiras:

* A primeira está relacionada ao arquivo XML ter a informação do ‘*número do pedido de compra*’ e o ‘*item do pedido de compra*’ (campos <xPed> e <nItemPed> cujo preenchimento não é obrigatório por parte do fornecedor). Tendo essas informações, o sistema irá verificar se o número do pedido informado no arquivo XML corresponde ao pedido de compra selecionado no processo. Caso afirmativo, irá vincular o item do XML ao item do pedido cujo sequencial corresponde ao número informado como ‘item do pedido de compra’.

**Atenção**: Como esta informação é livre por parte do fornecedor, o mesmo pode enviar dados incorretos, por isso é extremamente necessário conferir se a vinculação está correta. Caso não esteja, será necessário alterar manualmente a vinculação.

* A segunda está relacionada ao código do produto no cliente/fornecedor, informações da tabela TPRDCFO já descrita no processo anterior.

Não sendo identificado o produto automaticamente, o usuário deverá realizar a vinculação manual.

A pesquisa de itens inicialmente será realizada entre os itens dos pedidos de compras selecionados para recebimento.

Se o item mencionado no arquivo XML não estiver nos pedidos de compra selecionados e mesmo assim seu recebimento for necessário, o usuário poderá pesquisar este item em toda a tabela de produtos, clicando no botão ‘*Incluir Item Novo’*.

Ao finalizar o wizard, será aberta a edição do movimento. O mesmo terá as informações contidas no XML traduzidas para o ERP juntamente com as informações gerenciais dos pedidos de compras recebidos no processo.

**Observação**: O código da natureza de operação da entrada será copiado do pedido de compra relacionado, caso o mesmo tenha essa informação. Caso contrário, o sistema irá aplicar a regra de seleção parametrizada no tipo de movimento que está sendo utilizado para registrar a nota de entrada.

A correta escrituração dos movimentos, bem como a geração do SPED  estará vinculada ao código de CFOP informado no movimento de entrada.

**c)** **Cópia por Referencia - Devolução**

Na visão do movimento de Devolução, selecionar o processo de ‘*Assistente de Cópia por Referência*’ (processo padrão do sistema para lançamento de uma devolução).

Será aberto o wizard de ‘*Assistente de Cópia de Movimento por Referencia*’. Selecionar as opções conforme necessidades do processo.

Na sequencia, estando o movimento de devolução parametrizado para integração com o TOTVS Colaboração/Neogrid, o sistema abrirá o wizard de ‘*Tradução do arquivo XML*’.

Neste wizard deve-se selecionar o arquivo XML que será utilizado para incluir o movimento. Serão apresentados somente os arquivos XML com status de ‘Válido’ e cadastrados na filial selecionada no filtro de movimento.

Os dados do arquivo XML serão carregados na visão.

Na sequencia, deve-se vincular cada item do arquivo XML a um item do movimento relacionado selecionado.

Para salvar o movimento, o sistema irá executar todas as consistências pertinentes à inclusão de movimentos de devolução, quando gerados através de copia por referência.

**8.3**  **Recebimento de CT-e**

A inclusão de movimentos de entrada referente a aquisição de serviços de transporte pode ser realizada, utilizando um arquivo XML de NF-e das seguintes maneiras:

* Através da Inclusão Direta de um movimento, ou seja, que não tem pedido;
* Através do Recebimeto de Pedido(s);

**8.4**  **Parametrizações – Tipo Movimento – Recebimento de CT-e**

Acessar:

*MDI.Net:* Ambiente | Parâmetros Gestão de Estoque, Compras e Faturamento | Aquisição Serviços | Tipo de Movimento

* **Etapa: TOTVS Colaboração**

Integração Neogrid: Informar o tipo de documento que o tipo de movimento em questão irá tratar.

Opções válidas:

* Não Utiliza
* Envio NF-e / NFS-e
* Envio CT-e
* Recebimento NF-e
* **Recebimento CT-e**

**Atenção**: Parametrização alterada à partir da versão 11.52.56. Em versões anteriores, essa opção era indicada na Etapa |Outros Dados|.

Produto/Serviço Default (Recebimento CT-e): Parâmetro específico para o Recebimento de CT-e. Informa um default de código do produto/serviço para o recebimento de CT-e, visto que no XML não possui código do serviço, somente valor.

Busca PIS/COFINS em: Parâmetro específico para o Recebimento de NF-e. Sem valor para os demais processos do TOTVS Colaboração.

* **Etapa Fis – Tributação - Item**

O tributo ICMS, único tributo do XML de CT-e, deve ser parametrizado por ITEM DE MOVIMENTO.

Para esse tributo serão levados para a tributação do item de movimento: os valores de base de cálculo, alíquota e o valor do imposto, quando informados no XML.

**Observações**:

* É obrigatório que os tipos de movimentos utilizados para inclusão de CT-e de entrada tenham parametrizado o tributo ICMS mesmo que a empresa não tenha crédito desses impostos na entrada. Essa parametrização é necessária devido ao arquivo XML conter informações sobre esse tributo. A correta escrituração dos movimentos estará vinculada ao código de CFOP informado no movimento de entrada.

* Quando os valores dos tributos forem carregados para o movimento conforme as informações do arquivo XML, o sistema irá considerar que a tributação foi editada, deixando esta informação registrada na grid de tributação. Importante citar que uma vez carregado os tributos para o movimento, o sistema não irá realizar recalculo dos valores dos tributos se o código da natureza de operação for alterado.

* Sugerimos também verificar o tamanho do *Número do Movimento*, pois o tamanho definido para a CT-e é de até 9 dígitos, isto, para que seja possível carregar para o movimento o número que consta no arquivo XML da CT-e sem inconsistência.

* Sugerimos também verificar o tamanho do *Número do Documento Financeiro* *e do Documento Contábil*, que deverá ser alterado, tendo seu tamanho aumentado proporcionalmente ao tamanho do número do movimento.

**8.5**  **Inclusão de Movimento de Entrada Serviço de Tranporte**

**a)****Inclusão Direta – sem Pedido de Compra de Serviço**

Na visão de movimento, clicar no ícone ‘*Inclusão de Movimento com Arquivo XML*’.

Será aberto um wizard de ‘*Tradução de arquivo XML*’.

Neste wizard deve-se selecionar o arquivo XML que será utilizado para incluir o movimento. Serão apresentados somente os arquivos XML com status de ‘Válido’, cadastrados na filial selecionada no filtro de movimento cujo Tipo de XML corresponda ao Tipo de Documento TC parametrizado no Tipo de Movimento.

Os dados do arquivo XML serão carregados na visão.

O sistema irá carregar o Serviço/Produto Default (Recebimento CT-e) informado nos parâmetros de Integração TOTVS Colaboração. O mesmo poderá ser alterado de acordo com as necessidades do cliente.

Ao finalizar o wizard, será aberta a edição do movimento. O mesmo terá as informações contidas no XML traduzidas para o ERP. As informações gerenciais do movimento, como local de estoque, tabelas de classificação, condição de pagamento, dentre outras, deverão ser informadas pelo usuário, se o tipo de movimento não possuir default.

**Observação**: O código da natureza de operação da entrada será preenchido automaticamente, se o tipo de movimento tratar regras de seleção automática. Caso contrário, o usuário deverá informar a natureza de operação manualmente. O tratamento é o mesmo adotado para a inclusão de movimento, quando não se utiliza um arquivo XML.

A correta escrituração dos movimentos, bem como a geração do SPED  estará vinculada ao código de CFOP informado no movimento de entrada.

**b)** **Recebimento de Pedido(s) de Compra de Serviço**

Na visão de Pedido(s) de Compra, selecionar os movimentos que serão recebidos e clicar no ícone ‘*Receber*’ (processo padrão do sistema, quando se deseja receber um movimento).

Será aberto o wizard de ‘*Recebimento / Faturamento de Movimento*’. Selecionar as opções conforme necessidades do processo.

Na sequencia, estando o movimento destino parametrizado para integração com o TOTVS Colaboração/Neogrid, o sistema abrirá o wizard de ‘*Tradução do arquivo XML*’.

Neste wizard deve-se selecionar o arquivo XML que será utilizado para incluir o movimento. Serão apresentados somente os arquivos XML com status de ‘Válido’, cadastrados na filial selecionada no filtro de movimento cujo Tipo de XML corresponda ao Tipo de Documento TC parametrizado no Tipo de Movimento.

Os dados do arquivo XML serão carregados na visão.

Caso o Pedido tenha somente um item, o sistema irá vincular o item do pedido ao serviço de transporte do XML. Considerando o item informado no pedido para o registro do CT-e.

Como o XML de CT-e possui somente o valor para um serviço de transporte, o movimento de entrada de CT-e não poderá ser vinculado a mais de um item.

**Observação**: O código da natureza de operação da entrada será copiado do pedido de compra relacionado, caso o mesmo tenha essa informação. Caso contrário, o sistema irá aplicar a regra de seleção parametrizada no tipo de movimento que está sendo utilizado para registrar a nota de entrada.

A correta escrituração dos movimentos, bem como a geração do SPED  estará vinculada ao código de CFOP informado no movimento de entrada.

 

 **9. Emissão NF-e, CT-e, NFS-e e Carta de Correção**

A emissão de NF-e, CT-e e NFS-e pelo TOTVS Colaboração contempla os seguintes processos:

* Envio
* Consulta
* Inutilização
* Evento: Carta de Correção

**9.1**  **Parametrizações – Tipo Movimento – Emissão**

Acessar:

*MDI.Net:* Ambiente | Parâmetros Gestão de Estoque, Compras e Faturamento | Aquisição Serviços | Tipo de Movimento

* **Etapa: TOTVS Colaboração**

Integração Neogrid: Informar o tipo de documento que o tipo de movimento em questão irá tratar.

Opções válidas:

* Não Utiliza
* **Envio NF-e / NFS-e**
* **Envio CT-e**
* Recebimento NF-e
* Recebimento CT-e

**Atenção**: Parametrização alterada à partir da versão 11.52.56. Em versões anteriores, essa opção era indicada na Etapa |Outros Dados|.

Produto/Serviço Default (Recebimento CT-e): Parâmetro específico para o Recebimento de CT-e. Sem valor para os demais processos do TOTVS Colaboração.

Busca PIS/COFINS em: Parâmetro específico para o Recebimento de NF-e. Sem valor para os demais processos do TOTVS Colaboração.

* **Etapa Fis – NF-e**

Configurar etapa conforme documentação específica de cada processo, conforme links publicados abaixo:

**Emissão NF-e – acesse:** <http://tdn.totvs.com/pages/viewpage.action?pageId=45220587>

**Emissão de NS-e – acesse:** <http://tdn.totvs.com/pages/viewpage.action?pageId=45220646>

**Emissão de CT-e – acesse:** <http://tdn.totvs.com/pages/editpage.action?pageId=4814118>

**Geração de Carta de Correção – acesse:** <http://tdn.totvs.com/pages/viewpage.action?pageId=42043694>

Para maiores informações:

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015

---

[[1]](file:///C:/Documents%20and%20Settings/felipe.patricio/Configura%C3%A7%C3%B5es%20locais/Temporary%20Internet%20Files/Content.Outlook/90VTFXUY/TOTVS%20Colabora%C3%A7%C3%A3o%20x%20ERP%20RM.docx#_ftnref1)Para agendamento de Job, verifique orientações no Help Desk de Framework ou consulte o link: <http://tdn.totvs.com/pages/editpage.action?pageId=59441405>
