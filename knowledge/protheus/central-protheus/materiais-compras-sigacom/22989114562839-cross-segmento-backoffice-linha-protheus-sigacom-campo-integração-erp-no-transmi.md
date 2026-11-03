---
article_id: 22989114562839
category: Materiais - Compras (SIGACOM)
content_hash: ead04577eed7ad97dc44c4501f88849bb43b90b6747c0561dea654f8f05dda93
fetched_at: '2026-06-28T22:41:10.510354+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Campo Integração
  ERP no Transmite: Classificada'
type: support-article
updated_at: '2024-07-05T14:38:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22989114562839-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-Integra%C3%A7%C3%A3o-ERP-no-Transmite-Classificada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22989157574039) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais são os criterios para atualização do campo do campo Integração ERP como 'classificada' no Transmite?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.  
  
**Solução**O campo **Integração ERP** como '**classificada'** no transmite **aponta** que o XML enviado para o protheus foi recepcionado, e o **processo de classificação da nota fiscal foi realizado com sucesso**.

O job do protheus responsável por sinalizar ao transmite que a nota fiscal foi classificada  é o [SCHEDUPDTRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI), dessa forma é muito importante certificar que os agendamentos estão ativos e foram configurados corretamente conforme [documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI)

**Atenção:** Caso o campo o integração ERP do transmite não seja atualizado após a classificação, é necessario revisar as configurações do Schedule, garantindo que ele esteja ativo e operacional.

Persistindo, realize um teste **incluindo** o job [SCHEDUPDTRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI) no **menu** do módulo compras, e realize a **execução** **manual**, observando se ocorrerá alguma mensagem de erro: [Como executar as funções de carga SEM utilizar o Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-Schedule)

**Importante**: Para que o job funcione corretamente é extremamente importante que o ambiente esteja atualizado com a ultima expedição continua:  **[Atualização - COMPRAS](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)**

**Atenção:** Não se esqueça de executar o UPDDISTR para atualização do dicionario de dados!

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Quais são os criterios para que o job SCHEDUPTRA encaminhe uma requisição ao transmite informando que a nota foi classificada?**

**Resposta:** Para que job [SCHEDUPDTRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI) do Protheus encaminhe a requisição de atualização do campo status ERP para classificado no Transmite, é realizado algumas validações internas:

**Primeira validação:**

* Valida a existência do registro na tabela de integração CKOCOL (Filtrar pelo campo CKO\_DOC = Numero da nota):
  + O campo **CKO\_CHVDOC** **deve** estar **preenchido**;
  + O campo **CKO\_STRAN** **deve** ser **diferente** de **4** (caso seja 4 não será feito requisição para atualização status 'classificada');
  + O campo **CKO\_DT\_IMP** **deve** ter uma **data superio**r a data inserida no **parâmetro** **MV\_DTINITR**;
  + O campo **CKO\_CODEDI** **deve** conter um destes códigos **('109','214','273','319')**

**Segunda Validação:**

* Valida se o **dados** **da nota fiscal no monitor do importador XML** é **exatamente** igual aos **dados da nota fiscal** classificada no **documento de entrada:**
  + **Numero da nota** (SF1.F1\_DOC igual SDS.DS\_DOC);
  + **Serie** (SF1.F1\_SERIE igual SDS.DS\_SERIE);
  + **Fornecedor** (F1\_FORNECE igual SDS.DS\_FORNEC);
  + **Loja** (SF1.F1\_LOJA igual SDS.DS\_LOJA).

**Atenção,** **caso** um desses campos tenha **divergência** entre o **documento de entrada** (SF1) **e** o **monitor** (SDS), **Exemplo**: **Serie** da nota fiscal igual **'001'** no **documento de entrada** (SF1), **Serie** do registro xml **no** **monitor** igual '**1'** (SDS). Isso **poderá** causar uma **não conformidade**, e o status desse registro não ser atualizado no transmite.

**Terceira Validação:**

* Valida se a nota fiscal encontra-se classificada (Legenda vermelha, campo F1\_STATUS = A);

**Se todas condições** acima forem **atendidas** o job [SCHEDUPDTRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI) **atualizará** o campo **CKO\_STRAN para 4**, e irá requisitar **atualização** do **Integração ERP** no transmite para **Classificado**

***Saiba Mais:***

* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=485858148)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Os documentos não estão aparecendo na rotina do REPROCESSAR dentro monitor.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20435997213591)
* [IX10 - Integração Importador XML x TOTVS Transmite](https://tdn.totvs.com/x/m1tyK)
* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=678583195)
