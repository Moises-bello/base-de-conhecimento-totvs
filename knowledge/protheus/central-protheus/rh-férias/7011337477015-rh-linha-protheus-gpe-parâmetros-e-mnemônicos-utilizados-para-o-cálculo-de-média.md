---
article_id: 7011337477015
category: RH - Férias
content_hash: 4ae0941fb56b8b6041579733c1252ea2eed28c6b81ee66faca03dcc284f29db0
fetched_at: '2026-06-28T22:43:58.352966+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Parâmetros e Mnemônicos utilizados para o cálculo
  de Médias
type: support-article
updated_at: '2025-09-02T17:44:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7011337477015-RH-Linha-Protheus-GPE-Par%C3%A2metros-e-Mnem%C3%B4nicos-utilizados-para-o-c%C3%A1lculo-de-M%C3%A9dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20316352624279) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais são os parâmetros e mnemônicos que o sistema utiliza para o cálculo de Médias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Os parâmetros e mnemônicos observados pelo sistema quando realizado cálculo de médias, são:  
  
**• P\_MEDDIREN (MV\_MEDDIRE):** Define se o cálculo das medias será sobre meses de direito, sendo:   
**S** - Sim, **N** - Não e **M -** Misto.   
[Acesse a documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=224112471)  
  
**• P\_DTMDFER (MV\_DTMDFER):** Define se será considerado o último período fechado ou a data de início de férias, sendo:  
**1** - Último período fechado e **2 -** Data de início férias.  
[Acesse a documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=238035418)  
  
**• P\_COMISSA (MV\_COMISSA):** Define a quantidade de meses que será considerado para a apuração das médias de comissões para funcionários comissionados.  
[Acesse a documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019237571-RH-Linha-Protheus-GPE-Como-configurar-para-buscar-as-maiores-m%C3%A9dias-de-comiss%C3%A3o-de-um-determinado-per%C3%ADodo)  
  
**• P\_MCOMISS**: Define a quantidade de meses para o cálculo de médias de comissionados em Licença Maternidade  
  
**• P\_MEDORIG (MV\_MEDORIG)**: Define se será considerado o valor atual da média (mesmo que menor que o original) ou ao menos o valor original (caso o valor atual seja menor), sendo:  
**.T.** - Valor atual não será menor que o valor original e **.F.** - Valor atual pode ser menor que o original.  
[Acesse a documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012665411-RH-Linha-Protheus-GPE-Como-Configurar-as-M%C3%A9dias-para-que-o-valor-Atual-n%C3%A3o-seja-menor-do-que-o-Valor-Original)  
  
**• P\_BUSMEDI (MV\_BUSMEDI):** Define o mês inicial da busca das médias, quando utilizado a apuração sobre o período aquisitivo, sendo:  
**1 -** A partir do 1º mês do período, **2 -** A partir do 2º mês ou **3 -** Se dias do 1º mês maior que 14, 1º mês, senão 2º.  
[Acesse a documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=839970824)  
  
**• P\_NMESPER (MV\_NMESPER):** Define quantos meses será utilizados para o cálculo da médias dentro do período aquisitivo de férias, quando utilizado configuração de apuração de médias sobre o período aquisitivo.  
[Acesse a documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=839971591)  
  
**• P\_CCOMP13:** Informar se haverá o cálculo do Complemento de 13º Salário, sendo:  
**S** - Sim e **N**- Não  
[Acesse a documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016519791-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-gerar-automaticamente-valores-de-complemento-de-13%C2%BA-Sal%C3%A1rio?source=search)  
  
**• P\_INCCOMPL**: Define se irá utilizar verbas incluídas na Folha de Pagamento para cálculo de complemento de 13º Salário, sendo:  
**.T. -** Sim e  **.F. -** Não.  
[Acesse a documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=325849943)  
  
**• P\_M13ANOC (MV\_13ANOC):** Define se a composição de médias de 13º salário apenas irá considerar os meses do ano corrente, sendo:   
**1** - Sim e **2** - Não.  
[Acesse a documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033987014-RH-Linha-Protheus-GPE-Como-Funciona-o-C%C3%A1lculo-de-M%C3%A9dias-de-13%C2%BA-Sal%C3%A1rio-quando-o-P-M13ANOC-est%C3%A1-sendo-utilizado)  
  
**• P\_REFMED (MV\_REFMED):** Define se será utilizado referência diferente para o cálculo das médias no 13º salário, sendo:  
**T -** Sim e **F** -Não.  
[Acesse a documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016330711-RH-Linha-Protheus-GPE-Flexibiliza%C3%A7%C3%A3o-das-m%C3%A9dias-no-c%C3%A1lculo-do-13%C2%BA-Sal%C3%A1rio)  
  
**• P\_TAFAFER (MV\_TAFAFER)**: Indica os tipos de afastamento que serão avaliados para a possível troca de período aquisitivo, sendo:   
**O**- Acidente, **P**- Doença, **R**- Serviço Militar e **X**- Licença sem Vencimentos.  
  
**• P\_QTDIAMES:** Definir a quantidade de dias do mês para cálculo do salário hora  
[Acesse a documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=555278890)  
  
**• P\_MEDFER:** Definir se as médias serão calculadas pelos dias de direito ou sempre por 30, sendo:  
**.T.** - Dias de direito e **.F.** - Sempre por 30.  
[Acesse a documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035128814-RH-Linha-Protheus-GPE-Como-realizar-a-confer%C3%AAncia-do-pagamento-das-M%C3%A9dias-em-F%C3%A9rias-antecipadas-P-MEDFER)  
  
**• P\_SEGFALT (MV\_SEGFALT):** Define referência das faltas de forma analítica, onde:  
**.F.** - Não observa de forma analítica e .**T.** - Verifica de forma analítica (Conteúdo obrigatório)  
[Acesse a documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=847569991)   
  
**OBS:** Os parâmetros referentes à médias poderão ser convertidos em mnemônicos. Caso realize a conversão, a configuração deverá ser diretamente no mnemônico e o parâmetro será inutilizado.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de Médias para Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726351592855-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-M%C3%A9dias-para-F%C3%A9rias)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de médias para 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413521053079-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-m%C3%A9dias-para-13%C2%BA)

[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
