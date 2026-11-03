---
content_hash: 57d803e6d973333a4845121c8bbcc5155fd57cb3e66b1451cfb965d9cedcdafd
fetched_at: '2026-06-29T00:11:16.944566+00:00'
page_id: '674554088'
product: rm
source: tdn-rm
title: Log de Movimentações do Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=674554088
version: 5
---

O log de movimentações do contrato está presente tanto do ensino básico quanto no ensino superior, está disponível em Financeiro / Contábil | Contratos | sub menu: Log de Movimentações do Contrato. Ele se destina a salvar todas as inclusões, exclusões e alterações relacionadas ao **contrato** e as **parcelas do contrato**.

Para visualizar as informações armazenadas nos logs, é necessário que informe o RA ou o nome do Aluno e, em seguida clicar na coluna do log disponível.

### Log do contrato

As alterações no contrato são armazenadas na tabela SLOGCONTRATO. Nesse caso, só vai gravar log quando o controle de período contábil for manual.

Nesse log, são exibidos os campos R.A, Id do Período Letivo, Descrição do período letivo, Código do Contrato, Matriz aplicada, Usuário que realizou a operação, Operação, o Tipo da operação e a Data da ocorrência.

### Log da parcela

Quaisquer operação que envolva mudança em alguma parcela irá gera um registro na tabela do log da parcela (SLOGPARCELA). Essas mudanças podem ser relacionadas a inclusão, edição e exclusão de parcelas. A tabela de log armazena os campos código do serviço, tipo da parcela, valor da parcela, valor do desconto e tipo de desconto da parcela antes e depois da efetivação da mudança.

As mudanças que geram o log podem ser disparadas em diversos eventos, como por exemplo:

* Inclusão, edição e exclusão de parcela no contrato;
* Associação de plano de pagamento no contrato;
* Processo de reajuste das parcelas do contrato;
* Assistente de criação de parcelas do contrato;
* Processo de atualização de parcelas do plano de pagamento;
* Matrícula e rematrícula online (quando é selecionado ou editado algum plano de pagamento);
* Acordo (negociação online).

O log de movimentações do contrato está disponível a partir da versão **12.1.34** no patch **12.1.34.126**.
