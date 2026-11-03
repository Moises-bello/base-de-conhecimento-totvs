---
article_id: 20595351935511
category: Materiais - Compras (SIGACOM)
content_hash: a232b9da26249de02dc2358fbbbc03bcf7b0af17b18c90c61b3ef87376c89c0b
fetched_at: '2026-06-28T22:41:13.053060+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Se o XML ESTIVER for
  consumido da pasta IN para LIDOS, mas NÃO está aparecendo no MONITOR.
type: support-article
updated_at: '2024-08-15T18:41:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20595351935511-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Se-o-XML-ESTIVER-for-consumido-da-pasta-IN-para-LIDOS-mas-N%C3%83O-est%C3%A1-aparecendo-no-MONITOR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20595351892503) Tempo aproximado para leitura: **00h05 min****Dúvida**

O XML foi consumido na pasta IN e foi para a pasta lidos mas NÃO está aparecendo no MONITOR.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12

**Solução**

Para identificação deve-se abrir o Monitor > Reprocessar, verificar na aba Ocorrência qual inconsistência/erro está ocorrendo e corrigi-lo.

![gif - MONITOR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24163283487127)

Consulte a tabela com os Códigos de erros :  [Erros (Códigos)](https://tdn.totvs.com/pages/releaseview.action?pageId=271663193)

Caso o registro não seja exibido no botão Reprocessar, abrir a tabela **CKOCOL** e verificar qual o conteúdo do campo **CKO\_CODERR** e corrigir conforme a tabela de erros do link acima.  
  
**Observação:**

* Campo **CKO\_FLAG = 0** significa que rodou apenas o COLAUTOREAD ou seja, consta pendente execução da função SCHEDCOMCOL. Para mais detalhes sobre essas execuções consulte o artigo: [MP - SIGACOM - (Importador XML ou Totvs Colaboração) | Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule?source=search))
* Para consultar legenda dos campos DS\_STATUS, CKO\_STATUS e CKO\_FLAG [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037713954-MP-SIGACOM-COLABORA%C3%87%C3%83O-Legenda-dos-campos-DS-STATUS-CKO-STATUS-e-CKO-FLAG)
* Caso o ambiente esteja hospedado no **CLOUD** os diretórios e conteúdo dos parâmetros devem estar todos em letras minúsculas.

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Erros (Códigos)](https://tdn.totvs.com/pages/releaseview.action?pageId=271663193)

[Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
