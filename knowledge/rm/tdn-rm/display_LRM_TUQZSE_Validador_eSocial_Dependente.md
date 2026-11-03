---
content_hash: 4a25bdb5ed1f8ce81d36224824d43bbe551a0657fffa720cb4759a652ed6e1ee
fetched_at: '2026-06-29T00:08:09.743503+00:00'
page_id: '239040731'
product: rm
source: tdn-rm
title: TUQZSE_Validador_eSocial_Dependente
type: documentation
url: https://tdn.totvs.com/display/LRM/TUQZSE_Validador_eSocial_Dependente
version: 116
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *eSocial* |
| **Situação/Requisito:** | De acordo com o layout do eSocial é de preenchimento obrigatório a data de nascimento e o CPF do dependente maior de 18 que é identificado como dependente legal (Com incidência em pensão, INSS e IRRF). Ao gerar o processo de Validação do eSocial do arquivo S -2100 o sistema está validando o cadastro da filiação do funcionário que é realizado no cadastro de dependentes. O sistema valida o preenchimento da data de nascimento e do CPF dos registros cadastrados como Pai/Mãe mesmo sem ser dependentes legais, apresentando erro no processo. |
| **Solução/Implementação:** | Ajuste no validador do eSocial e geração do XML S-2100 para considerar apenas dependentes legais (Com incidência em pensão, INSS e IRRF). |
| **Chamados relacionados:** | TUROHC, TUSP38, TUSYY3, TUTS53, TUUEJX, TUUJ34, TUURUZ, TUVNZC, TUWTHD, TUWXLM, TUYDN8, TUYRNL, TUZQVT, TV4372, TVAGSN, TVAY82, TVBESN |
| **Versões/Release:** | 11.82.44 |

divs
