---
article_id: 16748624710039
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 09cb8eb49389481a9cf7ef8b5fa04777a64b6c6c816f40e93c2a27dd7aeb46fb
fetched_at: '2026-06-28T22:38:57.446384+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Transposição de estoque
  para Ativo Fixo
type: support-article
updated_at: '2026-04-07T16:05:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16748624710039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Transposi%C3%A7%C3%A3o-de-estoque-para-Ativo-Fixo
---

O processo de transposição de estoque para ativo fixo no TOTVS Backoffice (SIGAEST) ocorre via rotina de Movimentação Múltipla (MATA241), que gera ativos a partir de produtos em estoque. Para isso, configura-se o tipo de movimentação com os campos "Gera Ativo?", "Tipo Entrada" e "Atual. Ativo" marcados como "Sim". O custo pode ser médio ou da nota de aquisição, e o processo permite controle por lote.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16748647481239) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Qual o processo de Estoque que na baixa do item alimenta o Ativo Fixo através da transposição de estoque?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos (SIGAEST) - Todas as versões

**Solução**

A transposição de estoque é um processo que contempla a geração de ativos para produtos que estiverem no estoque através da rotina de Movimentação Múltipla (MATA241).

Esta condição proporciona mais flexibilidade nos processos de gestão que definem se o produto é um ativo da empresa ou se deve ser consumido. Dessa forma, é possível promover mais aderência na aplicação da regra de negócios.

**Campos chave:**

**Gera Ativo? (F5\_GERAATF)** - Informa se o tipo de movimentação informado irá gerar transposição de estoque para o ativo fixo.

**Tipo Entrada (F5\_TEATF)** - Tipo de entrada utilizada para gerar ativo fixo.

**Cust Med Ati (F5\_CUSTATF)** - Considera Custo Médio ao Gerar Ativo Fixo.

**Atual.Ativo (F4\_ATUATF)** com conteúdo igual a Sim.

O campo **F4\_BENSATF** da tes vinculado ao TM pode ser utilizado para desmembrar a geração dos itens no ativo fixo.

**Passos**

1. No módulo Estoque e Custos (SIGAEST), acesse **Atualizações > Cadastros > Fiscais > TES (MATA080)**.
2. Inclua ou altere um Tipo de Entrada e Saída (TES) garantindo que o campo **Atual. Ativo (F4\_ATUATF)** esteja preenchido com a opção **Sim**.
3. Acesse Atualizações > Cadastros > Movimentações > Internas (MATA230).

   Inclua um tipo de movimento para ser utilizado na circulação do estoque, preenchendo os campos obrigatórios e os de integração: **Gera Ativo? (F5\_GERAATF)**, **Tipo Entrada (F5\_TEATF)** e **Cust Med Ati (F5\_CUSTATF).**
4. Após geração do documentos de entrada, Acesse **Atualizações > Movimentações > Internas > Movimentação Múltipla (MATA241).**

   Clique em Incluir, selecione o produto para a requisição, preencha o tipo de movimento recém-criado e confirme a operação. A requisição gerada com o evento de inclusão de um movimento interno:

   **- RE0** caso voce opte pela TM de requisição olhar para o custo medio "**B2\_CM1**".

   **- RE6** caso não opte por usar o custo medio, mas sim o custo da nota de aquisição referida.

**O Custo** desejado, sera agregado na tabela **DH0**,

É possivel tambem, para produtos com controle de Lote, efetuar a seleção do lote, dessa forma sera validado a nota de entrada que deu origem ao lote.

**Caso não exista nota de entrada, assume sempre o custo médio.**

**Detalhes e informações tecnicas do processo:**

[Transposição de estoque para Ativo Fixo (SIGAEST)](https://tdn.totvs.com/x/DM4kJg)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Funcionalidade do campo F5\_GERAATF*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411465903383-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Funcionalidade-do-campo-F5-GERAATF)
