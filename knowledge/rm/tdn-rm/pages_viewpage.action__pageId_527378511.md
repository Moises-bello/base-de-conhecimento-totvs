---
content_hash: f2a0eea0ef55f4336703236710f9c14a44e7f91d541d4bd6c10b8d4c40cc551b
fetched_at: '2026-06-29T00:10:32.583911+00:00'
page_id: '527378511'
product: rm
source: tdn-rm
title: 0000_00Reversão de Impairmet.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527378511
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | reversão de impairmet |
| **Versões:** | 12.1.20 |
| **Ocorrência:** |  |
| **Ambiente:** |  |
| **Passo a passo:** | informar R$ 1.000,00 indicando este como valor absoluto da perda. Ao informar R$ 4.000,00, o sistema automaticamente indicará que R$ 1.000,00 são de perda por Impairment, fazendo com que, no final do mês, na tabela de cálculos, as faixas sejam representadas da seguinte forma:   * Informando o Valor total.        * Marcando a Opção de Inserir valores Absolutos de Impairment     R$:   * Valor Base: R$ 9.000,00 * Depreciação R$ 150,00 * Depreciação Acumulada R$ 5.150,00 * **Impairment R$1.000,00**   Observação : Ao realizar o processo de impairment, observe qual o calculo esta informado no cenário, ou seja se a opção de cota esta marcada ou desmarcada.  Se a opção ( **cota proporcional**) estiver marcada, o sistema irá calcular a depreciação proporcionalmente a partir da data que esta sendo realizado o impairment. Se a opção cota proporcional estiver desmarcada, o valor de depreciação será integral independente da data que esta sendo realizada.  Após 3 meses realizado o impairment verificou- se que a perda não foi de R$1.000,00 e sim de R$400,00. Para que esse processo fosse revertido, foi necessário usar o processo de reversão.  Ao selecionar previamente este patrimônio o sistema irá apresentar na coluna "valor de impairment" R$ 1.000,00, o usuário irá informar manualmente no campo "valor de reversão" R$ 600,00. O sistema irá gerar uma ocorrência de reversão de impairment, a partir deste momento a redução por perdas deste patrimônio será R$ 400,00 e não mais R$ 1000,00.  Após a reversão os valores ficará desta forma;    Contabilização: O sistema permite que a reversão seja contabilizada e integrada a Totvs Gestão Contábil.   **Para calcular a taxa de depreciação na Reversão de Impairment o sistema procede da seguinte forma:**   * 1º- Soma o "Valor Contábil" com o "Valor de Reversão": será o novo valor contábil;  9.600,00 * 2º- Soma o "Valor Base de Depreciação" com o "Valor de Reversão": será o novo valor base; * 3º- Divide o valor contábil calculado no item 1 com o valor base de depreciação calculado no item 2; * 4º- O resultado encontrado no divisão de valores realizada no item 3 é multiplicada por 100; * 5º- O valor encontrado no item 4 será dividido pela vida útil restante (meses), sendo o resultado a taxa de depreciação.   Ou seja, como é uma reversão, deve-se considerar o valor da reversão em relação ao valor contábil e o valor base de depreciação.   **Abaixo as regras do sistema para que a reversão seja realizada com sucesso:**   1. Patrimônios Inativos ou totalmente baixados não poderão sofrer a reversão de Impairment. 2. O valor da reversão não pode ser maior do que o valor de impairment realizado anteriormente para os patrimônios envolvidos no processo. 3. Valor de Reversão não pode ser negativo. 4. Data da reversão deve estar dentro do período de cálculo e maior que a data de aquisição do patrimônio. 5. Patrimônios remetidos ou integrados a objetos de manutenção não podem sofrer ocorrência de impairment ou reversão. |
| **Observações:** |  |
