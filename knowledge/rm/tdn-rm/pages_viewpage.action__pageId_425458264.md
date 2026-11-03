---
content_hash: 0436252b0c54e088616f0cf26783fc989061e34b00a5c9b7cd3aee90c202a660
fetched_at: '2026-06-29T00:09:29.769539+00:00'
page_id: '425458264'
product: rm
source: tdn-rm
title: Geração de inscrições anônimas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458264
version: 4
---

Existe uma modalidade de inscrições chamada "anônimas", normalmente captadas por formulários nas escolas, empresas, etc. Este processo consiste em reservar uma faixa de números de inscrições a partir do último número de inscrição gerado pelo sistema e esta faixa será representada por um lote.

Por exemplo,  se a última inscrição realizada pelo sistema gerou o número 500, ao executarmos o processo de geração de inscrições anônimas e pedir reserva de 100 inscrições, o processo irá reservar um lote de inscrições com a faixa iniciando pelo número 501 e terminando em 600. Após a execução deste processo, a próxima inscrição gerada pelo sistema será a de número 601.

**Para a execução deste processo deveremos informar os seguintes campos**:

Forma de inscrição: através deste campo será possível definir qual forma de inscrição será utilizada para as inscrições anônimas a serem geradas.

Quantidade de inscrições: este campo representa o número total de inscrições anônimas que serão geradas.

Funcionário: através deste campo será possível determinar qual o funcionário será responsável pela geração das inscrições anônimas.

Cliente/fornecedor: ideia similar ao campo "Funcionário", porém, neste caso estará sendo determinado o "Cliente" ou "Fornecedor" responsável pela geração das inscrições anônimas.  
 Para cada inscrição anônima criada também será gerado um lançamento. Após a execução do processo será exibido um Log notificando os resultados do processamento.

Caso o processo seja executado com sucesso serão apresentadas algumas informações importantes, tais como o número do lote das inscrições, o número de inscrições geradas, o tempo de duração da execução do processo e o usuário do Corpore que estava operando o sistema.

**Pré-requisitos do processo**:

1. Existir pelo menos uma forma de inscrição cadastrada para o processo seletivo em questão.
2. A forma de inscrição a ser utilizada deverá estar no período de inscrição.
