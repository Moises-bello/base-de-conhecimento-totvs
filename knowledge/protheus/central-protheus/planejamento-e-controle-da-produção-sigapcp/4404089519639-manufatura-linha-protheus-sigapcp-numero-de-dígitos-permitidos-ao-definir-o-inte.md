---
article_id: 4404089519639
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ae1630e9397501c76b2a67180124121ccc63291728e05602ec9615124b4c5d9a
fetched_at: '2026-06-28T22:42:44.623075+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Numero de dígitos permitidos ao definir
  o intervalo da característica
type: support-article
updated_at: '2021-08-04T17:48:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404089519639-Manufatura-Linha-Protheus-SIGAPCP-Numero-de-d%C3%ADgitos-permitidos-ao-definir-o-intervalo-da-caracter%C3%ADstica
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao tentar definir como intervalo o tipo de uma característica no **MATA098 - Codificação**, está permitindo somente um dígito no preenchimento dos campos **De** e **Ate**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa situação ocorre quando a máscara definida para a característica comporta somente um dígito.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **MATA093 - Configuração** e consulte a família e característica em questão;  
2. Preencha corretamente o campo **BQ\_MASCARA - Máscara,** que deve ter o mesmo tamanho informado no campo **BQ\_TAMANHO - Tamanho**.  
  
**Exemplo**  
Se desejar que o intervalo vá de 1 a 99 o campo **BQ\_TAMANHO** deve ter o valor 2 e o campo **BQ\_MASCARA** deve ter o valor 99.  
Se desejar que o intervalo vá de 1 a 999, o campo **BQ\_TAMANHO** deve ter o valor 3 e o campo **BQ\_MASCARA** deve ter o valor 999.
