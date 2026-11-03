---
article_id: 360008787852
category: RH - Relatórios
content_hash: 858ed25b8f3a1ad991ed219103b73f1606bf94c697c5069fbb875114fd25896f
fetched_at: '2026-06-28T22:44:43.462409+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Como exibir Verbas ou Apontamentos no rodapé do
  Espelho de Ponto
type: support-article
updated_at: '2025-10-14T13:31:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008787852-RH-Linha-Protheus-PON-Como-exibir-Verbas-ou-Apontamentos-no-rodap%C3%A9-do-Espelho-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32646725465623) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida:**Como exibir Verbas ou Apontamentos no rodapé do Espelho de Ponto?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução:**Na impressão do Espelho de Ponto, é possível escolher se no rodapé serão exibidos os **Apontamentos/Eventos** gerados durante o período ou as **Verbas dos Resultados** que serão integradas com a Folha de Pagamento.  
Esta escolha é feita nos parâmetros de impressão, através da pergunta **Eventos dos Resultados?**, que se estiver como **SIM**, imprime as Verbas dos Resultados, e se estiver como **NÃO**, imprime os Apontamentos/Eventos.  
  
Segue exemplo de um Espelho de Ponto mostrando os **Apontamentos/Eventos** no rodapé:  
  
- Apontamentos do período:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053161644183)  
  
- Pergunta **Eventos dos Resultados?** como **NÃO:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053161659031)  
  
- Rodapé do **Espelho de Ponto:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053161674647)  
  
Segue exemplo de um Espelho de Ponto mostrando **Verbas dos Resultados** no rodapé:  
  
- Verbas dos Resultados geradas após o Cálculo Mensal:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053161688727)  
  
- Pergunta **Eventos dos Resultados?** como **SIM:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053161700119)  
  
- Rodapé do **Espelho de Ponto:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053161713559)  
  
**OBS:** se o Espelho de Ponto for impresso com **datas parciais** do Período de Apontamento, o rodapé com as Verbas dos Resultados **não será impresso**, pois o Cálculo Mensal feito com o último dia do período gera as verbas nos Resultados com a Data de Pagamento neste mesmo dia, portanto, é feito este vínculo diretamente com o calendário do período do Ponto.  
Em casos de desligamentos durante o período, onde é necessária a impressão do Espelho de Ponto parcial e exibindo o rodapé com as Verbas, o **Cálculo Mensal** deve ser feito com a **data base** no dia do desligamento do funcionário, para que as Verbas sejam geradas com esta data. Segue exemplo abaixo:  
  
- Desligamento no dia 15.01.2024, portanto, o Cálculo Mensal foi executado com a data base neste dia e gerou as Verbas com esta mesma data:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053167400727)  
  
- Na impressão do **Espelho de Ponto** parcial, as **Verbas** serão exibidas corretamente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053167421207)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053161778327)  
  
Se o **Cálculo Mensal** for feito com o último dia do período, ou seja, o dia 31.01.2024, as **Verbas** serão geradas com esta data:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053167434775)  
  
E se o Espelho de Ponto for impresso parcialmente, por exemplo, de 01 à 15.01.2024, as Verbas não serão exibidas no rodapé:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053167421207)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21053161816471)

**Saiba mais:**[RH - Linha Protheus - PON - Como imprimir o Espelho de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004253171)[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
