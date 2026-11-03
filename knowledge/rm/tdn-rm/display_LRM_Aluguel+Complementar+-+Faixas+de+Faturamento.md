---
content_hash: d497dbede32a57f839a0f1d22dfd880bb7be38cd1df082c7e3c092b2376be8e8
fetched_at: '2026-06-29T00:11:57.007384+00:00'
page_id: '874192688'
product: rm
source: tdn-rm
title: Aluguel Complementar - Faixas de Faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Aluguel+Complementar+-+Faixas+de+Faturamento
version: 12
---

Anexo disponível a partir da versão 12.1.2410.

**Importante: Estaremos descontinuando o aditivo de alteração de parâmetros do aluguel complementar na release 12.1.2410. Toda a modificação das faixas será feita pelo próprio usuário, no cadastro de faixas de faturamento, proporcionando maior agilidade na alteração de valores, períodos e descontos, dispensando a necessidade do aditivo.**

* **Botões Incluir e Excluir:** Respectivamente realizam a inclusão e exclusão de novas faixas de faturamento.
* **Tipo:** Tipo de Faturamento podendo ser Faturamento, Fluxo de Vendas ou Faturamento Composto.
* **Data de início:** Início do Período da medição realizada.
* **Data Final:** Final do Período da medição realizada.
* **Percentual Faturamento:** Percentual que será acrescentado no valor do aluguel. Esse percentual pode ser definido com 0%, quando há a necessidade de inserir alguma isenção no período da faixa.
* **Valor Inicial:** Valor Inicial que será cobrado no valor do aluguel.
* **Valor Final:** Valor Final que será cobrado no valor do aluguel.
* **Percentual Faturamento 2:** Valor do percentual do segundo faturamento quando o faturamento é do tipo composto. Este faturamento é utilizado por exemplo nos faturamentos de cinema, onde existe o faturamento da bomboniere e também da bilheteria. Esse percentual pode ser definido com 0%, quando há a necessidade de inserir alguma isenção no período da faixa.
* **CTO Mensal:** O custo total da operação é compreendido no sistema como a soma de todos os valores do contrato, como **Condomínio**, **Fundo Promocional** e **Aluguel**. Seu total será utilizado para calcular os valores de aluguel complementar em determinada faixa.
* **Desconto CTO Mensal:** O desconto do CTO é um valor que será considerado nos cálculos de CTO, sempre a subtrair neste período.

### Exemplo de Faixas de medição com diferentes CTO's escalonando cobranças

---

Visando flexibilizar o cadastro do CTO, a partir da versão 12.1.2209, estamos atualizando o mesmo para que ele passe a fazer parte das faixas de medição. Possibilitando cobranças variadas e escalonamento de valores.

Na imagem acima temos algumas faixas cadastradas e divididas (inicio e fim) por meses ou competências. Veja que o sistema permite que tenhamos vários valores de CTO, de acordo com cada faixa cadastrada. Isso permite uma flexibilidade de cálculos, onde meses possuem diferentes cobranças e o CTO não necessariamente será estático durante esse tempo.

Exemplo do aluguel complementar gerado para a competência 01/21. Dentro da primeira faixa e o CTO mensal será de R$ 7.500. Saiba mais sobre o processo de Geração de Aluguel Complementar .

*Valor do faturamento na competência de 01/2021: 250.000,00*  
*Percentual do faturamento na competência de 01/2021: 4,0000%*  
*Cálculo do valor do aluguel complementar (Valor do faturamento \* percentual / 100): 250.000,00 \* 4,0000% / 100 = 10.000,00*

*Cálculo do valor do aluguel complementar (faturamento - valor CTO fixo (Valor Mensal)):*  
***10.000,00 - 7.500,00 = 2.500,00***

Exemplo do aluguel complementar gerado para a competência 04/21. Dentro da quarta faixa e o CTO mensal será de R$ 10.500. Saiba mais sobre o processo de Geração de Aluguel Complementar .

*Valor do faturamento na competência de 04/2021: 280.000,00*  
*Percentual do faturamento na competência de 04/2021: 7,0000%*  
*Cálculo do valor do aluguel complementar (Valor do faturamento \* percentual / 100): 280.000,00 \* 7,0000% / 100 = 19.600,00*

*Cálculo do valor do aluguel complementar (faturamento - valor CTO fixo (Valor Mensal)):*  
***19.600,00 - 10.500,00 = 9.100,00***

Após a criação destes períodos de Aluguel Complementar, os mesmos poderão ser utilizados para a geração destes novos valores a serem implementados ao valor do aluguel. O TCGI dispõe de um processo para a geração destes valores. Saiba mais sobre o processo de Geração de Aluguel Complementar .

As informações preenchidas nesta tela de Aluguel Complementar serão usadas como base para o preenchimento das Medições e o processo de Gerar Aluguel Complementar, usa as Medições cadastradas para esse fim. Para maiores informações sobre Medições .

Importante

* As faixas de faturamento com percentual e valores diferentes, poderão ser inseridas num mesmo período, desde que possuam os **mesmos valores de CTO e Desconto** cadastrados.
