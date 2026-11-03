---
content_hash: 166e9a1701807a709b9e6e5fd1542afd9827b3522f04fda664551b038c310181
fetched_at: '2026-06-29T00:10:04.054337+00:00'
page_id: '452719190'
product: rm
source: tdn-rm
title: Migração Cálculo .NET
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719190
version: 77
---

O TOTVS Folha de Pagamento (RM Labore) está sofrendo uma reestruturação em todo o seu cálculo. Tecnicamente, o cálculo anterior foi desenvolvido na linguagem Delphi e novo na linguagem .NET, por isso o nome Cálculo .NET, também conhecido como Máquina de Cálculo.  
 Buscando sempre atender as necessidades dos nossos clientes com agilidade e eficiência, evoluímos o processo de cálculo do sistema visando ampliar os cálculos, garantindo avanço tecnológico, melhorias em interfaces e diversas outras vantagens aos nossos usuários.  
 **Procedimentos a serem executados após a conversão:**

---

***Observação I:***
No cálculo em Delphi sempre era considerado os eventos com código de cálculo 1 e 2 para compor a base de salário família, independente dos mesmos estarem incidindo salário família.
***Atenção I:***
Este tratamento será adotado quando o parâmetro 'Usa salário nominal' existente em Opções | Parâmetros | RMLabore | Param. de Cálculo | Parâmetros, NÃO estiver marcado.
 
\*Diferença Salarial\*
 
O Cálculo .NET passou a consistir se os eventos com código de cálculo 37 (um com incidência em INSS e outro sem esta incidência) são do tipo PROVENTO.
 
\*Fórmulas\*
 
Com a migração do cálculo, algumas funções de fórmula foram ajustadas para uma melhor aplicação da função. Por isso, ao logar no sistema, após a conversão do cálculo, o usuário deverá rodar o \_Comparativo de Fórmulas Delphi para .NET\_ para cada coligada da base.
As fórmulas que apontarem divergências de cálculo serão apresentadas no log, sendo assim, o usuário do sistema deverá analisar as fórmulas e verificar se utiliza alguma função, caso afirmativo, deverá analisar a lógica da fórmula e adequar ao novo cálculo.
Utilize o módulo de comparação de fórmulas disponível em Rotinas/Comparativo de Fórmulas Delphi x .NET
(disponível a partir da versão 11.40)
Deverá analisar através do log do comparativo o motivo dos valores terem sido gerados diferentes.
\_Exemplo:\_
Fórmula EVT0023 - Base de cálculo de IRRF
Chapa 00001 - Na versão Delphi gerou 2915,55 , já na versão .NET gerou 3836,53
\*Atenção!\*
Deverá analisar e ser for necessário, adequar as fórmulas conforme necessidade da empresa, caso contrário, ocorrerá diferenças de cálculo na folha de pagamento.
 
Saiba mais a respeito de fórmulas em {\_}Informações Complementares / Fórmulas .NET{\_}.
 
\*Mudança de comportamento do cálculo\*]]>

* **Cálculo / Arredondamento**  
  O arredondamento no valor do evento é sempre a partir da 3ª casa decimal, porém, quando a 3ª casa decimal é "5" (cinco), o DELPHI ora arredonda para cima, ora arredonda para baixo, característica da linguagem de fórmula DELPHI. O .NET sempre arredonda para cima.  
  Exemplo:   
  Resultado da fórmula => 184,**635**   
  DELPHI => 184,63   
  .NET => 184,64  
  Dízimas  
  No caso de dízimas, ao invés de entender como "18,635", o DELPHI entende como "18,6344444444444".   
  Essas diferenças de centavos poderão ocorrer em todos os processos de cálculos do sistema.
* **Cálculo / Data de pagamento**  
  No cálculo será verificada a data de pagamento e depois o período para pagamento dos eventos. Quando existirem dois períodos com a mesma data, a segunda ordem será o período. As situações são quando existe um evento desconto onde tem que buscar o valor de um evento provento. As situações onde é necessário seguir uma seqüência de data de pagamento são as abaixo:   
  Código de cálculo 51 - Adiantamentos 13º Salário buscando o valor do Código de cálculo 102 - 2ª parcela 13º Salário;  
  Código de cálculo 35 - Adiantamentos13º Salário buscando o valor do Código de cálculo 9 - 1ª Parcela 13º Salário;  
  Código de cálculo 21 - Arredondamento Descontos buscando o valor do Código de cálculo 20 - Arredondamento Proventos.

* Versão Delphi verificava a ordem dos períodos, o maior era calculado por último.  
      
   · **Código de Cálculo 145 – Atestado Médico**  
   Quando em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros o parâmetro '*Lança o evento de atestado médico via grupo de eventos*' estiver marcado, o Cálculo .NET somente irá lançar o evento com cc145, quando for lançado o evento com cc1 ou cc2.  
   Foi retirado o parâmetro *'Soma dias afastados dentro período de carência pelo mesmo motivo'* existente em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros. O cálculo. Net passou a verificar quantidade de dias de atestado pagos pela empresa, de acordo com o período de carência e paga até um total de 15 dias.  
   **Exemplo:**  
   Período de carência 60 dias.  
   **Período de afastamento Qt dias Afastamento Tipo Motivo**  
   01/11/2010 a 14/11/2010 14 P 3  
   01/12/2010 a 05/12/2010 05 P 3  
   **Lançamentos dos eventos Atestado Médico e Dias Trabalhados:**   
   **Competência:**   
   Novembro/2010: 16 Dias Trabalhados e 14 dias de atestado médico.  
   Dezembro/2010: 25 Dias Trabalhados e 1 dia de atestado médico.  
   O restando dos dias, ou seja, quatro dias, para completar 30 dias trabalhados, quem irá pagar é a previdência.

  |  |  |
  | --- | --- |
  |  | Informações Complementares |

  ---

  Fórmulas .NET

  |  |  |
  | --- | --- |
  |  | Como Fazer |

  ---

  Como Fazer Conversão Cálculo .NET
