---
article_id: 360016520312
category: RH - Folha de Pagamento
content_hash: 69f8d94e113a90c7e84b1ff7066bed48eb408e256ac13538a7c9c5694089e90e
fetched_at: '2026-06-28T22:44:17.124378+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o cálculo de horas extras utilizando
  o conceito centesimal e sexagesimal
type: support-article
updated_at: '2025-10-20T13:56:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016520312-RH-Linha-Protheus-GPE-Como-funciona-o-c%C3%A1lculo-de-horas-extras-utilizando-o-conceito-centesimal-e-sexagesimal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24072839646487)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como funciona o cálculo de horas extras utilizando o conceito **centesimal e sexagesimal?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando for necessário efetuar cálculos com horas é preciso **converter o padrão de horas (sexagesimal) para o centesimal**. Não é possível realizar operações matemáticas utilizando a nomenclatura de horas e minutos.

**Por exemplo:**Um empregado horista tem seu valor estipulado por hora trabalhada de R$ 50,00.  
Veja a tabela como ficaria com horas diferenciadas.

|  |  |
| --- | --- |
| **Hora trabalhada** | **Valor R$** |
| 00:30 | 25,00 |
| 01:00 | 50,00 |
| 01:30 | 75,00 |
| 02:00 | 100,00 |
| 02:30 | 125,00 |

Se efetuar o cálculo utilizando os minutos, o resultado não corresponderá com a tabela.  
2,30 x 50,00 = 115,00 (deveria ser 125,00 o empregado saiu perdendo R$ 10,00)

Por isso é necessário **converter** os minutos (padrão sexagesimal) para centesimal. Logo 02:30 corresponde no formato centesimal 2,5.  
2,5 x 50,00 = 125,00 (cálculo correto para 02:30)  
  
O mesmo cálculo deve ser feito ao realizar a média de horas extras de um período. Não é possível somar as horas, deve-se primeiro converter para o formato centesimal. Após a conversão, apura-se a média e então é convertido de volta para sexagesimal.

No ponto eletrônico há um tratamento para valores lançados manualmente, controlados pelo parâmetro **MV\_HORASDE.**

**Vale lembrar:**Caso o parâmetro seja ativado, os resultados apresentados no ponto eletrônico, em lançamentos/ resultados, serão em horas também, ou seja com MV\_HORASDE habilitado o sistema fará a conversão de Centesimal para Sexagesimal.

Os valores apenas serão apresentados em horas na rotina de lançamentos, no recibo de pagamento e nos relatórios da folha (GPER040 e GPER106), nos acumulados e demais relatórios estes valores ficarão centesimais.

**Saiba mais:**

**[Documentação Técnica](https://tdn.totvs.com/display/public/PROT/GPE082FOL_Horas+centesimais+e+sexagesimais+na+folha+de+pagamento)**

**[RH - Linha Protheus - GPE - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)**
