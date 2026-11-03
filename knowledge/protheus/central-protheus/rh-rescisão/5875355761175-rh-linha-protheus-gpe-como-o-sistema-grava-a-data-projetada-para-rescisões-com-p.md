---
article_id: 5875355761175
category: RH - Rescisão
content_hash: 86e16822a7b8583e3ecce8e22e4f289c2838698e24889a83bebd138617da2ca2
fetched_at: '2026-06-28T22:43:52.104136+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema grava a Data Projetada para rescisões
  com pedido de demissão
type: support-article
updated_at: '2025-06-16T18:31:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5875355761175-RH-Linha-Protheus-GPE-Como-o-sistema-grava-a-Data-Projetada-para-rescis%C3%B5es-com-pedido-de-demiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como o sistema grava a Data Projetada para rescisões com pedido de demissão?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Em atualizações/Definições de Cálculo/Tabela S043, a data projetada será considerada de acordo com a coluna Aviso Prévio:![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5889217545495/mceclip4.png)

Verificaremos abaixo o comportamento da rotina, para cada um dos tipos de aviso prévio no pedido de demissão:

1) Utilizamos o tipo de rescisão **03 - Pedido de demissão - Trabalhado (Aviso Prévio = T)**.  Neste cenário a rotina entende que a data de aviso, uma vez definida como aviso trabalhando, deve ser projetada para 30 dias após a data do pedido de demissão (DATA AVISO), considerando que será cumprido o aviso:![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5890089996951/mceclip7.png)

2) Neste segundo print, utilizamos o tipo de rescisão **04 - Pedido de demissão - Descontado (Aviso Prévio = D)**.  Neste cenário a rotina entende que a data de aviso, uma vez definida como aviso descontado, não terá cumprimento do aviso e não grava informação da Data Projetada:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5890574151959/mceclip8.png)

3) Neste último exemplo, utilizamos o tipo de rescisão **05 - Pedido de demissão - Dispensa Aviso (Aviso Prévio = N)**.  Neste cenário a rotina entende que a empresa está dispensando o funcionário do Aviso e não projeta data de demissão:![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5890634988439/mceclip9.png)

**Saiba mais**  
Para adquirir maior conhecimento acesso o *link* abaixo:  
[Página Centralizadora da Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
