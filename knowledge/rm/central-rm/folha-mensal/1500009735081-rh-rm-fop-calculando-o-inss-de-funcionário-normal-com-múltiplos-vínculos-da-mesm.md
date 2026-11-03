---
article_id: 1500009735081
category: Folha Mensal
content_hash: 936b89692b7efb3ec106427ad436a1fc15d06625540b55a7bff9c39966d119ac
fetched_at: '2026-06-28T22:46:59.412558+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Calculando o INSS  de Funcionário normal com múltiplos vínculos
  da mesma base de dados
type: support-article
updated_at: '2024-09-16T18:22:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009735081-RH-RM-FOP-Calculando-o-INSS-de-Funcion%C3%A1rio-normal-com-m%C3%BAltiplos-v%C3%ADnculos-da-mesma-base-de-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21126688664855) Tempo aproximado para leitura: 00:05:05 min  
  
Dúvida**

Como calcular o INSS de funcionário normal com múltiplos vínculos e que pertencem a mesma base de dados?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

É importante que as parametrizações estejam adequadas, para que o sistema realize os cálculos corretos. Para solucionar essa dúvida, realize os passos abaixo. Nesse exemplo, será demonstrado o cálculo de um funcionário que possui dois vínculos na mesma base de dados, ou seja, na mesma coligada:  
  
**Tabela de INSS considerada no exemplo**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015318121)  
  
01. **Configurar o parametrizador**Para calcular o INSS conforme o eSocial, será necessário marcar o parâmetro “Calcula INSS conforme eSocial” e informar a partir de quando o sistema iniciará a calcular desta forma. Basta acessar o caminho: **Configurações | Parametrizador | Folha normal | Geral 1/2** e marcar as flags conforme o print abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21126700386839)  
  
02. **Cadastrar os novos códigos de cálculo**Deverão ser cadastrados os novos códigos de cálculos. Foram criados esses novos códigos de cálculo para controle do cálculo dos múltiplos vínculos:   
  
      **417** - Base Tributada de INSS Autônomos Múltiplos Vínculo

**418** - Base de INSS Autônomo outro Emprego

**428** - Base Tributada De Inss Folha Primeira Faixa

**429** - Base Tributada De Inss Folha Segunda Faixa

**430** - Base Tributada De Inss Folha Terceira Faixa

**431** - Base Tributada De Inss Folha Quarta Faixa

**432** - Base Tributada De Inss 13º Primeira Faixa

**433** - Base Tributada De Inss 13º Segunda Faixa

**434** - Base Tributada De Inss 13º Terceira Faixa

**435** - Base Tributada De Inss 13º Quarta Faixa

**Observação: Todos os eventos são do Tipo Base/Valor**Os códigos de cálculo abaixo deixaram de ser utilizados processo:

**387** - Base Tributada de INSS Folha Múltiplos Vínculos  
      **388** - Base Tributada de INSS 13º Múltiplos Vínculos  
  
03**. Lançar a movimentação da 1º chapa**

Foi realizado lançamento competência abril/2021 para as chapas 00082 e 10021, na coligada 1:  
Funcionário chapa 10021 – Salario – 2.000,00  
Funcionário chapa 00082 – Salario – 7.000,00  
  
Chapa 10021 - Envelope  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015005382)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015337361)  
  
Conforme tabela progressiva, o sistema calculou 1.100,00 na primeira faixa no evento de **código de calculo 428**, com a dedução de 7,5% e valor de 82,50;

Salário de 2.000,00 - 1.100,00 da primeira faixa, sobrando um valor de 900,00, onde será calculado o valor do INSS na segunda faixa, lançando a base no evento de **código de calculo 429**;  
900,00 \* 9% = 81,00;

Valor do INSS descontado do funcionário;  
chapa 10021 = 82,50 + 81,00 = 163,50;

Veja que o sistema lançou os eventos Base INSS Tributária de Folha Primeira e Segunda faixa, pois para calcular a segunda chapa, o sistema precisará dessas faixas e da base de INSS para atender ao eSocial.  
  
**04. Lançar movimentação para a 2ª chapa**Foi realizado lançamento da folha para a segunda chapa 00082, com a base de INSS de 7.000,00.  
Conforme tabela progressiva, sistema irá somar a base de INSS da primeira chapa (10021) com a base da chapa 00082:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015013402)  
  
Lembrando que a primeira faixa, já foi descontada integral na chapa 10021, restando um valor de 203,48 para ser calculado na segunda chapa, ou seja, 203,48\*9% = 18,31;  
7.000,00 - 203,48= 6.796,52;

Calculando a 3ª faixa da tabela = 3.305,22 (teto terceira faixa) - 2.203,48 (teto da segunda faixa)  = 1101,74\* 12% = 132,20;

Calculando a 4ª faixa da tabela = 6.433,57 (teto da tabela INSS) - 3.305,22 (teto da terceira faixa) = 437,96;

Valor a descontar de INSS na chapa 00082 = 18,31 + 132,20 + 437,96 = 588,47;  
Soma do INSS descontado das duas chapas 10021 e 00082 = 588,47 + 163,50 = 751,97;  
Lembrando que a soma das duas bases, o desconto não pode ser superior ao teto do INSS: 751,97.  
  
**Importante**Caso seja necessário alterar ou inserir qualquer evento no envelope de qualquer chapa, terá que cancelar toda a movimentação das duas chapas e refazer o processo para que o sistema reconheça os valores de acordo com as faixas tributadas**.  
  
Saiba Mais**[Novo Cálculo de INSS múltiplos vínculos conforme o eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=546683921)  
[Cálculo de INSS múltiplos vínculos conforme o eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=440829559)  
[Configurações Gerais - FOP](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719263)  
[Múltiplos Vínculos que necessitam de Recálculo](https://tdn.totvs.com.br/pages/releaseview.action?pageId=465386747)
