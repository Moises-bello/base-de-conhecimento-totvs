---
article_id: 4411465903383
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5710ea1704f1d015efe4d14b1268b5fcdd8c7050f8d38b9656b1b68765175d2b
fetched_at: '2026-06-28T22:38:55.544967+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Funcionalidade do
  campo F5_GERAATF
type: support-article
updated_at: '2026-04-07T16:13:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411465903383-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Funcionalidade-do-campo-F5-GERAATF
---

O campo F5\_GERAATF no TOTVS Protheus permite que, ao incluir um movimento interno, a movimentação gerada seja valorizada para evitar alterações de custo após recálculo de preço médio. O sistema busca notas fiscais que originaram o saldo do produto para determinar o custo e quantidade de ativos gerados, essenciais para o módulo Ativo Fixo e CIAP. Procedimentos devem ser testados fora do ambiente de produção.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39575705959447) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Qual a funcionalidade do campo F5\_GERAATF?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O campo **F5\_GERAATF** permite que, na inclusão de um movimento interno (similar a uma requisição RE6), a movimentação gerada seja valorizada, a fim de não sofrer alteração de custo após um eventual recálculo de preço médio.

No momento da inclusão, o sistema realiza uma busca no banco de dados para identificar as notas fiscais que originaram o saldo atual do produto. Isso determina o custo do movimento de requisição e a quantidade de ativos a serem gerados, uma vez que a geração de ativos ocorre por nota fiscal encontrada. A pesquisa identifica os documentos de entrada mais recentes (data de digitação em ordem decrescente) que somam a quantidade equivalente ao saldo atual do produto.

A partir desta verificação, o custo do bem para o módulo Ativo Fixo será determinado através da quantidade requisitada versus os documentos de entrada pesquisados (agora utilizados em ordem de digitação crescente). O mesmo procedimento é realizado para considerar os impostos calculados destas notas fiscais, sendo também consultado o tipo de movimentação para registrar o Tipo de Entrada e Saída vinculado através do campo Tipo de Entrada (**F5\_TEATF**). Essa etapa é indispensável para os casos em que há necessidade de gerar **CIAP** para o ativo criado.

**Observações importantes:**

* Nos casos que contemplam estorno de créditos pela geração de um bem, podem ser utilizadas as apurações de ICMS, IPI e PIS/COFINS para seus devidos acertos no livro fiscal.
* Dúvidas específicas referentes ao processamento e classificação dentro do Módulo Ativo Fixo devem ser validadas com o respectivo modulo.
* O suporte de Estoque/Custos não recomenda a execução deste procedimento de parametrização e teste diretamente em ambiente de produção.
* Verifique o parâmetro **MV\_ATFMOED**; quando configurado com valor diferente de 1, o sistema pode apresentar o [**HELP SN3DETAIL**.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17085684451735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-HELP-SN3DETAIL-VLDDATA-LINEPOST-ATFVALORUF-ao-tentar-incluir-uma-Movimenta%C3%A7%C3%A3o-Interna-de-Ativo-Fixo)

**Passos**

**Fluxo no módulo Estoque e Custos (SIGAEST):**

1. Acesse Atualizações > Cadastros > Fiscais > TES (**MATA080**).
2. Inclua ou altere um Tipo de Entrada e Saída (TES) garantindo que o campo Atual.Ativo (**F4\_ATUATF**) esteja preenchido com a opção Sim.
3. Acesse Atualizações > Cadastros > Movimentações > Internas (**MATA230**).
4. Inclua um tipo de movimento para ser utilizado na circulação do estoque, preenchendo os campos obrigatórios e os campos de integração: Gera Ativo? (**F5\_GERAATF**) e Tipo Entrada (**F5\_TEATF**).
5. Acesse Atualizações > Movimentações > Internas > Movim. Internas (**MATA241**).
6. Clique em Incluir, selecione um produto para a requisição e confirme a operação.

**Fluxo no módulo Ativo Fixo (SIGAATF):**

1. Acesse Atualizações > Cadastro > Ativo (**ATFA010**).
2. Realize a consulta do ativo que foi gerado e classifique-o, se necessário. Para relacionar as entidades de Ativo Fixo e Movimento Interno, **o sistema preenche o campo Num. Movimen (N1\_NUMSEQ) com o número da requisição de origem, permitindo o rastreio e estorno da ação.**
3. Para validar e consultar as notas fiscais que originaram o produto para o módulo de Ativo Fixo, retorne ao SIGAEST e acesse Relatórios > Análises > Notas Fiscais X Movim. Interno (**MATR324**), filtrando pela data de emissão do movimento interno.

**Saiba Mais**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[*SIGAEST - MATA241 - HELP SN3DETAIL VLDDATA\_LINEPOST ATFVALORUF ao tentar incluir uma Movimentação Interna de Ativo Fixo*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17085684451735)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Transposição de estoque para Ativo Fixo*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16748624710039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Transposi%C3%A7%C3%A3o-de-estoque-para-Ativo-Fixo)
