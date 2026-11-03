---
article_id: 360026742952
category: Materiais - Compras (SIGACOM)
content_hash: e12aa5737d409ec3279b38fac5da7e4651b961751d7497299feead1bd4abcd10
fetched_at: '2026-06-28T22:41:10.294008+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Principais Atualizações
  do Documento de Entrada (MATA103)
type: support-article
updated_at: '2022-05-13T11:46:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026742952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Principais-Atualiza%C3%A7%C3%B5es-do-Documento-de-Entrada-MATA103
---

**Dúvida**

Este artigo possui o objetivo de orientar como proceder para atualização da rotina de Documento de Entrada (MATA103).

Caso tenha dúvida sobre os procedimentos descritos abaixo, peço que entre em contato com o nosso time de suporte técnico. 

**IMPORTANTE: Realize todas as ações contidas neste documento em ambiente de homologação e somente após validação de seus processos replique para seu ambiente produtivo.**

**Atualização da rotina do Documento de Entrada (MATA103)**

**Ambiente**Protheus – Estoque/Custos – A partir da versão 12.1.17 e 12.1.23

**Solução**Aplicar todas as atualizações dos links abaixo *em ordem crescente e aceitando somente os mais atuais.*

*Observação: Os pacotes estão separados por fontes envolvidos na rotina versus manutenção.*

|  |  |
| --- | --- |
| **Data** | **Pacote de Atualização** |
| 16/04/2019 | 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=748803> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=748802> ; |
|  |  |

**Abaixo segue os incidentes já mapeados e solucionados com a aplicação dos pacotes de Atualização.**

|  |  |
| --- | --- |
| **Data** | **Descrição do Incidente** |
| 18/01/2019 | MATA103 - Documento de entrada erro no campo Tipo CT-e esta ficando em branco na visualização |
| 18/02/2019 | MATA103 - NOFUNCW FWX2UNICO |
| 13/02/2019 | MATA103 - invalid field name in Alias SM4->M4\_MSBLQL on VALIDSM4(MATA103X.PRX) |
| 06/02/2019 | MATA103 - Ao incluir um Documento de Entrada com a espécie CTE e preencher o Tipo CT-e, o sistema apresenta alerta para preencher o campo. |
| 28/01/2019 | MATA103 - Duplicidade de INSS – Entrada de nota fiscal com retenção de INSS o sistema duplica o INSS após salva a na aba duplicata e Contas a Pagar SE2. |
| 14/01/2019 | MATA103 - Array out of bounds ( 11 of 9 ) on A103GRAVA(MATA103.PRW) 02/01/2019 09:38:34 line : 12901 |
| 19/12/2018 | MATA116 - variable does not exist NAMRPROXFOR on A103GRAVA(MATA103.PRW) 13/12/2018 17:36:54 line : 14463 |
| 20/02/2019 | MATA103 - array out of bounds ( 9 of 8 ) on NFECABDOC(MATA103X.PRX) |
| 28/01/2019 | MATA103 - variable does not exist CFILUF on M103FILCTE(MATA103X.PRX) |
| 30/01/2019 | MATA103 - SELECT SCQ.R\_E\_C\_N\_O\_ SCQRECNO FROM SCQ990 SCQ , DHN990 DHN WHERE  SCQ.CQ\_FILIAL='01' AND DHN.DHN\_FILIAL = '01' AND DHN.D\_E\_L\_E\_T\_= ' ' AND DHN.DHN\_TIPO = '3' AND DHN.DHN\_DOCDES = SC1.C1\_NUM AND DHN.DHN\_ITDES = SC1.C1\_ITEM AND DHN.DHN\_DOCORI=SCQ.CQ\_NUM AND DHN.DHN\_ITORI=SCQ.CQ\_ITEM AND SCQ.CQ\_QUANT > SCQ.CQ\_QTDISP AND SCQ.CQ\_NUMREQ = '      ' AND SCQ.D\_E\_L\_E\_T\_=' '  on MAAVALPC(COMXFUN.PRX) 23/01/2019 16:38:34 line : 3789 |
| 01/03/2019 | InterFunctionCall: cannot find function A115VALOR |
| 01/03/2019 | InterFunctionCall: cannot find function A140DESPGA |
| 01/03/2019 | array out of bounds ( 0 of 6 ) on NFECOMBO(MATA103X.PRX) |
| 01/03/2019 | array out of bounds ( 0 of 15 ) on NFERATLOK(MATA103X.PRX) |
|  |  |

**Atualização de FrameWork (LIB) -****Recomendável**

A atualização da Lib (Framework Protheus) é altamente recomendada para o sucesso da atualização da rotina de cadastro de produtos. Abaixo segue o procedimento para realizar o download do pacote de atualização da LIB para aplicação em seu ambiente.

**Procedimentos**Atualização da LIB através do Portal Download da TOTVS ([www.suporte.totvs.com.br](http://www.suporte.totvs.com.br))

Link direto: <https://suporte.totvs.com/portal/p/10098/download#detail/494091>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019298731/mceclip1.png)

**Atualização de DICIONÁRIOS - Recomendável**

Na evolução do cadastro de produtos para nova tecnologia em MVC*\*\** foram implementados novos campos, perguntas, gatilhos e etc. que necessitam de atualização para o correto funcionamento da rotina. Por este motivo é obrigatória a aplicação dos novos pacotes de dicionários (arquivos SDF) via UPDDISTR. Veja abaixo:

**Como atualizar seus dicionários do Protheus**

1. Procedimentos para executar o **UPDISTR**<http://tdn.totvs.com/pages/releaseview.action?pageId=286020348>
2. Dicionario Completo (Download) - Ago/2018 (Release P12.1.17)  
   <https://suporte.totvs.com/portal/p/10098/download#detail/706375>
3. Dicionario Diferencial (Download) - Ago/2018 (Release P12.1.17)<https://suporte.totvs.com/portal/p/10098/download#detail/706376>

**Atualização de BINÁRIO/BUILD - Recomendável**

A atualização do Binário/Build (Framework Protheus) é altamente também recomendada para o sucesso da atualização da rotina de cadastro de produtos. Abaixo segue o procedimento para realizar o download do pacote de atualização do Binário/Build para aplicação em seu ambiente.

**Procedimentos**Atualização do Binário/BUILD através do Portal Download da TOTVS ([www.suporte.totvs.com.br](http://www.suporte.totvs.com.br))

Link direto: <https://suporte.totvs.com/portal/p/10098/download#detail/664020>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019375691/mceclip0.png)

**IMPORTANTE**: Para informações sobre documentação, ciclo de vida, lançamentos e demais atualizações do produto Protheus Compras acesse a nossa home no endereço <http://tdn.totvs.com/display/public/PROT/Home+SIGACOM>

![Conhe_a_o_Guia_Pr_tico_do_Documento_de_Entrada__MATA103_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360026459591/Conhe_a_o_Guia_Pr_tico_do_Documento_de_Entrada__MATA103_.png)  
 <http://tdn.totvs.com/pages/viewpage.action?pageId=189314941>
