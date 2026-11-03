---
article_id: 360033016073
category: SIGAEST - CUSTOS
content_hash: cfadb23b93d1b945fd136befe44ebb57f04ff0ef33a03402876d9305dac77f3c
fetched_at: '2026-06-28T22:39:00.622096+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como aglutinar os
  custos por empresa ou filial on-line?
type: support-article
updated_at: '2026-04-15T16:38:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033016073-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-aglutinar-os-custos-por-empresa-ou-filial-on-line
---

O parâmetro MV\_AGCUSTO permite aglutinar custos por empresa ou filial online, garantindo que todos os armazéns compartilhem o mesmo custo, sem precisar usar MV\_CUSMED = 'O'. Com MV\_AGCUSTO = .T., o cálculo dos custos é feito diretamente na tabela SB2, padronizando valores e facilitando a gestão dos custos médios nas movimentações de estoque. É necessário usar junto MV\_CUSFIL = 'E' ou 'F'.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28808001802519) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como aglutinar os custos por empresa ou filial? qual o conceito do parametro MV\_AGCUSTO?

**Ambiente**  
Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Todas as versões

**Solução**  
O parâmetro **MV\_AGCUSTO** foi implementado para permitir a **aglutinação de custos por empresa ou filial** de forma online, sem a necessidade de utilizar o parâmetro **MV\_CUSMED = 'O'**. Com essa configuração, o cálculo dos custos é realizado diretamente na tabela de saldos **SB2**, garantindo uma gestão mais eficiente e precisa dos valores, para que todos os armazens tenham o mesmo custo, quando sua aglutinação é por FILIAL ou EMPRESA.

Quando ativado, o parametro **MV\_AGCUSTO = .T.** possibilita que todos os armazéns de uma mesma empresa ou filial compartilhem o mesmo custo, garantindo padronização e consistência nos valores registrados para o calculo médio das movimentações **B2\_CM1** de forma equalizada.

Dessa forma, ao realizar movimentações de estoque, o sistema calcula e aplica os custos automaticamente sem a necessidade de processamento contábil específico para esta característica.

|  |  |
| --- | --- |
| **MV\_AGCUSTO** | Indica se deseja aglutinar os custos por empresa ou filial durante a inclusão dos movimentos.   * .T. - Aglutina. * .F. - Não aglutina. |

Para que a aglutinação ocorra corretamente, os seguintes somente se possuir custo por **EMPRESA** ou **FILIAL**, onde:

- **MV\_CUSFIL = 'E'** (Aglutinação de custos por Empresa) Ou  
- **MV\_CUSFIL = 'F'** (Aglutinação de custos por Filial)

Recomenda-se manter o **MV\_AGCUSTO** nessa condição de Filial e Empresa ativo, para garantir que os custos nos diversos armazéns sejam uniformes ao utilizar custo por empresa ou filial, fazendo sempre a atualização automatica a cada movimento registrado em estoque.

**Saiba mais:**

[*MP - SIGAEST - Rotina MATA330 - Perguntas do Recálculo do Custo Médio*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291)

[*MP - SIGAEST - MATR900 - Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio (com exemplo prático)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102)

[*MP - SIGAEST - Como extrair arquivo de trabalho TRB ao executar o Recálculo do Custo Médio (MATA330)?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011904591-MP-SIGAEST-Como-extrair-arquivo-de-trabalho-TRB-ao-executar-o-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-MATA330-)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
