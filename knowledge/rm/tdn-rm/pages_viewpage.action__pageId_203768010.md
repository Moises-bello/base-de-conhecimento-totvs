---
content_hash: 0844634416ee0276c5b5470ce64dd44ac7bc75ad1b9978ed41d12f34ff4a2c9c
fetched_at: '2026-06-29T00:06:11.336200+00:00'
page_id: '203768010'
product: rm
source: tdn-rm
title: ER_PCREQ-7798_Integração_Código de Barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203768010
version: 6
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Estoque |
| **Segmento Executor** | TOTVS Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-7798 | **Subtarefa1** | PDR\_CP\_MOV008-18 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

 Implementação do adapter de integração via Mensagem Única TOTVS do cadastro de Código de Barras com o PDV, viabilizando assim o CRUD completo do cadastro por envio de mensagem de integração.

 

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de envio de Mensagens Únicas TOTVS para integração do cadastro de Código de Barras, estando o adapter de recebimento desta mesma mensagem fora do escopo do requisito.

A análise e o desenvolvimento do adapter será efetuado considerando a integração com o PDV Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Código de Barras | Inclusão/Alteração/Exclusão | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Estoque, Compras e Faturamento \ Produto \ Código de Barras | - |

As inclusões, alterações e exclusões de Código de Barras são feitos através da Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao PDV Protheus. Os dados de Código de Barras que serão sincronizados pela mensagem única são cadastrados na pasta **Código de Barras** no cadastro de Produto.

Durante a alteração do Código de barra, caso o mesmo seja inativado ele será enviado para o PDV. O campo inativo não é considerado na integração deste cadastro, pois o código de barras não é utilizado como FK no retorno do Cupom. Ao informar o código de barras no cupom é enviado como FK o identificador do produto relacionado a este código de barras.

Para enviar o cadastro de Código de Barras os seguinte itens abaixo devem ser considerados:

* No cadastro de Transformação da mensagem ITEM o **Xslt Saída** deve considerar as informações de Códigos de barra. Este Xslt de saída será detalhado no tópico Mapeamento de Campos abaixo.
* As informações do envio da tag **ItemQuantity** será realizada através do **Extension**. Ao informar a **Unidade** no cadastro de Código de Barras será enviado para a tag o valor do **Fator de Conversão** utilizado por esta unidade de medida, com base na unidade de medida do produto.
* A mensagem de Códigos de Barra deve estar mapeada para a integração **1016 - BackOffice RM x PDV Protheus.**

Através do módulo **Integração \ Ferramentas \ Configurar** o usuário poderá executar o Configurador da Integração que irá criar toda a estrutura necessária para a integração deste cadastro com o PDV.

Para receber a mensagem o Protheus deve considerar:

* A configuração de compartilhamento de cadastros entre Empresas e Filiais para a entidade Códigos de Barras deve ser: **Exclusivo por Empresa**e**Compartilhado por Filial**.
* O tamanho padrão do Código de barras no Protheus é de 15 caracteres. Caso seja enviado um código de barras com mais de 15 caracteres, o adapter do Protheus irá apresentar mensagem de consistência na integração do cadastro. Para que isso não ocorra deve-se aumentar o tamanho deste campo no cadastro de Código de Barras do Protheus.

**Fórmula Visual**

Para sincronizar o cadastro será necessário importar a fórmula visual que encontra-se disponível na pasta “Sugeridos”, interna à pasta “\_ImpExp” no ambiente instalado do sistema (“../CorporeRM/\_ImpExp/Sugeridos”). Ao importar a fórmula visual deverá ser marcado para cada fórmula o parâmetro **Importar Gatilho** na rotina de **Importação de Fórmula Visual**.

**Carga Inicial**

Visando facilitar a sincronização das bases de dados RM e PDV foi desenvolvida uma atividade de fórmula visual que se responsabiliza por, a partir de alguns parâmetros, obter os dados necessários e solicitar o envio da Mensagem Única TOTVS.

Basicamente é necessário informar a esta atividade somente a lista de chaves dos registros que se deseja integrar, qual a Mensagem Única a enviar e qual o objeto de negócio (DataServer) responsável por retornar as informações do registro. A partir destas informações a atividade se responsabiliza pela leitura, transformação e envio dos dados ao sistema de destino, oferecendo como retorno o Log de integração.

Por padrão a consulta seleciona para envio registros Ativos que ainda não foram enviados para o Protheus ou que estejam desatualizados no mesmo (data de último envio anterior a data da última modificação do registro).

Todas as mensagens trafegadas também constarão no monitor da fila de integração, para posterior conferência.

**Listagem de Fórmula Visual:**

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Rotina** | **Operação** | **Fórmula Visual** |
| **Cadastro** | ``` Código de Barras ``` | ``` Inclusão / Alteração / Exclusão ``` | ``` 03_PDV_Código de Barras.TotvsWF ``` |
| ``` Código de Barras ``` | ``` Carga inicial ``` | 03.Sincronização de Código de Barras.TotvsWF |

**Tabelas Utilizadas**

* TPRDCODIGO – Cadastro de Código Genérico de Produtos.
* TPRODUTO – Produtos Globais.
* TUND – Unidades.

 

**Entidades de Integração** 

* DataServer envolvido
  + EstPrdDataBR
* Transformação
  + Id: Item
  + Versão: 3.004
* Fluxo da mensagem
  + Saída
* Tipo de Envio:
  + Síncrono.
* Extension:
  + 27490bfc-3d18-4e49-9eeb-b94e483baf01

## Fluxo do Processo

###### Diagrama de Sequência

## Mapeamento dos Campos

Os dados de Código de barras serão sincronizados na mensagem única Item (Produto) através da tag **ListOfBarCode** os demais campos da mensagem Item podem ser visualizados na especificação de requisitos da mensagem Item. Estão listados abaixo somente os mapeamentos referentes à tag de Código de Barras

* **Mensagem Código de barras**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **ListOfBarCode \ ListOfBarCodeType \ BarCode** | | | | Lista de Código de Barras dentro da mensagem de Produto |
| **BarCodeType** | Códigos de Barra |  |  |  |
| **Code** | Código de Barras do Produto | TPRDCODIGO | CODIGO | Caso o campo código seja maior que o parametrizado no Protheus é apresentada mensagem de consistência. |
| **InternalId** | Internal id do código de barras | TPRDCODIGO | CODCOLIGADA|TIPO|CODIGO |  |
| **UnifOfMeasureInternalId** | Unidade do código de barras | TPRDCODIGO | CODUND |  |
| **ItemQuantity** | Quantidade do produto | TUND | FATORCONVERSAO | Será enviado o fator de conversão da unidade de medida informada para o código de barras.  Este campo será enviado somente quando existir a Unidade do Código de barras. |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
