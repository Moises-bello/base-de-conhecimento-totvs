---
content_hash: 73db08900319672705fa43e56e6a37720e068c09255ad14b8557dee19f28c3cc
fetched_at: '2026-06-29T00:09:52.470745+00:00'
page_id: '439682301'
product: rm
source: tdn-rm
title: Produtos Faturados no Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Produtos+Faturados+no+Contrato
version: 2
---

Após definidas as parametrizações no Suprimentos/Faturamento, realiza-se o vínculo entre produto e dedução, no contrato de finalidade Prestação de Serviço, Insumo ou Marco Contratual. Este vínculo é feito na tela de liberação de períodos, quando o contrato é do tipo prestação de serviços/Insumo ou na tela de liberação de marco, quando o contrato é do tipo marco contratual.  
Na aba de Detalhamento da Retenção/Dedução/Adiantamento existe o botão "Adicionar Produtos Faturados a Dedução". Clicando neste botão será apresentado os itens adicionados ao contrato, itens estes adicionados no Suprimentos/Faturamento.

**Passos:**

Clique no botão "Adicionar Produtos Faturados a Dedução", e adicione o (s) produto (s) faturado (s) para deduzir na tela de Liberação de Período do contrato em seguida execute o processo.

\* Os produtos apresentados na tela de "Adicionar Produtos Faturados a Dedução", somente serão exibidos se o tipo de movimento (Nota Fiscal 1.2 ou 2.2) estiver parametrizado para "Dedução de Contrato" e não permitir faturamento.

 \* O contrato é informado na aba Integrações | Projetos | Dedução de Contrato do item de movimento.

 \* O tipo de movimento (Pedido de Compra) também pode ser configurado com "Dedução de Contrato", e após o Recebimento, o tipo de movimento gerado (Nota Fiscal 1.2 ou 2.2) terá o contrato automaticamente preenchido no campo "Dedução de Contrato".

 \* No Totvs Obras e Projetos, ao abrir a tela de Liberação de Período | aba Detalhamento da Retenção/Dedução/Adiantamento e clicar no botão "Adicionar Produtos Faturados a Dedução" serão apresentados os produtos faturados para dedução de contrato.

 \* Em contrato de marco contratual existe uma particularidade, o valor que será considerado para realizar a dedução do produto faturado é o valor que foi associado ao contrato.

Somente serão exibidos produtos (Itens de movimento) que possuírem saldo a deduzir maior que zero, que pertencem a movimentos com o parâmetro de dedução selecionado no tipo de movimento, e no item tenha contrato definido.

Para visualizar os valores deduzidos dos produtos selecionados, clique em anexos (do contrato) | "Produtos Faturados do Contrato". Os dados apresentados neste anexo servirão apenas para consulta. Este anexo ficará visível no contrato, apenas se existir integração com o Suprimentos/Faturamento (parâmetros do projeto| Integrações| Suprimentos/Faturamento).

**Atenção:**

O produto deve conter preço, caso o contrário não será apresentado na tela de liberação na opção de dedução.

No processo de "Backup do Projeto", os dados referentes ao produto e seus valores deduzidos não serão copiados. Isto por que cada produto (Item de movimento) do Suprimentos/Faturamento será vinculado a um contrato pertencente a um projeto no Obras e Projetos. Ao realizar o processo de restauração de backup de projeto, este poderá ser feito em outra coligada e irá gerar um novo identificador para o projeto, o vínculo com os produtos do Suprimentos/Faturamento não será mantido.

No processo de "Revisão de Projetos" a referência dos itens de movimento do Suprimentos/Faturamento com os contratos, serão atualizadas para o último projeto revisado.
