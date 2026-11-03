---
content_hash: a2465b236bb4fffeaa4475f77929996ee75899dcdccf40f70cca531bd45fb0dc
fetched_at: '2026-06-29T00:09:54.372337+00:00'
page_id: '444611569'
product: rm
source: tdn-rm
title: Excluir Lançamentos de Inscrições Anônimas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444611569
version: 2
---

Quando o processo Gerar Inscrições Anônimas for executado, ele irá gerar um número específico de inscrições anônimas, onde cada uma destas inscrições terá um lançamento associado. Posteriormente o processo Importar Inscrições Anônimas será executado, porém poderá ocorrer de nem todas as inscrições anônimas geradas serem importadas, ficando um número expressivo de lançamentos ociosos na base de dados sem terem sido utilizados. Portanto, será necessário excluir estes lançamentos que não foram utilizados por processos seletivos. Para isso basta executar o processo “Excluir Lançamentos de Inscrições Anônimas não Importadas”.

Para a execução deste processo não será necessário o preenchimento de quaisquer campos, apenas será exibido o nome do processo seletivo para o qual o processo será executado.

Após concluir o processo será exibido um Log notificando o resultado do processamento.  Primeiramente é informado o número total de lançamentos que foram excluídos. Em seguida, para cada lançamento excluído, foi informado o número da inscrição anônima, número do lote, número do lançamento, valor da inscrição, valor do desconto e valor do lançamento.

Curiosidades:

Quando exclui uma inscrição de candidato por motivos de desistência ou outros e se esta inscrição for proveniente às inscrições anônimas geradas, a inscrição anônima não será excluída nem seu lançamento, porque posteriormente se for de interesse da instituição, esta inscrição poderá ser reaproveitada com outra pessoa.

**Pré-requisitos do processo**

a) O processo seletivo para o qual o processo será executado deverá ter encerrado o período de divulgação de resultados.

b) Ter executado previamente o processo Gerar Inscrições Anônimas.
