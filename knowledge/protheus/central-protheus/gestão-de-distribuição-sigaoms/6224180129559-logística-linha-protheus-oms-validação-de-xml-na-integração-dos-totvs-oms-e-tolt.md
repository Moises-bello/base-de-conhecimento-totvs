---
article_id: 6224180129559
category: Gestão de Distribuição (SIGAOMS)
content_hash: 3405ed2a988207a056d63426ce2fabedd3314ea6434f0ce381b4f673676d25b2
fetched_at: '2026-06-28T22:45:51.058452+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Validação de XML na Integração dos TOTVS
  OMS e TOL/TRE
type: support-article
updated_at: '2022-12-01T11:07:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6224180129559-Log%C3%ADstica-Linha-Protheus-OMS-Valida%C3%A7%C3%A3o-de-XML-na-Integra%C3%A7%C3%A3o-dos-TOTVS-OMS-e-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:30 min** **Dúvida**Na Integração dos **TOTVS OMS**  e **TOL/TRE**, como configurar o Sistema para impedir que ocorram inconsistências no **Protheus** devido a **XML's** mal formatados?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Para impedir que ocorram inconsistência no **Protheus** por **XML's** mal formatados, foi desenvolvida a funcionalidade de validar **XML's**, baseadas em **XSD - XML Schema Definition**.  
  
Ao consumir o ***WebService*** do **Protheus** com as mensagens de **Liberação de Viagem - publishReleasedTripService**, **Reprogramação de Viagem - publishReprogrammingService** e **Cancelamento de Viagem - publishCancelService**, os **XML's** passarão por uma pré-valiação de estrutura.  
  
**1. Estrutura Para Pré-validação**  
Inclua a pasta **xsd dentro da system**, com os seguintes arquivos:

* envelope.xsd
* publishCancelService.xsd
* publishReleasedTripService.xsd
* publishReprogrammingService.xsd

![xsdd.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6224432192023/xsdd.JPG)

Os arquivos acima estão ao final desse artigo, na **sessão Anexos.****2. As falhas ocorridas durante o processo de integração serão retornadas para o XML de Resposta ou Log Appserver:**

* AAAA-MM-DD T09:39:25.122000-03:00 10084 **OMSXWS - OMSValXSD** - Verificando as configurações de validação de **XML** baseada em **Schema** **XSD**.
* AAAA-MM-DD T09:39:25.123000-03:00 10084 **OMSXWS - OMSValXSD** - Validação do **XML** de entrada através de **XSD** não executada por não existir o diretório \system\xsd com os **xsds** no servidor.
* AAAA-MM-DD T09:39:25.123000-03:00 10084 **OMSXWS - OMSValXSD** - Análise das configurações de validação de baseada em **Schema XSD** concluída.
* AAAA-MM-DD T09:39:43.890000-03:00 10084 **OMSXWS - OMSXConnect** - Conteúdo de **cErro**:  
  Opening and ending tag mismatch - ns2:publishReprogrammingService line 1 and tagParaErro:  
  Opening and ending tag mismatch - soap:Body line 1 and ns2:publishReprogrammingService  
  Opening and ending tag mismatch - soap:Envelope line 1 and soap:Body  
  Extra content at the end of the document

**3. Falha na Liberação da Viagem**Caso ocorra falha na liberação da viagem, será retornado **N** para a **TOL/TRE** e a inconsistência de estrutura estará no *log* do **Protheus**:

**![3.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6224784028311/3.JPG)**

**4. Falha de Reprogramação ou Cancelamento**Se forem falhas de reprogramação ou cancelamento será retornada a inconsistência no **XML** de resposta e também para o *log*:

**![4.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6224805195031/4.JPG)**

**5. Se Não Estiver Habilitado**Estas mensagens serão exibidas no *log* e processo de validação será descartado:

* AAAA-MM-DD T10:42:29.347000-03:00 10292 **OMSXWS - OMSValXSD** - Verificando as configurações de validação de **XML** baseada em **Schema XSD**.
* AAAA-MM-DD T10:42:29.347000-03:00 10292 **OMSXWS - OMSValXSD** - Validação do **XML** de entrada através de **XSD** não executada por não existir o diretório **\system\xsd** com os **XSDS** no servidor.
* AAAA-MM-DD T10:42:29.347000-03:00 10292 **OMSXWS - OMSValXSD** - Análise das configurações de validação de baseada em **Schema XSD** concluída.

**Importante**Esse tratamento destina-se a **XML** padrão.  
  
**6. Função Para Gerar Mensagens Auxiliares Para o Log**Para auxiliar na análise de inconsistências foi desenvolvida uma função para gerar mensagens auxiliares  
para o *log*, sendo que ela insere informações como queries e conteúdos de variáveis. Para habilitar são necessários três parâmetros em todos os ambientes:  
  
**LOGCPLOMS=.T.**  
**FWFRAME\_TRACELOG=1**  
**LOGTIPOMS**= **CONSOLE**O parâmetro **LOGTIPOMS**, define a forma de saída das mensagens.   
Como *default* o Sistema irá gerar no **Console.log do Appserver.**Caso desejar separar as mensagens e salvar com o nome de **omscpl.log** dentro da **pasta system**, informe **ARQUIVO.****Saiba mais**Mais informações sobre a geração do *Log* poderão ser acessadas do *link*:  
[Logística - Linha Protheus - OMS - Como habilitar Log de integração do TOTVS OMS e TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-Log%C3%ADstica-Linha-Protheus-OMS-Como-habilitar-gera%C3%A7%C3%A3o-do-arquivo-Console-log-do-PROTHEUS-com-mensagens-auxiliares-informa%C3%A7%C3%B5es-de-query-e-conte%C3%BAdos-de-vari%C3%A1veis-na-integra%C3%A7%C3%A3o-do-TOTVS-OMS-e-TOL)  
  
**Glossário  
TOL** - TOTVS Otimização Logística **TRE** - TOTVS Roteirização e Entrega **TOTVS OMS** - Order Management System  
 **Anexos**
