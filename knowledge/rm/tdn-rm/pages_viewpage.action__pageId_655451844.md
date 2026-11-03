---
content_hash: 5067da29d07f51654a15e62b9c0b054bf7b86c331471513ac9e827b673c248d3
fetched_at: '2026-06-29T00:11:12.598302+00:00'
page_id: '655451844'
product: rm
source: tdn-rm
title: 'Importar Cotações: API - Banco Central do Brasil'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655451844
version: 12
---

Por intermédio desse processo é possível importar as cotações de acordo com a disponibilização do Banco Central do Brasil via API.

**Moedas disponíveis para cotação:**

O Banco Central disponibiliza cotações para as seguintes moedas:

1. Dólar australiano (venda)
2. Dólar canadense (venda)
3. Franco suíço
4. Coroa dinamarquesa
5. Euro
6. Libra Esterlina
7. Iene
8. Coroa norueguesa
9. Coroa sueca
10. Dólar dos Estados Unidos (venda)

640432

**Funcionamento do processo:**

Deve-se optar por uma ou mais moedas disponíveis, informando respectivamente o seu paralelo no sistema, assim como, informar também o símbolo correspondente a moeda Real brasileira.

IMPORTANTE!

As informações referentes a moedas e seus respectivos símbolos serão gravadas como "preferência do usuário". Assim, ao realizar novamente o processo, será necessário alterar apenas ajustes pontuais.

**Cotação do fechamento do dia anterior (Agendamento)**

Esta opção deve ser usada para criar um agendamento (JOB) que buscará as cotações no BC, sempre considerando D-1 (dia anterior). Nesse processo, recomenda-se optar por dias que retornem cotações do dia anterior, por exemplo, terça-feira (retorna cotação de segunda-feira), quarta-feira (retorna cotação de terça-feira), quinta-feira (retorna cotação de quarta-feira), sexta-feira (retorna cotação de quinta-feira) e sábado (retorna cotação de sexta-feira). 

Para usar essa opção é preciso parametrizar seu ambiente para 3 camadas. Consulte esta documentação: [Ambiente 3 Camadas](https://tdn.totvs.com/display/public/LRM/Ambiente+3+Camadas).

Exemplo de agendamento

**Buscar Cotação por Período**

Utilize essa opção para buscar as cotações de um período específico. Essa opção não habilita o processo de recorrência, pois os valores retornados seriam sempre os mesmos. 

Fique ligado!

Ao optar por um período que já possua cotações para as moedas/símbolos selecionados, esses serão sobrescritos.

Imagem

**Inserir Cotação Inversa**

Ao habilitar opção de Cotação inversa, serão inseridas também cotações de Real para as Moedas escolhidas, geradas a partir do cálculo:  1 / cotação da moeda correspondente.

IMPORTANTE!

O valor gerado pela Cotação Inversa é calculado, portanto, podem haver diferenças ao arredondar ou ao truncar o valor.

**Informações úteis:**

Link da API: <https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/swagger-ui3#/>

Documentação: <https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/documentacao>
