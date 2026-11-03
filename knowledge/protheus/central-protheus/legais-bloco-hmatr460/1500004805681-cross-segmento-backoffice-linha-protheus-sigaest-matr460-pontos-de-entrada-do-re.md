---
article_id: 1500004805681
category: LEGAIS - BLOCO H/MATR460
content_hash: 4fa9bda5f21a34a632ded87c9f6d0a1845126ca74a71e7c461701ebeb39e104b
fetched_at: '2026-06-28T22:42:15.147861+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Pontos de
  Entrada do relatório de Inventário Modelo 7
type: support-article
updated_at: '2026-04-15T16:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004805681-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Pontos-de-Entrada-do-relat%C3%B3rio-de-Invent%C3%A1rio-Modelo-7
---

**Dúvida**  
Quais são os Pontos de Entrada relacionados ao relatório MATR460 (P7) - Inventário Modelo 7?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Veja abaixo os Pontos de Entrada relacionados à rotina MATR460 - Inventário Modelo 7 (clique no nome do ponto de entrada para obter maiores detalhes):

|  |  |  |
| --- | --- | --- |
| **Nome:** | **Título:** | **Descrição:** |
| [**A460AMZP**](https://tdn.totvs.com/pages/releaseview.action?pageId=651923296) | Define um ou mais armazéns para seção "Em Processo" | O ponto de entrada A460AMZP foi desenvolvido com a finalidade de definir mais de um armazém de processo (MV\_LOCPROC) na impressão do relatório "Registro de Inventário Modelo P7 (MATR460)".  Importante: O ponto de entrada somente possui funcionalidade na impressão do relatório, possuindo a finalidade de transferir o saldo do armazém informado para seção “Em Processo”. |
| [**A460RLOC**](https://tdn.totvs.com/pages/releaseview.action?pageId=651923218) | Adiciona intervalos de filtro de armazéns | Ponto de entrada responsável por incluir filtros personalizados de armazéns no relatório de Registro de Inventário Modelo 7 (MATR460). Sua utilização permite realizar o filtro de armazéns por vários intervalos distintos e disjuntos, como por exemplo, "01 ao 05", "10 ao 12", "25 ao 47" e "85 ao 88". |
| [**A460UNIT**](https://tdn.totvs.com/pages/releaseview.action?pageId=651922953) | Permite gravação do arquivo de trabalho na impressão do relatório | LOCALIZAÇÃO : Funções ReportPrint(), R460Imp( ), R460EmProcesso( ) - Funções utilizadas para imprimir o relatório do registro de inventário modelo 7.  DESCRIÇÃO : O ponto de entrada permite a gravação do arquivo de trabalho utilizado na impressão do relatório. O usuário pode regravar os valores de acordo com suas necessidades. Os principais campos do arquivo de trabalho que devem ser utilizados são: TOTAL, VALOR\_UNIT e QUANTIDADE. |
| [**A460TUNI**](https://tdn.totvs.com/pages/releaseview.action?pageId=651923107) | Permite gravar o arquivo de trabalho na impressão do relatório | LOCALIZAÇÃO : Funções ReportPrint(), R460Imp( ), R460Terceiros - Funções utilizadas para imprimir o relatório do registro de inventário modelo 7.  DESCRIÇÃO : O ponto de entrada permite a gravação do arquivo de trabalho utilizado na impressão do relatório. O usuário pode regravar os valores de acordo com suas necessidades. Os principais campos do arquivo de trabalho que devem ser utilizados são: TOTAL, VALOR\_UNIT e QUANTIDADE. |
| [**A460ALTRB**](https://tdn.totvs.com/pages/releaseview.action?pageId=651923375) | Manipula os valores da tabela TRB no relatório MATR460 | Localização: Está localizado na função R460GrvTRB que é utilizada para gravação do arquivo de trabalho para exportação de dados do SPED FISCAL.  Quando: O Ponto de Entrada é chamado antes de gravar os Registros na TRB. |
| [**A460TESN3**](https://tdn.totvs.com/pages/releaseview.action?pageId=236427905) | Considera Saldo Poder Terceiros para TES que não atualiza estoque. | O ponto de entrada A460TESN3 no relatório de Registro de Inventário Modelo 7 (MATR460) considera o saldo de poder de terceiros no Tipo de Entrada/Saída (TES) que não atualiza estoque. Desta forma, ele é utilizado quando a pergunta do relatório Saldo em poder de 3º? estiver configurada com a opção SIM e pode assumir os seguintes critérios: |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre o relatório MATR460 (P7)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)
