---
content_hash: 8f17c37c3e14b4ca3f5851821d1616a76c02fbd79c67c599d04533b3aa7837b9
fetched_at: '2026-06-29T00:09:58.962344+00:00'
page_id: '452718265'
product: rm
source: tdn-rm
title: Remover Funcionários da Requisição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718265
version: 4
---

**Remover Funcionários da Requisição**

Por esse processo é possível remover funcionários vinculados a requisição de transferência em lote. Somente os funcionários que ainda não tenham sua transferência efetivada poderão ser removidos da requisição.

Na aba "Funcionários" a coluna Removido será preenchida com "Sim" e será gerado um parecer com o mesmo status da requisição, informando a remoção do funcionário da requisição.

Se a requisição possuir uma requisição de substituição associada, a mesma também será cancelada.

**Observações**:

* Este processo só pode ser utilizado para requisições com status Aprovado, Em Andamento ou Suspenso. No caso de requisições com o status Pendente, a remoção do funcionário poderá ser realizada através do botão "excluir", dentro da pasta Funcionários.
* Uma vez removido da requisição, o funcionário pode ser inserido em outra requisição do mesmo tipo ou tipos diferentes.
* A requisição será concluída automaticamente quando **houver pelo menos um funcionário com a data de conclusão preenchida** e **todos os demais funcionários da requisição estiverem marcados como "Removido = SIM"**.
