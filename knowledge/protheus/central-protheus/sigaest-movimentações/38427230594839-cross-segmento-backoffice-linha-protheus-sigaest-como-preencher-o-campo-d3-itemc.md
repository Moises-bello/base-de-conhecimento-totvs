---
article_id: 38427230594839
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 16b0ef7a885c939a540a9af1bf40a08989819124af1d3ff7813279ca8310f427
fetched_at: '2026-06-28T22:38:55.393155+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como preencher o campo
  D3_ITEMCTA no processo de Inventario?
type: support-article
updated_at: '2026-02-16T13:22:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38427230594839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-preencher-o-campo-D3-ITEMCTA-no-processo-de-Inventario
---

No ERP Protheus, o campo D3\_ITEMCTA (Item Contábil) não é preenchido automaticamente nas rotinas de inventário (MATA270/MATA340), diferentemente de outras movimentações internas. Para preenchimento obrigatório, é necessário desenvolvimento técnico via Pontos de Entrada ou gatilhos, pois não há regra nativa para isso.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38427230588951) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como preencher o campo D3\_ITEMCTA quando processamos o inventário?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

No padrão do ERP Protheus, o campo **D3\_ITEMCTA** (Item Contábil) não possui regra nativa para preenchimento automático ou manual durante as rotinas de **Digitação de Inventário (MATA270)** ou **Processamento de Inventário (MATA340)**.

Embora o campo esteja presente na tabela de movimentos internos (**SD3**), sua alimentação automática não está prevista no escopo funcional do inventário, permanecendo vazio após a efetivação dos acertos de estoque.

Diferente do inventário, outras rotinas de movimentação interna possuem regras de "herança" de dados mapeadas no código-fonte para o campo **D3\_ITEMCTA**. Para auxiliar na compreensão técnica, seguem exemplos de como o sistema se comporta em outros contextos:

* **Movimentações Internas (MATA242):** O sistema busca a informação diretamente do cadastro de produtos (`SB1->B1_ITEMCC`) ou prioriza o conteúdo preenchido no grid (`aCols`).
* **Apontamento de Produção Simples (MATA250):** A informação é herdada da Ordem de Produção (`M->D3_ITEMCTA := C2_ITEMCTA`).

**Conclusão:** Não há uma regra de herança similar (seja via Cadastro de Produtos ou Ordem de Produção) implementada nativamente para as rotinas de inventário.

Caso a alimentação deste campo seja um requisito mandatório para o fluxo contábil ou operacional da empresa, será necessária uma intervenção técnica, visto que o padrão não atenderá a essa demanda de forma nativa.

**Sugestões para o Desenvolvimento:**

1. **Pontos de Entrada:** Avaliar o uso de Pontos de Entrada nas rotinas de processamento de inventário para forçar a gravação do item contábil desejado na SD3.
2. **Gatilhos:** Implementar gatilhos de dicionário, caso a interface de digitação permita a interação.

> **Suporte Técnico:**
>
> Para dúvidas específicas sobre a sintaxe de funções AdvPL ou comportamento de classes, recomendamos o acionamento do time **PROTHEUS ADVPL** ou a consulta ao **DevForum**, visto que o suporte padrão não abrange a criação de códigos customizados.

Saiba Mais:

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
