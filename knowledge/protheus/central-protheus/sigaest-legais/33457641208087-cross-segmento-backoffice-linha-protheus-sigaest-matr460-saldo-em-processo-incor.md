---
article_id: 33457641208087
category: SIGAEST - LEGAIS
content_hash: 5084aa95f0b4c5f28b4d222a09b4c00e6829f9935788e627e2bc2c1e39f681ff
fetched_at: '2026-06-28T22:38:51.747647+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Saldo em
  Processo incorreto quando se requisita duas vezes o mesmo insumo numa mesma OP
type: support-article
updated_at: '2025-07-14T16:55:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33457641208087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Saldo-em-Processo-incorreto-quando-se-requisita-duas-vezes-o-mesmo-insumo-numa-mesma-OP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33457627608343) Tempo aproximado para leitura: **00:02:35min**  
  
**Dúvida**  
Tenho um cenário onde requisito duas vezes o mesmo insumo (Matéria Prima) para uma mesma Produção onde gera um saldo em processo indevido no MATR460. Como fazer para que o saldo em processo venha corretamente no P7?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Avaliamos que em um cenário que precisa ser requisitado duas vezes a mesma matéria prima, existe a necessidade de configuração de sequencia na estrutura (G1\_TRT), conforme o conceito abordado abaixo:

**Parâmetro:** MV\_USATRT = .T.   
   
A estrutura com sequência, significa que o produto terá duas produções, na sequência 001 vai consumir a matéria prima da sequência 001, na sequência 002 vai consumir a matéria prima da sequencia 002.  
 

* Exemplo do Cadastro de Estrutura:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33457627610135)  
 

* Essa configuração significa que serão duas Ordens de Produção, uma para a sequência 001 e outra para a sequência 002:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33457627611159)  
 

* Ao concluir a OP será efetuado o empenho, e deve ser empenhado a matéria prima da sequência 001, deletando a matéria prima da outra OP e sequencia 002:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33457627611927)  
 

* Inclusão da segunda OP e sequencia 002:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33457627612695)  
 

* Ao concluir a OP será efetuado o empenho, e deve ser empenhado a matéria prima da sequência 002, deletando a matéria prima da outra OP e sequencia 001:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33457641173143)  
   
   
**Observação:** Uma outra opção seria fazer os empenhos a parte na tela de empenho simples:  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33457641175319)  
 

* Ao realizar o apontamento de ambas sequencias (001 e 002) sendo eles:
  + Primeiro da sequencia 001 de 50 UN
  + Primeiro da sequencia 002 de 50 UN
  + Segundo da sequencia 001 de 41 UN
  + Segundo da sequencia 002 de 41 UN

* Ao imprimir o MATR460 não é listado saldo em processo indevido :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33457627615767)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)
