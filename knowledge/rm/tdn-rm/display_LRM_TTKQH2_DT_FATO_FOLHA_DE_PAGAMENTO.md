---
content_hash: e7e831522b162819f603baeb1245d4c3cd859e79c03e006c8da6574979bea0e4
fetched_at: '2026-06-29T00:06:26.442018+00:00'
page_id: '225265684'
product: rm
source: tdn-rm
title: TTKQH2_DT_FATO_FOLHA_DE_PAGAMENTO
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKQH2_DT_FATO_FOLHA_DE_PAGAMENTO
version: 115
---

# FATO FOLHA DE PAGAMENTO - GOODDATA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Conceito - Fato Folha de Pagamento - Good Data* |
| **Situação/Requisito:** | Ao desenvolver a exportação de dados pelos conceitos para integração GoodData, não foi criado parâmetro ou filtro para limitar exportação de apenas uma coligada, gerando demora caso o cliente deseje exportar os dados apenas de uma coligada. |
| **Solução/Implementação:** | *Foi adicionado um tratamento para exportar os dados apenas da coligada atual. Para isso, basta seguir os passos abaixo:*    *1- Selecione o fato "Folha de Pagamento" e clique em editar.*    *2- Selecione a conexão de origem (READ\_DB) e clique no botão de editar logo acima.*    *3- No campo "Owner Data", preencha com o texto exato: "FILTRARCOLIGADA=1" (sem as aspas).*  *4- Salve as alterações e feche a edição do conceito.*  *Das próximas vezes que o conceito for executado, serão exportados os dados apenas da coligada atual.*  *Para voltar a exportar os dados de todas as coligadas, basta remover o valor preenchido no campo "Owner Data" no passo 3.* |
| **Chamados relacionados:** | TTKQH2, TUHQRE |

divs
