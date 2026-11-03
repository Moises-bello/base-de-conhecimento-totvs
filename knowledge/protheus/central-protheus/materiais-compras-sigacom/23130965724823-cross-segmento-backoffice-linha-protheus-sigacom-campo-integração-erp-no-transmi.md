---
article_id: 23130965724823
category: Materiais - Compras (SIGACOM)
content_hash: 97a627b825487a909204f136905f5d10e17555b31a41bb0be9725a2a5921b57f
fetched_at: '2026-06-28T22:41:10.522493+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Campo Integração
  ERP no Transmite: Exportada'
type: support-article
updated_at: '2025-02-05T13:30:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23130965724823-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-Integra%C3%A7%C3%A3o-ERP-no-Transmite-Exportada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23130982375447) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.  
  
**Ambiente**Quais são os criterios para atualização do campo do campo Integração ERP como 'exportada' no Transmite?  
  
**Solução**

O campo **Integração ERP** como '**exportada'** no transmite **aponta** que o XML enviado para o protheus foi recepcionado, porém a nota fiscal ainda **não** foi '**gerada**' nas rotinas de pré-nota/Documento de Entrada através do monitor do Importador XML.

Um dos principais motivos para que isso ocorra são erros apresentados no momento da integração, como por exemplo: **Fornecedor**, **Produto** ou **amarração Produto x Fornecedor** **inexistentes** na base de dados.

É possivel consultar esses erros através da opção "Reprocessar" do monitor do Importador XML, em seguida realizar o tratamento para correção (Exemplo criar amarração Produto x Fornecedor);

[- Códigos de erros que podem ocorrer no momento da integração;](https://tdn.totvs.com/pages/releaseview.action?pageId=485869227)

[- Clique aqui caso os documentos não estão aparecendo na rotina do REPROCESSAR dentro monitor;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20435997213591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Os-documentos-n%C3%A3o-est%C3%A3o-aparecendo-na-rotina-do-REPROCESSAR-dentro-monitor)

O jobs do protheus responsável por sinalizar ao transmite que a nota fiscal foi **exportada** são [SCHEDCOMCOL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062559984791-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDCOMCOL-dentro-do-novo-SCHEDULE-POUI) e [SCHEDUPDTRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI) , dessa forma é muito importante certificar que os agendamentos estão ativos e foram configurados corretamente conforme [documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI)

**Atenção:** Caso o campo Integração ERP do transmite não seja atualizado após exportação da nota para o monitor do Importador XML, é necessario revisar as configurações do Schedule, garantindo que ele esteja ativo e operacional.

Persistindo, realize um teste **incluindo** os jobs [SCHEDCOMCOL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062559984791-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDCOMCOL-dentro-do-novo-SCHEDULE-POUI) e [SCHEDUPDTRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI) no **menu** do módulo compras, e realize a **execução** **manual**, observando se ocorrerá alguma mensagem de erro: [Como executar as funções de carga SEM utilizar o Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-Schedule)

**Importante**: Para que o job funcione corretamente é extremamente importante que o ambiente esteja atualizado com a ultima expedição continua:  **[Atualização - COMPRAS](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)**

**Atenção:** Não se esqueça de executar o UPDDISTR para atualização do dicionario de dados!

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Quais são os criterios para que o job SCHEDUPTRA encaminhe uma requisição ao transmite informando que o XML foi exportado para o Protheus?**

**Resposta:** Para que job [SCHEDUPDTRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI) do Protheus encaminhe a requisição de atualização do campo Integração ERP para 'exportada' no Transmite, é realizado algumas validações internas:

**Primeira validação:**

* Valida a existência do registro na tabela de integração CKOCOL (Filtrar pelo campo CKO\_DOC = Numero da nota):
  + O campo **CKO\_CHVDOC** **deve** estar **preenchido**;
  + O campo **CKO\_STRAN** **deve** ser **1** (caso diferente de 1 não será feito requisição para atualização status 'exportada');
  + O campo **CKO\_DT\_IMP** **deve** ter uma **data superior** a data inserida no **parâmetro** **MV\_DTINITR**;
  + O campo **CKO\_CODEDI** **deve** conter um destes códigos **('109','214','273','319')**

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
