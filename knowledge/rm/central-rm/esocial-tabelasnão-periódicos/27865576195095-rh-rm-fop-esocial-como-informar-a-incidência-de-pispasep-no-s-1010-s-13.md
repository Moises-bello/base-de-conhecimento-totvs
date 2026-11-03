---
article_id: 27865576195095
category: eSocial - Tabelas/Não Periódicos
content_hash: d570d2a83465475531aa484989b727f91363c0dd75c0542a5ab43c53e12cd5c1
fetched_at: '2026-06-28T22:47:10.288362+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Como informar a incidência de PIS/PASEP no S-1010
  (S-1.3)
type: support-article
updated_at: '2025-04-10T13:11:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27865576195095-RH-RM-FOP-eSocial-Como-informar-a-incid%C3%AAncia-de-PIS-PASEP-no-S-1010-S-1-3
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27865570649751)**Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**Como informar a incidência de PIS/PASEP (Tag *codIncPisPasep*) nos eventos S-1010?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir dos Patches 12.1.2402.245, 12.1.2406.186, 12.1.2410.121 e superiores  
  
**Solução**No Leiaute S-1.3 foi criado a tag ***codIncPisPasep*** para informar o código de incidência da rubrica para o PIS/PASEP.

No sistema, foi criado o campo **Incidência PIS/PASEP** no cadastro de eventos (menu **Administração de Pessoal | Eventos**) tanto na aba **Inc. Proventos** quanto na **Inc. Descontos**.

*Aba Inc. Proventos*

![image-2024-8-14_16-35-56.png](https://tdn.totvs.com/download/attachments/862114556/image-2024-8-14_16-35-56.png?version=1&modificationDate=1723664197027&api=v2)

*Aba Inc. Descontos*

![image-2024-8-29_18-59-17.png](https://tdn.totvs.com/download/attachments/862114556/image-2024-8-29_18-59-17.png?version=1&modificationDate=1724968757393&api=v2)

Ao preencher este campo no cadastro de evento, será gerado gatilho do evento S-1010 e no XML a tag ***codIncPisPasep*** será de preenchida.

**Importante**

* Só será gerado o tag ***codIncPisPasep*** quando o campo de **indicador de tributação sobre folha - PIS e PASEP** estiver marcado no cadastro do empregador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27865576186519)

* Se o parâmetro não for preenchido no cadastro do evento, a *Tag* ***codIncPisPasep***não será gerada no XML do S-1010. Conforme diretriz do leiaute do eSocial, quando a tag não é informada, o governo assumirá automaticamente o valor ***00 - Não é base de cálculo do PIS/PASEP***.

![](https://tdn.totvs.com/download/attachments/862114556/image-2024-9-18_12-5-23.png?version=1&modificationDate=1726671962887&api=v2)

**Saiba mais**  
Para mais informações, acesse:  
    - [Leiaute Versão S-1.3 e NT 01/2024](https://tdn.totvs.com/pages/releaseview.action?pageId=862114556)
