---
article_id: 360052571913
category: RH - Relatórios Folha
content_hash: 9cced06dc384d0ae44a436a6e3db997ad9d9d6fc0b52643bc182ebd370ad6cd0
fetched_at: '2026-06-28T22:43:17.587040+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de folha de pagamento gerando apenas
  para funcionário demitido ou de férias
type: support-article
updated_at: '2024-08-26T12:32:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052571913-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-folha-de-pagamento-gerando-apenas-para-funcion%C3%A1rio-demitido-ou-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25907090097559) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**O que verificar quando ao emitir o relatório de folha de pagamento (GPER106) para funcionário ativo, Sistema gera apenas para funcionário demitido ou em situação de férias?    
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Verifique o parâmetro no campo situação Folha se o campo chave está com o mesmo conteúdo do campo Situação Normal no cadastro de funcionário. Caso não esteja é necessário ajustar via configurador.   
  
Para correção abra o configurador: **Ambiente > Cadastro > Tabela > filtre pela tabela 31**

**1.** Clique em Editar (campo em amarelo):**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082571854)**

**2.** Clique em Itens e deixe o campo Chave da Situação Normal em branco, após clique em **Confirmar**:**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082572134)**Feito isso gere um novo relatório.

**Saiba mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
