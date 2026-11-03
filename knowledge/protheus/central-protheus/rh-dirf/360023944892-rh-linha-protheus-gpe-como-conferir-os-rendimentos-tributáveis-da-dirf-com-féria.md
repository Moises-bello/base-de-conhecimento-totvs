---
article_id: 360023944892
category: RH – DIRF
content_hash: ee3468726e3e234d4ca1c93e418bbbd4d77e926e8c7f84c5271eaf845a819199
fetched_at: '2026-06-28T22:44:06.824500+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir os rendimentos tributáveis da DIRF
  com férias mês e mês seguinte
type: support-article
updated_at: '2025-08-13T19:52:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023944892-RH-Linha-Protheus-GPE-Como-conferir-os-rendimentos-tribut%C3%A1veis-da-DIRF-com-f%C3%A9rias-m%C3%AAs-e-m%C3%AAs-seguinte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34162034746135) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como conferir os valores de rendimentos tributáveis da DIRF, quando há valores de férias partidas e os IDs 0164 e 0232?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da release 12.1.27.  
  
**Solução**  
Foi liberada a melhoria na Ficha Financeira para impressão da linha Destaca Fer. nesta linha será demonstrada a soma de todos os valores de **FÉRIAS** que estão com **SIM** no campo **FER A FERIAS** e no campo **IR** da aba Incidências do cadastro de verbas, então para a conferência da coluna Rendimentos Tributáveis para a DIRF, se conferido com a ficha financeira, não será necessário somar os valores de férias com incidência A para a DIRF, basta somar os valores dessa linha.

**IMPORTANTE:** Para a melhoria ser implementada no ambiente, é necessário atualizar o ambiente com a ultima expedição contínua e atualização do dicionário.

Abaixo segue exemplo de conferência da coluna rendimentos tributáveis na DIRF com a ficha financeira:  
  
Folha 05/2022:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12305944938647)

Folha 06/2022  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12306021277591)  
  
1. Imprima a **ficha financeira** com os parâmetros conforme abaixo, pelo caminho **>Relatórios >Lançamentos >Ficha Financeira**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12216566229399)

2. Então, para o mês em questão, na ficha financeira, some todas as verbas com incidência A para a DIRF, considerando os proventos e os descontos, com exceção das verbas de férias, pois deve ser considerado o valor já somado da linha TOT FERIAS:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12216756896023)  
  
Temos os seguintes valores considerando a ficha financeira acima:

Proventos: 10500,00 + 146,85 + 954,55   
Linha TOTAL FÉRIAS: 14000,00  
Descontos: 350,00

Então temos: 10500,00 + 146,85 + 954,55 + 14000,00 - 350,00 = **25.251,40**

3. Entre na rotina de **Manutenção Arquivo**, pelo caminho **>Miscelânea >Dirf >Manutenção arquivo**, visualize o funcionário em questão, e valide que o valor esta de acordo com a conferência feita:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12216932267415)  
  
  
Nesse artigo mostramos o exemplo de férias partidas, verifique também os valores de adiantamento e outros que devem entrar para Rendimentos Tributáveis (incidência A para DIRF).  
  
Abaixo segue vídeo com orientação para conferência sem a melhoria da Ficha Financeira:  
  
  
E abaixo segue vídeo de como conferir as férias partidas com a melhoria da ficha financeira:

**Saiba mais**  
[RH - Linha Protheus - GPE - Como configurar ID 0164 Férias pagas mês anterior para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021045812)  
[Expedição contínua Gestão de Pessoal - RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Procedimento de Atualização de Dicionário do Protheus 12](https://tdn.totvs.com/pages/releaseview.action?pageId=366649057)
