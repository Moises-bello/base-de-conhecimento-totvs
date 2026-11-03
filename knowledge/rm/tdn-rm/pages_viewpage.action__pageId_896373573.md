---
content_hash: 13047817feafbeb0df1f07e5263895488de72b91602d0eadcffa0e761e089bed
fetched_at: '2026-06-29T00:12:01.585323+00:00'
page_id: '896373573'
product: rm
source: tdn-rm
title: PI - Proposta - Atribuir diferença tabela preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=896373573
version: 8
---

**Funcionalidade: Ajuste do Valor Total do Financiamento para Manter o Poder de Compra**

**Descrição Geral**  
Esta funcionalidade permite que, ao alterar qualquer componente do plano de financiamento (por exemplo, reduzir o valor total de um conjunto de parcelas anuais), o valor total do negócio não seja prejudicado. Caso haja uma redução em algum dos componentes (como a parcela anual), o sistema possibilita redistribuir o valor subtraído para outra(s) modalidade(s) de pagamento (mensal, entrada, ou demais componentes), garantindo que o total final do financiamento se mantenha inalterado.

Desta forma, se o cliente deseja modificar as condições iniciais de pagamento, mas o fornecedor precisa manter o mesmo poder de compra (ou seja, o valor total acordado na data da venda), esta funcionalidade oferece a ferramenta para ajustar o plano financeiro de modo simples e transparente.

Importante

O **desconto concedido na proposta** é tratado como uma **negociação global e o processo de atribuir diferença não irá zerar esse valor.**  
Ao salvar o desconto, o sistema **distribui automaticamente esse valor, de forma proporcional** entre todos os componentes da proposta, ajustando os valores de cada item conforme a proporção do desconto.

Se for necessário realizar uma negociação e atribuir diferença, e ainda assim conceder um desconto, recomendamos seguir esta ordem: primeiro, realizar a negociação e atribuir a diferença nos componentes; em seguida, aplicar o desconto desejado.

**Exemplo de Uso 01**  
Suponha um plano de financiamento original de R$ 1.100.000,00 distribuído em:

* Entrada: R$ 220.000,00
* Parcelas Mensais: R$ 440.000,00 (em 100 parcelas)
* Parcelas Anuais: R$ 440.000,00 (em 6 parcelas anuais)

Se o cliente decide reduzir a parcela anual em R$ 100.000,00 sem realocar este valor, o total do financiamento cai para R$ 1.000.000,00. Utilizando esta funcionalidade, é possível, por exemplo, somar esses R$ 100.000,00 removidos da parcela anual à componente mensal, elevando seu total para R$ 540.000,00 e retornando o financiamento ao total de R$ 1.100.000,00 originalmente pactuado.

**Exemplo de Uso 02**

* Valor total da unidade (tabela): **R$ 100.000,00**
* Soma atual dos componentes da proposta: **R$ 100.050,00**
* Diferença: **–R$ 50,00** (proposta maior que o valor da unidade)

**Ação:**  
O usuário seleciona o menu “...” de um componente e escolhe **Atribuir Diferença**.

**Resultado:**  
O sistema **subtrai R$ 50,00** do valor do componente escolhido.

Se o componente possuir **R$ 30,00** e a diferença a ser subtraída for **R$ 50,00**, o sistema:

1. **Remove o componente de R$ 30,00** (valor zerado);
2. Continua subtraindo os **R$ 20,00 restantes** de outros componentes (se aplicável), até atingir o total da diferença.

> Esse comportamento garante que o valor total da proposta sempre se alinhe ao valor da unidade, mesmo que seja necessário eliminar componentes de baixo valor.

**Passo a Passo para Utilização**

1. **Identificar a Diferença**: Após a mudança desejada pelo cliente (por exemplo, reduzir a parcela anual), verifique o valor total do financiamento atualizado.
2. **Determinar o Componente de Destino**: Escolha em qual outro componente (mensal, entrada ou outro) a diferença será inserida para restaurar o valor total original.
3. **Aplicar o Ajuste**: Atualize o componente de destino acrescentando a diferença, mantendo assim o total do financiamento inalterado.

**Benefícios**

* **Flexibilidade**: Permite acomodar solicitações do cliente sem perder o valor total negociado.
* **Transparência**: O cliente visualiza claramente como a redução em uma parte é compensada por um acréscimo em outra.
* **Simplicidade**: O procedimento evita cálculos complexos como o uso de Valor Presente Líquido (VPL), mantendo a operação simples e direta.

**Considerações**

* A funcionalidade não altera datas ou prazos de pagamento, apenas redistribui valores entre os componentes do financiamento.
* Caso o cliente deseje outra forma de compensação (por exemplo, dividir a diferença entre entrada e parcelas mensais), é possível aplicar o mesmo raciocínio.
* É responsabilidade do usuário do sistema garantir que as alterações sejam comunicadas e acordadas com o cliente, mantendo a clareza e a integridade do contrato original.

É importante reforçar que o **desconto geral** (aplicado pelo botão *Desconto*) pode ser definido de duas formas: **percentual sobre o valor** ou **valor fixo**.

A opção **percentual** serve apenas para o **cálculo imediato**, considerando o valor atual da proposta no momento em que o desconto é atribuído. O sistema **não armazena o percentual**, mas sim o **valor total do desconto** calculado nesse instante.

Após a aplicação, o **valor do desconto permanece fixo** e **não será recalculado automaticamente**, mesmo que o valor da proposta seja alterado posteriormente, por exemplo, ao atribuir diferenças nos componentes.

Caso o cliente deseje modificar o desconto, é necessário **excluir o valor existente e aplicar um novo desconto**.
