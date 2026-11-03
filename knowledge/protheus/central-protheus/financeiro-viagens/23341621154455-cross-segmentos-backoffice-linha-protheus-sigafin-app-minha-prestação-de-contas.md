---
article_id: 23341621154455
category: Financeiro - Viagens
content_hash: f627b36911a5b0b8afdb5afde97c421549d589dbd28e20fec6a11420fd8f1f3a
fetched_at: '2026-06-28T22:38:21.373284+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - APP Minha Prestação
  de Contas - Configuração do ambiente quanto a apresentação de Filiais para seleção
type: support-article
updated_at: '2024-05-08T20:24:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23341621154455-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-APP-Minha-Presta%C3%A7%C3%A3o-de-Contas-Configura%C3%A7%C3%A3o-do-ambiente-quanto-a-apresenta%C3%A7%C3%A3o-de-Filiais-para-sele%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23341621139351) Tempo aproximado para leitura: **00****:04:00 min** **Dúvida**Qual a configuração do ambiente quanto a apresentação de Filiais para seleção?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**Existe uma configuração que é feita somente para configurar qual grupo "**Filiais deste grupo**" de seu sistema estará configurada para utilizar *REST*, e não para realizar a configuração de quais filiais serão exibidas no aplicativo, sendo assim sua necessidade entra como uma melhoria no produto.  
  
Segue documentação da configuração *mobile* onde explica a funcionalidade da TAG em questão: [Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292)  
  
**PrepareIn=ALL**        
**;//PrepareIn:** Chave que indica qual *environment* será preparado para o *rest. ALL* significa que deve ser preparado para atender todas as empresas. Caso você queira utilizar o *REST* com empresa 1 filial 01, por exemplo, inserir na chave 1,01.

**Saiba mais:**  
Guia de uso - [Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292)
