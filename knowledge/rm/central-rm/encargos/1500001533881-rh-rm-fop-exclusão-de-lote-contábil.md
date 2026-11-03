---
article_id: 1500001533881
category: Encargos
content_hash: 0c8da8e499cdd0f2bf90dc68f32328b236b4d044a125b111ffb9248dbac94b8d
fetched_at: '2026-06-28T22:46:53.265044+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP -  Exclusão de lote contábil
type: support-article
updated_at: '2024-10-09T20:00:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001533881-RH-RM-FOP-Exclus%C3%A3o-de-lote-cont%C3%A1bil
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16109388318999)** Tempo aproximado para leitura: **00:02:19 min  
  
Dúvida**No módulo Folha de Pagamento, como excluo lotes contábeis?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a exclusão dos lotes contábeis, realize os seguintes passos:  
  
1. Verificar se o lote contábil está presente nos menus **Encargos | Lançamentos | Lançamentos** (Folha de Pagamento), e em **Encargos | Lançamentos | Lançamentos** (Gestão Contábil).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16108762513943)

Veja no exemplo abaixo:  
  
**Folha de Pagamento:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16108917547671)

**Gestão Contábil:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16108911954711)  
  
2. Identificado que os lotes estão integrados, é necessário que seja feita a integração com lote 0. Para isso, basta selecionar o lote contábil no Folha de Pagamento e acessar **Processos | Integrar lote contábil** com Gestão Contábil:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16108914258199)

3. Na tela de integração do lote, verifique se o mesmo está sendo apresentado e clique em Avançar até o procedimento concluir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16108937409303)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16108986281623)

Concluído o procedimento, o lote contábil sumirá da tela dos lotes.  
  
4. No Folha de Pagamento, é necessário realizar a solicitação de tarefa. A mesma é executada através do menu **Encargos | Cadastro | Solicitação de Tarefas:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16108995927831)

Ao abrir, basta localizar o lote que deseja excluir e executar o processo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16109064817303)

![kcs_7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001606142)

5. Após executar a solicitação de tarefa no Folha de Pagamento, acesse o Gestão Contábil. No menu **Utilitários | Tarefas | Permissões** é necessário liberar a permissão para o usuário na **Exclusão Contabilidade Lote Zero**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16109258339863)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16109284688151)

Para liberar, basta editar a opção **Exclusão Contabilidade Lote Zero** e adicionar o usuário responsável:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16109287058711)

6. Após adicionar a permissão para usuário, acessar o menu **Utilitários | Tarefas | Gerenciador**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16109309510679)

A solicitação de tarefa realizada estará localizada. Selecione-a acessando **Processos | Executar Tarefa**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16109297982871)

Feito isso, o lote será excluído.  
  
**Saiba mais  
[COMO FAZER - Exclusão de Lotes do RMLABORE que foram contabilizados](https://tdn.totvs.com/pages/releaseview.action?pageId=118882973)**
