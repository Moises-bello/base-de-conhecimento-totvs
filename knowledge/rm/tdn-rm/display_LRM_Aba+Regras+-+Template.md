---
content_hash: 6b31b6d159aec749d40f4676d9c4b061410d12c936b7ca8d43a85a20b3f8a296
fetched_at: '2026-06-29T00:09:18.460578+00:00'
page_id: '421388698'
product: rm
source: tdn-rm
title: Aba Regras - Template
type: documentation
url: https://tdn.totvs.com/display/LRM/Aba+Regras+-+Template
version: 19
---

Usar juros futuros

Serão definidos somente no template as opções de uso, que pode ser: Não utiliza juros, Juros simples ou juros compostos.

Taxa de juros ao dia

Essa opção só estará habilitada se o sistema estiver parametrizado para usar juros simples ou compostos. Será definido seu valor mínimo e máximo em percentual, e também se será permitido ao usuário alterar esse valor no momento da geração do acordo através da opção 'Permitir alterar juros'.  No valor default será carregado o mínimo e validado ao ser alterado pelo usuário (dentro da faixa).

Acréscimo

São definidos os valores do acréscimo, podendo ser em valor ou percentual mínimo e máximo, também é possível definir se o usuário poderá alterar esses valores através da opção 'Permitir alterar acréscimo'. No valor default será carregado o mínimo e validado ao ser alterado pelo usuário (dentro da faixa).

Desconto

São definidos os valores de desconto, podendo ser em valor ou percentual mínimo e máximo, também é possível definir se o usuário poderá alterar esses valores através da opção 'Permitir alterar desconto'. No valor default será carregado o mínimo e validado ao ser alterado pelo usuário (dentro da faixa).

Parcelas

Será carregado como default o valor indicado da quantidade máxima de parcelas e ficará disponível para alteração se a opção "Permitir alterar número de parcelas" estiver marcada. O valor indicado deve estar em branco ou maior / igual a 1.

Manter dia vencimento

Quando marcado o sistema irá manter a data de vencimento e desabilitar a opção intervalo em dias.

Intervalo em dias

Se a opção anterior estiver desmarcada será permitido ao usuário definir um intervalo de dias, que terá como default o valor indicado e estará disponível para alteração, esse valor aplicado na data de vencimento a partir da segunda parcela do acordo.

Prazo

Esse é o prazo em dias para vencimento da primeira parcela do acordo. O intervalo será usado para definir a data das outras parcelas a partir da primeira do acordo.

Primeira Parcela (%)

Pode se definir o percentual a ser considerado na geração da primeira parcela do acordo a ser gerado. O percentual informado será aplicado sobre o total da negociação para o valor da primeira parcela. 

Permitir Lançamentos "A vencer"

Permite gerar Acordo também de Lançamentos não vencidos.

Exibir soma valores lançamentos

Com essa opção marcada, as informações de soma dos valores do(s) lançamento(s) de origem do Acordo estarão visíveis.

Permitir alterar Cliente/Fornecedor

Marcando esta opção, na geração do acordo será exibido um campo para informar o Cliente/Fornecedor que será utilizado na geração dos lançamentos financeiros do Acordo. Vale ressaltar que nos casos em que forem selecionados lançamentos de Cliente/Fornecedor Pessoa Jurídica, o sistema permitirá utilizar apenas cadastros de Cliente/Fornecedor com a mesma raiz de CNPJ (8 primeiros dígitos iguais).

Informar opções para gerar Número do Documento

Habilita campo para informar os dados do número do documento. Esta opção não está disponível para templates usados na web pois o usuário não informa neste opções de numeração.

Permitir acordo para lançamento com boleto registrado, remetido ou vinculado a transação PIX com pagamento solicitado

Permite que seja gerado acordo para lançamentos Registrados, Remetidos ou que estejam vinculados a uma transação PIX com pagamento solicitado.

Permitir acordo para lançamentos gerados por acordo

Quando marcado será permitido a geração de acordo para lançamentos gerados por acordo, desde que o acordo origem esteja efetivado. Caso desmarcado o sistema fará a validação do mesmo durante o processo de geração de acordo e caso algum dos lançamentos de origem seja oriundo de um outro acordo, será emitida mensagem e o acordo não será gerado.
