---
content_hash: 13ed9ebc97b64b3a790f6745e4109d98ee4aaa9dff4262dc0cee78b1271df303
fetched_at: '2026-06-29T00:08:20.586431+00:00'
page_id: '268577638'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-162_ConversorEAI1_EAI2
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_FRW_FRW002-162_ConversorEAI1_EAI2
version: 17
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo: EAI** |  |
| **Segmento Executor** |  | | |
| **Projeto1** | Framework BH - 004 | **IRM1** |  |
| **Requisito1** | FRW\_FRW002-160 | **Subtarefa1** | FRW\_FRW002-162 |
| **Chamado2** |  | | |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

Efetuar a migração dos dados cadastrados nas tabelas de integração do EAI 1.0 para as tabelas do EAI 2.0.

### Definições importantes

* É importante que um backup da base seja feito  antes da execução desse processo;

# Modelo de solução

Abaixo será descrito as regras de negócio do conversor.

## 1) - Localização

O assistente de conversor deve ser chamado do caminho abaixo:

*Integração/Mensagem Única/Conversor EAI 2.0*

Obs: Esse menu deve ser habilitado para o usuário no sistema de segurança do RM.

## 2) - Opções do assistente de conversão

## a) - Tipo de execução

 

Converter para o EAI 2.0:

Efetuará a migração dos dados do EAI 1.0 para as tabelas do EAI 2.0.

Porém, o EAI 2.0 ficará travado até a execução desse processo com a opção "Liberar utilização do EAI 2.0".

Durante esse período, tanto o EAI 1.0 quanto o EAI 2.0 ficarão fora de operação.

Voltar para o EAI 1.0

 Exclui todas as linhas geradas nas tabelas do EAI 2.0 e volta para o EAI 1.0.

Liberar utilização do EAI 2.0

Libera a utilização do EAI 2.0. A partir desse momento todas as mensagens recebidas e enviadas serão processadas pelo EI 2.0.

## b) - Mensagens de conversão

Algumas mensagens aparecerão para o usuário nessa página do assistente.

O usuário deverá selecionar a opção  "Continuar Conversão" para prosseguir com o processo.

## c) - Integrações disponíveis

Todas as integrações, com exceção das integrações inativas,  (cadastradas na tabela HCIntegracao) aparecerão na grid.

O usuário deverá selecionar uma ou várias integrações a serem convertidas para o novo modelo de EAI.

```
Opção "Atualiza informação de "Sourceapplication" dos aplicativos chamando a mensage Whois":
```

      Com essa opção marcada, o processo enviará uma mensagem de Whois para cada endereço de webServices cadastrado nas integrações selecionadas.

      O processo fará uma leitura na resposta dessa mensagem e buscará a informação de "SourceApplication".

      O valor desse atributo será usado para preencher o campo "SourceApplication" da tabela GEAIApp.

**Caso essa opção não seja marcada no processo de conversão, o valor para o campo "SOURCEAPPLICATION", disponível no cadastro de aplicativos, deve ser alterado manualmente após a conversão.**

Opção "Importa mensagens assíncronas":

   Com essa opção marcada, todas as mensagens assíncronas, que não foram processadas com sucesso, com menos de 5 (cinco) tentativas de processamento,

   serão migradas para a nova tabela de mensagens;

Opção "Data Início das mensagens":

Somente as mensagens assíncronas com data de inclusão maior que o informado serão migradas.

## 3) - Mapeamento de informações (EAI 1.0 / 2.0)

# Aplicativos

|  |  |  |
| --- | --- | --- |
| **Tabela/Coluna EAI 1.0** | **Tabela/Coluna EAI 2.0** | **Regras** |
|  | GEAIAPP.ID | auto incremento |
|  | GEAIAPP.SOURCEAPPLICATION | O valor de SourceApplication será recuperado pela busca do atributo "SourceApplication" da resposta da mensagem de Whois.  A mensagem de whois será enviada para cada endereço de webServices cadastrado nas integrações a serem convertidas. |
| HCINTEGRACAO.SISTEMAINTEGRADO | GEAIAPP.CODDPRODUTO |  |
|  | GEAIAPP.NOME | Concatenação dos campos HCIntegracao.SISTEMAINTEGRADO + "-" + SOURCEAPPLICATION  O valor de SourceApplication será recuperado pela busca do atributo "SourceApplication" da resposta da mensagem de Whois. |
|  | GEAIAPP.DESCRICAO | Concatenação dos campos HCIntegracao.SISTEMAINTEGRADO + "-" + SOURCEAPPLICATION  O valor de SourceApplication será recuperado pela busca do atributo "SourceApplication" da resposta da mensagem de Whois |
| HCINTEGRACAO.WSURL | GEAIAPP.URLWSDLEXTERNO |  |
| HCINTEGRACAO.WSUSUARIO | GEAIAPP.USRWSDLEXTERNO |  |
| HCINTEGRACAO.WSSENHA | GEAIAPP.PASSWSDLEXTERNO |  |
| HCINTEGRACAO.RMCOLIGADAONPROTHEUS | GEAIAPP.RMCOLIGADAONPROTHEUS |  |

**Não poderá existir mais de um aplicativo com o mesmo "SourceApplication" / "CodProduto".**

**A partir de agora o RM poderá integrar com mais de um aplicativo "Protheus" desde que os mesmos possuem SourceApplications diferentes.**

# Transação

|  |  |  |
| --- | --- | --- |
| **Tabela/Coluna EAI 1.0** | **Tabela/Coluna EAI 2.0** | **Regras** |
|  | GEAITRANSACAO.ID | Auto incremento |
| HCTRANSFORMACAO.TRANSACTIONID | GEAITRANSACAO.TRANSACAO |  |
| HCTRANSFORMACAO.DESCRICAO | GEAITRANSACAO.DESCRICAO |  |
|  | GEAITRANSACAO.MODOSUPORTADO | 1 - Envio  **HCTRANSFORMACAO.XSLTSAIDA diferente de vazio**  **HCTRANSFORMACAO.XSLTENTREDA vazio**  2 - Recebimento  **HCTRANSFORMACAO.XSLTSAIDA vazio**  **HCTRANSFORMACAO.XSLTENTREDA **diferente de** vazio**  3 - Ambos  **HCTRANSFORMACAO.XSLTSAIDA ****diferente de**** vazio**  **HCTRANSFORMACAO.XSLTENTREDA **diferente de** vazio** |
|  | GEAITRANSACAO.SYNCASYNCENVIO | Será gravado o valor "0 - Sincrono".  No EAI 1.0 RM não deve existir mensagens assincronas, pois o mesmo não foi projetadopara enviar  /receber esse tipo de mensagem. Somente mensagens com características de "falso assíncrono" que será detalhado nesse mesmo documento. |
|  | GEAITRANSACAO.PERMITERECASYNC | Será gravado o valor "0 - Não permite"  O EAI 1.0 não está preparado para envio/recebimento assíncrono |
|  | GEAITRANSACAO.EXECVIAJOB | Esse campo definirá se as mensagens de envio (nas transações em questão) serão executadas via Job ou imediatamente na chamada do método.  Esse campo foi criado para resolver a situação do "falso assíncrono". Algumas mensagens são enviadas para o EAI 1.0 com o tipo de entrega assíncrono.  Porém, essas mensagens , no momento de execução pelo Job, são enviadas para outro aplicativo com o tipo entrega "sincrono".  Abaixo serão listadas essas transações com esse comportamento:  DEVICEEQUIPMENTAPPOINTMENT  DEVICETASKSAPPOINTMENT  DEVICETRANSPORTCYCLEAPPOINTMENT  LABORDEVICETASKSAPPOINTMENT |

 

# Transação / Versão

 

 

 

|  |  |  |
| --- | --- | --- |
| **Tabela/Coluna EAI 1.0** | **Tabela/Coluna EAI 2.0** | **Regras** |
| HCMAPAINTEGRACAO.VERSAOMENSAGEM | GEAITRANSACAOVERSAO.VERSAO |  |
| HCMAPAINTEGRACAO.ENTIDADE | GEAITRANSACAOVERSAO.IDTRANSACAO | O campo identificação da transação será buscado da tabela GEAITransacao. |
|  |  |  |

 

# Transação / Aplicativo (rotas)

|  |  |  |
| --- | --- | --- |
| **Tabela/Coluna EAI 1.0** | **Tabela/Coluna EAI 2.0** | **Regras** |
| HCMAPAINTEGRACAO.IDINTEGRACAO  HCINTEGRACAO.SISTEMAINTEGRADO | GEAITRANSACAOAPP.IDAPP | O identificador do App será buscado da tabela GEAIApp. |
| HCMAPAINTEGRACAO.ENTIDADE | GEAITRANSACAOAPP.IDTRANSACAO | O campo identificação da transação será buscado da tabela GEAITransacao. |
| HCMAPAINTEGRACAO.VERSAOMENSAGEM | GEAITRANSACAOAPP.IDTRANSACAO |  |
|  | GEAITRANSACAOAPP.IDSOURCECODE | Identificador do código fonte (GSourceCode). |
|  | GEAITRANSACAOAPP.INCLUIMENSAGEMORIGINAL | Será gravado o valor 1. Por default, a mensagem original sempre será incluída na mensagem de resposta. |
|  | GEAITRANSACAOAPP.MODOHABILITADO | O valor será copiado da transação (GEAITRANSACAO.MODOSUPORTADO) |
|  |  |  |

Não será permitido o mapeamento entre um aplicativo e uma transação em versões diferentes.

Ex: A transação "COSTCENTER" poderá ser mapeada para o aplicativo "Protheus/Enviromment" somente na versão 1.000.

Os códigos fontes cadastrados na tabela GSourceCode e mapeados na tabela "HCMapaTransacao.Extensions" não serão migrados para tabela GEAITransacaoApp.IdSourceCode.

No EAI 2.0 esse campo será usado exclusivamente para armazenar códigos customizados feitos pelo cliente/customização.

**Ex: Transação mapeada para mais de um um aplicativo:**

O RM ao enviar uma mensagem dessa transação, a mesma poderá ser enviada somente em caso assíncrono.

O RM ao receber uma mensagem, os atributos "SourceApplication" e "ProductCode" do xml TotvsMessage serão recuperados e usados para localizar o aplicativo correto.

# Pacote de instalação

 

|  |  |  |
| --- | --- | --- |
| **Tabela/Coluna EAI 1.0** | **Tabela/Coluna EAI 2.0** | **Regras** |
| HCINTEGRACAO.NOMEINTEGRACAO | GEAIPACOTEINSTALADO.NOMEPACOTE |  |
| HCINTEGRACAO.NOMEREDUZIDO | GEAIPACOTEINSTALADO.NOMEREDUZIDO |  |
|  | GEAIPACOTEINSTALADO.ID | Novo Guid |
| HCINTEGRACAO.SISTEMAINTEGRADO | GEAIPACOTEINSTALADO.APPID | O valor do campo "SistemaIntegrado" será usado para buscar o AppId da tabela GEAIApp. |
|  |  |  |

## 4) - Atualização das informações de DE/PARA

* A chave primária da tabela "HCINTEGRACAOID" foi removida;
* Foi criada nessa tabela a coluna "APPID" para armazenar o identificador do aplicativo responsável pela inclusão/atualização do De/Para;
  + Ex: O centro de custo do RM 001, no protheus/Produção  possuirá o externalId 1|001 e no Protheus/Homologação o externalId 0007.
* A coluna "SistemaIntegrado" dessa tabela  não será mais usada. A mesma não será removida para questões de histórico.
* A coluna AppId será atualizada de acordo com o campo "SistemaIntegrado".

## 5) - Migração das mensagens assíncronas

* Todas as mensagens assíncronas, que não possuem execução com sucesso e com menso de 5 tentativas de execução serão migradas para a nova tabela de mensagens;
* Para cada uma dessas mensagens migradas, será criado um job responsável em executar essa mensagem em questão;
* Mensagens de envio "assíncronas" serão tratadas como "falso assíncrono"  
  Essas serão processas pelo Job  (da mesma forma que uma mensagem assíncrona) porém serão enviadas para o aplicativo destino como uma mensagem síncrona;
* Sentença de seleção das mensagens:

  = :datainicio
  and HCFILAMENSAGEM.STATUSPROCESSAMENTO = 0
  ORDER BY HCFILAMENSAGEM.DATAINCLUSAO]]>

###
