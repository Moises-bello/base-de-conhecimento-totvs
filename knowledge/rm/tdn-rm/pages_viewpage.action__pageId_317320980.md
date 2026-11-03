---
content_hash: fe0f845e55a5f8e2da2d6dd27222795fd20c2f3d98da46e228995ab9e60d1400
fetched_at: '2026-06-29T00:08:47.033623+00:00'
page_id: '317320980'
product: rm
source: tdn-rm
title: FOPROTINAS01-2468 Adequações no CAGED Referentes à Reforma Trabalhista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317320980
version: 5
---

# INCLUSÃO DO TIPO DE MOVIMENTAÇÃO '90' E CAMPOS 'TRABALHO PARCIAL', 'TELETRABALHO' E 'TRABALHO INTERMITENTE'

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | CAGED |
| **Situação/Requisito:** | No dia , o MTE liberou novo layout do CAGED referente às mudanças decorrentes da Reforma Trabalhista (Lei 13.467/17), que pode ser encontrado no endereço: <ftp://ftp.mtps.gov.br/pdet/arquivos/CAGED/Reforma_Trabalhista/>  O novo layout inclui o tipo de movimentação '90 - Desligamento por acordo empregado/empregador' e os campos 'Trabalho Parcial', 'Teletrabalho' e 'Trabalho Intermitente' (todos com opção '1-sim' ou '2-não'). |
| **Solução/Implementação:** | Obs.: É necessário executar script, havendo duas situações:  1. Clientes que estão em versões anteriores a 12.1.17 deverão executar os scripts da Reforma Trabalhista durante a conversão para 12.1.17 ou 12.1.18    2. Clientes que estão na 12.1.17 e 12.1.18 terão de executar somente a marcação LB.2017.11\_03 separadamente (que já está disponibilizada junto ao patch das versões, basta acessar o RM.Script.Executor)    Acessando o cadastro de funcionários, na aba 'Salário/Jornada', será possível definir quando o funcionário trabalha em tempo parcial e quando trabalha em regime de teletrabalho:          Os parâmetros acima especificados serão utilizados para o preenchimento dos novos campos do CAGED.    Para o novo tipo de movimentação (90) ser informada no CAGED, é necessário que o tipo de rescisão cadastrada (no cadastro de rescisão ou cadastro de aviso prévio) para o funcionário seja do tipo 'V - Comum acordo': |
| **Tickets relacionados:** | - |
