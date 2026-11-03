---
content_hash: de715b554dc152300e4786a6091e0af752e347673e8ffe9fbe7a2a488e10e3d2
fetched_at: '2026-06-29T00:06:13.798354+00:00'
page_id: '208346579'
product: rm
source: tdn-rm
title: ER_PCREQ-7807_Local de Estoque - Warehouse
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7807_Local+de+Estoque+-+Warehouse
version: 11
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
| **Requisito1** | PCREQ-7807 | **Subtarefa1** | PDR\_CP\_MOV008-40 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Implementação do adapter de integração via Mensagem Única TOTVS do cadastro de Local de Estoque com o PDV Protheus, viabilizando assim o CRUD completo do cadastro por envio de mensagem de integração.

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de envio de Mensagens Únicas TOTVS para integração do cadastro de Local de Estoque (Warehouse), estando o adapter de recebimento desta mesma mensagem fora do escopo do requisito.

A análise e o desenvolvimento do adapter será efetuado considerando a integração com o PDV Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Locais de Estoque | Inclusão/Alteração/Exclusão | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Estoque, Compras e Faturamento \ Locais de Estoque | - |

As inclusões, alterações e exclusões de Locais de Estoque são feitos através da Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao PDV Protheus. Os dados de locais de estoque que serão sincronizados pela mensagem única são :

* **Pasta Identificação:** Filial, Estoque, Inativo, Descrição

A integração deste cadastro é necessário, pois será utilizado como filtro na consulta de saldo de estoque.

### Regras de Integridade

* O cadastro deve ser feito no BackOffice RM e sincronizado para o PROTHEUS via Integração TOTVS Mensagem Única.
* Serão enviados para o PROTHEUS somente os Locais de Estoque da Filial que está integrada.
* O campo Código do Local de Estoque no RM possui tamanho de 15 caracteres e no PROTHEUS o campo Código possui tamanho padrão de 2 caracteres extensível até 6 caracteres (até a presente data). Sendo assim será realizado o seguinte tratamento para o tamanho do campo Código:
  + Se o campo Código no PROTHEUS for configurado como auto-incremento, ele irá ignorar o código enviado pelo RM, gerando na inclusão do local de estoque o código com auto-incremento.
  + Se o campo Código no PROTHEUS não for configurado como auto-incremento, caso seja cadastrado um Local de Estoque com código maior do que o permitido no PROTHEUS será exibida mensagem de consistência similar a: "*Tamanho do campo Código maior que o permitido: Enviado X Permitido Y*."

**Compartilhamento de registros por Coligada e Filial**

Visto que o registo no BackOffice RM considera a Filial como parte da Chave e existe a restrição na Mensagem Única TOTVS para envio do 'CompanyInternalId' completo (Coligada + Filial), é necessário que o sistema destinatário possua este cadastro exclusivo por Coligada e exclusivo por Filial.

Em relação ao Protheus deve seguir o seguinte compartilhamento:

* + Empresa:  Exclusivo
  + Unidade:   Exclusivo.
  + Filial:        Exclusivo.

**Fórmula Visual**

Para sincronizar o cadastro será necessário importar a fórmula visual que encontra-se disponível na pasta “Fórmulas Visuais”, interna à pasta “ObjetosGerencias” no ambiente instalado do sistema (“../CorporeRM/ObjetosGerencias/Fórmulas Visuais”). Ao importar a fórmula visual deverá ser marcado para cada fórmula o parâmetro “Importar Gatilho” na rotina de Importação de Fórmula Visual.

Visando facilitar a sincronização das bases de dados RM e PDV foi desenvolvida uma atividade de fórmula visual que se responsabiliza por, a partir de alguns parâmetros, obter os dados necessários e solicitar o envio da Mensagem Única TOTVS Warehouse\_1.000.

Basicamente é necessário informar a esta atividade somente a lista de chaves dos registros que se deseja integrar, qual a Mensagem Única a enviar e qual o objeto de negócio (DataServer) responsável por retornar as informações do registro. A partir destas informações a atividade se responsabiliza pela leitura, transformação e envio dos dados ao sistema de destino, oferecendo como retorno o Log de integração.

Todas as mensagens trafegadas também constarão no monitor da fila de integração, para posterior conferência.

**Tabelas Utilizadas**

* TLOC- Locais de Estoque

**Entidades de Integração**

* DataServer envolvido
  + EstLOCData
* Transformação
  + Id: Warehouse
  + Versão: 1.000
* Fluxo da mensagem
  + Saída
* Tipo de Envio:
  + Síncrono.
* Fórmula Visual
  + 05\_PDV\_LocalDeEstoque.TotvsWF
  + 05.Sincronização de Locais de Estoque.TotvsWF: utilizada para carga inicial

## Fluxo do Processo

## Mapeamento dos campos

* **Mensagem Warehouse 1.000**

| **Mensagem Padrão** | **Descrição** | **RM** | | |
| --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da empresa. | TLOC | CODCOLIGADA |  |
| **BranchId** | Código da filial | TLOC | CODFILIAL |  |
| **CompanyInternalId** | InternalId da chave completa de empresa | TLOC | CODCOLIGADA|CODFILIAL |  |
| **Code** | Código Local de Estoque | TLOC | CODLOC |  |
| **InternalId** | InternalId da Entidade | TLOC | CODCOLIGADA| CODFILIAL| CODLOC |  |
| **Description** | Descrição Local Estoque | TLOC | NOME |  |
| **Active** | Local Estoque Ativo? | TLOC | INATIVO | Inativo=0: Ativo Inativo=1: Inativo |
| Type | Tipo do Local de Estoque |  |  | Não utilizada na linha RM |
| IsFinalItem | Local de Estoque é de produto acabado? |  |  | Não utilizada na linha RM |
| IsQualityControl | Local de Estoque é de controle de qualidade? |  |  | Não utilizada na linha RM |
| IsProcess | Local de Estoque é de processo? |  |  | Não utilizada na linha RM |
| IsWaste | Local de Estoque é de rejeito? |  |  | Não utilizada na linha RM |

* Somente os campos marcados em negrito são tratados no Adapter, sendo os demais não enviados na mensagem.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
