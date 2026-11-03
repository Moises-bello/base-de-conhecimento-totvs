---
article_id: 38505027100055
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 74b18f780374addd409c0a172a12ed444dd7d62de208febacc56fe22460a7b05
fetched_at: '2026-06-28T22:38:58.533112+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento – Backoffice (Linha Protheus) – SIGAEST – Inventário – Campo
  Documento gravado como "INVENT" na rotina de Inventário
type: support-article
updated_at: '2026-02-19T18:41:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38505027100055-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Invent%C3%A1rio-Campo-Documento-gravado-como-INVENT-na-rotina-de-Invent%C3%A1rio
---

No TOTVS Backoffice (Protheus), ao efetivar um acerto de inventário, o sistema grava automaticamente o campo “Documento” como “INVENT”, ignorando o valor digitado pelo usuário. Esse comportamento é padrão para padronizar, facilitar auditorias e identificar movimentos de inventário, não se tratando de uma inconsistência.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38505027082135) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Na rotina de **Digitação de Inventário**, o sistema permite que o usuário informe livremente o conteúdo do campo **“Documento”**, definindo o nome ou número desejado para aquele inventário.

Entretanto, ao salvar e posteriormente efetivar o acerto, o sistema grava o documento como **“INVENT”**, desconsiderando a informação digitada anteriormente.

Por que o sistema altera automaticamente o conteúdo do campo Documento para “**INVENT**”?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa:**  
Todo **Acerto de Inventário** realizado pela rotina **MATA340** gera um **movimento interno** por meio da rotina **MATA241**, ajustando a diferença entre:

* Quantidade contada no inventário
* Saldo anterior registrado no sistema

Por padrão do sistema, esse movimento é gravado com:

**D3\_DOC = "INVENT"**

Esse comportamento é nativo do sistema e tem como finalidade padronizar os movimentos originados por inventário.

**Solução:**

O preenchimento do campo **Documento** na digitação do inventário não é considerado no momento da geração do movimento interno.

O sistema grava automaticamente **“INVENT”** no campo **D3\_DOC** para:

* Identificar no **Kardex** (MATR900) que o movimento foi originado por inventário;
* Padronizar rastreabilidade;
* Facilitar auditorias e análises de movimentação;

Trata-se de comportamento padrão do sistema, não sendo uma inconsistência.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Controle de numeração D3\_DOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34841866033175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Controle-de-numera%C3%A7%C3%A3o-D3-DOC)
