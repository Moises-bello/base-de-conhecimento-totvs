---
article_id: 4421540343063
category: SIGAEST - CUSTOS
content_hash: 989d76559c45b2ab8fe32a347c0e75393267693d19e0300d7e8049b7552d61f4
fetched_at: '2026-06-28T22:39:02.259232+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Movimentos de Transferência
  (DE4) e Desmontagem (DE7) no Recálculo do Custo Médio
type: support-article
updated_at: '2025-03-12T12:26:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421540343063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Movimentos-de-Transfer%C3%AAncia-DE4-e-Desmontagem-DE7-no-Rec%C3%A1lculo-do-Custo-M%C3%A9dio
---

**Dúvida**

Como são ordenados os Movimentos de entrada de **Transferência** (DE4) e **Desmontagem** (DE7) são no **Recálculo do Custo Médio?**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Movimentos de entrada de **Transferência** (DE4) e **Desmontagem** (DE7) são ordenados ao final de todos os movimentos do período ao processar o **Recálculo do Custo Médio**.

O Recalculo do Custo Médio (MATA330), quando processado por apropriação **Mensal** ou **Diária**, utiliza uma chave:

**(TRB\_DTBASE+TRB\_SEQPRO+TRB\_ORDEM+TRB\_NIVEL+TRB\_NIVSD3+TRB\_CHAVE+TRB\_SEQ)**

Para ordenação dos movimentos no arquivo de trabalho (TRB). Esta chave utilizada para ordenação atende o processo produtivo da grande maioria das empresas, porém em alguns processos, devido a sequência em que os movimentos são gerados, as **Transferências** (RE4 / DE4) e **Desmontagens** (DE7 / RE7) podem não ser ordenados conforme o esperado.

Para estas situações existe o parâmetro **MV\_SEQ300**, que tem como objetivo ordenar os movimentos de **Ordem 300** (Movimentos Internos) por sequência de inclusão (**D3\_NUMSEQ**) ignorando a chave padrão.

Com a ativação do parâmetro a grande maioria das exceções são tratadas e solucionadas.

No entanto existem processos muito específicos que mesmo a ativação do parâmetro não realiza a ordenação esperada dos movimentos.

Para estes casos será necessário utilizar o ponto de entrada **MA330TRB** para manipular o arquivo de trabalho (TRB) e definir uma regra especifica de ordenação com base nos movimentos do cliente.

Quando há a necessidade de utilização do ponto de entrada, o processo do cliente deve ser estudado para identificar um padrão para as movimentações e consequentemente uma regra para ordenação delas, junto a um Desenvolvedor/Programador.

**Saiba mais**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

[*FAQs - Estoque e Custos*](https://tdn.totvs.com/display/public/PROT/FAQs+-+Estoque+e+Custos)
