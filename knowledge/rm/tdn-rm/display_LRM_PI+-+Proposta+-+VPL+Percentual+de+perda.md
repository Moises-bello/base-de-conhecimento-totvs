---
content_hash: 2e73e917a0a87fdb3579491bf6954bf565c7ff90c08a57e2e90cd0d6a9059dd8
fetched_at: '2026-06-29T00:11:33.962661+00:00'
page_id: '763255081'
product: rm
source: tdn-rm
title: PI - Proposta - VPL Percentual de perda
type: documentation
url: https://tdn.totvs.com/display/LRM/PI+-+Proposta+-+VPL+Percentual+de+perda
version: 5
---

---

No sistema de Gerenciamento de Relações com o Mercado (RM), é possível configurar o percentual de perda do Valor Presente Líquido (VPL). Essa configuração se aplica exclusivamente durante a criação de propostas no Portal de Imóveis. Os percentuais podem ser definidos nas seguintes seções de cadastro:

1. Modalidade: Essa configuração está disponível na seção de Integração/Portal de Imóveis.
2. Empreendimento: A configuração correspondente está disponível na seção de Integração/Portal de Imóveis.

É importante observar que, se o percentual de perda estiver configurado tanto na modalidade quanto no empreendimento, a modalidade sempre terá prioridade sobre o empreendimento. Isso significa que a opção de menor nível será considerada na hora de calcular o percentual de perda.

Além disso, caso o desconto oferecido pelo usuário seja superior à parametrização dos percentuais de perda, uma mensagem será exibida no portal, informando que a proposta foi reprovada para o usuário ou corretor.

Exemplo:  
Plano reprovado:  
A taxa de perda do VPL da proposta 60,00% é superior ao máximo da(o) Modalidade 10,00%

**OBS: Sobre os parâmetros necessários para validar VPL:**  
**Validar o valor do VPL acumulado:** Verifica se o (VPL) calculado para o cliente é maior do que um valor de referência estabelecido na tabela. Isso ajuda a determinar se um investimento é financeiramente atrativo, com base em critérios financeiros predefinidos. Se o VPL do cliente for superior ao valor da tabela, o investimento pode ser considerado vantajoso.  
  
**Validar o valor do VPL até a entrega:** Validar ou não o valor do VPL até a data de entrega comparando com o valor da tabela de preço envolve decidir se o VPL calculado até a data de entrega é aceitável, com base na comparação com um valor de referência estabelecido na tabela de preços. Se o VPL calculado for igual ou superior ao valor da tabela, geralmente é considerado adequado. Isso ajuda a avaliar se o projeto ou investimento está alinhado com os critérios financeiros estabelecidos.  
  
**Validar o VPL de modo linear:** Verifica o (VPL) período a período, avaliando as condições de pagamento do cliente em comparação com a tabela.  
 **A opção "Sim"** indica que a validação será feita periodicamente, considerando as condições de pagamento do cliente em relação à tabela para cada período individual.  
**A opção "Não"** indica que a validação será baseada no VPL acumulado, ou seja, a comparação do VPL total, sem avaliar cada período separadamente.

A nota destaca que, quando a validação é feita de modo linear, o parâmetro de percentual de aprovação do VPL não terá efeito, pois a validação é realizada período a período, não considerando um limite de aprovação global.
