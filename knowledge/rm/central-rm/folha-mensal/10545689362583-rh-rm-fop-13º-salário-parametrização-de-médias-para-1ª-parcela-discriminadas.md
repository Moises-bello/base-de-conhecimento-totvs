---
article_id: 10545689362583
category: Folha Mensal
content_hash: 065778fcf6034a02afe144911c40049623366a927f5c7f8471e51372ab629971
fetched_at: '2026-06-28T22:46:58.315681+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - 13º Salário: Parametrização de médias para 1ª parcela discriminadas'
type: support-article
updated_at: '2024-10-18T15:11:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10545689362583-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Parametriza%C3%A7%C3%A3o-de-m%C3%A9dias-para-1%C2%AA-parcela-discriminadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:06:21min  
  
Dúvida**Como parametrizar o sistema para pagamento das **médias** discriminadas sobre a **1ª Parcela** de **13º Salario**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**1. Para realizar a parametrização das médias discriminadas para pagamento da **1ª Parcela** do **13º Salário**, acesse**Administração de Pessoal | Sindicatos | 13º Salário** e desmarque a opção **Paga média na 1ª parcela**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10545648476311)

2. Criar fórmula que fará o cálculo da média dos eventos discriminados. Abaixo segue exemplo lembrando que é de responsabilidade do usuário criar a fórmula que atenderá as necessidades da empresa.  
  
Para isso acesse o menu **Administração de Pessoal |Fórmulas  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10545723206807)**

**Código:** A0020  
**Título:** Média 13º na 1ª Parcela  
**Texto:** CALCMED(201) / 2  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10545729597079)  
  
**Função CALCMED**  
Retorna o valor da Média referente ao Sindicato. CALCMED (Valor utilizado para o retorno dos tipos de médias Grupo de Média).  
Onde os valores utilizados para o retorno dos tipos de médias pela CALCMED são:  
1 para Férias  
2 para13º Salário  
3 para Aviso Prévio  
4 para Licença maternidade  
5 para férias proporcionais  
  
**Exemplo:**  
CALCMED(201) - Retornará o valor da média de 13o salário do grupo 1.   
CALCMED(105) - Retornará o valor da média de férias do grupo 5.    
CALCMED(304) - Retornará o valor da média de Aviso Prévio do grupo 4.   
CALCMED(519) - Retornará o valor da média de Férias Proporcionais do grupo 19.   
  
**Observações:**  
-A variável CALCMED poderá ser usada apenas com os valores do primeiro parâmetro.  
  
CALCMED(1) - Retornará o valor total da média de férias.  
CALCMED(2) - Retornará o valor total da média de 13º salário.  
CALCMED(3) - Retornará o valor total da média do Aviso Prévio.  
O tratamento da variável CALCMED é diferente para o cálculo das médias de Licença Maternidade. Para que o sistema retorne o valor das médias de Licença Maternidade nesta variável é necessário efetuar o lançamento do salário maternidade com média no primeiro mês do Afastamento, assim o sistema guardará automaticamente o valor das médias no campo em Funcionários | Parâmetros campo "Média Salário Maternidade".  
  
3. Cadastrar um evento de média que seja do tipo Provento, Valor, com Código de Cálculo 9 e incidência em FGTS. No campo "fórmula de valor", associe a fórmula criada no 1º passo.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10545850882839)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10545882819095)  
  
4. Execute o pagamento da primeira parcela através do menu **Folha Mensal | Calculo 13º***. Nesse passo **será lançado somente o evento referente a primeira parcela**.*

[RH - RM - FOP - 13º Salário: lançamento da 1ª parcela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014812211-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-lan%C3%A7amento-da-1%C2%AA-parcela)  
  
5. No menu **Folha Mensal | Lançamentos | Grupo de Eventos***, c*rie um grupo de evento específico para lançar os eventos de médias. Na aba "Eventos do grupo", informe o evento criado no 3º passo. Após procedimento basta executar o lançamento do grupo de eventos para a seleção desejada.

[RH - RM - FOP - Lançamento do Grupo de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014011632-RH-RM-FOP-Lan%C3%A7amento-do-Grupo-de-Eventos)  
  
Ou  
  
Acesse **Configurações | Parametrizador | 13 Salario**. Informe o evento em **Eventos Adicionais Globais**  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10546008488983)  
  
Habilite a seguinte flag: "**Paga eventos adicionais na 1 parcela do 13 salario**".  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10546013284247)  
  
**Saiba Mais**[1ª Parcela de 13º Salário(Com média discriminada)](1%C2%AA%20Parcela%20de%2013%C2%BA%20Sal%C3%A1rio%20(Com%20m%C3%A9dia%20discriminada))
