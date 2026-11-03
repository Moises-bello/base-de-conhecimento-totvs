---
article_id: 25990039318167
category: SIGAEST - INTEGRAÇÕES
content_hash: 0a981ed7c7475d9ae78688c0daa2c4da96cc46f68e5d5aa792fc2d319f795787
fetched_at: '2026-06-28T22:38:46.225248+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração ITEM está
  gerando o campo B1_LOCPAD = .
type: support-article
updated_at: '2024-08-29T12:11:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25990039318167-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-ITEM-est%C3%A1-gerando-o-campo-B1-LOCPAD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25989999635095) Tempo aproximado para leitura: **00:00:45min** **Dúvida**Ao realizar a Integração de ITEM no Protheus, o campo B1\_LOCPAD está sendo gerado com um ponto, porém esse armazém não deveria ser gerado como ponto, como corrigir ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Esse comportamento ocorre por conta do Cadastro do Adapter no Configurador, a Integração de Item é gerenciada por dois fontes diferentes:

- MATA010 do módulo de Estoque/Custos;

- EECAC120 do módulo Easy Import Control;

Ao utilizar o nosso Adapter da MATA010 o B1\_LOCPAD vai respeitar o conteúdo gerado no XML de envio do outro sistema.

Já ao utilizar o Adapter EECAC120 por padrão ele adiciona o campo B1\_LOCPAD = "."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25990042816023)

Dessa maneira, caso tenha maiores dúvidas sobre o Adapter EECAC120 se faz necessário contatar o time do módulo SIGAEIC.

Segue documentação com maiores detalhes da integração quando existe os Cadastros do módulo Easy Import Control [Clique aqui.](https://tdn.totvs.com/x/oYtqIQ)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Integrações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
