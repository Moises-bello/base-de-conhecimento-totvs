---
article_id: 29958024820247
category: LEGAIS - BLOCO H/MATR460
content_hash: 6cc6aedc5eb9afd39095492e0f9099caa04f69c216050adab650b5b1f441e979
fetched_at: '2026-06-28T22:42:15.002951+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Alguns produtos não
  estão sendo levados no registro K200
type: support-article
updated_at: '2025-03-12T12:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29958024820247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Alguns-produtos-n%C3%A3o-est%C3%A3o-sendo-levados-no-registro-K200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29958024816279) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Devido alguns processos internos, foi notado que alguns tipos de produtos, deixaram de serem levados no registro K200, como fazer para que eles sejam considerados novamente?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Para esse processo, avalie se o tipo do produto desejado, esta configurado corretamente sob os parâmetros o qual ele pertence: **MV\_BLKTP**\*\*

**Detalhamentos dos tipos cadastrados no padrão e parametros:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MP - SIGAEST- Como definir um tipo de produto que não seja padrão do sistema para que seja considerado no Bloco K?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MP-SIGAEST-Como-definir-um-tipo-de-produto-que-n%C3%A3o-seja-padr%C3%A3o-do-sistema-para-que-seja-considerado-no-Bloco-K)

**Outras possiveis causas:** Talvez o produto esteja com o campo '**B1\_FANTASM**' preenchido, para tornar os produtos '**fantasma**', produtos fantasmas **não possuem controle de estoque**, não são comprados e/ou produzidos, sendo assim isso faz a não gravação no registro K200.

Ou talvez esteja fazendo uma validação no ponto de entrada [**SPDFISBLCK**](https://tdn.totvs.com/x/Mt0cKw)

**Conclusão:** Dessa forma, os tipos de itens configurados conforme instruções, serão considerados no registro.

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K- Conceito e configurações mínimas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421126537879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Conceito-e-configura%C3%A7%C3%B5es-m%C3%ADnimas)
