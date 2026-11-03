---
content_hash: 7d1e34a16980050b7786560a677e930e02efac4e0e71074768d63b9244877b99
fetched_at: '2026-06-29T00:05:58.807241+00:00'
page_id: '188613502'
product: rm
source: tdn-rm
title: RMFIS00001_Importar layout e gerar relatório VAF/DAMEF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=188613502
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:**11.82.38 |
| **Processo** | **:** | Rotina Legal VAF/DAMEF |
| **Subprocesso** | **:** | Importar layout e gerar relatório VAF/DAMEF |
| **Data da publicação** | **:** | 20/05/2015 |

**Introdução**  
Para a rotina VAF/DAMEF o Totvs Gestão fiscal não gera um arquivo a ser importado no programa, ele gera um relatório com as informações a serem digitadas manualmente pelo cliente no programa validador.

**Desenvolvimento/Procedimento**

Para gerar o relatório é necessário importar o layout compatível com a versão do módulo Fiscal e base de dados utilizada. EX: Versão 11.82, Base de dados SQL.

**Importar o layout**

A. No menu do Totvs Gestão Fiscal, acessar Relatórios | Gerador. NET

B. Processos | Importar Estrutura de Relatório (selecionar o layout na pasta onde o salvou)

C. Layout importado

**Gerar Relatório**  
A. Selecionar o layout importado | Processos | Gerar relatório | Avançar

B. Selecionar a primeira linha da coluna Filtros, clicar no botão ... e informar o código da filial.

OK e Avançar

C. Informar a data inicial e final do período desejado (formato dd/mm/aaaa) e avançar.  
Selecionar as opções que desejar e avançar.

D. Executar

E. Aparecerá uma mensagem informando que o processo foi finalizado

**Informações Adicionais**

Para visualizar a sentença de SQL do grupo de relatório basta acessar a aba Logs, selecionar SQL (ou Oracle) e clicar em Bloco de Notas.
