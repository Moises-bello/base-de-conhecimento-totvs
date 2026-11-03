---
content_hash: 3ec3129ff382dc255ca00fe1bf39f0544f2bfb6e8e2fd343ea9fb3956d7d8e1f
fetched_at: '2026-06-29T00:11:06.351391+00:00'
page_id: '634036760'
product: rm
source: tdn-rm
title: Dados para aprovação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=634036760
version: 2
---

Nos Dados para Aprovação, o usuário poderá visualizar os dados detalhados da tarefa que está sendo aprovada.

A demonstração destes dados ocorrerá através dos relatórios que estiverem configurados no cadastro do respectivo tipo do atendimento do TOTVS Aprovações e Atendimento.

Os relatórios são parametrizados no tipo de atendimento, sendo cada modelo de relatório associado a uma etapa do tipo de atendimento, ou seja, para um mesmo tipo de atendimento podem ser configurados vários modelos de relatório conforme a etapa do fluxo em que o atendimento se encontra.

Caso em todas as etapas vá ser utilizado o mesmo relatório, basta informá-lo apenas na primeira etapa, senão em cada etapa deve ser informado o respectivo relatório. A parametrização dos relatórios é realizada nos tipos de atendimento no anexo etapas do atendimento na aba **Configuração do aplicativo 'Minhas Aprovações'**.

Anexo Etapa do atendimento

Para atendimentos gerados a partir de movimentação no TOTVS Gestão de Estoque, Compras e Faturamento foram disponibilizados os relatórios **CRMREL0010 - WorkFlow Minhas Aprovações - Movimento** e **CRMREL0001 - Dados para aprovação - Movimento.** Ambos os relatórios exibem **dados dos movimentos** incluídos e o fluxo para aprovação gerado no atendimento, e diferem no formato.

Para atendimentos gerados a partir dos contratos no TOTVS Obras e Projetos foi disponibilizado o relatório **CRMREL0011 - WorkFlow Minhas Aprovações - Contratos** e **CRMREL0002 - Dados para Aprovação - Contrato**. Os relatórios exibem as **informações dos contratos** e dos **itens/objetos** associados a ele.

Para atendimentos gerados a partir de Requisições de Aumento de Quadro do TOTVS Gestão de Pessoas, foi disponibilizado os relatórios **CRMREL0014 - WorkFlow Minhas Aprovações - Requisição de Aumento de Quadro** e **CRMREL0003 - Dados para aprovação -****Requisição de Aumento de Quadro**, que trazem as informações e competências necessárias para atender a  requisição que deu origem à tarefa.

Para atendimentos gerados a partir de Requisições de Desligamento do TOTVS Gestão de Pessoas, foram disponibilizados os relatórios **CRMREL0012 - WorkFlow Minhas Aprovações - Requisições de Desligamento** e **CRMREL0004 - Dados para aprovação -****Requisição de Desligamento**, ambos trazem as informações e competências necessárias para atender a requisição que deu origem à tarefa. 

Para atendimentos gerados a partir de uma Requisição de Alteração de dados funcionais do TOTVS Gestão de Pessoas, foram disponibilizados os relatórios **CRMREL0013 - WorkFlow Minhas Aprovações - Alteração de Dados Funcionais** ou **CRMREL0005 - Dados para aprovação - Alteração de Dados Funcionais**, que trazem as informações referentes ao tipo de requisição de alteração de função. Eles diferem apenas no formato, pois o primeiro foi desenvolvido para visualização em celular e o segundo em formato A4, respectivamente.

Foi disponibilizado também entre os objetos gerenciais, o relatório **CRMREL0006 - Workflow Minhas Aprovações - Pedido de Material**, que traz as informações referentes as requisições de materiais incluídas a partir do TOTVS Obras e Projetos.

Para atendimentos gerados a partir de adiantamentos do contrato, foi disponibilizado o relatório **CRMREL0007 - Workflow Minhas Aprovações - Adiantamento** , que traz as informações referentes ao adiantamento de contratos incluídos no TOTVS Obras e Projetos. 

O relatório **CRMREL0008 - Workflow Minhas Aprovações - Liberação de Período**, traz as informações (medições, deduções e retenções ) referentes ao período liberado dos contratos incluídos no TOTVS Obras e Projetos.

Foi disponibilizado também utilizando um modelo diferente de lista entre os objetos gerenciais, o relatório **CRMREL0009 - Workflow Minhas Aprovações - Liberação de Período**, mantendo o formato do Boletim de medição, que também traz as informações (medições, deduções e retenções ) referentes ao período liberado de contratos incluídos no TOTVS Obras e Projetos.

Com o relatório corretamente parametrizado, na geração do atendimento, será gerado o relatório em arquivo pdf no anexo do atendimento em **Arquivos anexos do atendimento**e pode ser visualizado no **Aplicativo Minhas Aprovações** e ao clicar no botão **Carregar documento****.**

Para visualizar a geração de relatórios no aplicativo **Minhas Aprovações**, deve-se acessar o atendimento gerado no aplicativo e selecionar **Dados para aprovação** ou os **Anexos**do atendimento.

Abaixo os modelos dos relatórios citados acima e disponíveis no book:

* **CRMREL0010 - WorkFlow Minhas Aprovações - Movimento**

* **CRMREL0001 - Dados para aprovação - Movimento**

     

* **CRMREL0011 - WorkFlow Minhas Aprovações - Contratos**

Contrato de Serviço:

      

Contrato de Insumo:

* **CRMREL0002 - Dados para aprovação - Contrato**

* **CRMREL0014 - WorkFlow Minhas Aprovações - Requisição de Aumento de Quadro**

* **CRMREL0003 - Dados para aprovação - Requisição de Aumento de Quadro**

     

* **CRMREL0012 - WorkFlow Minhas Aprovações - Requisições de Desligamento**

* **CRMREL0004 - Dados para aprovação -****Requisição de Desligamento**

* **CRMREL0013 - WorkFlow Minhas Aprovações - Alteração de Dados Funcionais**

     

* **CRMREL0005 - Alteração de Dados Funcionais**

* **CRMREL0006 - Workflow Minhas Aprovações - Pedido de Material**

     

* **CRMREL0007 - WorkFlow Minhas Aprovações - Adiantamentos**

    

* **CRMREL0008 - Workflow Minhas Aprovações - Liberação de Período**

Contrato de serviço:

          

Contrato de Insumo:

          

* **CRMREL0009 - Workflow Minhas Aprovações - Liberação de Período**

**C****riando relatórios personalizados.**

É possível criar seus próprios relatórios com dados que se adeguem melhor a sua realidade, para isso, o relatório deve ter uma sentença SQL com a tabela HATENDIMENTOBASE como fonte de dados, essa sentença deve ser filtrada pela chave primária da tabela HATENDIMENTOBASE, que é composta por CODCOLIGADA, CODLOCAL e CODATENDIMENTO, além disso, devem ser incluídos parâmetros nesse relatório para cada um dos campos que compõe a chave, ou seja, CODCOLIGADA, CODLOCAL, CODATENDIMENTO, os 3 parâmetros devem ser do tipo inteiro. Segue abaixo um exemplo de como seria a sentença SQL e os parâmetros do relatório:

Sentença SQL:

SELECT \* FROM HATENDIMENTOBASE (NOLOCK)

              WHERE CODCOLIGADA       = :CODCOLIGADA

              AND     CODLOCAL              = :CODLOCAL

              AND    CODATENDIMENTO = :CODATENDIMENTO

Dessa forma, é possível usar qualquer campo da tabela de atendimento no relatório, bastando pra isso substituir o \* pelos campos desejados, também é possível usar outras tabelas desde que tenham alguma ligação com a tabela de atendimentos, o que ocorre nas integrações.

Abaixo, como os parâmetros devem ser incluídos no relatório:
