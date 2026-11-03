---
content_hash: 0083fb5f9399d95d353126e3474a650b59c856ec4b1fd5b013696873b3bb3c27
fetched_at: '2026-06-29T00:08:18.768912+00:00'
page_id: '266968944'
product: rm
source: tdn-rm
title: TVVJ25_DT_Base_AAS_Incorreta
type: documentation
url: https://tdn.totvs.com/display/LRM/TVVJ25_DT_Base_AAS_Incorreta
version: 113
---

# LIBERAÇÃO DE COMPETÊNCIA - BASE AAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Base AAS* |
| **Situação/Requisito:** | *O relatório de Salário Contribuição não está demonstrando os valores corretamente em sua geração.* *O correto seria cada PROVENTO de uma determinada Base abater SOMENTE o DESCONTO pertencente ao mesmo grupo. Porém notamos que não é isto que o sistema está fazendo:*  *Observei também que a composição da tabela PFAAS também não está corretamente discriminada em seus grupos.* |
| **Solução/Implementação:** | *Realizada a criação de um processo para acertar a Base AAS. O mesmo terá como parâmetro a competência inicial e final na qual se deseja efetuar a atualização, juntamente com um filtro de Seleção de Funcionários, caso seja necessário efetuar a atualização apenas de alguns funcionários.*   * *Acessar Folha de Pagamento, aba Folha Mensal, grupo Relatórios da Folha - Atualizar Base AAS.* * Realizar a parametrização o intervalo da competência que deseja atualizar e caso necessário o filtro de funcionários e executar o processo.   A rotina realizará a atualização da Base AAS conforme os lançamentos da ficha financeira do período parametrizado .  Através da rotina a composição da tabela PFAAS será ajustada corretamente possibilitando a geração dos relatórios corretamente.  **Atenção**: O processo só deverá ser executado em competências menores ou iguais as competências atuais e que estejam com alguma adversidade em relação a ficha financeira. |
| **Chamados relacionados:** | *TVVJ25, TVWUIJ* |

divs
