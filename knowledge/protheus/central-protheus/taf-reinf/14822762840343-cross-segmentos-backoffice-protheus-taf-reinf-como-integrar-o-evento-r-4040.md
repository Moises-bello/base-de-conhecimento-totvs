---
article_id: 14822762840343
category: TAF - REINF
content_hash: 0e2fddd30f11989251668f28e5296c7925af7ce7058212b4a8cf005a81006871
fetched_at: '2026-06-28T22:41:33.732020+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como integrar  o evento
  R-4040
type: support-article
updated_at: '2023-05-31T12:16:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14822762840343-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-o-evento-R-4040
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como gerar o evento R-4040 manualmente no TAF.  
  
**Ambiente**  
Microsiga Protheus - Livros Fiscais - A partir da versão 12.   
  
**Solução:**

O evento R4040  é relacionado a pagamentos/créditos a beneficiários não identificados.

O  cadastro para esse evento  pode ser preenchido de forma manual por meio do programa **TAFA542** ou pode ser integrado por meio do layout **T162/T162AA.**

Para incluir  esse evento manualmente no TAF  acesse a rotina  no caminho:

**Atualizações > Movimentos Reinf >  Retenção Recebimento/beneficiário Não identificado (TAFA542) > Incluir**

**Critérios:**

O  campo  Natureza da Fatura/Recibo  (**V4K\_INDNAT**)  deve ser igual a  0  ( A pagar ) ;

O  campo  Cod natureza Retenção (**V4K\_CODNAT**) deve ser preenchido com a  natureza de rendimento do grupo 19

O campo Data de Pagamento (**V4K\_DTPAG**) O mês/ano selecionado para apuração deve corresponder ao mês/ano de competência do pagamento.

O campo Valor  Reajuste  (**V4K\_VLREAJ**) deve ser preenchido  com o valor reajustado do pagamento.

O campo  Valor Base IR (**V4K\_BASEIR**)  deve ser preenchido com o valor de base do IRRF 

A informação do Código de Participante (**V4K\_CODPAR**) é obrigatória apenas quando a Natureza da fatura   (**V4K\_INDNAT**)  for igual a 1 (a Receber), uma vez que apenas no R-4080 há a obrigatoriedade de identificar a fonte pagadora do rendimento.

Segue o exemplo:

![4040.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14821580988695)

Após a apuração do  evento no painel Reinf,  o evento pode ser acessado através do menu:

**Eventos REINF > Periódicos > R-4040 - Pagamentos/créditos a beneficiários não identificados**

As tabelas envolvidas para esse evento são:

V4N - R-4040 Pgto/Credito Beneficiário não identificado  
V4O - Natureza do Rendimento          
V4P - Info Pgto. Beneficiário não identificado  
V9C - R4040 Info Processo Referenciado
