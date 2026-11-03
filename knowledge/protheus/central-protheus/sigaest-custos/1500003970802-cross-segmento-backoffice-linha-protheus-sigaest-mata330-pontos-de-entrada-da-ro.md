---
article_id: 1500003970802
category: SIGAEST - CUSTOS
content_hash: 179dad563af21510f07a170337be429247ab6f36893aa71a0058f4d90ddf5e97
fetched_at: '2026-06-28T22:39:02.206428+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Pontos de
  Entrada da rotina Recálculo do Custo Médio
type: support-article
updated_at: '2026-02-06T15:06:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003970802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Pontos-de-Entrada-da-rotina-Rec%C3%A1lculo-do-Custo-M%C3%A9dio
---

**Dúvida**  
Quais os Pontos de Entrada do Recálculo do Custo Médio - MATA330? Quais as suas funções no Protheus?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Veja abaixo os Pontos de Entrada relacionados ao Recálculo do Custo Médio - MATA330

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada:** | **Título:** | **Descrição:** |
| [**MA330CP**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087631) | Define regras para classificação de matéria-prima | LOCALIZAÇÃO : Function MATA330( ) - Localizado nas rotinas de processamento de custo em partes.  DESCRIÇÃO : O recálculo do custo médio possibilita dividir o custo de produtos fabricados em mais de uma parte, facilitando a visualização da composição de custos dos produtos acabados. |
| [**MA330CTB**](https://tdn.totvs.com/pages/releaseview.action?pageId=461909699) | Customização após o recálculo contábil | O Ponto de Entrada MA330CTB foi implementado na rotina MATA330 para ser acionado quando Quando a pergunta Gera lancto. Contábil? da MATA330 for igual a Sim ou Não.  Eventos: Após reprocessar os lançamentos contabeis apagados e antes de processar o recalculo de custo |
| [**MA330TRB**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087642) | Manipulação deste arquivo antes do processamento | O Ponto de entrada é executado após a gravação de todas as partes do arquivo de trabalho que serão utilizadas na rotina de recalculo do custo médio, este ponto tem como objetivo a manipulação deste arquivo antes do processamento.  Apesar de não ser recomendado, mas se voce deseja tal customização: Voce pode usalo para filtrar tipos de produto, a serem ou nao calculados, mas isso requer uma validação interna junto com o desenvolvedor da customização, para certificar da gravação ou não dos saldos iniciais. |
| [**MA330FIM**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087635) | Customizações no final da rotina | Executada após todo o processamento do recalculo do custo médio para que se possa realizar customizações no final da rotina. |
| [**MA330MOD**](https://tdn.totvs.com/pages/releaseview.action?pageId=832651171) | Customiza o cálculo do custo de mão-de-obra | LOCALIZAÇÃO : Function MA330Mod - Função que calcula o custo das requisições de mão de obra feitas no período, localizado no fonte do MATA330. |
| [**A330GRUP**](https://tdn.totvs.com/pages/releaseview.action?pageId=651923919) | Considera Grupo Contábil | O ponto de entrada A330GRUP será utilizado para definir se na apuração do custo da mão-de-obra, será considerado o grupo contábil informado no cadastro do produto por meio do campo 'Gr cnt Custo' (B1\_GCCUSTO). |
| [**A330DECC**](https://tdn.totvs.com/pages/releaseview.action?pageId=419549295) | Cria cálculo customizado de despesa de centro de custo | O Ponto de Entrada A330DECC permite criar um cálculo customizado de despesa de centro de custo, sobrepondo o cálculo atual realizado pela função MA330SalCC. |
| [**A330QTMO**](https://tdn.totvs.com/pages/viewpage.action?pageId=745130942) | Realiza ajustes na quantidade apurada da mão-de-obra | Ponto de entrada utilizado para realizar ajustes na quantidade apurada da mão-de-obra, este ponto e executado antes da gravação do registro do MOD na tabela SB2 |
| [**M330FCC**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087589) | Filtra Contas Contábeis para o Cálculo nos Centros de Custo | O ponto e chamado no momento que o sistema filtra as contas contabeis para o calculo de valor nos centros de custo que resultarão no valor da MOD. |
| [**MA330SEQ**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087641) | Permite alterar a ordem do recálculo do custo médio, alterando o campo TRB -> TRB\_ORDEM | O Ponto de entrada e executado no inicio da função A330TRB( ), onde permite alterar a ordem de recalculo do custo medio, alterando o campo TRB->TRB\_ORDEM. |
| [**MA330D1**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087632) | Atualiza SB2 após gravar SD1 | O Ponto de Entrada e utilizado apos a gravação dos movimentos SD1 e a devida atualização do SB2. |
| [**MA330D2**](https://tdn.totvs.com/display/public/PROT/MA330D2) | Atualiza SB2 após gravar SD2 | O Ponto de Entrada e utilizado apos a gravação dos movimentos SD2 e a devida atualização do SB2.  Eventos |
| [**MA330D3**](https://tdn.totvs.com/display/public/PROT/MA330D3) | Atualiza SB2 após gravar SD3 | O Ponto de Entrada e utilizado apos a gravação dos movimentos SD3 e a devida atualização do SB2.  Eventos |
| [**MA330P3**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087639) | Alterar o valor do custo médio em partes de movimentos internos | O Ponto de entrada e executado apos a gravação do custo dos movimentos SD3, este ponto de entrada e utilizado para alterar o valor do custo medio em partes dos movimentos internos RE0,1,2,3 e suas DE's respectivas. |
| [**A330CDEV**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087864) | Contabilização dos movimentos de devolução de compras | Ponto de Entrada utilizado para permitir que os movimentos de devolução de compras sejam contabilizados nas rotinas Recálculo do Custo Médio (MATA330) e Contabilização do Custo Médio (MATA331). |
| [**M330CD2**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087587) | Altera o custo médio unitário da Nota Fiscal de Saída | Descrição: LOCALIZAÇÃO : Function A330Recalc - Função utilizada para recalcular o custo medio dos movimentos.  EM QUE PONTO : Executada antes de atualizar o custo medio unitario dos itens das NFs de Saida, este ponto de entrada tem a finalidade de alterar o custo medio unitario dos itens da Nota Fiscal de Saida (SD2) |
| [**MA330C3**](https://tdn.totvs.com/display/public/PROT/PEST07667_MA330C3+-+Altera+o+Custo+dos+Movimentos) | 'Altera o Custo dos Movimentos | O Ponto de Entrada MA330C3 é utilizado após a gravação dos movimentos (SD3) e a devida atualização do saldo (SB2). |
| [**M330CD1**](https://tdn.totvs.com/display/public/PROT/M330CD1+-+Manipula+custo+em+parte+nas+notas+de+entrada) | Manipula custo em parte nas notas de entrada | Descrição: LOCALIZAÇÃO : Function A330Recalc - Função utilizada para recalculo o custo medio dos movimentos.  EM QUE PONTO : Executada antes de realizar a atualização do custo em partes dos movimentos de entrada 'SD1' que possuem o D1\_TIPO diferente de 'D'. O Ponto de Entrada e utilizado para manipular o custo em partes das notas de entrada. |
| [**MA330AL**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087629) | Valida filtro do armazém | Descrição: LOCALIZAÇÃO : Function A330Inicia( ) - Função utilizada para pegar valores do inicio do periodo para serem reprocessados.  EM QUE PONTO : O Ponto de Entrada e utilizado para validar se devera filtrar o armazem na rotina de recalculo do custo medio. |
| [**M330CMU**](https://tdn.totvs.com/pages/viewpage.action?pageId=804621965) | altera o custo médio unificado para os produtos | Descrição: LOCALIZAÇÃO : Function A330Inicia - Função utilizada para pegar os valores do inicio do periodo para serem reprocessados.  EM QUE PONTO : Executada antes de atualizar o custo medio unificado. O Ponto de entrada M330CMU e utilizado no recalculo do custo medio quando o parametro MV\_CUSFIL estiver com o conteudo igual 'S', este ponto de entrada serve para alterar o custo medio unificado para os produtos. |
| [**MA330OK**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087638) | Validar execução do recálculo do custo médio | Descrição: LOCALIZAÇÃO : Function MTA330TOk() - Função que valida se pode efetuar o recalculo do custo medio.  EM QUE PONTO : O Ponto de entrada e executado no inicio da função MTA330TOk(), utilizado para validar se permite executar o recalculo do custo medio. |
| [**MA330PRC**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087640) | Desliga o processo de transferência de materiais no recálculo do custo médio | Ponto de entrada utilizado para desligar o processo de transferência de materiais executado na rotina de recalculo do custo médio. Somente devera ser utilizado por clientes que não utilizam o processo de transferência de matérias do produto Protheus Estoque e Custos e desejam melhorar a performance da execução da rotina de recalculo do custo médio. |
| [**MA330PGI**](https://tdn.totvs.com/pages/releaseview.action?pageId=73893614) | Ponto de entrada acionado no início da rotina de contabilização do custo médio, pode ser usado em conjunto com o MA330PGF que é executado no final da rotina. | Ponto de entrada acionado no início da rotina de contabilização do custo médio, pode ser usado em conjunto com o MA330PGF que é executado no final da rotina. |
| [**MA330PGF**](https://tdn.totvs.com/pages/releaseview.action?pageId=73082852) | O ponto de entrada MA330PGF é acionado ao final da rotina de contabilização do custo médio, e pode ser usado em conjunto com o MA330PGI que é executado no início da rotina. | O ponto de entrada MA330PGF é acionado ao final da rotina de contabilização do custo médio, e pode ser usado em conjunto com o MA330PGI que é executado no início da rotina. |
| [**MA330TRF**](https://tdn.totvs.com/display/public/PROT/MA330TRF) | Tratamento dos custos apurados | Descrição: LOCALIZAÇÃO: Rotina MATA330 (recálculo do custo médio).  EM QUE PONTO: Na função A330RecTrf() que faz o tratamento do vetor com os custos apurados (aRet). Essa função tem por objetivo encontrar no vetor aListaTrf a nota fiscal (ou remito) que dá origem a nota de transferência que está sendo processada. |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000275147)
