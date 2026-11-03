---
content_hash: 3f42d46fc05bda865ff4884038c4d9389ca5b7b69718ab4278f14a0574b374fd
fetched_at: '2026-06-29T00:05:54.876972+00:00'
page_id: '110432042'
product: rm
source: tdn-rm
title: Otimização da geração do desconto no movimento para geração de NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=110432042
version: 1
---

**CENÁRIO**

Existem dois tipos de descontos possíveis na emissão de Nota Fiscal de Serviço:

1)       Desconto incondicional

2)       Desconto condicional

O primeiro é concedido por liberalidade do prestador do serviço, sem ficar sujeito a evento futuro. Geralmente definido na contratação, deve ser destacado no documento fiscal e o ISS incide sobre o preço final do serviço, já deduzido o desconto.

Já para o segundo caso, o desconto está sujeito a um evento futuro que pode vir ou não a acontecer. Neste caso, o valor do desconto NÃO deve ser deduzido do preço do serviço para fins de tributação.

O processo Fiscal de geração de NFS-e está preparado para ambos os casos, desde que os respectivos valores estejam lançados nos campos equivalentes.

No caso do Educacional, todos os descontos concedidos pelas Bolsas que estão com o flag “**Válida após a data de vencimento**” MARCADO são lançados como descontos incondicionais. Já os descontos concedidos por Bolsas com este flag DESMARCADO não são levados para o movimento tendo efeito apenas financeiro.

Por ser um tributo de esfera municipal, temos observado que as Prefeituras possuem entendimentos divergentes quanto à classificação do desconto e, também, variações na validação dos valores informados no xml da NFS-e.

Um segundo ponto identificado é que, na geração do movimento, o valor do serviço é sempre o valor original do lançamento financeiro gerado pelo Educacional. Esse comportamento, quando a Prefeitura não possui e/ou não lê as tags de desconto, ocasiona rejeição da NFS-e uma vez que o valor total do serviço não fecha com a base de cálculo do tributo.

Diante deste cenário, é preciso fornecer ao usuário a flexibilidade de informar, por Filial, se determinado desconto concedido através de Bolsa é ou não condicional e, também, que valor será considerado como valor de serviço.

**IMPLEMENTAÇÕES**

Para atender esta demanda, propomos as seguintes implementações no sistema:

1. **1.** **Cálculo do valor do serviço:**

1. Será criado um parâmetro por Filial, para informar se o Valor do Serviço no Item de Movimento será gerado com o Valor Original (comportamento atual) ou com o Valor Líquido do lançamento, já abatidos os descontos.

1. Caso o cliente opte por usar o Valor Líquido, o campo referente ao desconto no item do movimento será gerado com valor 0 (zero).

1. **2.** **Tipo de desconto:**

1. Será criado um anexo no cadastro de bolsas para informar, por Filial, o tipo de desconto: condicional ou incondicional.

Este anexo irá conter 3 (três) opções:

                                                        i.            Não considerar desconto;

                                                       ii.            Considerar como desconto incondicional;

                                                     iii.            Considerar como desconto condicional.

Na geração do Movimento de NFS-s, o sistema hoje leva em consideração a marcação do parâmetro “**Válida após a data de vencimento**” e somente gera o desconto nesta ocasião.

1. A conversão irá criar a nova tabela e preencher o campo do Tipo de Desconto levando em consideração o parâmetro “**Válida após a data de vencimento**”:

                                                        i.            **Considerar como desconto incondicional**: todos os registros que estiverem com o flag marcado;

                                                       ii.            **Não considerar desconto**: todos os registros que estiverem com o flag desmarcado.

Dessa forma, garantimos que não vamos mudar o comportamento que temos hoje.

**IMPORTANTE!!!**

**Com estas implementações, o sistema deixará de olhar o parâmetro e irá considerar o anexo que criaremos.**

**OUTRAS CONSIDERAÇÕES**

**Bolsa de Crédito**

No caso de Bolsa de Crédito com outro sacado, o sistema já possui comportamento correto, pois são gerados dois movimentos, ou seja, duas notas fiscais: uma para o aluno e outra para o segundo sacado, ambas tributadas.

**FIES**

As Bolsas FIES devem ser tratadas no sistema como Bolsa de Crédito.

Na geração da NFS-e, existe o parâmetro "**Desconsiderar bolsas de crédito para valores de desconto**" que deve ser utilizado nas seguintes situações:

a) Caso tenha que ser emitida nota fiscal 100% em nome do aluno, o referido parâmetro deve ser MARCADO. Dessa forma, o sistema **não** irá considerar o valor do financiamento como desconto.

Exemplo:               Lançamento do Aluno:

                               Vr. do serviço:     1.000,00

                               Desconto:                     0,00

                               Vr. Líquido:           1.000,00 (valor tributado no movimento)

**OBS.: Nesta situação, NÃO deve ser gerado movimento para o lançamento gerado para o sacado para evitar a duplicidade de tributação.**

b) Caso a instituição tenha que emitir nota fiscal para o agente financiador, o referido parâmetro deve ser mantido DESMARCADO. Deve-se gerar o movimento para os dois lançamentos gerados para a parcela para que a tributação aconteça de forma correta:

Exemplo:               Lançamento do Aluno:

                               Vr. do serviço:     1.000,00

                               Desconto:                  700,00

                               Vr. Líquido:                300,00 (valor tributado no movimento)

                                Lançamento do sacado:

                               Vr. do serviço:         700,00

                               Desconto:                     0,00

                               Vr. Líquido:              700,00 (valor tributado no movimento)
