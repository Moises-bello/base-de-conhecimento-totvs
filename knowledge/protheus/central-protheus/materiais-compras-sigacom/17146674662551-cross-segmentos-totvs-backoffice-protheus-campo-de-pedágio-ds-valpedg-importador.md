---
article_id: 17146674662551
category: Materiais - Compras (SIGACOM)
content_hash: befcabc70d049ae4ce40d3252b9db7866215932a8c5c6f11063926f55a7d55ba
fetched_at: '2026-06-28T22:41:12.851923+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - Campo de Pedágio (DS_VALPEDG)
  / Importador XML
type: support-article
updated_at: '2024-06-11T17:59:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17146674662551-Cross-Segmentos-Totvs-Backoffice-Protheus-Campo-de-Ped%C3%A1gio-DS-VALPEDG-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17146663860759) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao importar um documento de Transporte que tenha valor de pedágio, o valor é desconsiderado na importação documento para o campo próprio (F1\_VALPEDG).  
Qual a configuração necessário para este campo aparecer na tela de do Importador do XML, e importar para o campo correto na geração do documento para classificação ?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Implementado campo (**DS\_VALPEDG**) onde poderá informar o valor do pedágio e ser enviado para pré-nota (MATA140) e/ou documento de entrada (MATA103).

Obs: Para preencher o valor do pedágio (DS\_VALPEDG) deve-se utilizar os ponto de entradas [A140IGRV](https://tdn.totvs.com/pages/viewpage.action?pageId=6085827) ou [MT116XMLCT](https://tdn.totvs.com/pages/viewpage.action?pageId=243012688)Tratamento para gerar documento automático de notas do tipo "B - Beneficiamento", quando MV\_COMCOL1 = 2.

Importante : Atualização de dicionário estará disponível automaticamente a partir do release**12.1.2310**, porém poderá ser criado através da aplicação da próxima expedição contínua de compras, com data maior a**primeira quinzena Setembro/23**

***Saiba Mais:***

[Campo de Pedágio (DS\_VALPEDG) / Importador XML](https://tdn.totvs.com/pages/releaseview.action?pageId=763245608)

[Pontos de Entrada disponíveis nas funções](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)

[Códigos de Erros](https://tdn.totvs.com/pages/releaseview.action?pageId=485869227)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Integração Importador XML x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7557934491159-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-Importador-XML-x-TOTVS-Transmite?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
