---
content_hash: 64234ce936e26faf973baf9851b00fed2ea406e3c3ece88286b8c8eee6802cce
fetched_at: '2026-06-29T00:09:25.891831+00:00'
page_id: '423938195'
product: rm
source: tdn-rm
title: Controle de Deduções Contratuais (Integração Gestão de Construção e Projetos
  x Gestão de Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938195
version: 3
---

As deduções tratadas neste processo são aquelas que envolvem descontos ou débitos não fiscais, como: alimentação, transporte, combustível, dentre outras.  Estas não são abatidas do valor do serviço, mas sim descontadas no momento do pagamento.

**Controle de Deduções através do TOTVS Gestão de Estoque, Compras e Faturamento**

Deverão ser realizadas as seguintes parametrizações:  
 O movimento utilizado para tratar as deduções de um contrato de prestação de serviços no TOTVS Gestão de Estoque, Compras e Faturamento deve ser do tipo 1.1.XX e deve estar parametrizado na etapa Item – Valores Financeiros 2/2 , campo Dedução Este parâmetro com uma das seguintes opções:

* **Não Usa**: não usa dedução no item.
* **Usa Percentual**: o valor da dedução deverá ser informado em percentual.
* **Usa Valor**: a dedução deverá ser informada em valor.
* **Usa Ambos**: utiliza percentual e valor.

No movimento deve ser informada a fórmula do Valor do Documento - etapa MOV - Valores Financeiro 2/4. Essa fórmula deve considerar o valor de todas as deduções dos itens.   
 Exemplo: MVB - TVIM('VALORDEDUCAO')  
 Caso, utilize um movimento do tipo 1.2.XX que gere lançamentos financeiros e deseja considerar a dedução nos lançamentos financeiros, o movimento deverá ser parametrizado na etapa Fin-Faturamento 3/6 - Fórmula do Valor a Ratear.

**Descrição do Processo**

Os campos Valor Deduzido e Percentual Deduzido serão apresentados na pasta Tributos e Valores na edição do item de movimento.  
Quando o tipo de movimento estiver configurado com Tipo de Dedução igual a Ambos, sempre que na edição do Item for alterado o valor ou percentual, deve-se realizar o recálculo considerando o novo valor ou percentual informado.   
Para isso devem ser consideradas as seguintes fórmulas de cálculo:  
Percentual: Valor Deduzido  (Valor do Item   100).  Valor: Valor Deduzido (Valor do Item  Percentual Deduzido)  100.   
O cálculo dos valores financeiros dependentes dos itens também deve considerar a dedução do item, ou seja, quando o tipo de movimento utilizar dedução deve-se realizar os cálculos dos valores considerando as fórmulas listadas acima.  
***Observações***: Os campos de Percentual Deduzido e Valor Deduzido deverão respeitar as casas decimais definidos nos parâmetros gerais do sistema.

**Regras para Faturamento e Cópia de Referência**

1. Quando os tipos de movimento de origem e destino utilizarem Dedução no Item igual a Usa Valor: • Valor deduzido do item de movimento destino recebe o valor deduzido do item de movimento origem. • Se o movimento de destino Usar Dedução igual a Percentual, o campo recebe o valor zero.
2. Quando os tipos de movimento origem e destino Utilizarem Dedução no Item igual a Usa Percentual: • Percentual deduzido do item de movimento destino recebe o percentual deduzido do item de movimento origem. • Se o movimento de destino Usar Dedução igual a Valor o campo recebe o valor zero
3. Quando os tipos de movimento de origem e destino utilizarem Dedução no Item igual a Usa Ambos • Valor deduzido do item de movimento destino recebe o valor deduzido do item de movimento origem. • Percentual deduzido do item de movimento destino recebe o percentual deduzido do item de movimento origem.

**Controle de Deduções Contratuais via TOTVS Obras e Projetos**

Deverão ser realizadas as seguintes parametrizações:  
 O movimento deve ser do tipo 1.1.XX e deve estar parametrizado na etapa "Mov – Valores Financeiros 1/4", parâmetro "Desconto", para ser registrado em Valor, Percentual ou Ambos.  
 Assim como no controle de deduções feito através do módulo de Materiais, deverá ser parametrizada a Fórmula do Valor do Documento na etapa MOV-Valores Financeiros 2/4.

**Descrição do Processo**

O movimento será enviado ao BackOffice Materiais através de contrato gerado no TOTVS Obras e projetos. O valor da medição do contrato será enviado integralmente e o valor referente á dedução será enviado para o campo "Desconto" no movimento |aba Valores.   
 ***Observação***: Quando o movimento é gerado pelo TOTVS Obras e Projetos, o campo Desconto não poderá ser alterado, assim como nos movimentos de destino gerados através de faturamento.
