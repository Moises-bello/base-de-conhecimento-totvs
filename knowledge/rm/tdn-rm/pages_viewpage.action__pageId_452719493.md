---
content_hash: 277a0aeaf932a50a967909e33c3b7d6a6ce6930e471c0fe4cd7b15f3ba92edb9
fetched_at: '2026-06-29T00:10:07.996381+00:00'
page_id: '452719493'
product: rm
source: tdn-rm
title: Opções de Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719493
version: 2
---

**Opções de Lançamento**

---

Geralmente o lançamento é feito após a compensação, mas vale a pena lembrar que o lançamento pode ser ou não realizado separadamente conforme as opções do Banco de horas e consiste apenas em lançar as horas do banco para a movimentação conforme período e parametrização.  
   
**Ordenação**  
Para o lançamento, também poderá ser definida a prioridade e a ordenação, possibilitando lançar da data mais atual ou mais antiga, ou mesmo determinar a ordem por tipo de ocorrência ou código de cálculo para o lançamento. Fique atento, pois a ordenação do lançamento interfere no resultado final da movimentação. Para facilitar o entendimento, realize o lançamento utilizando a simulação e observe a Memória de compensação do histórico de da compensação.

Os códigos de cálculo a considerar no lançamento poderão ser selecionados conforme necessidade e são determinados separadamente dos códigos de cálculo da compensação, por exemplo, o código de cálculo pode ser utilizado na compensação e não ser lançado para movimentação.

O lançamento poderá ser realizado conforme parametrização do número de horas ou um percentual definido.

**Número de horas**  
Ao marcar a opção de lançamento utilizando número de horas, será habilitado o número de horas para os tipos de ocorrências (extras, atrasos e faltas) ou pelas faixas de extras possibilitando o número de horas serem calculados por fórmulas.  
   
Utilize o parâmetro **'Considerando o número de horas'** caso queira determinar o número de horas que serão lançadas para o movimento do funcionário. As horas que restarem serão mantidas no banco de horas.

**Exemplo**  
Considerando número de horas extras = 06:00h  
Horas no banco do funcionário:  
Horas Extras = 40:00  
Atrasos = 10:00  
Faltas = 08:00  
Cálculo da Compensação do Banco de Horas:  
40:00 ( Horas Extras ) - 10:00 ( Atrasos ) - 08:00 ( Faltas ) = 22:00 ( Horas Extras )  
Dessas 22 horas apenas 6 horas, conforme parametrização, serão lançadas para a movimentação e o restante será mantido no banco de horas. Veja:  
Movimento do Funcionário = 06:00 Horas Extras Pagas no movimento  
Banco de Horas do Funcionário = 16:00 Horas Extras a Compensar  
   
Ou utilize o parâmetro '**Somente acima do número de horas'** caso queira lançar para o movimento todas as horas que ultrapassarem o limite informado. As horas efetuadas até o limite permanecerão no banco de horas.

**Exemplo**  
Somente acima do número de horas extras = 06:00h  
Horas no banco do funcionário:  
Horas Extras = 40:00  
Atrasos = 10:00  
Faltas = 08:00  
Cálculo da Compensação do Banco de Horas:  
40:00 ( Horas Extras ) - 10:00 ( Atrasos ) - 08:00 ( Faltas ) = 22:00 ( Horas Extras )  
Dessas 22 horas, o que exceder as 6 horas conforme parametrização será lançado para o banco e o restante será mantido no banco de horas. Veja:  
Movimento do Funcionário = 16:00 Horas Extras Pagas no movimento  
Banco de Horas do Funcionário = 06:00 Horas Extras a Compensar

**Percentual**  
Ao marcar a opção de lançamento utilizando percentual, informe um percentual para que seja lançado às horas do banco para o movimento respeitando este percentual para os tipos de ocorrências (extras, atrasos e faltas) ou por faixas de extras.  
O percentual informado é aplicado e lançado para a movimentação da seguinte forma:

**Exemplo**  
Percentual das horas a serem lançadas para o movimento = 40%  
Horas no banco do funcionário:  
Horas Extras = 40:00  
Atrasos = 10:00  
Faltas = 08:00  
Cálculo da Compensação do Banco de Horas:  
40:00 ( Horas Extras ) - 10:00 ( Atrasos ) - 08:00 ( Faltas ) = 22:00 ( Horas Extras )  
Dessas 22 horas, serão aplicados 40% e lançado para movimentação e o restante será mantido no banco de horas. Veja:  
Movimento do Funcionário = 08:48 Horas Extras Pagas no movimento  
Banco de Horas do Funcionário = 13:12 Horas Extras a Compensar  
   
Para retornar ao menu 'Compensação/Lançamento do Banco de Horas' Clique aqui
