---
article_id: 25307319775767
category: SIGAEST - CUSTOS
content_hash: d668f655c0303cc2be6e7dd03655958c09b69fcef43af1a0b5a173783bc34340
fetched_at: '2026-06-28T22:39:01.981553+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Incluir Custo de um
  Serviço em OP sem alterar Estrutura do PA
type: support-article
updated_at: '2025-03-12T12:25:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25307319775767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Incluir-Custo-de-um-Servi%C3%A7o-em-OP-sem-alterar-Estrutura-do-PA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25307319735319) Tempo aproximado para leitura: **00:04:30 min**

**Dúvida**

Como incluir o **Custo de Serviço** em uma Ordem de Produção na qual o Serviço não seja um **produto MOD, Gastos Gerais** e também que o mesmo **não faça parte da Estrutura do Produto Acabado**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Vamos exemplificar com o seguinte cenário:

 - Temos uma estrutura de um **Produto Acabado** que utiliza uma **Matéria Prima**, e por qualquer motivo precisamos efetuar um Serviço Interno onde o Prestador emite uma Nota Fiscal desse Serviço. Nesse exemplo a Matéria Prima tem um Custo (B2\_CM1) de R$ 100,00 e foi efetuado um Serviço que custou R$ 50,00.

![estrutura pa.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25308449674263)

 - É necessário a criação do Cadastro do Produto que será o Serviço utilizado na OP, sugerimos **tipo Serviço (B1\_TIPO=SV)**.

![produto sv.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25308662437143)

 - Incluir a **Ordem de Produção (MATA650)** para o Produto Acabado (PA);

![ordem producao.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25309611961879)

 - Incluir Documento de Entrada informando, **Quantidade, Valor do Serviço**, utilizar uma **TES que Atualize Estoque (F4\_ESTOQUE=S)** e principalmente informar o campo **Ordem de Produção (D1\_OP)** indicando a OP que vai receber o Valor do Serviço;

![d1_op.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25314093392535)

 - Na rotina MATA250 apontar a Produção;

![aponntamento ordem producao.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25314374355863)

- Efetuar o processamento do recalculo de custo médio;

 - Verifique agora no Relatório **Detalhamento de Ordem de Produção (MATR860)** o resultado obtido para o Produto Acabado no Custo e observe as movimentações geradas;

![MATR860 PARAM.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25314717218327)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25314717226007)

**OBSERVAÇÕES:** Gerou o **movimento tipo RE5** indicando que foi direcionado diretamente na OP, **apropriando o Custo do Serviço de forma correta** sem que efetue alterações no cadastro da Estrutura do Produto Acabado. Nesse cenário de exemplo o Custo do PA ficou R$ 150,00 corretamente.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - O que é um produto do tipo MOD e GGF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5986881139607-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-que-%C3%A9-um-produto-do-tipo-MOD-e-GGF?source=search)
