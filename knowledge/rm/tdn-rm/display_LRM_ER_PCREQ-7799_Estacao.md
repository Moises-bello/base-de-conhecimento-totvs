---
content_hash: 30f925d50663f1766413b63ea1a5fe732a4b0850fde4a64c72a689c973bd1068
fetched_at: '2026-06-29T00:06:11.432510+00:00'
page_id: '203768868'
product: rm
source: tdn-rm
title: ER_PCREQ-7799_Estacao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7799_Estacao
version: 17
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Faturamento |
| **Segmento Executor** | TOTVS Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-7799 | **Subtarefa1** | PDR\_CP\_MOV008-26 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Implementação do adapter de integração via Mensagem Única TOTVS do cadastro de Estação PDV, viabilizando assim o CRUD completo do cadastro por envio de mensagem de integração.

 

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de envio de Mensagens Únicas TOTVS para integração do cadastro de Estação (Ponto de Venda), estando o adapter de recebimento desta mesma mensagem fora do escopo do requisito, ou seja , os pontos de vendas (Estação-PDV) serão cadastrado somente no BackOffice RM.

A análise e o desenvolvimento do adapter será efetuado considerando a integração com o PDV Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Ponto de Venda | Inclusão/Alteração/Exclusão | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \  Estoque, Compras e Faturamento \ Mais \ Tabelas Auxiliares \ Ponto de Venda | - |

**Tabelas Utilizadas**

* TGRPPONTOVENDA – Grupamento de Pontos de Venda
* TPONTOVENDA – Ponto de Venda

 

**Entidades de Integração** 

* DataServer envolvido
  + MovGrpPontoVendaData
* Transformação
  + Id: LISTOFSTATIONSALEPOINT
  + Versão: 1.000
* SourceCode (Evento)
  + GUID: f1b94c0a-3982-455a-a9d3-d4c26bc775b2
  + Nome: StationSalesPoint\_1.000
* Fórmula Visual
  + 03\_PDV\_PontoVenda.TotvsWF

## Regras de Integridade

* O cadastro deve ser feito no BackOffice RM e sincronizado para o PROTHEUS via Integração TOTVS Mensagem Única.
* O código do ponto de venda no RM (TPONTOVENDA.PONTOVENDA) deve ser igual ao código do ECF no Protheus (SLG.LG\_PDV). É obrigatório incluir um código do ponto de venda no RM com o valor **001**.
* No RM os cadastros de Pontos de Venda (PDV) são consolidados pelo cadastro de Grupo de Venda, sendo enviado ao Protheus na Mensagem Única a lista com todos os Pontos de Venda do grupo.
  + O tratamento de evento será efetuado através do campo "Event" interno ao item da mensagem, visto que em uma mesma mensagem de evento 'Upsert' podem existir itens com eventos 'Delete'. Ex.: Foi incluído um PDV e outro foi excluído.
* Serão enviados para o PROTHEUS somente os registros que são do Tipo 'Impressora Fiscal' (TPONTOVENDA.TIPO=1).
  + Esta validação é efetuada na Fórmula Visual e no XSLT de saída.
* Caso o campo TIPO seja alterado de 'Impressora Fiscal' para qualquer outro será enviada a exclusão do respectivo Ponto de Venda ao Protheus.

* Caso o Código do Ponto de Venda seja alterado será enviada ao Protheus a exclusão do registro referente ao código anterior e a inclusão de novo Ponto de Venda com o novo código.
* **CRO - Default**
  + O Contador de Reinicio de Operação é trafegado na mensagem única, pois será utilizado na integração de inclusão do Cupom Fiscal. Para obter maiores informações sobre o a integração de Cupom Fiscal .

**Compartilhamento de registros por Coligada e Filial**

Visto que o registo no BackOffice RM não considera a Filial como parte da Chave e existe a restrição na Mensagem Única TOTVS para envio do 'CompanyInternalId' completo (Coligada + Filial), é necessário que o sistema destinatário possua este cadastro exclusivo por Coligada e compartilhado por Filial.

Em resumo, o sistema de destino não deve considerar a informação de Filial enviada, pois caso no BackOffice RM este campo esteja nulo será enviada a Filial do contexto de integração, que e a primeira filial da empresa disponível na tabela De-Para.

Em relação ao Protheus deve seguir o seguinte compartilhamento:

* + - Empresa:  Exclusivo
    - Unidade:   Deve ser equivalente à entidade relacionada no De-Para de integração (Empresa ou filial)
    - Filial:        Compartilhado

## Restrições e Ponto de Atenção

* Os campos enviados do RM para o PROTHEUS não poderão ser alterados no PDV.
* Conforme uso normal do FrontLoja, o usuário deverá acessar o cadastro de Estação no mesmo para efetuar as configurações referentes aos devices agregados, como Impressora Fisca, PinPad, Leitor de Código de Barras e demais.

## Mapeamento dos campos

* **Mensagem LisOfStationSalePoint 1.000**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da empresa. | TPONTOVENDA | CODCOLIGADA | Código da Coligada é obtido a partir do De-Para de Filial. |
| **BranchId** | Código da filial | TPONTOVENDA | CODFILIAL |
| **CompanyInternalId** | InternalId da chave completa de empresa do produto | TPONTOVENDA | CODCOLIGADA|CODFILIAL |
| **Code** | Código Ponto de Venda | TPONTOVENDA | PONTOVENDA |  |
| **InternalId** | InternalId de Integração | TPONTOVENDA | CODCOLIGADA|PONTOVENDA |  |
| **Series** | Série | TPONTOVENDA | SERIE |  |
| **SeriesInternalId** | Id de integração da Série | TPONTOVENDA | CODCOLIGADA|SERIE |  |
| **Description** | Descrição | TPONTOVENDA | DESCRICAO |  |
| **WarehouseInternalId** | Id de integração do Local de Estoque(Armazem) | TPONTOVENDA | CODLOC |  |
| **WarehouseCode** | Código do Local de Estoque | TPONTOVENDA | CODCOLIGADA|CODFILIAL|CODLOC |  |
| **Active** | Estação Ativa? | TPONTOVENDA | INATIVO | TPONTOVENDA.INATIVO = 0: Ativo  TPONTOVENDA.INATIVO = 1: Inativo |
| **Event** | Evento do item (Ponto de Venda) |  | EVENT | Campo adicionado no tratamento da Fórmula Visual para controle de evento por Ponto de Venda do Grupo. |
| **CRO** | Contador Reinício de Operação | TPONTOVENDA | CRO |  |

* Somente os campos marcados em negrito são tratados no Adapter, sendo os demais não enviados na mensagem.

## Fluxo do Processo

A integração de Pontos de Venda é efetuada em duas etapas, iniciada no BackOffice RM onde todos os dados de integração fiscal devem ser efetuadas e finalizada com a completa configuração dos equipamentos agregados ao FrontLoja (Pinpad, leitores, impressora fiscal, etc).

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
