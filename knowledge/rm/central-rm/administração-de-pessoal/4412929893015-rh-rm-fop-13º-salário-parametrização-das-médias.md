---
article_id: 4412929893015
category: Administração de Pessoal
content_hash: a9a3e7fdb52f8d69326e824561f576f72a7cdf9b84c5470f459d4ec09ccfa46c
fetched_at: '2026-06-28T22:47:02.097436+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - 13º Salário: Parametrização das Médias'
type: support-article
updated_at: '2024-06-18T12:24:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412929893015-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Parametriza%C3%A7%C3%A3o-das-M%C3%A9dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24255878276119) Tempo aproximado para leitura: **00:06:44 min** **Dúvida**Quais as parametrizações e funcionalidades das médias de 13º?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O cadastro de sindicato mantém, principalmente, as parametrizações de médias relativas a CLT ou Convenções Coletivas dos sindicatos dos trabalhadores. É dividido em pastas que contém parametrizações específicas de média de Férias, 13º Salário, Aviso Prévio, Licença Maternidade, Valores Associados do Sindicato e HomologNet.   
  
As parametrizações de 13º se encontram em: **Administração de Pessoal | Sindicatos | selecione o sindicato |** **Aba 13º Salário | Sub-aba Media 13º.****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8904700087703)  
  
C****onsidera ano anterior p/ médias:** Se marcado, irá considerar meses do ano anterior para o cálculo da média do 13º salário. Caso contrário, se desmarcar, validará somente ano atual. De acordo com a CLT, a média de 13º salário somente poderá envolver eventos relativos ao ano a que se refere o 13º, mas acordos coletivos podem alterar esta restrição.  
  
**Paga média na 1ª parcela:** Se marcado paga média na 1° parcela. Caso contrário, se desmarcado, paga somente na 2° parcela.  
  
**Despreza fórmula base salário:** Se estiver marcado, as fórmulas adicionais cadastradas em: **Configurações | Parametrizador | 13º Salário** não serão consideradas nos cálculos das médias. Este parâmetro influencia apenas o cálculo das médias.  
  
**Desconsidera o mês em que houver período de férias também para a soma dos valores:** Para desconsiderar eventos que incide em médias, e foram pagos no mês do período de gozo das férias.  
  
Este parâmetro depende do próximo parâmetro **Desconsidera para contagem o mês em que houver período de férias igual ou maior**.  
  
**Exemplo:**  
Período do gozo de férias: 10/03/2013 a 08/04/2013  
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Evento do tipo valor que incidem em média de férias lançados em:  
03/2013 = 100,00  
06/2013 = 100,00  
Média dos últimos 6 meses  
  
**--> Com o parâmetro desmarcado:**  
São considerados os dois valores e o valor encontrado é divido por 6 para retorna a média.  
  
**--> Com o parâmetro marcado e o campo Desconsidera para contagem o mês em que houver período de férias igual ou maior informado 8.**  
Os meses 03/2013 e 04/2013 são desconsiderados no cálculo da média, tanto para o divisor do cálculo da média como para buscar valores de eventos que incidem na média.  
  
**Desconsidera para contagem o mês em que houver período de férias igual ou maior:** Para desconsiderar o mês do período de gozo das férias no divisor do cálculo das médias. O dia informado neste parâmetro compara com a quantidade de dias de férias no mês.  
   
**Exemplo I:**  
Parâmetro = 8 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013  
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso serão desconsiderados os meses 03 e 04/2013 no divisor da média, devido no mês 03/2013 ter 22 dias de férias e no mês 04/2013 ter 8 dias de férias.  
   
**Exemplo II:**  
Parâmetro = 10 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013  
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso é desconsiderado apenas o mês 03 no divisor da média.  
  
Caso não deseje desconsiderar o mês deve informar 31 neste campo. Este parâmetro não depende do parâmetro anterior. Caso o parâmetro anterior Desconsidera o mês em que houver período de férias também para a soma dos valores esteja desmarcado, o período do gozo de férias é desconsiderado apenas no divisor da média.  
  
**Considera mês atual p/ cálculo de média de 13º:** Marcando esta opção o sistema irá considerar os eventos que incidem nas médias de 13º salário e que estão na movimentação no mês do lançamento do 13º salário para o cálculo da média.  
  
**Considera fórmula adicional na 1ª parcela de 13º:** Se marcado, o valor da Fórmula Adicional que consta em **Configurações | Parametrizador | 13º Salário | Fórmulas Adicionais**, irá compor o evento da 1° Parcela. Sempre o resultado dividido por 2.  
  
**Mês da admissão entra para cálculo se admitido até dia:** O mês de admissão será considerado no cálculo conforme o dia passado no parâmetro.   
  
**Exemplo I:**   
Admissão dia 20.   
Parâmetro = 15.   
Neste caso, o mês será desconsiderado.  
  
Caso seja informado 0 (zero) o mês de admissão não é considerado. Quando informado 31 o mês de admissão é sempre considerado.  
  
**Importante**  
Apenas será pago médias na 1° Parcela, se o parâmetro do Sindicato for marcado. Se for pago médias na 1° Parcela, por padrão os valores serão acumulados no evento da 1° Parcela, somente na 2° Parcela os eventos serão descriminados.  
  
Caso, a empresa realmente queira discriminar as médias também na 1° Parcela, é possível fazer por Fórmulas. Para acessar o roteiro com as orientações, [CLIQUE AQUI.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014800711/preview/eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MzYwMDE0ODAwNzExLCJleHAiOjE2MzY3MjQ4OTR9.qCZPShkm4r7xbtFHBadM5o_2p5Ev13KhVW4FeWs2UUE)  
  
**Saiba Mais**[RH - RM - FOP - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020075531-RM-FOP-13%C2%BA-Sal%C3%A1rio)  
[RH - RM - FOP - 13º Salário: Lançamento da 1ª Parcela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014812211-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Lan%C3%A7amento-da-1%C2%AA-Parcela)
