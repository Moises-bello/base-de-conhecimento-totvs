---
content_hash: 0b033e78e9601ebaf450a0f79621bb64d3a07df91b4d2089c7937f51029b251a
fetched_at: '2026-06-29T00:10:20.187026+00:00'
page_id: '489764485'
product: rm
source: tdn-rm
title: BD0000_Delimitação de Registros na Visão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=489764485
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | Todas |
| **Ocorrência:** | Delimitação de Registros na Visão |
| **Ambiente:** | CorporeRM |
| **Passo a passo:** | A quantidade de registro definida para visão, pode ser caracterizado como um ofensor para performance.  Tal cenário é importante uma vez que os registros em visão raramente são gerenciados pelo usuário. A montagem da visão difere por exemplo da construção de um relatório, que explora o potencial de processamento analítico de dados, podendo lidar com volumes maiores. Os registros carregados na visão do produto, quando superior a mil registros, podem ocasionar consumo elevado de memória e CPU nos servidores de aplicação, client e Banco de Dados ocasionando overhead destas camadas.  Recomendo que altere para 500 a quantidade de registros na visão, conforme resultado da seguinte consulta SQL: *SELECT \* FROM GBKSERVER WHERE NUMMAXREGS > 500* <http://tdn.totvs.com/pages/releaseview.action?pageId=173899839>  Porém tal alteração exigirá um alinhamento prévio com os setores da empresa, possibilitando determinar um limite gerenciável para operação do sistema. ***Por exemplo***, se o cadastro de funcionários do RM Labore, atualmente possibilita a filtragem de 30.000 registros, em debate interno, poderá ser definido um valor menor, como 5.000 registros, evitando assim, a execução de filtros que podem onerar os demais usuários.  Em determinados cenários, será necessário um contato com o suporte do módulo, para possíveis mudança na execução de processos, que atualmente exigem a filtragem de um número considerável de registros. |
| **Observações:** |  |
