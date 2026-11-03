---
content_hash: 59204a0d017ec798b47b069be7ed62f0ee364e35a57d3576f4896d9679107a58
fetched_at: '2026-06-29T00:06:01.136646+00:00'
page_id: '198936430'
product: rm
source: tdn-rm
title: TSW546_ER_Parametrizacao_Movimento_NFC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/TSW546_ER_Parametrizacao_Movimento_NFC-e
version: 6
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Compras Estoque e Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não se aplica |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Parametrização do Tipo de Movimento a ser utilizado e da Filial a usar a integração para emissão da Nota Fiscal de Consumidor Eletrônica (NFC-e).

## Definição da Regra de Negócio

*<Regra de negócio é o que define a forma de fazer o negócio, o processo definido e/ou as regras que devem ser contempladas. Devem ser descritas restrições, validações, condições e exceções do processo. Caso necessário, incluir neste capítulo também regras de integridade que devem ser observadas no momento do desenvolvimento>.*

# Emissão da NFC-e

## Parametrização do Tipo de Movimento

**Importante:** A identificação do consumidor não é obrigatória na emissão da NFC-e. Sendo assim, deve-se observar as seguintes regras:

* **Com identificação:** registrar consumidor no  cadastro de Cliente/Fornecedor para seleção no movimento;
* **Sem identificação:** utilizar registro de Cliente/Fornecedor fictício (Exemplo: “Cliente de Balcão”) para selecionar no movimento já que o campo é de preenchimento obrigatório.

 

 A configuração deve ser realizada através do módulo BackOffice >> “Gestão de Estoque, Compras e Faturamento” >> Ambiente >> Parâmetros, item “Gestão de Estoque, Compras e Faturamento”, acessar o processo referente ao movimento desejado (Vendas ou Outras Movimentações), selecionar o tipo de movimento e solicitar para parametrizar.

 Abaixo estão relacionados os principais processos diretamente ligados à NFC-e:

* **Etapa “Mov – Emitente/Destinatário”:** Se a integração não usar a identificação do consumidor deve-se informar o “Cliente/Fornecedor Destino Default” do “Cliente de Balcão”;
* **Etapa “Fis – Escrituração 1/2”:** Informe o tipo de documento escrituração modelo “65” (NFC-e);
* **Etapa “Fis - NF-e”:** No grupo de dados para emissão de NFC-e informe:
  + **Tipo da Integração:** “Não integrado”, “Integrado NFC-e”.
  + **Formato da Impressão:** “DANFE NFC-e em Mensagem Eletrônica”, “DANFE NFC-e”.
  + **Relatório .Net Default:** Report .Net da NFC-e.

 

## Emissão do Movimento

Através do módulo BackOffice >> “Gestão de Estoque, Compras e Faturamento” >> Vendas >> Faturamento, “SPED NF-e (Estadual)”, selecionar o movimento devidamente parametrizado para emissão da NFC-e.

A integração deverá consistir se o tipo de documento é o “65” para liberação dos campos dos dados da NFC-e.

Os campos para CPF/CNPJ/ID Estrangeiro e Nome deverão ficar disponíveis se a integração NFC-e estiver habilitada, caso contrário os campos deverão ficar indisponíveis. Por padrão será consistido o preenchimento dos campos e, caso estejam vazios, o consumidor será identificado pelo Cli/For selecionado no movimento.

 

**Observações:**

* O CPF/CNPJ será consistido no mesmo campo com a verificação da quantidade de caracteres sendo desprezados os caracteres especiais de máscara (TMov.CNPJCPFAdquirente);
* O “ID Estrangeiro” terá um campo próprio (TMov.DocEstrangeiroAdquirente) – a definição do nome do campo obedeceu a mesma regra da antiga rotina de Cupom Fiscal (tabela TCupomFiscal);
* O consumidor pode ser identificado apenas pelo campo de CPF/CNPJ ou ID Estrangeiro, sendo opcional o preenchimento do campo Nome (TMov.NomeAdquirente). Desta forma, na geração do XML somente suas respectivas tags serão preenchidas (sem informação de endereço);
* Para consumidor não identificado o valor máximo permitido é de R$10.000,00 (dez mil reais). Acima desse valor o consumidor obrigatoriamente deverá ser identificado;

 

# Envio da NFC-e

 

Através do módulo BackOffice >> “Gestão de Estoque, Compras e Faturamento” >> Vendas >> Faturamento >> “SPED NF-e (Estadual)”, selecione o filtro desejado e execute o processo “Enviar  NF-e\NFC-e”.

Para cada movimento selecionado será gerado o XML e registrado na tabela TNFeEstadual, conforme a modalidade em uso no momento (Normal, Contingência EPEC ou Contingência Offline). Se o envio obter sucesso o registro terá o status “Pendente” (default) e deverá ser executado o processo para consultar a autorização, caso contrário o registro terá o status “Inconsistente” e será informado ao usuário para correção do problema e retransmissão.

O reenvio da NFC-e será permitida para registros no status “Inconsistente” ou “Rejeitada”.

Se foi gerada NFC-e para o movimento ele não poderá ser alterado, exceto quando a NFC-e estiver com status “Rejeitada” ou “Inconsistente”.

 

**Importante:**

* Ao enviar NFC-e é necessário consistir se os campos de Código de Segurança do Contribuinte e seu respectivo ID estão preenchidos, pois os mesmos devem ser informados na alteração de parametrização do Ambiente NFC-e da Filial (homologação/produção);
* As NFC-es emitidas em contingência não serão enviadas para a SEFAZ. Os documentos deverão ser reenviados em um prazo de 24h (vinte e quatro horas) para obter a autorização e possibilitar ao consumidor a consulta da Chave de Acesso na base de dados da SEFAZ. Na impressão deverá constar a mensagem “EMITIDA EM CONTINGÊNCIA”;
* Na impressão de NFC-e emitido em ambiente de homologação é obrigatório constar na área de Mensagem Fiscal o termo “EMITIDA EM AMBIENTE DE HOMOLOGAÇÃO – SEM VALOR FISCAL”;
* Na impressão de NFC-e emitido sem identificação do consumidor deverá constar em seu respectivo quadro a expressão “CONSUMIDOR NÃO IDENTIFICADO”.

# Cancelamento da NFC-e

O cancelamento da NFC-e poderá ser realizada em um prazo de 30 (trinta) minutos após sua autorização.

 

# Inutilização da NFC-e

A inutilização da NFC-e segue os mesmos princípios da NF-e (processo de evento).

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [PAR.014 – Parametrização Tipo de Movimento] | [Alteração] | [Ambiente -> Parâmetros -> TOTVS Gestão de Estoque, Compras e Faturamento -> Tipo de Movimento] | - |
| [MOV.001 – Inclusão de Movimento] | [Envolvida] | [Vendas -> Faturamento] | - |
| [PAR.008 – Parametrização - Integrações] | [Envolvida] | [Ambiente -> Parâmetros -> TOTVS Gestão de Estoque, Compras e Faturamento -> Integrações -> Fiscal -> Dados Fiscais] | - |

***Tabelas Utilizadas***

* GCOLIGADA – Coligadas
* GFILIAL – Filiais
* TPAR – Parâmetros Gerais
* TPARFILIAL – Parâmetros por Filial
* TTMV – Tipos de Movimento
* TTMVEXT – Tipos de Movimento
* TMOV – Movimentos
* RRPTREPORT - Relatórios .NET

### Opcional

## Dicionário de Dados

**Arquivo ou Código do Script:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Novos Campos** **TPARFILIAL** | **Descrição / Conteúdo** | **Tipo** | **Tamanho** |
| VERSAOLAYOUTNFCE | Versão Lay-Out NFC-e | Varchar | 10 |
| AMBIENTENFCE | Ambiente de Envio NFC-e | Smallint |  |
| MODALIDADENFCE | Modalidade de Operação NFC-e | Smallint |  |
| URLQRCODENFCE | URL QRCode NFC-e | Varchar | 250 |
| CSCNFCE | Código Segurança Contribuinte | Varchar | 50 |
| IDCSCNFCE | ID do Código Segurança Contribuinte | Varchar | 20 |

|  |  |  |  |
| --- | --- | --- | --- |
| **Novos Campos** **TTMVEXT** | **Descrição / Conteúdo** | **Tipo** | **Tamanho** |
| NFCE | Integração NFC-e | Smallint |  |
| FORMATONFCE | Formato DANFE NFC-e | Smallint |  |
| CODCOLRELATNFCE | Código Coligada DANFE NFC-e | DCodColigada |  |
| IDRELATNFCE | Relatório Default DANFE NFC-e | Int |  |

 \* Inclusão de Foreign Key “FKTTMVEXT\_IDRELATNFCE” para a qual os campos CODCOLRELATNFCE e IDRELATNFCE são relacionados com a tabela RRPTREPORT e seus campos CODCOLIGADA e ID.

|  |  |  |  |
| --- | --- | --- | --- |
| **Novos Campos** **TMOV** | **Descrição / Conteúdo** | **Tipo** | **Tamanho** |
| CNPJCPFADQUIRENTE | CNPJ/CPF do Adquirente | Varchar | 20 |
| NOMEADQUIRENTE | Nome do Adquirente | Varchar | 60 |
| DOCESTRANGEIROADQUIRENTE | Doc. Estrangeiro do Adquirente | Varchar | 20 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
