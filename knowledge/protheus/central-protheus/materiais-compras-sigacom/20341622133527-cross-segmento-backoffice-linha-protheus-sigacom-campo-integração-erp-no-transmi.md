---
article_id: 20341622133527
category: Materiais - Compras (SIGACOM)
content_hash: 31dbc24e4d53e77b435c5742ea8faed8635fa136689d5343d387dfb92fd1a6c2
fetched_at: '2026-06-28T22:41:10.535986+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Campo Integração
  ERP no Transmite: Pendente'
type: support-article
updated_at: '2026-05-19T13:15:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20341622133527-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-Integra%C3%A7%C3%A3o-ERP-no-Transmite-Pendente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20341607991447) Tempo aproximado para leitura: **00:00:05min**  
  
**Dúvida**  
A integração não está ocorrendo, permanecendo com o status de integração ERP como "Pendente"  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Solução**

Essa ocorrência geralmente acontece devido às notas ainda não estarem completamente disponíveis no portal da SEFAZ. Para validar se já foram liberadas, siga os passos abaixo:

![b006069d-f61e-4de5-8402-e9b582d16e1f (online-video-cutter.com).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22504162460823)

Acessar o Portal Transmite, na parte de "Gerenciador de Colunas":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22504162515991)

Desmarque uma coluna, como por exemplo, "Atuação Filial", e marque a coluna "XML NF-e". Em seguida, forneça informações sobre o status dos documentos que ainda não foram integrados.![](https://centraldeatendimento.totvs.com/hc/article_attachments/22504162544151)

Se o status estiver como "Aguardando Sefaz", os documentos realmente não serão integrados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22504169619991)

Será necessário aguardar até que a SEFAZ libere completamente o documento, para que o Importador XML possa realizar a requisição e efetuar a importação das notas.

**Importante:** Caso o campo XML NFe esteja disponivel, verifique se o agendamento abaixo estão configurados corretamente:

- [SCHEDIMPTRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062311546775-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDIMPTRA-dentro-do-novo-SCHEDULE-POUI)

- [SCHEDUPDTRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062370970647-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDUPDTRA-dentro-do-novo-SCHEDULE-POUI)

- [SCHEDCOMCOL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062559984791-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDCOMCOL-dentro-do-novo-SCHEDULE-POUI)

Persistindo, execute as funções SCHEDIMPTRA e SCHEDUPDTRA através da ferramenta de auxilio do Importador XML: [Como executar a rotina IMPTRATOOL para importação de notas do Transmite?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32791819194391/live_preview/01JXMRTXBBG3MB6YQ06JA3BDEZ)

***Saiba Mais :***

[IX10 - Integração Importador XML x TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=678583195#Funcionalidades-Par%C3%A2metros)

[Cross Segmentos - Totvs Backoffice Protheus - Importador XML X TOTVS Transmite - "Em qual momento o Importador XML altera o status - Integração ERP no Portal do Trasnsmite"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19877027865495-Cross-Segmentos-Totvs-Backoffice-Protheus-Importador-XML-X-TOTVS-Transmite-Em-qual-momento-o-Importador-XML-altera-o-status-Integra%C3%A7%C3%A3o-ERP-no-Portal-do-Trasnsmite-)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
