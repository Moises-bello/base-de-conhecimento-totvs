---
article_id: 360017515832
category: RH - Férias
content_hash: 150e6f36b984040c9a4ed23baeeeafa0078f6ede2fb655bbd8e10024f9a4a947
fetched_at: '2026-06-28T22:43:58.238746+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Determinar qual a data utilizada como base para
  iniciar a contagem dos meses das médias utilizando o Mnemônico P_DTMDFER (Antigo
  MV_DTMDFER)
type: support-article
updated_at: '2025-01-08T11:34:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017515832-RH-Linha-Protheus-GPE-Determinar-qual-a-data-utilizada-como-base-para-iniciar-a-contagem-dos-meses-das-m%C3%A9dias-utilizando-o-Mnem%C3%B4nico-P-DTMDFER-Antigo-MV-DTMDFER
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17323954072343) Tempo aproximado para leitura: 00:02:00 min****Dúvida**Determinar qual a data utilizada como base para iniciar a contagem dos meses das médias utilizando o Mnemônico P\_DTMDFER (Antigo MV\_DTMDFER)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A formação do período de pesquisa das médias, nas rotinas de férias normais, programadas e coletivas, foi padronizada pela criação e utilização do Mnemônico **P\_DTMDFER** (Antigo MV\_DTMDFER)  
  
O Mnemônico poderá ser configurado com:  
**1 = Último período fechado**, que é a configuração padrão ou   
**2 = Data de início das férias**, que determina qual a data utilizada como base para iniciar a contagem dos meses das médias.

Ressalta-se que esta configuração tem efeito somente para as empresas que calculam as médias de férias, utilizando uma quantidade de meses (Ex: 6 últimos meses, 3 últimos meses ou configuração similar).  
  
Acesse: Atualizações/ Definições de Cálculo/ Mnemônicos  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29060070001943)  
  
Exemplos do resultado encontrado, com a seguinte situação:  
Período atual da folha: 07/2022  
Início das férias: 01/08/2022  
**Verbas** para média configuradas com os **06 últimos meses** para média de férias

1. **P\_DTMDFER**  configurado com **1 – Último período fechado**:  
No cálculo das férias se o campo de Mês para média estiver igual a **Sim:**Período a ser considerado para média: 02/2022 a 07/2022.  
No cálculo das férias se o campo de Mês para média estiver igual a**Não:**Período a ser considerado para média: 01/2022 a 06/2022.

2. **P\_DTMDFER**  configurado com **2 - Data início das férias**:  
No cálculo das férias se o campo de Mês para média estiver igual a **Sim:**Período a ser considerado para média: 03/2022 a 08/2022.  
No cálculo das férias se o campo de Mês para média estiver igual a **Não:**Período a ser considerado para média: 02/2022 a 07/2022.

Caso o início das férias esteja dentro do período atual da folha, o funcionamento será o mesmo tanto com P\_DTMDFER = 1 quanto para P\_DTMDFER = 2.  
  
**Importante!**Esse mnemônico **não**tem efeito para empresas que calculam a **média pelo período aquisitivo**do funcionário, utilize o mnemônico [P\_BUSMEDI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041828894-RH-Linha-Protheus-GPE-Como-Alterar-a-Defini%C3%A7%C3%A3o-de-M%C3%AAs-Inicial-das-M%C3%A9dias-de-F%C3%A9rias)

**Saiba Mais:**[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de Médias para Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726351592855-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-M%C3%A9dias-para-F%C3%A9rias)  
[RH - Linha Protheus - GPE - Como imprimir relatório de memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052314713-RH-Linha-Protheus-GPE-Como-imprimir-relat%C3%B3rio-de-mem%C3%B3ria-de-c%C3%A1lculo-das-f%C3%A9rias)
