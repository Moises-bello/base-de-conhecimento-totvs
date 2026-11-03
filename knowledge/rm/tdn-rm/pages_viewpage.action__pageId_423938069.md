---
content_hash: fce3dccd62d1fd37b454c10f0efbabec8639cefc2aa1beda652babddb39aec72
fetched_at: '2026-06-29T00:09:25.227192+00:00'
page_id: '423938069'
product: rm
source: tdn-rm
title: Empenho de Materiais - Migração Duplicado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938069
version: 1
---

**Empenho de Materiais**   
O empenho de materiais é uma transferência entre locais de estoque, para que todo o material disponível neste local de estoque designado como empenho não seja considerada para as próximas ordens de produção.  
   
**Parametrizações necessárias:**   
1 - No menu Opções | Parâmetros | Produção | Pasta "Gerais", marque a opção "Empenha Matéria Prima".   
   
2 - No menu Opções | Parâmetros | Produção | Pasta "Movimentação de Estoque", selecione um movimento de "Transferência para Empenho de Matéria Prima".   
   
3-No TOTVS Gestão de Estoques, Compras e Faturamento através do "Assistente de Implantação de Processos", acessado pelo menu Opções | Parâmetros | RM Nucleus. 04.04 Gestão de Estoque | 04.04.06 Transferências | Item preços marque o parâmetro "Aceita preço zero" e  "Buscar Preço Em". Em Mov - Emitente/Destinatário 1/2 no parâmetro "Edição do Local de Destino" selecione "Edita". Em Mov - Emitente/Destinatário 2/2 no parâmetro "Edição do Local de Saída"' selecione "Não Edita".  
   
**Observações:**   
1- O movimento de Empenho de Material deve ser criado no TOTVS Gestão de Estoques, Compras e Faturamento através  do  "Assistente de Implantação de Processos", acessado pelo menu Opções | Parâmetros | RM Nucleus.     
   
2 - No TOTVS Gestão de Estoques, Compras e Faturamento, menu Cadastros | Local de Estoque, cadastre um local de estoque   que será determinado para o Empenho de Materiais.   
   
3 - No menu Opções | Parâmetros | Produção | Pasta "Locais de Estoque", informe o local de Estoque de Empenho no campo "Matéria Prima Empenhada".       
   
   
**Considerações na utilização da funcionalidade de empenho/desempenho de materiais**   
   
**O empenho de materiais ocorre em duas situações:** Ao promover a Ordem de Produção para "Aguardando Recursos" e através do ícone na visão de Ordens de Produção.   
   
As operações de empenho e desempenho são realizadas através de uma visão com todos os materiais necessários para a produção da ordem selecionada. Os materiais serão exibidos combinados de acordo com os "Locais de Estoque" a que pertencem, ou seja, caso estejam cadastrados (nos Parâmetros de Produção) três Locais de Estoque para Matéria Prima, aparecerá três vezes o material na visão, uma vez para cada Local de Estoque. O sistema mostra todos os locais de estoque disponíveis para os materiais mesmo que possua saldo em estoque igual a zero ao marcar a opção "Exibir Produtos sem Saldo Disponível (Considera os Locais de Estoque parametrizados)".  
   
Ao efetuar empenho de materiais, o TOTVS Planejamento e Controle da Produção gera um movimento de transferência no TOTVS Gestão de Estoques, Compras e Faturamento,  e quando faz o desempenho gera outro movimento de devolução do material. Todo o rastreamento destes movimentos é armazenado na tabela KMOVESTOQUE, caso o produto tenha controle de lote essa informação é gravada na tabela KMOVESTOQUELOTE e número de série na tabela KMOVESTOQUESERIE.  
   
Não será permitido excluir um item de ordem, pois o mesmo já gerou movimentos TOTVS Gestão de Estoques, Compras e Faturamento (Transferência e/ou Devolução) que ficarão no histórico.   
   
Caso desista de realizar a produção do item a ordem deverá ser cancelada. Se uma atividade for cancelada após o empenho do material, o sistema deverá permitir o desempenho do material da atividade cancelada. Caso a atividade seja reativada, o material deverá aparecer para ser empenhado.   
   
   
**Edição da tela de material a ser Empenhado/Desempenho**   
Na tela de edição do empenho existe o campo "Opção" para empenho/desempenho de material.  
   
**Opção Empenho:**  
É permitido digitar número negativo para diminuir a quantidade a ser empenhada ou número positivo para aumentar a quantidade a ser empenhada.    
   
**Opção Desempenho:**  
Ao editar a tela as quantidades a serem desempenhas apareceram negativas.  
   
Caso a quantidade a ser desempenhada seja -7: se o usuário digitar -10 o sistema fará restrição, pois a "Quantidade informada é maior que a empenhada!".  
   
Caso a quantidade a ser desempenhada seja -7: se o usuário digitar -7 a quantidade a ser desempenhada ficará zero. O sistema não irá fazer o desempenho e, ao editar novamente a tela, a matéria prima aparecerá a ser desempenhada -7.   
   
Caso a quantidade a ser desempenhada seja -7: se o usuário digitar -5 o sistema irá desempenhar -2 e, ao editar novamente a tela, a matéria prima aparecerá -5 para ser desempenhada.  
 

|  |  |
| --- | --- |
|  | Veja Também |

---

[Como Fazer - Parametrização de empenho de materiais](http://totvsconnect.blogspot.com/2011/01/como-fazer-parametrizacao-de-empenho-de)   
   
[Como Fazer – Gerar movimento de empenho de materiais](http://totvsconnect.blogspot.com/2011/01/como-fazer-gerar-movimento-de-empenho)
