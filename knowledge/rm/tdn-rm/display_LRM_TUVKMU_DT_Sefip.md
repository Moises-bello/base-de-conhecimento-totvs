---
content_hash: b799275faee23220c5d018281c141d5b4ed3590346268bc1769bcd974c0fdf48
fetched_at: '2026-06-29T00:08:10.724821+00:00'
page_id: '240978713'
product: rm
source: tdn-rm
title: TUVKMU_DT_Sefip
type: documentation
url: https://tdn.totvs.com/display/LRM/TUVKMU_DT_Sefip
version: 116
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | O cliente RGIS possui a base parametrizada para trabalhar com o tomador do tipo Cessão Mão de Obra. Verificamos que mesmo após o sistema retornar a mensagem que as linhas do arquivo selecionado após marcar o flag Importar valores de retenção de outro Sistema (Lei 9711/98) foram importadas com sucesso, ao editar o arquivo SEFIP.RE o valor não é apresentado no Registro 20 na posição 243 a 257. |
| **Solução/Implementação:** | Conforme alinhado com equipe prime, a situação não se trata de um bug, visto que no arquivo importado com os valores das retenções não existia tomadores gerados no arquivo do SEFIP.  Será realizada uma melhoria, no sentido de informar no log quais os tomadores tiveram valor de retenção levados para o arquivo do SEFIP.  Será realizada melhoria também na mensagem na importação do arquivo com as retenções, informando o usuário que os valores só serão considerados para os tomadores presentes no arquivo do SEFIP.  A implementação está prevista para ser disponibilizada para os clientes na release da 11.82.45 |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUVKMU TVCVFQ |
| **Requisito (ISSUE):** |  |

divs
