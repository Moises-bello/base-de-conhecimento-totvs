---
content_hash: de6268df1b9cdc36382ae9458123d0f12b7a35298419725ea3c3f884e39798a9
fetched_at: '2026-06-29T00:09:09.786049+00:00'
page_id: '394205083'
product: rm
source: tdn-rm
title: 3445133 FOPCALCULO01-4514 Salário Composto - Movimento de Ensino
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394205083
version: 1
---

# Salário Composto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cálculo Movimento de Ensino e Lançamento do Movimento de Ensino |
| **Situação/Requisito:** | Ao executar a rotina de ‘Cálculo do Movimento de Ensino’ os valores são calculados consideradas 4 casas decimais para composição do salário composto do funcionário, porém ao efetuar a rotina de ‘Lançamento do Movimento de Ensino’ o sistema considera para o cálculo 2 casas decimais (com valor arredondado). Desta forma valor do evento apresentado no envelope é diferente de seu valor no salário composto. |
| **Solução/Implementação:** | Ajuste no lançamento e cálculo do movimento de ensino, para considerar 4 casas decimais dos valores. |
| **Tickets relacionados:** | 3445133 |
