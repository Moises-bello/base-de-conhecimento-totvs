---
article_id: 23060612979863
category: Materiais - Compras (SIGACOM)
content_hash: 6416df64de84d71eb7e8433cec2ca8846121314f1aa921d3b8bd205b6f5a19ba
fetched_at: '2026-06-28T22:41:11.519792+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Quais status estão
  disponiveis no campo "Integração ERP" no Monitor de Documentos do TOTVS Transmite?
type: support-article
updated_at: '2024-07-05T14:43:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23060612979863-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Quais-status-est%C3%A3o-disponiveis-no-campo-Integra%C3%A7%C3%A3o-ERP-no-Monitor-de-Documentos-do-TOTVS-Transmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23060645215639) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais status estão disponiveis no campo "IntegraçãoERP" no Monitor de Documentos do TOTVS Transmite?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23060645216919)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.  
  
**Solução**O campo "Integração ERP" do TOTVS Transmite é utilizado para informar qual status da integração do XML do transmite com o Protheus. Neste campo é utilizado alguns status:

* **[Classificada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22989114562839-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-status-ERP-no-Transmite-Classificado):** Esse status será apresentado quando houve integração do XML com Protheus, e a **nota** **fiscal** foi **classificada** com sucesso;
* **[Integrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23130208065303-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-status-ERP-no-Transmite-Integrada):** Esse status será apresentado quando houve integração do XML com Protheus, mas a **nota** **fiscal** ainda **não** **foi classificada** (Em recebimento de Pré-Nota);
* **[Exportada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23130965724823-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-status-ERP-no-Transmite-Exportada):** Esse status será apresentado quando houve integração do XML com Protheus, mas a **nota** ainda **não** foi **gerada** através do **monitor** **no Importador** **XML**. Neste cenario, verifique a opção "Reprocessar" do Importador XML e verifique se existe algum erro na geração da nota (Exemplo, fornecedor não existe na base de dados);
* [**Disponível:**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23138650080663-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Campo-Integra%C3%A7%C3%A3o-ERP-no-Transmite-Disponivel) Esse status será apresentado quando o Protheus já solicitou a importação dos novos XMLs para o TOTVS Transmite (Fase de processamento dos dados requisitados);

* **[Pendente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20341622133527-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGGACOM-Importador-XML-X-TOTVS-Transmite-A-integra%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-ocorrendo-permanecendo-com-o-status-de-integra%C3%A7%C3%A3o-ERP-como-Pendente):** Este status será apresentado quando o documento está pendente (ainda não houve requisição do Protheus para importação do XML ou XML ainda não está disponivel). Para que o processo da integração seja iniciado é obrigadorio que o campo **XML NF-e** esteja como **"disponivel"**. Caso o campo XML NF-e esteja como **"Aguardando sefaz"** será necessario realizar a [ciência no documento.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23061920210327-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-manifestar-ci%C3%AAncia-da-opera%C3%A7%C3%A3o-no-TOTVS-Transmite)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23060645217943)

**Importante:** Para saber mais sobre cada status e como são feitas as atualizações, clique no hiperlink disponivel no nome de cada status listado acima;

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
