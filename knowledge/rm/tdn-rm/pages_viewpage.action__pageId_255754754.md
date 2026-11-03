---
content_hash: a8856c752b63afc314c3509a01674ed7c52e2eebba234b388089a0417e33766e
fetched_at: '2026-06-29T00:08:17.253949+00:00'
page_id: '255754754'
product: rm
source: tdn-rm
title: TVQYM0_DT_Cálculo_Salário_Funcionário_Professor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=255754754
version: 120
---

# CADASTRO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Funcionário Tipo Recebimento Professor* |
| **Situação/Requisito:** | *O usuário utiliza tabela salarial para definir os salários dos funcionários cadastrados na base, recentemente ele realizou a demissão de uma funcionária e cadastrou outra funcionária para realizar a substituição da funcionária demitida.*  *A nova funcionária admitida possui a mesma função, tabela, nível e faixa salarial da funcionária que foi demitida, porém nas versões atuais o sistema não está calculando o salário da funcionária de acordo com as tabelas salariais.*  *De acordo com a tabela salarial, o salário hora da funcionária seria no valor de R$22,23, totalizando um salário mensal de R$2.254,49 com uma jornada de 101:25. No cadastro da nova funcionária o sistema está calculando o salário mensal no valor de R$2.245,23 com a mesma jornada e valor de salário hora, o sistema está considerando apenas as 101 horas informadas na jornada e não considera os 25 minutos.* |
| **Solução/Implementação:** | *Ajuste no cálculo do salário para jornada composta por fração de minutos.* |
| **Chamados relacionados:** | *TVQYM0* |

divs
