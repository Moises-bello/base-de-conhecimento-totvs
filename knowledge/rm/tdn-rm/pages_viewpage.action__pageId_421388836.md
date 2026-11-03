---
content_hash: a0ffd0c9888ae96402aad53321b1306a3ef49d87bc021dabfbf442ddffd3a2c9
fetched_at: '2026-06-29T00:09:19.273820+00:00'
page_id: '421388836'
product: rm
source: tdn-rm
title: Contabilização das Provisões de IOF e IR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388836
version: 3
---

Na Aplicação Financeira é possível contabilizar os lançamentos de provisão de IOF e IR no encerramento do período sem incidência de resgate nas aplicações de natureza CDB Pós Fixado, Fundo Curto prazo e Fundo Médio Prazo.

Parâmetro de contabilização das provisões (Parâmetro 02.03.02 – Aplicação Financeira).  
 No menu  Ambiente | Parâmetros | Totvs Gestão Financeira | Controle Bancário |Aplicação Financeira basta marcar a opção "Contabiliza Provisões"  para que seja possível a execução do processo.  
 Menu Movimentações Bancárias |Aplicação Financeira:

Cadastro da Aplicação Financeira

Ao marcar o parâmetro, os campos para preenchimento dos eventos contábeis de "Evento Provisão de IOF" e "Evento Provisão de IR", serão habilitados e será preciso preencher estes campos para que os lançamentos de provisão sejam contabilizados.

Processo de Encerramento do Período

Após cadastrar a Aplicação Financeira, incluir uma nova aplicação e fazer o encerramento do período os valores de IOF e IR a serem provisionados serão calculados e lançados juntamente com o valor do Rendimento no encerramento do período.

Processo de Encerramento do Período Em Lote

Ao encerrar o período em lote, as provisões do período anterior são excluídas e lançadas novas provisões no final do período. No caso da aplicação ser do tipo Fundo, nos meses que tem incidência do IR Come-cotas (Maio e Novembro) será gerado o lançamento de imposto, calculado e lançado a diferença como provisão de IR. 

Processo de Integração Contábil

Ao executar o processo de integração contábil o sistema contabiliza os lançamentos das provisões do período. Na visão do cadastro da Aplicação Financeira, acessar os Anexos menu "Contabilização de Período" para visualizar todas as Contabilizações geradas para a respectiva Aplicação Financeira, inclusive os lançamentos de provisão do IOF e do IR.

Processo de Estorno Contábil

Ao executar o processo a contabilização integrada ao lote "N" será excluída e se integrada ao lote "0" será estornada. Para que sejam gerados novos lançamentos de provisão será preciso executar o processo de Encerramento de Período novamente e Integração Contábil para contabilizar os mesmos.

Processo de Reabertura do Último Período

Ao tentar reabrir o último período o sistema bloqueia a reabertura e informa que será necessário executar o processo de "Estorno Contábil".  Após estornar a contabilidade e reabrir o último período os lançamentos de provisão serão excluídos.

Processo de Resgate

Ao realizar o resgate parcial a provisão continuará a ser gerada nos períodos seguintes. No resgate total da aplicação o sistema exclui o lançamento de provisão e gera o lançamento do imposto.
