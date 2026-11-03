---
content_hash: 0911d4e2767d63d29c61fd48eff8c58f631d9a3892f5e5caad1653735e55fc41
fetched_at: '2026-06-29T00:06:18.468609+00:00'
page_id: '218431659'
product: rm
source: tdn-rm
title: TTSPXJ_DT_Inserir_Valor_Default_Secao_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/TTSPXJ_DT_Inserir_Valor_Default_Secao_Funcionario
version: 1
---

# INSERIR NOVO FUNCIONÁRIO CAMPO DEFAULT DA SEÇÃO NÃO PREENCHE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Paga* |
| **Função:** | *Valor default campo seção* |
| **Situação/Requisito:** | Ao definir o campo Seção no cadastro do funcionário como Default e criar um novo funcionário o sistema não está trazendo a seção preenchida. |
| **Solução/Implementação:** | Foi realizado uma validação se o campo de seção estiver visível e o campo de código da seção não estiver vazio e o valor default para esse campo estiver vazio ou nulo realiza a alteração que já existia no código que estava limpando o valor default. |
| **Chamados relacionados:** | TTSPXJ |
| **Versões/Release:** | *12.1.9* |

divs
