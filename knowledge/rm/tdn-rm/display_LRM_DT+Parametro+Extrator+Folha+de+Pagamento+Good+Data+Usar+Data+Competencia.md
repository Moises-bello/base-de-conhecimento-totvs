---
content_hash: 851c1c3d41aad123e994544180ad3853e8a9386179d28f7d30b3978ba07e50d8
fetched_at: '2026-06-29T00:08:39.897298+00:00'
page_id: '286024777'
product: rm
source: tdn-rm
title: DT Parametro Extrator Folha de Pagamento Good Data Usar Data Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Parametro+Extrator+Folha+de+Pagamento+Good+Data+Usar+Data+Competencia
version: 2
---

# EXTRATOR FOLHA DE PAGAMENTO GOODDATA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Extrator Folha de Pagamento - GoodData* | *Extrator RH - Folha de Pagamento* | |  |  | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FOPROTINAS01-1049 |
| **País(es):** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |

---

# Interpretação da demanda

Criação de um novo parâmetro de Business Analytics para o extrator de forma de pagamento para informar se o campo de data da tabela HLP utilizará a data de pagamento ou a data da competência do envelope do funcionário. Será necessário também criar um novo campo na tabela para armazenar o valor da data de pagamento, em caso de utilização da data de competência.

# Analise da demanda

### Criação do Parâmetro

Foi implementado nos parâmetros de "TOTVS Business Analytics",  "Parâmetros Globais",  "TOTVS Smart Analytics" do módulo de integrações, um novo campo para informar se deve ser considerada a data da competência na extração da folha de pagamento.

Caso o parâmetro esteja desmarcado o processo continuará o mesmo, levando a data de pagamento do evento para o campo HLP\_DATA.

Caso esteja marcado, o campo HLP\_DATA será preenchido com a data da competência do envelope (considerando o dia como 01) e o novo campo HLP\_DTCX será preenchido com a data de pagamento.

Nota: para que o novo campo seja preenchido, tenha certeza de utilizar o novo modelo do conceito de folha de pagamento "Fato - RH - Folha de Pagamento\_DTCX.concept"
