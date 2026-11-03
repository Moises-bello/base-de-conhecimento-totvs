---
article_id: 27875406336279
category: Gestão organizacional
content_hash: 86579aeca3ead5dd4b3c1c0f766715bfccccb8f1fdafdf7f23de93834453c4a3
fetched_at: '2026-06-28T22:47:22.248638+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processos Trabalhistas - Cadastro do S-2500 - Erro no campo
  Informações do evento: Deve ser igual a ''Sim'' se ''Tipo de vínculo'' for igual
  a 1,2,3 ou 4.'
type: support-article
updated_at: '2026-01-08T12:16:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27875406336279-RH-RM-RHU-Processos-Trabalhistas-Cadastro-do-S-2500-Erro-no-campo-Informa%C3%A7%C3%B5es-do-evento-Deve-ser-igual-a-Sim-se-Tipo-de-v%C3%ADnculo-for-igual-a-1-2-3-ou-4
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27875375413015) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao realizar o cadastro do S-2500 na inclusão do Contrato de Trabalho, o campo **Informações do evento** emite a seguinte mensagem de erro: ***Deve ser igual a 'Sim' se 'Tipo de vínculo' for igual a 1,2,3 ou 4.***  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - 12.1.2402.245, 12.1.2406.185 e 12.1.2410.121 e superiores.  
  
**Causa**  
O erro geralmente ocorre quando o campo **Informações do evento** for preenchido com a opção **Não** e o **Tipo de vínculo** for igual aos tipos de contratos de trabalho **1,2,3** ou **4.**   
  
**Solução**  
Conforme citado, esta mensagem será exibida quando o campo **Informações do evento** for preenchido com a opção **Não** e o **Tipo de vínculo** for igual aos tipos de contratos de trabalho **1,2,3** ou **4.**

**1** - Trabalhador com vínculo formalizado no eSocial, sem alteração nas datas de admissão e de desligamento.  
**2** - Trabalhador com vínculo formalizado no eSocial, com alteração na data de admissão.  
**3** - Trabalhador com vínculo formalizado no eSocial, com inclusão ou alteração de data de desligamento.  
**4** - Trabalhador com vínculo formalizado no eSocial, com alteração na data de admissão e inclusão ou alteração de data de desligamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27904604898967)

Para correção, deve informar no campo **Informações do evento** a opção **Sim**.

**Saiba Mais**

Para maiores informações, acesse:

- [Processo Trabalhista - Cadastros dos eventos S-2500 e S-2501](https://tdn.totvs.com/display/public/LRM/Processo+Trabalhista+-+Cadastros+dos+eventos+S-2500+e+S-2501)
