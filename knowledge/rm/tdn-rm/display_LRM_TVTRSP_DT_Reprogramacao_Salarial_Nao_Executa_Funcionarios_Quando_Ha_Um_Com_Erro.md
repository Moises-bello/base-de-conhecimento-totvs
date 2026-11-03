---
content_hash: c03d2e52e2696962657bd53a2da7cee8b4deac9620a301cc2f5660ec0679dfd2
fetched_at: '2026-06-29T00:08:20.606962+00:00'
page_id: '268579295'
product: rm
source: tdn-rm
title: TVTRSP_DT_Reprogramacao_Salarial_Nao_Executa_Funcionarios_Quando_Ha_Um_Com_Erro
type: documentation
url: https://tdn.totvs.com/display/LRM/TVTRSP_DT_Reprogramacao_Salarial_Nao_Executa_Funcionarios_Quando_Ha_Um_Com_Erro
version: 112
---

# REPROGRAMAÇÃO SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Reprogramação SalarialInforme a função.* |
| **Situação/Requisito:** | Ao gerar a reprogramação salarial para todos os funcionários sem utilização de filtros de seleção e quando na base existem atividades que não possuem centro de custo informado, o sistema não reprograma os salários dos funcionários que estão com a parametrização correta. |
| **Solução/Implementação:** | *Alterado o processo para que não seja executado apenas os funcionários com erro e alterado o log para mostrar quais os funcionários não foram executados.* |
| **Chamados relacionados:** | *TVTRSP* |

divs
