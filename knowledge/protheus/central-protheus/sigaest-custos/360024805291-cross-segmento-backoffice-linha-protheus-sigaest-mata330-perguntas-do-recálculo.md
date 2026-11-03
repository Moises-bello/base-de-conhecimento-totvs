---
article_id: 360024805291
category: SIGAEST - CUSTOS
content_hash: d012583a467285c6cf18d82622c4af76cc101d36d9142d177ea5e08d1bb85902
fetched_at: '2026-06-28T22:39:00.412929+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Perguntas
  do Recálculo do Custo Médio
type: support-article
updated_at: '2026-05-21T21:48:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio
---

A rotina Recálculo do Custo Médio (MATA330) no TOTVS Protheus permite configurar parâmetros como data limite, visualização e aglutinação de lançamentos contábeis, atualização de movimentações, percentual de aumento na mão de obra, centros de custo, inibição de contas, exclusão de estornos, geração de lançamentos, estrutura provisória para produtos, método de apropriação (mensal, diária ou sequencial), e opções de cálculo por filial e custo em partes, garantindo controle e precisão no cálculo do custo médio.

**Dúvida**  
Qual o significado de cada pergunta na rotina Recálculo do Custo Médio (MATA330) ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Segue abaixo o significado das perguntas do Recálculo. Assim, podemos entender melhor quais opções deverão selecionar para que os movimentos sejam contabilizados da maneira desejada:

**Data Limite Final:** 

Data em que esta sendo efetuada a rotina.

**Mostra Lanç. Contábil:** 

Sim, para que o usuário possa visualizar os lançamentos contábeis, resultantes da rotina de recalculo do custo médio.

**Aglutina Lançamentos:** 

Se selecionado como "Sim", o sistema aglutina os lançamentos contábeis em um só lançamento.

**Atualiza Arq. Movimentação:**

**(OBRIGATORIO PARA ATUALIZAR AS MOVIMENTAÇÕES E CALCULO)**

Se selecionado como "Sim", o arquivo de movimentações internas (SD3), será atualizado bem como SD1, SD2, SDB e SD5. (Recomendável estar preenchido como "Sim").

**% de aumento na MOD:** 

Indica qual o percentual de aumento no custo da Mão de Obra Direta.

Segue documentação explicativa: 

[**Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Qual o significado da Pergunta "% de Aumento da MOD"?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414029760023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Qual-o-significado-da-Pergunta-de-Aumento-da-MOD)

**Centro de Custo:** 

Indica se os centros de custos são contábeis ou extra-contábeis.

**Conta a inibir de/Conta a inibir até**: 

Intervalo entre as contas contábeis a serem inibidas (não receberão lançamentos).  
 

**Apaga Estornos:**

Na lista de perguntas da rotina de recálculo do custo médio configure o parâmetro **Apagar Estornos?** com o conteúdo igual a **Não**, com esta configuração a rotina não irá executar a limpeza de registros estornando gerando uma melhora na performance da rotina.

**(aviso) Importante:** O uso da pergunta **"Apaga Estornos = Sim"** **com o uso de procedures, irá excluir fisicamente os itens estornados nos movimentos internos da tabela SD3**, **nos movimentos de requisições por lote da tabela SD5 e nos movimentos de distribuição da tabela SDB, no período executado, afim de diminuir o volume de dados a serem tratados visando melhor performance**.

**Já o uso sem procedures**, estes itens estornados **são marcados como deletados permanecendo na base.** O maior motivo de serem marcados com delete é que nas versões antigas do Protheus não era possível no ADVPL excluir fisicamente os registros estornados, apenas marca-los como o delete.

**Gera Lançamento Contábil:** Se selecionado como "**Sim**", o sistema gera lançamentos contábeis nesta rotina, ou seja, contabilizará ou recontabilizara os movimentos. **E sempre, sera primeiro APAGADO os lançamentos do periodo em ABERTO**, para que sejam refeitos, pois isso é um processo para não existir DUPLICIDADE de lançamentos.

Se estiver = **Não**: o Protheus **apaga** os Lançamentos Contábeis da tabela CT2 do período de processamento em aberto.

Se estiver = **Mantém Lançamentos:** O Protheus apenas mantém os lançamentos, não apaga e nem gera a contabilização dos movimentos internos do estoque, vai deixar como está.  
 

**Gera estrutura pela movimentação:**

Se usado como "**Sim**", o Protheus passa a gerar uma estrutura **provisória para os produtos produzidos no período, calculando assim adequadamente o custo primeiro das MPs, PIs e depois PAs se baseando nas movimentações SD3 e geração da tabela temporária TRBSPSG1 para ordenação das movimentações CASO OS PRODUTOS DE INSUMOS, NÃO POSSUAM ESTRUTURA CADASTRADA NA SG1 e você não possua cenarios recursivos.** dessa forma a serem efetuadas gravando o nível de acordo a estrutura cadastrada do produto, ou então temporária caso o produto de consumo não faça parte da OP e necessite então de uma estrutura para cálculo temporário. Com a utilização deste parâmetro como "Sim", o sistema também detectará se o usuário tem problema de recursividade na base de dados, que são movimentos de requisição de um produto para ele mesmo dentro de uma OP, este movimento é comum para quem efetua retrabalho nos produtos.

**Contabilização Por?:** 

Consumo (movimentação de materiais), Produção (informe de produção) ou Ambas (consumo e produção).

**Calcula Mão de Obra:** 

Se preenchido como "Sim", irá pegar o valor acumulado no centro de custos na contabilidade e irá calcular o valor médio da mão de obra daquele período. Se preenchido como "Não", irá pegar o valor existente no campo B2\_CM1 do produto e dividir por local.

**Método de Apropriação**

**ATENÇÃO, ISSO É DEFINIDO NA IMPLATAÇÃO DE CUSTOS, A ALTERAÇÃO DA APROPRIÇÃO SEM CONHECIMENTO, VAI ALTERAR A FORMA A QUAL OS CUSTOS SÃO RECALCULADOS NO SEU AMBIENTE:**

**- Mensal** (Custo Médio calculado pela movimentação mensal dos materiais, ou seja, o sistema apura todas as entradas do mês, calcula o custo médio ponderado, e valoriza todas as saídas com este custo).

**- Diária** (Custo Médio calculado pela movimentação diária dos materiais, seguindo o mesmo critério do mensal, porém para os movimentos de cada dia).

**- Sequencial** (Custo Médio calculado a cada movimentação dos materiais). 

**Recalcula níveis pela estrutura:** 

Se preenchido como "Sim", alinha o nível da estrutura do produto, se "Não" ele não tentara refazer o nivel da estrutura dos itens que tenham ou não estrutura.

**Mostra Sequência de Cálculo**: 

Se selecionada como "Não", esta visualização serve para analise do arquivo de trabalho gerado pelo sistema, este arquivo determina a sequência de calculo de cada produto em decorrência dos movimentos, ela pode ser alterada para que determinadas necessidades sejam atendidas no momento do calculo.

**Sequência FIFO:** 

Seq. Calc./ CM (somente para empresas que utilizam custo FIFO).

**Movimentos internos valorizados**: 

Processam os movimentos internos valorizados antes ou depois dos demais movimentos internos.

**Recálculo custo de transportes:**

Não é utilizada, foi criada para futuras integrações, porém não trata. Pode ser usada com qualquer conteúdo pois não interferirá no recálculo.

**Cálculo do custo por:** 

indica se o custo médio devera ser processado considerando:   
- Todas filiais - considera os movimentos de todas as filiais da empresa corrente.   
- Filial corrente - considera os movimentos somente da filial corrente.   
- Seleciona filiais - permite a escolha de quais filiais da empresa corrente serão consideradas para recalculo do custo.

**Calcular custo em partes:** 

Indica se o calculo do Custo em Partes será executado.   
- Sim = Calcula Custo em Partes.   
- Não = Custo Partes não será calculado.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
