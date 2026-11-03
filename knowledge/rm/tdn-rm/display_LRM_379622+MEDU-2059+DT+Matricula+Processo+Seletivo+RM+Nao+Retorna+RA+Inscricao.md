---
content_hash: 74a7ec822d1a318ac64892451a83658c6f1a96423cc5737131433222f303c304
fetched_at: '2026-06-29T00:08:26.548638+00:00'
page_id: '271183653'
product: rm
source: tdn-rm
title: 379622 MEDU-2059 DT Matricula Processo Seletivo RM Nao Retorna RA Inscricao
type: documentation
url: https://tdn.totvs.com/display/LRM/379622+MEDU-2059+DT+Matricula+Processo+Seletivo+RM+Nao+Retorna+RA+Inscricao
version: 109
---

# PROCESSO SELETIVO RM - MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Educacional / Processo Seletivo* |
| **Função:** | *Processo seletivo RM - Matrícula* |
| **Situação/Requisito:** | *Ao efetuar uma matrícula de um aluno pelo processo de matrícula que utiliza o candidato chamado no processo seletivo RM, o sistema não vincula na inscrição do candidato no processo seletivo o registro acadêmico (RA) gerado *ou utilizado para aquele novo aluno*, sendo que a coluna do RAMAT existe no banco de dados na tabela de inscrição do processo seletivo (SPSINSCRICAOAREAOFERTADA).* |
| **Solução/Implementação:** | *Foi identificado que ao finalizar a matrícula de um aluno originado do processo seletivo RM, o sistema altera na inscrição do candidato no processo seletivo o status da inscrição, porém não atualiza a coluna RAMAT com o RA que será utilizado pelo candidato que virou aluno, sendo assim, foi implementado uma função para que juntamente com a alteração de status da inscrição do candidato, salve também o RA gerado para o aluno na coluna RAMAT.*  *Caso o candidato do processo seletivo já tenha se tornado um aluno por meio do processo de matrícula do educacional, será possível consultar pelo processo seletivo o RA gerado para o candidato. A informação ficará disponível pela tela de inscrição do candidato do processo seletivo através da aba de informações complementares.*  *OBS: Na tabela *SPSINSCRICAOAREAOFERTADA existe uma coluna chamada RA, esta coluna não se refere ao RA gerado para o aluno, a coluna é referente ao registro acadêmico do aluno no caso de indicação.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
