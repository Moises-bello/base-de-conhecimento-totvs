---
article_id: 4428159240983
category: Materiais - Compras (SIGACOM)
content_hash: 383b924f3c1f94bffd8d14cc5af09ba28d17dab2456c6f49540c71c4a6b4d57e
fetched_at: '2026-06-28T22:41:19.960701+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Impostos na rotina
  monitor do Importador xml/Totvs Colaboração
type: support-article
updated_at: '2024-05-17T17:05:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4428159240983-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Impostos-na-rotina-monitor-do-Importador-xml-Totvs-Colabora%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23561164354199) Tempo aproximado para leitura: **6 min** **Dúvida**Como funciona os cálculos de impostos na rotina do monitor?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - A partir da versão 12.1.25.

**Solução**

Ao realizar a integração do XML com impostos via Importador XML ou Totvs Colaboração, o sistema validará as informações geradas na aba "Impostos", conforme o print abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4428065306775)

- Caso o calculo de impostos realizado pela TES esteja igual o calculo vindo do XML o sistema vai apresentar uma legenda verde conforme o print do campo ( DT\_TES) abaixo: Calculo do imposto "Valor TES" e "Valor XML":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4428067404823)

Neste caso o sistema vai permitir gerar o documento sem ocorrência de mensagem de divergências de impostos.

- Quando existe divergências entre esses calculos (TES x XML), a legenda ficará vermelha:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4428104531223)

Caso haja alguma divergência, será demonstrado uma mensagem informativa:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4428136519575)

**Importante:** O help apresentado acima não impede de gerar o documento.

***Opções da mensagem:***

**Cancelar:**

Vai sair do documento e não será realizado a importação da nota para o MATA140 ou MATA103.

**Ignorar:**

Vai importar o documento gerando na rotina MATA140 e MATA103, respeitando o calculo gerado pela TES;

**Conformes:**

No monitor, é possivel importar mais de um documento ao mesmo tempo. Ao clicar em " Conformes", o sistema vai incluir apenas os documentos que não possuem nenhum tipo de divergência no calculo do imposto.

***Obs.:***

*Em caso de duvida de calculo de impostos da TES, acionar equipe do Fiscal para auxilio.*

***Saiba Mais :***

***[IX02 - Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Mensagem de " Divergência Fiscal " ao gerar documento no Monitor do Colaboração / Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414500639511)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-MP-SIGACOM-Importador-XML)

[MP - SIGACOM - Pontos de Entrada - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000169747)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
