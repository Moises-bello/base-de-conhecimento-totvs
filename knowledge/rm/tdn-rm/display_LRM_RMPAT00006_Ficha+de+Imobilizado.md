---
content_hash: 8276e5040845c9378e7719702f66bd48d5e03fcb2526bce0f8378345d88414f9
fetched_at: '2026-06-29T00:11:28.228842+00:00'
page_id: '73073104'
product: rm
source: tdn-rm
title: RMPAT00006_Ficha de Imobilizado
type: documentation
url: https://tdn.totvs.com/display/LRM/RMPAT00006_Ficha+de+Imobilizado
version: 10
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Totvs Gestão Patrimonial – **Versão:** 11.52 |
| **Processo** | : | Ficha de Imobilizado |
| **Subprocesso** | : | Relatórios |
| **Data da publicação** | : | 24/07/2013 |

**Introdução**

O Relatório Ficha de Imobilizado se trata do relatório de maior utilização dentro do Totvs Gestão Patrimonial.

Substituindo o Razão Auxiliar, este relatório reúne informações referentes às movimentações tendo como finalidade o gerenciamento do patrimônio e/ou a prestação de contas à legislação em vigor.  
Ele ainda permite que as informações sejam filtradas pelo intervalo de [contas contábeis](http://fwrm-wiki:21598/WikiHelp/CTB/CTB.planoContaContabil.aspx) ou por [grupo de patrimônio](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.GrupoPatrimonio.aspx), possibilitando maior flexibilidade durante a parametrização.

**Procedimento (Importar a estrutura do relatório)**

 Acesse o Bonum pela MDI, localizado no ambiente corporeRM – pasta RM.NET, arquivo RM.exe

* Acesse o BackOffice Gestão Patrimonial / aba Gestão / sub aba RM Reports
* Vá em Processos / Importar Relatório.

Selecione o layout no diretório o qual está salvo, será apresentada tela abaixo e clique em executar:   
  
  
  
**Procedimento (Emitir o Relatório)**

 Acesse menu Utilitários / Ficha Imobilizado:

* Defina as informações do filtro e Avance.

* Defina o ou os grupos de patrimônios a visualizar

* Selecione–os e avance.

* Defina o tipo da impressão;
* Selecione o código do relatório importado anteriormente (conforme descrito no inicio deste arquivo). Avance. Execute.

Será visualizado o relatório.

   
   
OBS.:

O Ficha de Imobilizado permite totalizar cada conjunto de informações definidas, neste caso, como de aquisições ou ocorrências ([baixas](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.OcorrenciaBaixa.aspx), [acréscimos](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.OcorrenciaAcrescimo.aspx) e [transferências monetárias](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.OcorrenciaTranferenciaMonetaria.aspx)).A totalização pode ser realizada para cada um dos conjuntos acima citados ou para todos.

 Podem existir na base de dados patrimônios que possuem saldo, porém não tiveram movimentação no período a ser gerado o relatório. Desta forma, caso seja necessário exibir este tipo de informação é fundamental marcar a opção que permite imprimir dados dos grupos de patrimônio sem movimentação.

Também podem existir situações como a movimentação com valores zerados que está exemplificada abaixo:O patrimônio foi inserido no sistema, consequentemente no relatório será apresentada uma aquisição. Porém por algum motivo o cálculo de depreciação não foi executado.Desta forma, ao marcar opção "Imprime movimentações com valores zerados" o sistema apresentará a aquisição do patrimônio e depreciação igual a 0,00.
