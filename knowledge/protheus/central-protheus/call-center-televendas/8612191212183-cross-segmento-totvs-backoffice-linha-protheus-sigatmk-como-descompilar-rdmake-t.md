---
article_id: 8612191212183
category: Call Center - Televendas
content_hash: b94658124fdcde10f6584d9b2563c4a271ed4c9090ae2b2e5a5c2e7ba670da83
fetched_at: '2026-06-28T22:41:30.353382+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Como descompilar
  rdmake TMKR3A?
type: support-article
updated_at: '2023-12-07T16:42:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8612191212183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Como-descompilar-rdmake-TMKR3A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19640773556631) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como desabilitar o RDMAKE "TMKR3A" a partir da versão 12.1.33  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - a partir da versão 12.1.33  
  
**Solução**O RDMAKE "TMKR3A" é disponibilizado no RPO Padrão Protheus e, devido à mudança a partir da versão 12.1.33, as compilações de customizações ocorrem separadamente, no RPO Custom. Por isto, quando é executada a exclusão deste fonte dentro do RPO padrão do Protheus, ocorre uma mensagem impossibilitando essa ação.

Mensagem

**Is not allowed more than one source with same name. Rename your source:**  
  
Para que seja desabilitada a utilização do RDMAKE, a partir da versão 12.1.33, será necessário compilar o fonte do relatório conforme exemplo abaixo: 

![image__1_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8612485895959)  
  
User Function Tmkr3A(cNumAte)   
Return(.F.)  
  
**IMPORTANTE**:

A partir da atualização do binário harpia 20.3.1.x do TOTVS | Application Server, ou superior, não será possível conter o mesmo nome de um fonte RDMAKE no RPO Custom e no RPO padrão TOTVS.

Sendo assim, efetue os seguintes passos:

1. Altere o nome do arquivo de “TMKR3A.PRX” para outro, não poderá ser **TMKR3A.PRW**, utilize por exemplo **MYTMKR3A.PRW**.

2. Compile este novo RDMAKE em seu ambiente para que seja criado o arquivo em seu RPO Custom;

**Saiba mais**: [Layout de Impressão do Atendimento Televendas](https://tdn.totvs.com/x/rNdeI)
