---
content_hash: 81346aab3e55ecd7310c24c4c9a90120dc4d725fa8e1b7fb095b3f7e1dc48ff8
fetched_at: '2026-06-29T00:10:53.159280+00:00'
page_id: '577605160'
product: rm
source: tdn-rm
title: Ativar conexão cobrança recorrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=577605160
version: 6
---

A ativação da conexão utilizada na cobrança recorrente deve ser feito com o mesmo cuidado que o agendamento da cobrança recorrente, uma vez que ao concluir esse processo, as informações de cobrança com cartão de crédito existentes nessa base de dados, serão utilizadas para quitação dos títulos cadastrados em cobrança recorrente.

Esse processo será necessário para controlar durante a execução da cobrança recorrente se a conexão parametrizada é a mesma da cobrança em execução, e se forem as mesmas, finalizar o processo fazendo a cobrança com os dados cadastrados. Para os casos em que houver alteração da conexão, será enviado um e-mail para que um responsável tenha conhecimento da divergência da alteração e a cobrança não será realizada.

O(s) e-mail(s) para receber a notificação pode ser cadastrado no parametrizador.

**Parâmetros**

Os parâmetros financeiros para configuração dos e-mails a serem notificados podem ser  acessados em ***"******Ambiente >> TOTVS Gestão Financeira >> Contas a Receber >> Baixas >> Cobrança Recorrente"***

* **E-mail dos usuários a serem informados da alteração da conexão da recorrência.**

**Observações:**

Esse comportamento é responsável por impedir cobranças duplicadas, nos casos que existam ambientes concorrentes, por exemplo ambiente de produção e de testes, no qual uma copia atualizada da base de produção está sendo utilizada no ambiente de testes.

**Importante:**Esse processo funciona somente para o modelo de pagamento CyberSource.
