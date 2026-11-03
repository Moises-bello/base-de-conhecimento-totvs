---
article_id: 10069793553303
category: RH - Folha de Pagamento
content_hash: e2b27bfab5f388fb514df815b058d9eeb220c347bbd0ca24cd51bc4685af4d65
fetched_at: '2026-06-28T22:44:13.622615+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como ocorre a geração da tabela RAW e RAZ automaticamente
  no cálculo.
type: support-article
updated_at: '2024-09-11T19:01:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10069793553303-RH-Linha-Protheus-GPE-Como-ocorre-a-gera%C3%A7%C3%A3o-da-tabela-RAW-e-RAZ-automaticamente-no-c%C3%A1lculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26305786463383) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como o sistema gera a tabela RAW e RAZ automaticamente durante o cálculo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**A geração automática no cálculo ocorre apenas para funcionários múltiplos vínculos em empresas de CNPJ RAIZ diferente**(onde as empresas/filiais estão dentro do mesmo grupo protheus).**

Ao realizar o calculo, o sistema verifica se existem outro vínculo para o mesmo CPF, ao calcular o primeiro vínculo é gravado o campo RC\_SEQMV = 1, quando for calculado o segundo vínculo, é verificado que já foi calculado o primeiro vinculo, é verificado que o funcionário trabalha em filiais com a raiz de CNPJ diferentes, ou seja, empresas diferentes, nesse cenário, é criado a tabela RAW e RAZ com as informações de múltiplos vínculos.

**Filiais dentro do mesmo grupo com a mesma RAIZ de CNPJ não é criado a RAW e RAZ!**

**Saiba Mais**

[Como gerar funcionários com múltiplos vínculos no evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013550551)

[Novo Cálculo MULTV - Multiplos Vinculos](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=552575179)

[RH - Linha Protheus - GPE - Alteração no cadastro do Sindicato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052464393-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-no-cadastro-do-Sindicato)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
