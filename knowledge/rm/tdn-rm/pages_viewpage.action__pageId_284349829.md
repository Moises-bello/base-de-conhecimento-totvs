---
content_hash: d395266252af08c42e7c0cf2bb5e27e404078f2e1ede1d8457c1859379c6bbae
fetched_at: '2026-06-29T00:08:36.083994+00:00'
page_id: '284349829'
product: rm
source: tdn-rm
title: DT Limite de Exibição de Alteração Salarial no RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284349829
version: 2
---

# HISTÓRICO DE ALTERAÇÃO SALARIAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Histórico de Alteração Salarial* | *Histórico de Alteração Salarial* | |  |  | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FOPROTINAS01-607 |
| **País(es):** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |

---

# Interpretação da demanda

Visando atender a necessidade dos clientes de limitar a visibilidade de alteração salarial no RM Portal de forma a evitar a visualização de alterações ainda não finalizadas, foi criado um novo parâmetro para definir a data limite das alterações salariais a serem exibidas no RM Portal. O parâmetro é válido apenas para funcionários visualizando suas alterações. Chefes continuarão visualizando todo o histórico de seus subordinados.

# Analise da demanda

### Criação do Parâmetro

Foi implementado nos parâmetros de "Demonstrativo de Pagamento" do RM Portal um novo campo para informar a data limite da exibição das alterações salariais para o funcionário.

Selecione então o seu grupo de acesso ao portal que deseja parametrizar e clique no botão especificado:

Caso o parâmetro seja deixado em branco, não será estabelecido um limite para a data da exibição dos históricos salariais.
