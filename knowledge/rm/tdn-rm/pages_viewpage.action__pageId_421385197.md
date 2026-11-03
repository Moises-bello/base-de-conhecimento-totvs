---
content_hash: bc7190e7ad0e15e1ff23afca51d9af5a4348c6f546999615a7944e39b66ea17f
fetched_at: '2026-06-29T00:09:14.321236+00:00'
page_id: '421385197'
product: rm
source: tdn-rm
title: Períodos Cronograma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385197
version: 2
---

---

**Data de Início:**

Informe a data do primeiro período dos cronogramas planejado, realizado e medido.

Ao aumentar a data de início do cronograma, pode-se fixar o cronograma por data, onde os valores já informados permanecem para aquela mesma data.

**Observações:**

Para fixar o cronograma por data, é necessário que o tipo de período obrigatoriamente seja "Mensal".

Somente será possível fixar o cronograma por data, caso o número de períodos seja aumentado.

**Exemplo:**

O cronograma está parametrizado para trabalhar da seguinte maneira:

Data de início: 03/01/2008

Número de Períodos: 5

Tipo do Período: Mensal

A seguinte estrutura foi gerada, a partir da parametrização acima:

| Número do Período | Data de Início | Data de Término | Lançamento (%) |
| --- | --- | --- | --- |
| 1º | 03/01/2008 | 31/01/2008 | 12,84 |
| 2º | 01/02/2008 | 29/02/2008 | 18,72 |
| 3º | 01/03/2008 | 31/03/2008 | 16,89 |
| 4º | 01/04/2008 | 30/04/2008 | 24,56 |
| 5º | 01/05/2008 | 31/05/2008 | 26,99 |

Alterei a parametrização do cronograma e optei por fixar o cronograma por data conforme abaixo:

Data de início: 05/12/2007

Número de Períodos: 6

Tipo do Período: Mensal

Fixando o cronograma pelas datas, a estrutura dos lançamentos deverá ser a seguinte

| Número do Período | Data de início | Data de Término | Lançamento (%) |
| --- | --- | --- | --- |
| 1º | 05/12/2007 | 31/12/2007 | - |
| 2º | 01/01/2008 | 31/01/2008 | 12,84 |
| 3º | 01/02/2008 | 29/02/2008 | 18,72 |
| 4º | 01/03/2008 | 31/03/2008 | 16,89 |
| 5º | 01/04/2008 | 30/04/2008 | 24,56 |
| 6º | 01/05/2008 | 31/05/2008 | 26,99 |

Os lançamentos foram mantidos nos períodos em que eles foram lançados primeiramente.

**Núm. de Períodos:**

Informe a quantidade de períodos que terá no cronograma. A quantidade máxima de períodos é 250. O número de períodos só poderá ser alterado, após os lançamentos dos Cronogramas (Previsto, Realizado, Medido), se este número for maior ou igual ao número de períodos que já possuem previsões.

**Dicas:**

1) Suponha que o Cliente necessite fazer um controle diário da obra, utilizando períodos diários. Como algumas obras podem ter um período de 1 a 4 anos, recomenda-se usar a medição de contrato que possibilita a medição diária em quantos períodos desejar. Depois atualize o cronograma com os dados da medição, pois, o gerenciamento mensal é melhor.

2) Suponha que a obra tenha duração de 4 anos, dessa forma a periodicidade não poderia ser diária, pois excederia a quantidade máxima de períodos do Sistema. Quando isso ocorre recomenda-se a utilização de períodos onde a quantidade de períodos fica, no máximo, 250.

Tipo dos Períodos:

Informe se o cronograma será mensal, quinzenal (corridos), quinzena, semanal (corridos), semana, diária ou personalizada. Se for escolhido o tipo personalizado, informe o número de dias por período.

Dias por Período:

Este campo será habilitado se for escolhido como tipo dos períodos a opção "Personalizado". Informe o número de dias que terá cada período.

**Observações:**

Ao gerar Períodos de Cronograma cujo Tipo de Período for "Personalizado", será possível editar manualmente a data de inicio e término dos períodos gerados, respeitando as reagras abaixo:  
    
 1 - As Datas não podem sobrepor umas as outras;

2 - As Datas não podem ter períodos posteriores com datas menores que os anteriores,

3 - As Datas não podem deixar existir espaços entre os períodos.

4 - As Datas de inicio dos Períodos, não podem ser maiores que as datas finais do Período.  
    
 **Exemplos:**

O Tipo do Período Quinzena vai preencher os períodos com quinzenas fechadas. O 1º período irá até o dia 15 e o 2º até o último dia do mês sempre. Se o 1º período começar no dia 09, irá terminar no dia 15. O 2º período irá começar no dia 16 e terminar no último dia do mês. E assim, sucessivamente.

O Tipo de Período Quinzenal (corridos) vai preencher os períodos com quinzenas com dias corridos. O 1º período irá iniciar na data início dos períodos e a data de término será quinze dias (corridos) depois. Se o 1º período começar no dia 09, irá terminar no dia 24. O 2º período irá começar no dia 25 e terminar quinze dias depois. E assim, sucessivamente.

O Tipo de Período Semana vai preencher os períodos com semanas fechadas. O 1º período irá até o 7º dia da semana e o 2º irá começar no 1º dia da semana seguinte até o último dia dessa semana. Se o 1º período começar no dia 01/10/2003, irá terminar no dia 04/10/2003. O 2º período irá começar no dia 05/10/2003 e terminar no dia 11/10/2003. E assim, sucessivamente.

O Tipo do Período Semanal (corridos) vai preencher os períodos com semanas com dias corridos. O 1º período irá começar da data de início dos períodos e a data de término será sete dias (corridos) depois. Se o 1º período começar no dia 09, irá terminar no dia 15. O 2º período irá começar no dia 16 e terminar sete dias depois. E assim, sucessivamente.

---
