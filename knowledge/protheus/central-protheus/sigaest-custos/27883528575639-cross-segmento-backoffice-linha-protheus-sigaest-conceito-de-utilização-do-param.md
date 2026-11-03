---
article_id: 27883528575639
category: SIGAEST - CUSTOS
content_hash: 4ab784076d541812f7ef0439dd454ca40836a479bdb8931cd1ee9157e9e214bf
fetched_at: '2026-06-28T22:39:00.813523+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito de utilização
  do parametro MV_SEQ300
type: support-article
updated_at: '2025-09-30T14:46:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27883528575639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-do-parametro-MV-SEQ300
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27883528546327) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Para que serve o parametro MV\_SEQ300, e oque ele faz com os movimentos internos da tabela SD3, após calculo de custo médio?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O parâmetro **MV\_SEQ300** indica se deve sequenciar a ordem **300** do arquivo de trabalho "**TRB**" da rotina de recalculo do custo médio **(.T. = Sequenciar / .F.= Não Sequenciar )**.

Implementado na rotina Recálculo do Custo Médio (**MATA330**) e Acompanha Custos (**MATA038**), visa ordenar os registros contidos no arquivo de trabalho (Tabela Temporária “**TRB**” gerada na execução da rotina de recálculo do custo médio) de forma que somente os registros que contenham o campo Ordem (**TRB\_ORDEM**) preenchidos com **300**, sejam ordenados pelo número sequencial da movimentação (**D3\_NUMSEQ**). O parâmetro é somente considerado quando utilizado os métodos de apropriação Mensal ou Diário.

Detalhes e exemplo: [MV\_SEQ300 - Sequenciamento da Ordem 300 no Recálculo do Custo Médio](https://tdn.totvs.com/x/WrHPN)

**Basicamente:** Se voce tem o parametro ativo, seus custos são calculados na ordem que foram digitados. E se voce desliga, eles são calculados conforme sua apropriação.

**Relacionado**:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é feita a ordenação dos movimentos após recálculo do custo médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17221653862551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-ap%C3%B3s-rec%C3%A1lculo-do-custo-m%C3%A9dio)

**Saiba mais:**

*[Clique aqui e veja artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)*

*[Clique aqui e veja artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
