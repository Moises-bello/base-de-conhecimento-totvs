---
article_id: 32753855374615
category: eConsignado (Crédito do Trabalhador)
content_hash: c271062c007dbc62d9ac066a8b19533555d9b393955227dbcbfcee4faccc5406
fetched_at: '2026-06-28T22:43:07.097023+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH  - Linha Protheus - GPE - Desconto do Emprestimo Programa Crédito Trabalhador
  quando há insuficiência de saldo - eConsignado (MP 1.292/2025)
type: support-article
updated_at: '2026-06-25T18:45:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32753855374615-RH-Linha-Protheus-GPE-Desconto-do-Emprestimo-Programa-Cr%C3%A9dito-Trabalhador-quando-h%C3%A1-insufici%C3%AAncia-de-saldo-eConsignado-MP-1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32753864206999) Tempo aproximado para leitura: **02:00:00min****Dúvida**Desconto do econsignado quando há insuficiência de saldo  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A insuficiência de saldo pode ocorrer e ainda assim o sistema realizar o desconto da parcela do econsignado, isso porque para o calculo da margem consignável por padrão o sistema soma todas as verbas de provento com incidência de INSS e deduz as verbas com incidência de INSS e o IRRF para chegar na margem consignavel.  
Ou seja, se o colaborador possui margem consignável para o desconto da parcela, mas tem outros descontos como por exemplo Assistência Médica, Assistência odontológica, Vale transporte, Vale refeição e descontos diversos, como essas verbas não possuem incidência de INSS caso elas não estejam informadas no mnemonico P\_DEDCONS - [RH - Linha Protheus - GPE - Como deduzir outras verbas de desconto da margem de consignação do Programa Crédito Trabalhador eConsignado (MP 1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32696289251351-RH-Linha-Protheus-GPE-Como-deduzir-outras-verbas-de-desconto-da-margem-de-consigna%C3%A7%C3%A3o-do-Programa-Cr%C3%A9dito-Trabalhador-eConsignado-MP-1-292-2025) , o sistema não abate da margem consignável.

Exemplo.   
**Valores Futuros**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32753855362071)

**Mnemonico P\_DEDCONS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32753855362839)

**Lançamento por funcionário**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32753864209431)

Observe que exceto a verba de Faltas , as demais verbas informadas não possuem incidência para INSS e não estão informadas no mnemonico, dessa forma elas não serão deduzidas da margem consignável.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32753855363351)  
Margem consignável = 4000.00 - 2.400,00 - 93,33 - 355,56  (Salario - INSS - Faltas - DSR de faltas)  = 1.151,11 \* 35% = **R$ 402,89**  
Depois de calcular o empréstimo , o sistema realiza o calculo dos Provento menos o Desconto, com isso gera a insuficiência de saldo, mas o desconto do empréstimo foi calculado corretamente sobre a margem consignável. 

**Saiba Mais:**

[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Econsignado - Como incluir a rotina de Importação do arquivo Econsignado GPEM944](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32201275142295-RH-Linha-Protheus-GPE-Econsignado-Como-incluir-a-rotina-de-Importa%C3%A7%C3%A3o-do-arquivo-Econsignado-GPEM944)  
[RH - Linha Protheus - GPE - Provisionamento nas Férias referente ao eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32480529848087-RH-Linha-Protheus-GPE-Provisionamento-nas-F%C3%A9rias-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador)  
[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)  
[RH - Linha Protheus - GPE - Importação do arquivo Crédito trabalhador mês atual - Econsignado MP(1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32576676990487-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-arquivo-Cr%C3%A9dito-trabalhador-m%C3%AAs-atual-Econsignado-MP-1-292-2025)  
[RH - Linha Protheus - GPE - Provisionamento no Adiantamento referente ao Econsignado (Programa Crédito do Trabalhador MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32581967990935-RH-Linha-Protheus-GPE-Provisionamento-no-Adiantamento-referente-ao-Econsignado-Programa-Cr%C3%A9dito-do-Trabalhador-MP1-292-2025)  
[RH - Linha Protheus - GPE - Como consultar o Historico de Importação RUO Econsignado (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32579319541271-RH-Linha-Protheus-GPE-Como-consultar-o-Historico-de-Importa%C3%A7%C3%A3o-RUO-Econsignado-MP1-292-2025)
