---
article_id: 19883858772119
category: Materiais - Compras (SIGACOM)
content_hash: cf499a5b7940244805b2430beaf55c17add1be032392decd34dbf3c37029d70d
fetched_at: '2026-06-28T22:41:16.019926+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a importação
  de um XML e já gerar pré-nota automaticamente ?
type: support-article
updated_at: '2024-06-12T21:35:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19883858772119-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-importa%C3%A7%C3%A3o-de-um-XML-e-j%C3%A1-gerar-pr%C3%A9-nota-automaticamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19883884528919) Tempo aproximado para leitura: **00:02 min** **Dúvida**Como realizar a importação de um XML e já gerar pré-nota automaticamente ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Solução**

Para importar um XML do tipo normal em pré-nota, você precisa seguir as instruções abaixo e configurar os parâmetros conforme suas necessidades:

1. **MV\_COMCOL1:**

   * Defina como 1.
2. **MV\_COMCOL2:**

   * Atribua o valor "N".
3. **MV\_COMCOL3:**

   * Configure como ".T." (verdadeiro) para que seja alterada a database na geração do documento, ou ajuste conforme sua necessidade específica.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19883884531735)

Essas configurações são essenciais para garantir que a importação do XML em pré-nota seja executada corretamente.

Lembre-se de ajustar os parâmetros de acordo com os requisitos específicos do seu processo.

***Saiba Mais :***

* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=485858148)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível Importar um documento do Tipo Beneficiamento Classificado ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12969026890007-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-Importar-um-documento-do-Tipo-Beneficiamento-Classificado-?source=search)
* [IX10 - Integração Importador XML x TOTVS Transmite](https://tdn.totvs.com/x/m1tyK)
* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
