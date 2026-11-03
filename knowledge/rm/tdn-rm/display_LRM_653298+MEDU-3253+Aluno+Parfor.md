---
content_hash: 2d3af0e236a1f685b81338351002e6af213c63b8625cbfba9f6c2cda70a8ca1e
fetched_at: '2026-06-29T00:08:30.460391+00:00'
page_id: '272432418'
product: rm
source: tdn-rm
title: 653298 MEDU-3253 Aluno Parfor
type: documentation
url: https://tdn.totvs.com/display/LRM/653298+MEDU-3253+Aluno+Parfor
version: 108
---

# ALUNO PARFOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | *****Totvs Educacional***** |
| **Função:** | Censo da Educação Superior |
| **Situação/Requisito:** | Ao rodar o processo de preparação para os dados do censo, o valor no campo PARFOR, do curso/habilitação do aluno, é apagado. |
| **Solução/Implementação:** | O campo PARFOR é apenas um campo visual.  É no assistente de geração dos dados do Censo que será definido se o aluno é PARFOR ou não. Para isso deve-se marcar a forma de ingresso Especial e Parfor. Lembrando o curso deve ser Licenciatura.  O sistema será alterado para considerar o campo complementar Licenciatura com o valor "S" ou "1". Antes considerava apenas "S", mas existe uma mensagem no sistema pedindo para que esse campo seja cadastrado como inteiro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | MEDU-3371 |
| **Requisito:** | N/A |

divs
