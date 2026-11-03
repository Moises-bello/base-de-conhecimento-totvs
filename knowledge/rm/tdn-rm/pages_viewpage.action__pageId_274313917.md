---
content_hash: f4448dc5241f1c97eb57f8c359e82f7b5f8f6cfc04b117c76128cd3e02c450e6
fetched_at: '2026-06-29T00:08:33.348590+00:00'
page_id: '274313917'
product: rm
source: tdn-rm
title: 449081 FOPROTINAS01-141 Folha Analítica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274313917
version: 105
---

# FILTRAR BASE DE FGTS DE AFASTADOS POR PERÍODO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Folha Analítica |
| **Situação/Requisito:** | Na geração da folha analítica (.Net) em um período específico e com movimentação para apenas um funcionário na empresa o sistema apresenta o totalizador de seção contendo informações de base de FGTS em seções em que não existem movimentação no período, mas possuem funcionários afastados com o tipo T - Acidente de Trabalho. Isso aconteceria também se a seção tivesse funcionários afastados com os tipo M - Serviço Militar e O - Doença Ocupacional. As movimentações que compõe estas bases que o sistema está levando na folha analítica foram identificadas em outro período nos funcionários afastados com o tipo T. Além disso a folha analítica também está dobrando o valor destas bases. |
| **Solução/Implementação:** | Relativo aos totais de seção aparecendo sem que a seção tenha funcionários com movimento no período período: Em versões anteriores do sistema, os eventos de base de FGTS de afastados não pertenciam a nenhum período e, portanto, sempre constavam nos totais de seção da Folha Analítica. Ao ser realizada a migração, a implementação foi feita de modo a preservar o comportamento anterior. Para que tal comportamento possa ser modificado, foi criado o parâmetro "Filtrar Base de FGTS de Afastados por Período" no Wizard da Folha Analítica. Quando esse parâmetro é marcado, o sistema exibirá os totais apenas das seções onde há funcionários com movimento no período (considerando que o cliente não marcou o parâmetro para imprimir funcionários sem movimento). Se o parâmetro permanecer desabilitado, o sistema continuará exibindo totais de seção contendo base de FGTS de afastados onde há funcionários afastados no período, mesmo que o funcionário não tenha movimento.  Relativo ao cálculo de base de FGTS dobrado: Em versões anteriores do sistema, o cálculo das bases era realizado sempre que uma Folha Analítica era gerada. Ao introduzir um Evento com CC 315 para o cálculo da base de FGTS de afastados, o funcionário já possui o lançamento em seu envelope, pois é calculado automaticamente ao lançar os códigos de cálculos 1-Horas Normais, 2-Dias Trabalhados ou 145-Atestado Médico. Desse modo, a Folha Analítica considerava tanto a base de FGTS já lançada quanto a que ela calculava, dobrando o valor. Tal comportamento foi modificado para verificar se existe evento com CC 315 na coligada antes de calcular a base de FGTS de Afastados. |
| **Tickets relacionados:** | FOPROTINAS01-141 |

divs
