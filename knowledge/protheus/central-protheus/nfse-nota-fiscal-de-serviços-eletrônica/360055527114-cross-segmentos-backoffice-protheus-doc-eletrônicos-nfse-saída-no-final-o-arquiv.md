---
article_id: 360055527114
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 99371d7b316337a110b592be6a67e1cbf07bac93d2b007036a6afd72c033f346
fetched_at: '2026-06-28T22:39:58.486556+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Saída no
  final: O arquivo SX210 não existe (AUTONFSE)'
type: support-article
updated_at: '2025-07-18T14:52:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055527114-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Sa%C3%ADda-no-final-O-arquivo-SX210-n%C3%A3o-existe-AUTONFSE
---

**Ocorrência**Ao observar o console do Protheus destinado ao AUTONFSE é apresentado: "***Saída no final: O arquivo SX210 não existe."*****Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Causa**Essa mensagem ocorre quando a seção do ENVIRONMENT no appserver.ini do AUTONFSE está com as linhas de DEBUG configuradas incorretamente.  
  
Exemplo:  
Se configurado dessa maneira abaixo e na verdade o código de empresa for **01** e filial **01**, terá esse erro, visto que a rotina não irá conseguir filtrar a empresa/filial corretamente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096120833/mceclip0.png)  
  
**Solução**Portanto, é de extrema importância informar exatamente como estão cadastrados os **códigos de empresa/filial + série** correspondentes:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096121013/mceclip1.png)  
  
Caso queira pegar de uma maneira geral o DEBUG, sem filtros por filial, poderá utilizar apenas o **AUTONFSE\_DEBUG = 1** e comentar as demais:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096121233/mceclip2.png)   
  
***Obs.: O serviço de AUTONFSE deverá ser reiniciado após ajustes.***
