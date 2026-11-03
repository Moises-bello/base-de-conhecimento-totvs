---
article_id: 17221653862551
category: SIGAEST - CUSTOS
content_hash: 97616beb01f668acfe15f12c0a9a57a5df9c78e285f42f7a3b2883f33a997ddf
fetched_at: '2026-06-28T22:39:00.738456+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é feita a ordenação
  dos movimentos após recálculo do custo médio?
type: support-article
updated_at: '2026-06-17T18:43:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17221653862551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-ap%C3%B3s-rec%C3%A1lculo-do-custo-m%C3%A9dio
---

O Protheus utiliza o método de Média Ponderada para recálculo do custo médio, organizando os movimentos de estoque na tabela TRB para garantir a Ordem Fiscal, processando entradas antes das saídas. A ordenação depende do método de apropriação escolhido e o campo TRB\_ORDEM classifica os movimentos em blocos numéricos. Para ajustes na ordenação de movimentos internos, pode-se usar o parâmetro MV\_SEQ300 ou o ponto de entrada MA330TRB. Transferências entre filiais são tratadas como movimentos internos para manter o custo correto.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17221633602327) Tempo aproximado para leitura: **00:09:05 min**  
  
**Dúvida**  
Como é realizada a ordenação após processamento do recalculo de custo médio?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

**1. Objetivo do Recálculo (Ordem Fiscal)**

O Protheus utiliza o método de **Média Ponderada** (aceito pelo Fisco). O objetivo principal da rotina de recálculo é organizar os movimentos de estoque (Entradas, Internos e Saídas) para garantir a **Ordem Fiscal**. Isso significa assegurar que as entradas de materiais **(Notas Fiscais de Compra)** ocorram antes das saídas **(Notas Fiscais de Venda)** dentro do período apurado.

O recálculo do custo médio é processado em etapas (preparação de saldos, cálculo de mão de obra, níveis de estrutura, etc.). A etapa central é a montagem da tabela temporária TRB. A TRB centraliza e rastreia todas as movimentações do período. Ela é a responsável absoluta por organizar a sequência em que os custos serão aplicados, movimentação por movimentação, antes de gravar os dados definitivos no sistema (tabela SB2).

**2. Como a Ordenação é Feita (Tipos de Apropriação)**

A ordem em que o sistema processa os movimentos na TRB é definida pelo Índice 3, que é composto pela seguinte chave: `TRB_DTBASE + TRB_SEQPRO + TRB_ORDEM + TRB_NIVEL + TRB_NIVSD3 + TRB_CHAVE + TRB_SEQ`

A forma como essa chave é preenchida depende do **Método de Apropriação** escolhido:

* **Sequencial:** Processa os movimentos exatamente pelo número sequencial em que foram digitados no sistema.
* **Diária ou Mensal:** O sistema organiza os movimentos em um arquivo de trabalho (chamado **TRB**) utilizando uma regra que considera: *Data do movimento + Sequência + Ordem + Nível dos materiais na estrutura (produto pai/filho)*.

  [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Quais são os Métodos de Apropriação para execução do Recálculo do Custo Médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033673914-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Quais-s%C3%A3o-os-M%C3%A9todos-de-Apropria%C3%A7%C3%A3o-para-execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)

  ![Etapas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41152363099031)

**3. Sobre o calculo e ordenação dos movimentos internos, ordem 300.**

O campo mais importante para garantir a Ordem Fiscal e lógica é o `TRB_ORDEM`. O sistema classifica as notas e movimentos em blocos numéricos para garantir que as "entradas" valorizem o estoque antes das "saídas":

Segue um resumo com exemplo sob algumas:

* **Ordem 100 (Notas de Entrada):** Processadas primeiro para dar valor ao estoque.

  + *Exceção CQ (Ordem 110):* Liberações de Controle de Qualidade geram transferências internas. Elas caem na ordem 110 para serem valorizadas imediatamente com o mesmo custo da Nota de Entrada 100 associada.
* **Ordem 150 (Devolução de Compra):** Abate as entradas do período.
* **Ordem 200 (Devolução de Venda de Períodos Anteriores):** Entram no início do cálculo pois precisam devolver o produto ao estoque com o custo *do período passado*, antes que as novas regras alterem o custo atual.
* **Ordem 250 a 290 (Terceiros):** Remessas e devoluções de/para terceiros.
* **Ordem 300 (Movimentos Internos):** Requisições, produções, transferências e desmontagens (detalhado na próxima seção).
* **Ordem 500 (Notas de Saída / Vendas):** Retiram o produto com o custo já totalmente apurado e formado pelas etapas anteriores.

  + *Devoluções do mesmo período:* Caem junto à Ordem 500, garantindo que se anulem com as saídas recentes.
* **Ordem 600 (Reavaliação de Custo Médio):** Lançamentos manuais ([MATA338](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020608652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Reavalia%C3%A7%C3%A3o-de-Custo-M%C3%A9dio-MATA338)) para forçar um custo final. Processados por último para calcular a diferença exata necessária para atingir o custo desejado pelo usuário, a ser levado para o "Proximo Periodo"!

  [Lista geral TRB - Ordenacao dos movimentos](https://tdn.totvs.com/x/A9pc)

Muitas vezes, a ordenação padrão (Diária/Mensal) pode não organizar as movimentações internas (Movimentos de Ordem 300, como requisições e produções) da forma que a empresa espera, pois isso depende de n fatores, e esses movimentos dependem exclusivamente das configurações e apropriações, então pode variar de cliente para cliente, mas existem duas soluções para isso, caso a ordem dos movimentos internos, não seja a mais adequada para a necessidade da empresa:

* **Parâmetro** `MV_SEQ300`**:** É a solução mais comum. Ao ativar este parâmetro, o sistema ignora a regra padrão e passa a ordenar os movimentos internos apenas pela sua **sequência de inclusão(D3\_NUMSEQ)**. Isso resolve a grande maioria dos casos de ordenação incorreta. [Recálculo do custo médio - apropriação sequencial e MV\_SEQ300](https://tdn.totvs.com/x/eoQNOw)
* **Ponto de Entrada** `MA330TRB`**:** Se o parâmetro não resolver por conta de um processo produtivo muito específico, a solução é utilizar este Ponto de Entrada. Ele permite manipular o arquivo TRB e criar uma regra de ordenação sob medida para a empresa. [PE MA330TRB - Manipulação deste arquivo antes do processamento](https://tdn.totvs.com/x/2uNc)

**4. Notas Fiscais de Transferência entre Filiais**

* Por padrão, o Protheus trata transferências como movimentações internas para garantir que o custo da filial de origem seja transferido para a de destino.
* Se você processar o custo de todas as filiais ao mesmo tempo, ele manterá essa amarração.
* Se processar o custo de uma filial por vez (paralelo), ele manterá a ordem fiscal pura **(Tipo 100 para entrada e 500 para saída)**. O Ponto de Entrada `MA330TRB` também pode ser usado para forçar a ordenação fiscal nas transferências se assim desejar.

**5. Como Validar se a Ordem Está Correta?**

Para confirmar se a ordenação calculada está certa, você deve analisar o arquivo gerado de trabalho (**TRB**) através do sistema *(APSDU baixando o arquivo em formato Sqlite, e abrindo em um programa externo, como Sqlite ou outro, para aplicar o indice, ou consultar diretamente na base de dados)*, filtrando o produto ou filial desejada. A sequência mostrada neste arquivo deve espelhar exatamente a sequência apresentada no **Relatório Kardex (** [**MATR900**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Como-parametrizar-o-relat%C3%B3rio-Kardex-por-Per%C3%ADodo-MATR900) **ou** [**SmartView**](https://tdn.totvs.com/x/VyueLQ)**), de acordo aplicação do indice de calculo no seu arquivo TRB**

O indice padrão da apropriação Diaria ou Mensal é:

```
DTOS(TRB_DTBASE)+TRB_SEQPRO+TRB_ORDEM+TRB_NIVEL+TRB_NIVSD3+TRB_CHAVE+TRB_SEQ
```

Para consulta no banco, de acordo sua necessidade, exemplo em SQL:

```
SELECT * FROM TRB01SP WHERE TRB_COD IN ('PA12345') ORDER BY
TRB_DTBASE,TRB_SEQPRO,TRB_ORDEM,TRB_NIVEL,TRB_NIVSD3,TRB_CHAVE,TRB_SEQ
```

**Observação:** O nome da tabela TRB no banco de Dados é composto por: "**TRB+Código da Empresa+SP**"

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
