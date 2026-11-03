---
article_id: 360033758794
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e4395c4e3ddfb6bda036007a79bf255dfe89a0d697efe942bf86fd63359007c4
fetched_at: '2026-06-28T22:38:30.076711+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos- TOTVS Backoffice (Linha Protheus)- SIGAFAT - Nota sobre Error-
  TOPCONN - TC_Blob_Length
type: support-article
updated_at: '2021-08-27T16:25:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033758794-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-Error-TOPCONN-TC-Blob-Length
---

**Ocorrência**

Ao abrir uma rotina mata440,  o sistema exibe erro: Error - TOPCONN - TC\_Blob\_Length.  
  
**Ambiente**

Cross Segmentos- TOTVS Backoffice (Linha Protheus)- SIGAFAT – A partir da versão 12.  
  
**Causa**

Este incidente **ocorre** quando a tabela possui **campos do tipo Memo (M)** e o conteúdo destes campos é muito **extenso**, ao tentar abrir a tabela o sistema exibe erro.

Pode ocorrer em qualquer rotina, onde a tabela contenha campo memo , conforme a descrição acima.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Aumente a capacidade do sistema apresentar os campos do Tipo MEMO:

* Insira o **TopMemoMega** ou aumente sua capacidade: <http://tdn.totvs.com/display/tec/TOPMemoMega> ,tanto no server.ini como ini do Dbacess;
* Insira o **MaxStringSize** ou aumente sua capacidade: <http://tdn.totvs.com/pages/viewpage.action?pageId=161349793> , tanto no server.ini como ini do Dbacess;
* Se após os procedimentos problema permanecer, encaminhe o erro.log do Dbacess para a equipe de suporte avaliar, qual o campo de usuário do tipo memo que possa estar gerando a ocorrência .
