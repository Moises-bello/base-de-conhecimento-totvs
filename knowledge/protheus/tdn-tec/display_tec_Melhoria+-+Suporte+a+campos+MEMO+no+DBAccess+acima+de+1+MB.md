---
content_hash: 7a6a8d3dbc40d213c9f8e44c7da3185926e7a2e93be06344d317ef9dc1221f3b
fetched_at: '2026-07-02T19:24:21.370477+00:00'
page_id: '266980358'
product: protheus
source: tdn-tec
title: Melhoria - Suporte a campos MEMO no DBAccess acima de 1 MB
type: documentation
url: https://tdn.totvs.com/display/tec/Melhoria+-+Suporte+a+campos+MEMO+no+DBAccess+acima+de+1+MB
version: 3
---

Esta build contém uma melhoria na configuração MEMOMEGA / TOPMEMOMEGA, para suportar campos Memo com conteúdo acima de 1 MB.

|  |  |
| --- | --- |
| Situação | Utilização de tabelas com campo "M" memo através do DBAccess |
| Ocorrência | Por default, o limite de tamanho de um campo "M" Memo no AdvPL é 65535 bytes. Usando a RDD TOPCONN, junto da configuração MEMOMEGA=1, era possível suportar até 1 MB de conteúdo em campos "M" Memo. |
| Melhoria | A partir desta build, podemos configurar o tamanho máximo em MB suportado em um campo "M" Memo no AdvPL, quando usada a RDD TOPConn. Para isto, informamos o tamanho máximo em MB na configuração **MEMOMEGA**, na seção [DBACCESS] do arquivo de configutração do TOTVS | Application Server (appserver.ini).  O limite suportado por um campo MEMO esta relacionado ao tamanho da string no **true** e no **true**, que por default é 1 MB, logo, para aumentar o limite de tamanho do campo MEMO, deve-se também aumentar o limite de string, através da configuração **MaxStringSize** para ambos, **true** e  **true**. |
| Informações adicionais | * Não há chamado relacionado. Implementação realizada em conformidade com o processo de melhoria contínua da ferramenta. * Referente à ocorrência: TEC-7474 * Disponível a partir da Build 7.00.131227A, com data de geração superior a * Para o funcionamento da implementação, deve ser também atualizado o DBAccess, com a build 20161016 ou superior, com data de geração superior a |

## Veja também
