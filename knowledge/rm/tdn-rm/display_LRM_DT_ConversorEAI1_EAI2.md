---
content_hash: 849b3fa4d50cc9c4d0fb2ab9ec5da32b24daec9ec8e9868c4bcbbd2106530434
fetched_at: '2026-06-29T00:08:20.671494+00:00'
page_id: '268582802'
product: rm
source: tdn-rm
title: DT_ConversorEAI1_EAI2
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_ConversorEAI1_EAI2
version: 30
---

# Índice:

---

.\*ndice:

# Características do Requisito

---

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *FRAMEWORK* |
| **Módulo:** | *EAI 2.0* |

**Descrição**  
     Efetuar a migração dos dados cadastrados nas tabelas de integração do EAI 1.0 para as tabelas do EAI 2.0.

**Definições importantes**  
     É importante que um backup da base seja feito antes da execução desse processo.

# Modelo de Solução

---

Abaixo será descrito as regras de negócio do conversor.

## **Localização**

false

O assistente de conversor deve ser chamado do caminho abaixo: ***Integração/Mensagem Única/Conversor EAI 2.0***

falseSegurança:

Esse menu somente poderá ser executado após a liberação de um script de segurança para habilitação de um parâmetro interno do EAI.

Esse script deve ser gerado pelas equipes de segmentos.

## Mensagens de conversão

false

Algumas mensagens aparecerão para o usuário nessa página do assistente. O usuário deverá selecionar a opção  "Continuar Conversão" para prosseguir com o processo.

## Integrações disponíveis

false

Todas as integrações, com exceção das integrações inativas, aparecerão na grid.

O usuário deverá selecionar uma ou várias integrações a serem convertidas para o novo modelo de EAI.

***Botão "Atualizar SourceApplication manualmente"***: Ao clicar nesse botão, aparecerá uma janela para o usuário informar o "Sistema Integrado" para ser pesquisado e o "SourceApplication" para ser atualizado dentre as integrações selecionadas.O preenchimento desse campos é obrigatório.

***Botão "Atualizar SourceApplication automaticamente"***: Ao clicar nesse botão, o processo enviará uma mensagem de Whois para cada endereço de webServices cadastrado nas integrações selecionadas. O processo fará uma leitura na resposta dessa mensagem e buscará a informação de "SourceApplication". O valor desse atributo será usado para preencher o campo "SourceApplication" da tabela GEAIApp.

***Opção "Importar fila de mensagens":*** Com essa opção marcada, todas as mensagens (síncronas e assíncronas) serão migradas para as novas tabelas de mensagens (GEAIMensagem / GEAIRotaMensagem / GEAIExecRotaMensagem);

***Opção "Data Início das mensagens":*** Somente as mensagens com data de inclusão maior ou igual que o informado serão migradas.

false

Caso o usuário selecione uma "data de início de mensagens" maior que um mês (diferente do default), o sistema verificará se a quantidade de mensagens a serem importadas será maior que 1000 mensagens.

Caso positivo, aparecerá uma mensagem de inconsistência.

false

Na grid de integrações a serem convertidas, o usuário poderá selecionar a opção de alteração de "SourceApplication". Para isso, basta clicar na imagem de um lápis. Essa alteração será por integração.

# Mapeamento de Informações (EAI 1.0 / 2.0)

---

## **Aplicativos**

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

false

Não poderá existir mais de um aplicativo com o mesmo "SourceApplication" / "CodProduto".  
A partir de agora o RM poderá integrar com mais de um aplicativo "Protheus" desde que os mesmos possuem SourceApplications diferentes.

## **Transação**

| Tabela/Coluna EAI 1.0 | Tabela/Coluna EAI 2.0 | Regras |
| --- | --- | --- |
|  | GEAITRANSACAO.ID | Auto incremento |
| HCTRANSFORMACAO.TRANSACTIONID | GEAITRANSACAO.TRANSACAO |  |
|  | GEAITRANSACAO.MODOSUPORTADO | 1 - Envio **HCTRANSFORMACAO.XSLTSAIDA diferente de vazio** **HCTRANSFORMACAO.XSLTENTREDA vazio**  2 - Recebimento **HCTRANSFORMACAO.XSLTSAIDA vazio** **HCTRANSFORMACAO.XSLTENTREDA diferente de vazio**  3 - Ambos **HCTRANSFORMACAO.XSLTSAIDA diferente de vazio** **HCTRANSFORMACAO.XSLTENTREDA diferente de vazio** |
|  | GEAITRANSACAO.SYNCASYNCENVIO | Será gravado o valor "0 - Sincrono". No EAI 1.0 RM não deve existir mensagens assincronas, pois o mesmo não foi projetadopara enviar /receber esse tipo de mensagem. Somente mensagens com características de "falso assíncrono" que será detalhado nesse mesmo documento. |
|  | GEAITRANSACAO.PERMITERECASYNC | Será gravado o valor "0 - Não permite" O EAI 1.0 não está preparado para envio/recebimento assíncrono |
|  | GEAITRANSACAO.EXECVIAJOB | Esse campo definirá se as mensagens de envio (nas transações em questão) serão executadas via Job ou imediatamente na chamada do método.  Esse campo foi criado para resolver a situação do "falso assíncrono". Algumas mensagens são enviadas para o EAI 1.0 com o tipo de entrega assíncrono. Porém, essas mensagens , no momento de execução pelo Job, são enviadas para outro aplicativo com o tipo entrega "sincrono".  Abaixo serão listadas essas transações com esse comportamento: DEVICEEQUIPMENTAPPOINTMENT DEVICETASKSAPPOINTMENT DEVICETRANSPORTCYCLEAPPOINTMENT LABORDEVICETASKSAPPOINTMENT |

## **Transação / Versão**

| Tabela/Coluna EAI 1.0 | Tabela/Coluna EAI 2.0 | Regras |
| --- | --- | --- |
| HCMAPAINTEGRACAO.VERSAOMENSAGEM | GEAITRANSACAOVERSAO.VERSAO |  |
| HCMAPAINTEGRACAO.ENTIDADE | GEAITRANSACAOVERSAO.IDTRANSACAO | O campo identificação da transação será buscado da tabela GEAITransacao |

## **Transação / Aplicativo (rotas)**

| Tabela/Coluna EAI 1.0 | Tabela/Coluna EAI 2.0 | Regras |
| --- | --- | --- |
| HCMAPAINTEGRACAO.IDINTEGRACAO HCINTEGRACAO.SISTEMAINTEGRADO | GEAITRANSACAOAPP.IDAPP | O identificador do App será buscado da tabela GEAIApp |
| HCMAPAINTEGRACAO.ENTIDADE | GEAITRANSACAOAPP.IDTRANSACAO | O campo identificação da transação será buscado da tabela GEAITransacao |
| HCMAPAINTEGRACAO.VERSAOMENSAGEM | GEAITRANSACAOAPP.IDTRANSACAO |  |
|  | GEAITRANSACAOAPP.IDSOURCECODE | Identificador do código fonte (GSourceCode) |
|  | GEAITRANSACAOAPP.INCLUIMENSAGEMORIGINAL | Será gravado o valor 1. Por default, a mensagem original sempre será incluída na mensagem de resposta |
|  | GEAITRANSACAOAPP.MODOHABILITADO | O valor será copiado da transação (GEAITRANSACAO.MODOSUPORTADO) |

false

Não será permitido o mapeamento entre um aplicativo e uma transação em versões diferentes.  
Ex: A transação "COSTCENTER" poderá ser mapeada para o aplicativo "Protheus/Enviromment" somente na versão 1.000.  
  
Os códigos fontes cadastrados na tabela GSourceCode e mapeados na tabela "HCMapaTransacao.Extensions" não serão migrados para tabela GEAITransacaoApp.IdSourceCode. No EAI 2.0 esse campo será usado exclusivamente para armazenar códigos customizados feitos pelo cliente/customização.  
  
**Ex: Transação mapeada para mais de um um aplicativo:**  
O RM ao enviar uma mensagem dessa transação, a mesma poderá ser enviada somente em caso assíncrono.  
O RM ao receber uma mensagem, os atributos "SourceApplication" e "ProductCode" do xml TotvsMessage serão recuperados e usados para localizar o aplicativo correto.

# Pacote de instalação

---

| Tabela/Coluna EAI 1.0 | Tabela/Coluna EAI 2.0 | Regras |
| --- | --- | --- |
| HCINTEGRACAO.NOMEINTEGRACAO | GEAIPACOTEINSTALADO.NOMEPACOTE |  |
| HCINTEGRACAO.NOMEREDUZIDO | GEAIPACOTEINSTALADO.NOMEREDUZIDO |  |
|  | GEAIPACOTEINSTALADO.ID | Novo Guid |
| HCINTEGRACAO.SISTEMAINTEGRADO | GEAIPACOTEINSTALADO.APPID | O valor do campo "SistemaIntegrado" será usado para buscar o AppId da tabela GEAIApp |

## **De/Para**

| Tabela/Coluna EAI 1.0 | Tabela/Coluna EAI 2.0 | Regras |
| --- | --- | --- |
| HCINTEGRACAOID.TABELARM | GEAIDEPARA.TABELARM |  |
| HCINTEGRACAOID.IDNOMERM | GEAIDEPARA.CAMPOSRM |  |
| HCINTEGRACAOID.IDVALORRM | GEAIDEPARA.VALORRM |  |
| HCINTEGRACAOID.SISTEMAINTEGRADO | GEAIDEPARA.IDAPP |  |
| HCINTEGRACAOID.IDENTIDADE | GEAIDEPARA.TRANSACAO |  |
| HCINTEGRACAOID.IDINTEGRACAO | GEAIDEPARA.VALOREXTERNO |  |

## **Mensagem**

| Tabela/Coluna EAI 1.0 | Tabela/Coluna EAI 2.0 | Regras |
| --- | --- | --- |
| HCFILAMENSAGEM.UUID | GEAIMENSAGEM.UUID |  |
| HCFILAMENSAGEM.TIPOENTREGA | GEAIMENSAGEM.TIPOENTREGA |  |
| HCFILAMENSAGEM.ENTRADASAIDA | GEAIMENSAGEM.ENTRADASAIDA |  |
| HCFILAMENSAGEM.EVENTOMENSAGEM | GEAIMENSAGEM.EVENTO |  |
| HCFILAMENSAGEM.TIPOMENSAGEM | GEAIMENSAGEM.TIPO |  |
| HCFILAMENSAGEM.TRANSACTIONID | GEAIMENSAGEM.IDTRANSACAO |  |
| HCFILAMENSAGEM.MENSAGEMORIGINAL | GEAIMENSAGEM.XMLORIGINAL |  |
| HCFILAMENSAGEM.STATUSPROCESSAMENTO |  | Essa coluna foi descontinuada |
| HCFILAMENSAGEM.VERSAOMENSAGEM |  | A versão da mensagem foi criada na tabela de Rotas |
| HCFILAMENSAGEM.DATAINCLUSAO | GEAIMENSAGEM.DATAMSGORIGINAL |  |
| HCFILAMENSAGEM.IDINTEGRACAO |  | Essa coluna foi descontinuada |
| HCFILAMENSAGEM.CODCOLIGADA |  | Essa coluna foi descontinuada |
| HCFILAMENSAGEM.CODFILIAL |  | Essa coluna foi descontinuada |
| HCFILAMENSAGEM..CODUSUARIO |  | Essa coluna foi descontinuada |
| HCFILAMENSAGEM.MENSAGEMRECIBO |  | Essa coluna foi descontinuada |
| HCFILAMENSAGEM.NOMEPRODUTO |  | Essa coluna foi descontinuada |

## **Rotas da Mensagens**

| Tabela/Coluna EAI 1.0 | Tabela/Coluna EAI 2.0 | Regras |
| --- | --- | --- |
| HCFILAMENSAGEM.VERSAOMENSAGEM | GEAIROTAMENSAGEM.VERSAO |  |
| HCFILAMENSAGEM.IDINTEGRACAO | GEAIROTAMENSAGEM.IDAPP | Nessa coluna será grava não mais o identificador do pacote de integração, mas sim o aplicativo |

## **Execução da rota da Mensagem**

| Tabela/Coluna EAI 1.0 | Tabela/Coluna EAI 2.0 | Regras |
| --- | --- | --- |
| HCFILAEXECUCAO.DATAEXECUCAO | GEAIEXECROTAMENS.DATAEXECUCAO |  |
| HCFILAEXECUCAO.MENSAGEMTRANSFORAMDA | GEAIEXECROTAMENS.XMLMENSTRANSFORMADA |  |
| HCFILAEXECUCAO.CODIGOEXECUCAO | GEAIEXECROTAMENS.CODIGOEXECUCAO |  |
| HCFILAEXECUCAO.STATUSEXECUCAO | GEAIEXECROTAMENS.STATUSEXECUCAO |  |
| HCFILAEXECUCAO.MENSAGEMEXECUCAO | GEAIEXECROTAMENS.MENSAGEMEXECUCAO |  |
| HCFILAEXECUCAO.UUID |  | Essa coluna foi descontinuada |
| HCFILAEXECUCAO.SEQUENCIA |  | Essa coluna foi descontinuada |
| HCFILAEXECUCAO.MENSAGEMRESPOSTA |  | Essa coluna foi descontinuada |
| HCFILAEXECUCAO.TIPOEXECUCAO |  | Essa coluna foi descontinuada |

## **Migração das mensagens**

* Todas as mensagens executadas com erros, síncronas ou assíncronas, serão migradas para a nova tabela de mensagens;
* Mensagens assíncronas, com menos de 5 tentativas de execução,  será criado um job responsável em executá-las;
* Mensagens de envio "assíncronas" serão tratadas como "falso assíncrono", ou seja, elas serão migradas como "síncronas" mais processadas pelo Job;
* Segue abaixo a lista de transações contempladas pelo recurso de falso assíncrono:

**DEVICEEQUIPMENTAPPOINTMENT**  
**DEVICETASKSAPPOINTMENT**  
**DEVICETRANSPORTCYCLEAPPOINTMENT**  
**LABORDEVICETASKSAPPOINTMENT**

---
