---
content_hash: 99ac74441df2c01afe44f1074c9923e1def97eb81c8c0fd7d6b658a3fded1d14
fetched_at: '2026-06-29T00:06:20.935269+00:00'
page_id: '223159636'
product: rm
source: tdn-rm
title: GLB0013_CONTABILIZA_NUMERO_DE_PAGINAS_DE_IMPRESSSO-DELPHI
type: documentation
url: https://tdn.totvs.com/display/LRM/GLB0013_CONTABILIZA_NUMERO_DE_PAGINAS_DE_IMPRESSSO-DELPHI
version: 6
---

**[Contabiliza o número total de páginas de impressão - Delphi](http://tdn.totvs.com/display/LRM/GLB0013_CONTABILIZA_NUMERO_DE_PAGINAS_DE_IMPRESSSO-DELPHI)**

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gerador de Relatórios |
| **Versões:** | **Versão:**11.50.XX |
| **Ocorrência:** | Renumeração de página em relatórios Delphi |
| **Ambiente:** |  |
| **Passo a passo:** | Objetivo  ---   Atualmente o Gerador de relatórios Delphi não possui uma ferramenta que faça a contabilidade total do número de páginas, porém como solução paliativa pode-se obter o desejado utilizando uma consulta SQL. Como configurar  ---   Primeiramente o sistema deve estar configurado para manter o log de execução dos relatórios. Esta configuração é feita através dos parâmetros globais do sistema.        Salva a configuração na estrutura do relatório onde deseja-se incluir o respectivo controle de página deve ser incluído um componente “Página” (). Este componente irá retornar o número atual da página gerada pelo relatório. Inclua em seguida uma consulta SQL que retornará o total de páginas do relatório. ; (Consulta no link)    **Exemplo em SQL;**      **Exemplo em Oracle;**     false A linha CODAPLIC = 'T' se refere ao código do aplicativo. Se atente ao código do sistema que utilizará a consulta SQL. Nos exemplos acima estamos utilizando o RM Nucleus e RM Labore respectivamente.    O agrupamento de ambos os componentes devem ficar da seguinte forma;        Lembrando que após feito todo este processo o sistema não irá realizar a contagem das páginas corretamente quando impresso o relatório pela primeira ou única vez. Deve-se gerar o relatório uma primeira vez para que esta geração seja computada no banco de dados com informações deste relatório, inclusive com o número de páginas gerados. Somente após a segunda geração do relatório a contagem de páginas será realizada corretamente.    Informamos que esta é uma saída paliativa para o cliente, pois dependendo do tempo gasto para gerar o primeiro relatório não vale a pena aguardar a primeira geração para iniciar a segunda somente para obter a contagem de páginas com total e página atual. |
| **Observações:** | **Este recurso já encontra-se disponibilizado em .NET - Acesse: [Contabiliza número de páginas de impressão - Reports](http://tdn.totvs.com/x/PAixAw)** |

divs
