---
content_hash: 551aaf402f68423b188ab78a75410e4ef4588da1988f53834d87d58155a16cbe
fetched_at: '2026-06-29T00:10:31.019496+00:00'
page_id: '520659271'
product: rm
source: tdn-rm
title: Contrato de Locação - Dados Gerais - Aluguel Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659271
version: 19
---

O Aluguel Complementar é uma forma de cobrança que visa implementar um valor a mais aos valores de aluguel de acordo com o Faturamento do Locatário. Esse complemento é feito por período, por exemplo, supondo que o valor do aluguel seja R$ 1.000,00 e o valor do Aluguel Complementar seja R$ 500,00, com isso o valor total do aluguel será de R$ 1.500,00. Estes valores são gerados baseados no faturamento.

Para acessar a tela de Aluguel Complementar abra Aluguel / Contrato de Locação / Aba lateral de Dados Gerais / Definir Aluguel Complementar, este anexo do Contrato de Locação possibilita a inclusão dos parâmetros do Aluguel Complementar. O sistema dispõe também de um processo que irá gerar os valores referentes ao Aluguel Complementar.

**Campos da tela:**

* **Tipo de Evento:** Este registro pode ser cadastrado também em Aluguel / Cadastros / Tipo de Evento Financeiro. O único Tipo de Evento Financeiro aceito para o Aluguel Complementar é o do tipo **Locação Complementar;**
* **Buscar Vencimento:** Possui apenas duas opções, Informar e Contrato. Quando a opção selecionada é Informar, o campo **Regra de Vencimento** ao lado é habilitado para edição, caso a opção seja Contrato, as informações de vencimento serão buscadas do Contrato de Locação em questão. As informações de vencimento estão localizadas em Contrato de Locação / Identificação / Código regra vencimento;
* **Regra de Vencimento:** Este campo é habilitado para edição quando o campo Buscar Vencimento está com a opção Informar selecionada;
* **Buscar Parâmetro:** Possui apenas duas opções, Informar e Contrato. Quando a opção selecionada é Informar, o campo Parâmetro de integração financeira ao lado é habilitado para edição, caso a opção seja Contrato, as informações de parâmetros de integração financeira serão buscadas do Contrato de Locação em questão. As informações de parâmetros de integração financeira estão localizadas em Contrato de Locação / Identificação / Parâmetro de Integração Financeira;
* **Parâmetro de integração financeira:** Este campo é habilitado para edição quando o campo Buscar Parâmetro está com a opção Informar selecionada;
* **Fórmula para o cálculo do Aluguel Complementar:** Visando uma maior flexibilidade nos cálculos do aluguel complementar, além das funções de fórmula já existentes, à partir da **versão 12.1.2310**, estamos expandindo este cadastrando e dando novas opções para cálculos complementares. Para entender melhor sobre essas modificações**, [acesse a página aqui (Clique Aqui).](https://tdn.totvs.com/pages/viewpage.action?pageId=808480005)**

* Para maiores informações sobre Funções de Fórmula ;
* **% Faturamento:** Para atender empresas que trabalham com aluguel de lojas e estabelecimentos, foi criado o campo **% Faturamento**. Existem casos em que o Contrato de Locação trata de um ou mais imóveis, que compõe a locação de uma loja composta de mais imóveis, sendo que parte pertence a terceiros. Com este campo o usuário poderá informar que indica o que aquele imóvel representa em relação ao todo da loja alugada. Este campo deve ser utilizado apenas com fórmula. Para ver um exemplo de Aluguel Complementar com aplicação de % Faturamento .
* **Valor Período:** Na locação de shopping este é o campo que define o valor mínimo anual que deverá ser atingido para que não seja gerada uma cobrança complementar.
* **Meses:** Período em meses em que ocorrerá a cobrança do aluguel complementar caso não se atinja o valor mínimo anual.
* **Considera condomínio:** Quando esta opção é preenchida o condomínio será sempre deduzido do aluguel complementar quando a base do mesmo é sobre o contrato de locação. Caso seja utilizado o Valor CTO Mensal presente na faixa dos períodos de medição, esta opção estará marcada automaticamente, podendo ser desmarcada pelo usuário.
* **Considera fundo promocional:** Quando opção é preenchida o fundo promocional será sempre deduzido do aluguel complementar quando a base do mesmo é sobre o contrato de locação. Caso seja utilizado o Valor CTO Mensal presente na faixa dos períodos de medição, esta opção estará marcada automaticamente, podendo ser desmarcada pelo usuário.
* **Considera valor contrato:** É utilizado para definir se o valor do contrato de locação será considerado no cálculo do aluguel complementar. **Quando ativado (marcado):** O cálculo do aluguel complementar leva em consideração o valor do contrato principal como base para determinar o faturamento. Isso é útil quando o aluguel complementar deve ser proporcional ou relacionado ao valor do contrato original. **Quando desativado (desmarcado):** O cálculo do aluguel complementar ignora o valor do contrato principal. Nesse caso, o faturamento do aluguel complementar será calculado com base em outras condições ou regras parametrizadas, sem depender do valor do contrato.
* **Informar valor bruto no faturamento:** Ao marcar este campo, será apresentado o valor bruto para que possa ser informado no momento da realização o controle de faturamento e controle de faturamento diário. Permitindo registrar o valor total da receita gerada por esses contratos. OBS: Este campo é informativo não sendo possível a utilização de fórmulas.

Importante

A partir da release **12.1.2502** evoluímos o cadastro de períodos de medição, que estará localizado no anexo Faixas de Faturamento.

Veja Também

---
