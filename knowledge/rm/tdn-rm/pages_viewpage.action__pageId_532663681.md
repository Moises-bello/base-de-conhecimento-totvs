---
content_hash: e7c19ad582d83dcc3323fc7426ec7c9fe94616404ce6e194bac7464b7ec0c0e8
fetched_at: '2026-06-29T00:10:36.549288+00:00'
page_id: '532663681'
product: rm
source: tdn-rm
title: Como fazer Transição para o cálculo finalidade 5 - INSS_REFORMA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532663681
version: 13
---

Para atender a emenda Constitucional 103/2019 que altera o sistema de previdência social e estabelece regras de transição os usuários deverão seguir os seguintes passos:

Deverá criar a tabela de cálculo para o INSS com finalidade (5) INSS\_REFORMA com vigência a partir de 01 de Março de 2020.

Dica

Após a atualização de versão, deverá ser feito um recalculo no envelope do funcionário para que a finalidade 5 seja disponibilizada no cadastro da tabela de cálculo.

Atenção

O cálculo até 29 de Fevereiro de 2020 considerará a tabela de finalidade (1)  INSS e a partir de 01 de Março de 2020 considerará a tabela de finalidade (5) INSS Reforma.

Os cálculos em cada faixa devem ser realizados mediante o truncamento após a segunda casa decimal.

**Exemplo de cálculo de folha:**

**Para o cálculo feito em fevereiro/2020**

**Salário =5000,00**

Calculando evento: 0003 - INSS  
              Código de Cálculo 3 - Prioridade 81  
               
                     Base de INSS:  
                         Proventos = 5.000,00  
                         Descontos = 0,00  
                         Base Líquida = 5.000,00

            Percentual da Faixa na Tabela de INSS: 11.00%

            Limite Superior da Faixa na Tabela de INSS: 6.101,06

             INSS: 11.00% \*Base(5.000,00) = 550,00

             Valor do evento: 550,00

   
**Cálculo feito com a tabela a partir de Março/2020**

**Salário =5000,00**

Calculando evento: 0003 - INSS  
              Código de Cálculo 3 - Prioridade 81  
               
                     Base de INSS:  
                         Proventos = 5.000,00  
                         Descontos = 0,00  
                         Base Líquida = 5.000,00  
                          
                     INSS: 7,5000% \* Base(1.045,00) = 78,37  
                     INSS: 9,0000% \* Base(1.044,60) = 94,01  
                     INSS: 12,0000% \* Base(1.044,80) = 125,37

                    INSS: 14,0000% \* Base(1.865,60) = 261,18  
                     Valor do evento: 558,93

**Exemplo de cálculo de férias que iniciam em Fevereiro/2020 e terminam em Março/2020**

Período de Gozo: 15/02/2020 a 15/03/2020

       Calculando evento: 0098 - INSS FERIAS

       Código de Cálculo 82 - Prioridade 81

              Base de INSS:

                  Proventos = 5333,33

                  Descontos = 0

                  Base Líquida = 5333,33

              Base de INSS mesmo mês: 2.800,00

              Base para o 1º mês (15 dias): 2666,67

              Base para o 2º mês (15 dias): 2666,66

              Total da Base de INSS do 1º mês: 5.466,67

              Limite Superior da Faixa na Tabela de INSS: 6101,06

              Percentual da Faixa na Tabela de INSS: 11,00

              INSS 1o.mês: 11,00% \* Base Mês 1(5466,67) = 601,33

              Abatendo INSS já descontado no mês: 601,333700 - 308,00 = 293,33

              Valor do evento: 293,33

       Calculando evento: 0196 - INSS FERIAS PROX MES

       Código de Cálculo 130 - Prioridade 81

              Base de INSS:

                  Proventos = 5333,33

                  Descontos = 0

                  Base Líquida = 5333,33

              Base de INSS mesmo mês: 2.800,00

              Base para o 1º mês (15 dias): 2666,67

              Base para o 2º mês (15 dias): 2666,66

              Parâmetro "Desconta INSS Férias integral no primeiro mês" está confirmado.

              Base de INSS mesmo mês: 2800,00

              INSS: 7,5000% \* Base(1.045,00) = 78,37

              INSS: 9,0000% \* Base(1.044,60) = 94,01

              INSS: 12,0000% \* Base(1.044,80) = 125,37

              INSS: 14,0000% \* Base(2.332,26) = 326,51

              INSS 2º Mês: 624,26

              Abatendo INSS já descontado no mês: 624,281400 - 371,88 = 252,401400

              Valor do evento: 252,40

## **eSocial**

A geração do XML dos eventos abaixo sofreram alterações no cálculo da tag **<indMV-Indicador de desconto da contribuição previdenciária do trabalhador>** passando a considerar os novos códigos de cálculo. Veja mais detalhes sobre o cálculo nos helps dos códigos de cálculos:

### Eventos que sofreram alterações

S-1200-Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social

S-2299-Desligamento 

S-2399-Trabalhador Sem Vínculo de Emprego/Estatutário - Término

### **Códigos de Cálculos**

[428 - Base Tributada De Inss Folha Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857540)

[429 - Base Tributada De Inss Folha Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857547)

[430 - Base Tributada De Inss Folha Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857555)

[431 - Base Tributada De Inss Folha Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857562)

[432 - Base Tributada De Inss 13º Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857570)

[433 - Base Tributada De Inss 13º Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857577)

[434 - Base Tributada De Inss 13º Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857583)

[435 - Base Tributada De Inss 13º Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)
