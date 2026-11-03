---
content_hash: 365a12b01b697b165a6afec8155e437a6c54c8b68e0357e54532b7a58d7c51be
fetched_at: '2026-06-29T00:10:14.569541+00:00'
page_id: '461909014'
product: rm
source: tdn-rm
title: 11.50.0 (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461909014
version: 2
---

**Contratos**

Disponibilizado o módulo de Manutenção de Contratos migrado para a plataforma .NET.

**Vinculações – Adiantamento**

Este recurso tem por finalidade a associação de um movimento em outro, associar o movimento classificado como adiantamento em um movimento classificado como controla adiantamento.   
Para este processo será necessário trabalhar com dois tipos de movimentos distintos, onde um tipo de movimento, em sua parametrização, estará classificado como “Adiantamento” e o outro, classificado “Controla Adiantamento”. Ao classificar um tipo de movimento para Adiantamento, não será possível gravar movimentações que controlem adiantamento neste tipo de movimento e vice-versa.  
Apenas tipos de movimento 1.2.XX e 2.2.XX podem ser parametrizados para trabalhar com Vinculações/Adiantamentos.

**Fiscais - Informações Adicionais:**

Para que seja possível gerar o Registro D120 no SPED Fiscal de forma a atender ao modelo de documento 07, sendo ele filho do Registro de Itens do Documento, serão criados os seguintes campos no item do Movimento:

* Município e UF de origem
* Município e UF de destino
* Placa e UF do veículo

Esses campos devem ser habilitados em lançamentos associados a Tipo de Documento cujo Código do Modelo do Documento seja 07.  
No momento de salvar o movimento, caso esses campos não estejam preenchidos, o sistema irá replicar as informações do movimento para os itens.

**Data Competência Serviço:**

Para atender a geração da rotina EFD PIS/COFINS, foi criado um novo campo o movimento, Data Competência Serviço. Este campo será exibido quando o tipo de movimento estiver parametrizado com o tributo ISS, no item ou movimento, e o tipo dos itens for Serviço ou Ambos. O campo será exibido em Integrações>>Fiscais do movimento.

**Inclusão de campos complementares para a rotina de EFD PIS/COFINS:**

Campos Indicador da natureza do frete, Número do ato concessório do Regime Drawback, Natureza da receita, Data da competência do Serviço e Código da Base de Crédito na aba fiscal do tipo de movimento mediante as parametrizações necessárias.

**Data de contabilização do movimento**

Foi disponibilizado na tela de contabilização de movimentos que é executado através da tela de visão de movimentos o campo "Data de Contabilização" para que o usuário possa escolher uma data na qual ele queira que o movimento seja contabilizado.

**Parâmetros**

Inseridos parâmetros para envio de NFe para email na etapa concernente nos parâmetros do tipo de movimento.

**Outras atualizações**

* Atualização na inclusão de município que existe para mais de um estado em movimentos parametrizados para trabalhar com CTRC.
* Atualização na inclusão de natureza orçamentária-financeira com mais de dez dígitos no cadastro de produto.
* Atualização na exclusão de produto que possui número de série cadastrado.
* Atualização na exclusão de movimento pela edição quando a visão dos movimentos só apresenta um movimento disponível.
* Atualização na execução de fórmulas de aprovação de modo que o sistema apresente uma mensagem de consistência para fórmulas que não utilizem somente 0 ou 1 como condições.
* Atualização na geração de fatura para lançamentos originados do TOTVS Educacional.
* Atualização na geração dos lançamentos financeiros com cli/for que possua carência de vencimento.
* O sistema permite a gravação do movimento validando o valor do serviço calculado por fórmula ao gerar o lançamento financeiro. Desse modo a gravação do valor do serviço ocorre quando não ultrapassa o valor original do lançamento ou quando não há fórmula.
* Atualização na cópia por referência que utiliza o motivo NF Complementar / Retificadora em tipo de movimento de transferência para que não consista o cliente/fornecedor ao salvar o movimento.
* Atualização para que quando for alterado algum parâmetro da data de fechamento de estoque, seja apresentada a mensagem de será preciso regerar saldos e custos.
* Atualização no faturamento de movimentos de modo que leve os tributos calculados se assim parametrizados.
* Atualização na consistência na inclusão de registros no cadastro de produtos quando já existe um com o mesmo código inserido.
* Atualização para que ao clicar na descrição de uma fórmula no parametrizador, seja possível visualizar o conteúdo da fórmula corretamente.
* Atualização no serviço de estoque para números de série para que na alteração dos itens de movimento, os registros de número de série também sejam recalculados.
* Atualização no serviço de estoque para números de série para que na alteração dos itens de movimento, os registros de número de série também sejam recalculados.
