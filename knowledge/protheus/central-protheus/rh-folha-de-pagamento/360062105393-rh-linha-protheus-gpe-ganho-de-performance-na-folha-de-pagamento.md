---
article_id: 360062105393
category: RH - Folha de Pagamento
content_hash: 732e602bb87b56dff311b6910be2967fd2e159115efefdce8985b17f3d995b1a
fetched_at: '2026-06-28T22:44:14.965020+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Ganho de Performance na Folha de Pagamento
type: support-article
updated_at: '2025-08-22T18:42:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062105393-RH-Linha-Protheus-GPE-Ganho-de-Performance-na-Folha-de-Pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26358434639895)** Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Ganho de Performance na **Folha de Pagamento**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Existem algumas tecnologias disponíveis para processamentos de grandes volumes em sistemas, e na **folha de pagamento** do **Protheus** utilizamos duas diferentes tecnologias:

* ***Multi-thread***- Tem como característica a distribuição de processamentos em diversas *threads* no mesmo servidor de aplicação.
* **GRID**- Além da distribuição de processamento em diversas *threads* no servidor de aplicação, esta tecnologia possibilita a distribuição em diversos servidores de aplicação e inclusive servidores físicos  
    
  A seguir o detalhamento para ganho de performance na solução:

***Multi-thread*:****Como funciona**: O processamento é distribuído em diversas *threads* (configuração) dentro do mesmo servidor de aplicação.

**Como configurar:** Preencher o parâmetro **MV\_CALCTHD** via **Configurador (SIGACFG)** com no mínimo 2 (este parâmetro tem como objetivo definir o número de threads que serão abertos para o processamento).

**Importante:** No **binário 32 Bits** a quantidade de *threads* era limitada a 5, com **binário 64 Bits** não há limite. O número de *threads* deverá ser definido através de análise de infraestrutura no qual deverá ser levado em consideração o servidor, número de usuários conectados, entre outras informações que direcionam o melhor aproveitamento desta tecnologia. 

**Documento de apoio:** <https://tdn.totvs.com.br/pages/viewpage.action?pageId=269085476>

**Rotinas:**

* **GPEM020A** (Cálculo Unificado)
* **GPEM120** (Fechamento Mensal)

**Quando usar:**

* Ambiente que possuem um volume razoável de funcionários para processamento e com infraestrutura que suporte as conexões de várias threads realizando o processamento
* Analisar o aumento do número de threads que dará melhor performance e melhoria no tempo de cálculo.

**Pontos de atenção para implementação:**

* O serviço não é dedicado, possuindo as *threads* da rotina mais as conexões de outros usuários, balanceados via **Broker**;
* É preciso ter cuidado com a quantidade de *threads*, para não gerar sobrecarga ao servidor, pois rotinas de cálculo consomem *CPU*.
* As conexões concorrentes podem ter sua performance afetada.

**Indicação:**Recomendamos o uso de ***multi-thread*** quando:

* O tempo de processamento está alto (porém importante considerar a configuração de *hardware*):

+ Pode ser utilizado ***multi-thread,*** mas deve se ter cuidado para não configurar muitas *threads*, de forma a afetar a performance;
+ Recomendamos avaliar sua infraestrutura para definir o número de *threads*, pois em alguns casos muitas *threads* podem piorar a performance.

* Quando se possui diversas filiais e empresas, e o cálculo é descentralizado;
* Empresas/Filiais com menos de 500 funcionários, e que mesmo não fazendo uso de ***GRID***, realizam um cálculo em tempo considerado aceitável.

**GRID****Como funciona:** Além da distribuição de processamento em diversas *threads* no servidor de aplicação, esta tecnologia possibilita a escalabilidade em diversos servidores de aplicação e até mesmo em servidores físicos.

**Como configurar:** <https://tdn.totvs.com/pages/releaseview.action?pageId=267782422>

Parâmetros envolvidos: **MV\_GPEGRID**, **MV\_GRID**, **MV\_MINGRID**, **MV\_REGGRID**

**R****otinas:**

* **GPEM020** (Cálculo por Roteiros),
* **GPEM690** (Cálculo de Dissídio Retroativo),
* **GPEM070** (Cálculo de Provisão).

**Quando usar:**

* Consegue atender o cálculo no menor tempo possível, podendo aumentar o número de threads, caso possua hardware para atender;
* É possível realizar ajuste no **GRID**, podendo atender de acordo com o hardware disponível;
* No caso de ambientes virtualizados, é possível criar **VM’s** dedicadas para o cálculo;
* Também é possível criar servidores físicos dedicados.
* Permite um crescimento vertical em **VM’s**, podendo manter o tempo de cálculo independente da quantidade de funcionários, bastando adicionar mais **VM’s** com serviços dedicados ao **GRID**;
* Sem concorrência com o ***backoffice***, podendo:

+ Isolar em **VM’s** dedicadas;
+ No caso de ***Failover***, é possível criar roles dedicadas, e executar o cálculo em nós dedicados;

**Pontos de atenção para implementação:**

* É preciso ter cuidado com a quantidade de threads, para não gerar sobrecarga ao servidor, pois rotinas de cálculo consomem CPU.
* Necessário avaliar a quantidade de threads que precisam estar disponíveis, versus a quantidade de funcionários que executam a rotina, cálculos e hardware disponível.

**Indicação:**

Recomendamos o uso de **GRID** quando:

* o hardware físico possui alta performance;

+ Nesse caso pode ser utilizado **GRID**, mas deve se ter cuidado para não configurar muitas threads, de forma a afetar a performance;
+ Recomendamos que comecem com 10 threads e vão subindo em testes avaliando o consumo de CPU e tempo de cálculo desejado.

* Recomendado para clientes com mais de 500 funcionários.
