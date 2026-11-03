---
article_id: 19846202661911
category: Materiais - Compras (SIGACOM)
content_hash: 383fb00dabc3b79b84d9f1909004bf30320e1e0342ae946d8fa42b4681718ee6
fetched_at: '2026-06-28T22:41:20.079113+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - MATA103 - Ocorrências
  do help A103APOESP
type: support-article
updated_at: '2023-12-14T17:24:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19846202661911-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-MATA103-Ocorr%C3%AAncias-do-help-A103APOESP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19846156420375) Tempo aproximado para leitura: **04:00:00 min****Ocorrência**Ao incluir um documento de entrada, sistema gera o help A103APOESP.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19846202618775)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.33  
  
**Causa**

O help A103APOESP é gerado quando a soma dos três valores referentes à aposentadoria é maior que o valor total do item. Nesta rotina, o fonte possui a função A103ApoTok() de validação que verifica se os valores de aposentadoria digitados estão coerentes.

Para acessar a tela de digitação dos valores da aposentadoria especial, é necessário clicar em "Outras Ações" -> Apos. Especial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19846144005783)

O sistema irá abrir a tela abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19846156426775)

Essas informações são gravadas por linha, ou seja, a cada item individualmente. São gravadas na tabela DHP. Na função A103ApoTok(), o sistema realiza as verificações abaixo:

1. Se foi digitado algum valor nesses campos;

2. Se sim, ele soma esses três valores (DHP\_FAIXA1 + DHP\_FAIXA2 + DHP+FAIXA3);

3. Valida se essa soma é maior que o valor total do item D1\_TOTAL;

4. Se sim, gera o help A103APOESP informando isso ao usuário.

**Solução**Verificar os valores que foram digitados nos campos DHP\_FAIXA1, DHP\_FAIXA2, DHP+FAIXA3. A soma desses três valores deve ser menor que o valor D1\_TOTAL do item em questão.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Aposentadoria especial Tela apresentada sem o grid para incluir os percentuais da aposentadoria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038352734-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Aposentadoria-especial-Tela-apresentada-sem-o-grid-para-incluir-os-percentuais-da-aposentadoria)
