---
article_id: 36890554604311
category: SIGAEST - MOVIMENTAÇÕES
content_hash: efd8935afd4d6378091a909c8bf5637829d75eed3c2885dfee8d3cdd734a290c
fetched_at: '2026-06-28T22:38:54.044420+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Uso do campo
  Quantidade(CP_QUANT) na regra de  lançamento do PCO
type: support-article
updated_at: '2025-12-09T17:25:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36890554604311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Uso-do-campo-Quantidade-CP-QUANT-na-regra-de-lan%C3%A7amento-do-PCO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36890554595351) Tempo aproximado para leitura: **01:00 min**  
  
**Dúvida**  
Como utilizar o campo CP\_QUANT na configuração da regra de bloqueio de lançamento do PCO (PCOA035)?  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
No momento em que a tela de inclusão da Solicitação ao Armazém (MATA105) está aberta, as informações que são digitadas pelo usuário estão em memória.

Dessa forma, para utilizar as informações em memória como por exemplo a do campo CP\_QUANT que será digitada, é necessário utilizar funções como a GDFieldGet("nome do campo") na regra para o lançamento no módulo de PCO.

**Exemplo**

Ao invés de escrever:

```
SB1->B1_UPRC*SCP->CP_QUANT
```

Deve-se utilizar a fórmula:

```
SB1->B1_UPRC*GDFieldGet("CP_QUANT")
```

No exemplo acima, o conteúdo do campo B1\_UPRC está gravado no Banco de Dados, por isso pode ser chamado diretamente. Já o conteúdo do campo CP\_QUANT está sendo digitado em tela, necessitando do tratamento através da função GDFieldGet.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

# [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Solicitação, Pré-Requisição e Baixa da Pré-Requisição MATA105 - MATA106 - MATA185](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Solicita%C3%A7%C3%A3o-Pr%C3%A9-Requisi%C3%A7%C3%A3o-e-Baixa-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-MATA105-MATA106-MATA185)
