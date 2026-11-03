---
content_hash: 28aca63613b0ed3233d4d601faf044419a3cc1cb4f4bd5342c35890ab3212e93
fetched_at: '2026-06-29T00:11:04.280665+00:00'
page_id: '625937735'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Globais - Componentes de Venda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625937735
version: 10
---

#FF9000Introdução

O Cadastro de componentes da venda é de extrema importância para o correto funcionamento do Portal de Imóveis, que deve refletir os componentes cadastrados nas modalidades do TOTVS. Portanto se temos no TOTVS uma modalidade com os componentes:

| Código | Descrição |
| --- | --- |
| 1 | Sinal |
| 2 | Mensal |
| 37 | Parcela 37 |
| 280 | Chaves |
| 400 | Financiamento |

Para que esta modalidade de venda apareça corretamente no Portal de Imóveis, os componentes da tabela de modalidades do RM deverão estar cadastrados no Portal de Imóveis. Para isto acesse Backend > Globais > Componentes da Venda.

Neste cadastro é importante registrar o Código do Componente RM no campo ID\_ERP, esta é a ligação entre os componentes do Portal de Imóveis e da modalidade do RM, ou seja, para que todos os componentes da venda apareçam no Portal de Imóveis estes devem estar cadastrados e relacionados no Portal de Imóveis.

#FF9000Procedimentos para Utilização

Os demais parâmetros do cadastro de componentes, indicam o comportamento deste componente para o Portal de Imóveis. Segue a descrição destes:

* ID ERP - campo para relacionar o código do componente presente na modalidade do TOTVS.
* ORDEM - através deste campo define-se a ordem em que este componente aparecerá no Portal de Imóveis, exemplo se tenho sinal, mensal e financiamento e estes devem aparecer nesta ordem, devemos ter o campo sinal com o menor valor. Este campo não precisa ser sequencial, somente ter valores de acordo com a sequencia desejada.
* PERIODICIDADE
* MESES A ADICIONAR DA DATA INICIAL
* MESES A SUBTRAIR DA DATA INICIAL
* QUANTIDADE MÁXIMA DE PARCELAS
* QUANTIDADE MÁXIMA DE MESES APÓS ENTREGA
* PERCENTUAL MÍNIMO DE RETENÇÃO SOBRE O VALOR DA UNIDADE - o número colocado neste campo indicará o valor mínimo que deverá ficar para a empresa neste componente, após descontada comissão (quando houver). Exemplo, digamos que tenhamos uma unidade no valor de R$ 100.000,00 e o componente sinal, possui como percentual mínimo de retenção sobre o valor da unidade de 3%. Desta forma o valor mínimo aceito para a parcela de sinal será de R$ 3.000,00 ou seja 3% sobre o valor total da unidade.
* OBRIGATÓRIO - este componente é obrigatório e não pode ser excluído da simulação da proposta
* CALCULAR PARCELAS - calcula a quantidade de parcelas do inicio do componente até a data de entrega do empreendimento.
* USAR DATA DE ENTREGA COMO DATA INICIAL - tem como data de referência inicial a data de entrega do empreendimento
* USAR DATA DO COMPONENTE ANTERIOR - este campo é usado se o anterior não for utilizado. Usa a data do componente de ordem imediatamente inferior a este como data de referencia incial.
* PERMITE MUDAR O COMPONENTE - permite trocar o tipo de componente. Exemplo trocar mensal para anual.
* PERMITE MAIS DESTE COMPONENTE - permite criar mais componentes. **Observação: Este parâmetro é soberano no Portal de Imóveis para adicionar mais do componente específico, e atua de forma independente da flag "Restringe Novos Componentes" da modalidade no RM (que bloqueia a inclusão mais tipos de componentes diferentes). Logo, se o parâmetro 'Permite mais deste componente' estiver marcado, mesmo que o parâmetro da modalidade no RM "Restringe Novos Componentes" também esteja marcado, será permitido a duplicação daquele componente selecionado.**
* PERMITE ALTERAR QUANTIDADE DE PARCELAS - idem a descrição
* PERMITE ALTERAR A DATA DE VENCIMENTO - idem a descrição
* DESCONTAR COMISSÃO - quando existe percentual de comissão registrado, ele descontará desde componente o valor da comissão.
* PERMITE SELECIONAR PARA DESCONTAR COMISSÃO - quando marcado, permite que o usuário selecione o flag no componente durante a simulacão da proposta, indicando que descontará comissão deste componente.
* CALCULAR VALOR PRESENTE - faz o calculo de VPL desde componente
* EXIBIR DATA DE VENCIMENTO NA SIMULAÇÃO - quando marcado mostra no componente a data prevista deste, para não apresentar a data de vencimento da parcela, exemplo parcelas de financiamento de MCMV, basta desmarcar este parâmetro no componente.
* NÃO SOMA PERÍODO - o calculo do VPL necessita de períodos onde são aplicadas as taxas de atratividade definidas. Caso deseje que o componente permaneça com o período 0 (ou seja, sem depreciação do VPL), marque este parâmetro. Exemplo: temos uma venda que o sinal será em 4x e não desejamos que o sinal tenha o VPL descontado, portando se marcarmos este parâmetro neste componente de sinal, ele ficará assim:

|  |  |  |
| --- | --- | --- |
| **Componente** | **Período** | **Data** |
| Sinal 1 | Período 0 | Mês inicial |
| Sinal 2 | Período 0 | Mês 1 |
| Sinal 3 | Período 0 | Mês 2 |
| Sinal 4 | Período 0 | Mês 3 |
| Mensal 1 | Período 1 | Mês 4 |

* PERMITE ALTERAR VALOR - idem a descrição
* ATIVO - define se o componente estará ativo no Portal de Imóveis
* PERCENTUAL MÁXIMO RETIDO DE COMISSÃO - exemplo: O componente Sinal tem desconto de Comissão. Existe uma venda de R$100.000,00 e uma comissão de R$10.000,00. Se neste campo estiver informado 50% por exemplo, os R$10.000,00 de comissão passam a ser de R$5.000,00 (50% sobre os R$10.000).

**Contrato:**Existem algumas tags especificas para sair no contrato de venda impresso.

Existe um texto padrão do Portal de Imóveis, mas o usuário pode alterar o texto padrão acrescentando as tags disponíveis.

Tag de parcela

Foram criadas novas tag’s para agregar na parametrização da minuta e essas novas tags, tem como responsabilidade de demonstrar o valor da parcela e ou valor do montante total sem correção.

Importante:

O Parâmetro Usar valor da parcela PRICE nos relatórios deve estar parametrizado para ”SIM”

Essa tag's são configuradas no cadastro do componente no backend

As tag’s são:

* valor\_parcela\_real
* valor\_parcela\_real\_extenso  
    
  A descrição do contrato tanto em singular / plural, aceitam as tag acima.
