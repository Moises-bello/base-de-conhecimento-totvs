---
article_id: 5421825426199
category: SIGAEST - CUSTOS
content_hash: c97c24bcb1969261c43076bc7ec7d5372510799803062aa456836cad83470e9e
fetched_at: '2026-06-28T22:39:02.137013+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como são
  gravados os níveis do arquivo de trabalho TRB?
type: support-article
updated_at: '2026-03-02T16:47:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5421825426199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-s%C3%A3o-gravados-os-n%C3%ADveis-do-arquivo-de-trabalho-TRB
---

**Dúvida**Como é gravado, os níveis gerados na tabela TRB no campo **TRB\_NIVEL**?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Essas informações, são contidas de forma interna**, pois se trata da geração e conceito atrelado por dentro do próprio sistema.  
  
Especificamente ao arquivo de trabalho TRB do recalculo do custo médio, ([Clique aqui e veja a FAQ com instruções sobre como extrair a TRB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011904591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-extrair-arquivo-de-trabalho-TRB-ao-executar-o-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-MATA330?source=search)) publicamos os campos de maior interesse externo que visam definir a ordenação de classificação e sequencia de calculo do custo, limitando aos campos **TRB\_DTBASE, TRB\_SEQPRO, TRB\_ORDEM, TRB\_NIVEL, TRB\_NIVSD3, TRB\_CHAVE, TRB\_SEQ** que fazem parte de uma das chaves de leitura do arquivo de trabalho e que determina a ordenação que o recalculo usará durante o processamento, e sua publicação é para orientar o cliente no caso que deseje intervir nesta ordenação mudando-a e customizando conforme suas considerações.  
  
Especificamente o campo **TRB\_NIVEL é o nível da estrutura do produto na ordem 300 (Movimentos internos)**, porem na Estrutura de produtos, o nível pode ser **01,02....99** e para que a ordenação no arquivo de trabalho corresponda a uma hierarquia é usado o nível invertido, ou seja, onde na estrutura o nível é 01 no arquivo será **99, 02 será 98** e assim nos demais níveis.

Os niveis gerados pela estrutura, são gravados na tabela auxiliar **TRBSG1SP.**  
  
Lembrando que este nível pode ser de forma direta através do nível da estrutura de produto ou de forma indireta pelos movimentos requisitados para uma OP, mesmo não tendo uma estrutura.  
(Isto é definido em um dos parâmetros do recalculo, chamado "Gera estrutura pela movimentação").

**Saiba mais sobre os perguntes do custo médio:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Perguntas do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)  
  
As letras agregadas ao nível são explicadas nos links mencionados.  
  
Considerando o parâmetro **MV\_SEQ300**, este irá instruir ao recalculo que considere os movimentos de ordem 300 de forma cronológica, ou seja, na ordem em que foram sendo movimentados no sistema e caso ocorra um movimento com data retroativa este será considerado na ordem em que foi movimentado.

[MV\_SEQ300 - Sequenciamento da Ordem 300 no Recálculo do Custo Médio](https://tdn.totvs.com/x/WrHPN)

Produtos que não possuem estrutura, ao processar o custo com o pergunte **"gera estrutura pela movi"** e **"recalcula niveis da estrutura"** ambos como NAO, dessa forma não sera gerado **NIVEL no arquivo TRB.**

**Saiba mais sobre a ordenação dos movimentos no custo médio:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é feita a ordenação dos movimentos após recálculo do custo médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17221653862551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-ap%C3%B3s-rec%C3%A1lculo-do-custo-m%C3%A9dio)

**Veja vídeo com instruções sobre como gerar e gravar a TRB**

***Saiba mais:***

*[SIGAEST - MATA330 - Como extrair arquivo de trabalho TRB ao executar o Recálculo do Custo Médio (MATA330)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011904591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-extrair-arquivo-de-trabalho-TRB-ao-executar-o-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-MATA330?source=search)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
