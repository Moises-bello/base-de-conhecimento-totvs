---
content_hash: be1c2154ac01dc84ab2dbb8a7f4f46e624fbac0d5b2591a010426d01e3c0eaa3
fetched_at: '2026-06-29T00:09:16.775026+00:00'
page_id: '421385553'
product: rm
source: tdn-rm
title: Relatório Composições do Projeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385553
version: 2
---

**Relatório Composições do Projeto**

---

**Algumas pré condições para utilização do Relatório:** Os Relatórios devem ser do tipo Composições do Projeto. Acesse o Produto | Gestão | RM Reports. Recomenda-se calcular o projeto antes de gerar os relatórios. Os valores dos totalizadores dos relatórios, por questões de arredondamento (uma vez que os relatórios não utilizam as casas decimas definidas nos parâmetros de projeto), podem apresentar valores aceitavelmente um pouco maiores ou menores.

Selecione o Relatório e clique em Editar e verifique se no campo Tipo do Relatórios está escrito Composições do Projeto. Caso não esteja, selecione o tipo correto.Após importados, podem ser visualizados em; Construção e Projeto | Relatórios | Composições | Composições do Projeto.

**Relatórios Baseados no Gerador:** **Composição de Custo Unitário Utilizadas no Projeto:** Este relatório exibe as composições do tipo CPU (Custo Unitário) separadas pelo grupo DNIT (Equipamentos, Materiais, Mão de Obra e Transporte).

**Composição Por Produção Utilizadas no Projeto :** Este relatório exibe as composições do tipo Produção separando seus recursos pelo Grupo DNIT (Equipamentos, Materiais, Mão de Obra e Transporte). Ao final é mostrado um totalizador para cada grupo além da Produção da Equipe e o Custo Unitário da Execução.

**Relatórios de Modelo Fixo:** **Planilha de Composição Analítica por Tarefas Considerando BDI Diferenciado e Separado:** O relatório de BDI DIFERENCIADO exibe uma planilha com as composições utilizadas no projeto por tarefa considerando BDI diferenciado. Ele será gerado da mesma forma que os outros relatórios do gerador e possuirá os mesmo filtros descritos no item anterior. No Gerador antigo possui dois filtros que não serão mais apresentados na tela de geração do relatório, pois o novo gerador RM Reports  possui funcionalidades que suprem esses filtros. BDI Diferenciado SEPERADO é um filtro que foi criado para apresentar o BDI diferenciado junto aos totalizadores ao invés de aplicá-lo em cada coeficiente dos recurso da composição.

**Planilhas de Composição Analíticas de Custos Unitários:** Este exibe uma planilha analítica com as composições de custos unitários utilizadas no projeto agrupadas pelo grupo de custo. Ele será gerado da mesma forma que os outros relatórios do gerador e possuirá os mesmo filtros descritos no item anterior.

**Planilhas de Composição Analíticas de Preços Unitários por Produção:** Este exibe uma planilha analítica com as composições de preços unitários por produção utilizadas no projeto agrupadas pelo grupo DNER. Ele será gerado da mesma forma que os outros relatórios do gerador e possuirá os mesmo filtros descritos no item anterior.

**Planilha Analítica de CPUs por Tarefas com Descr. Composição Auxiliar:**  
 Exibe uma planilha analítica com as composições de preços unitários e suas composições auxiliares recursivas utilizadas no projeto por tarefas. Ele será gerado da mesma forma que os outros relatórios do gerador e possuirá os mesmo filtros descritos no item anterior.

Este relatório, na versão do Delphi possui alguns filtros que não serão mais apresentados na tela de geração do relatório, pois o novo gerador (RM Reports) possui funcionalidades que suprem esses filtros. Abaixo segue uma tabela com os filtros e as medidas tomadas para atenderem ao novo gerador de relatórios.

|  |  |
| --- | --- |
| **Filtro** | **Nova característica** |
| Ordenação por código da tarefa ou descrição | O novo gerador possui esta funcionalidade. O relatório padrão será ordenado pelo código da tarefa. Para mudá-lo, abra o template do relatório, clique no Detalhe da tarefa e selecione "Ordenação". |
| Imprimir composições repetidas | O novo gerador também possui esta funcionalidade. Para isso insira um cabeçalho no Detalhe de tarefa para agupá-la pela composição. |
| Imprimir composições ao final | Para atender a este filtro foi criado um outro template (04.009.1 - Planilha Analítica de CPUs por Tarefas com Descr. Composição Auxiliar ao final) onde neste são impressos as composições auxiliares ao final do relatório. Os dados são os mesmos de ambos os relatórios, porém as composições auxliares no primeiro são exibidas logo após a sua composição pai e no segundo são exibidas ao final do relatório. |
| Data do relatório | O novo gerador possui um campo para a data do relatório. |
| Aba Texto para cabeçalho e rodapé. | Pode ser inserido um cabeçalho e rodapé do relatório com texto padrão no template do relatório pelo RM Reports. |

Com as alterações oferecidas pelo RM Reports é possível modificar o relatório para atender aos filtros acima ou a qualquer customização que o queira fazer. Para isso, é possível criar uma cópia do relatório usando o processo de mesmo nome na guia Gestão do menu principal e o modificar a maneira  que achar interessante.

---
