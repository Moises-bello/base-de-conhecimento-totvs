---
article_id: 360043193774
category: MDFe - Manifesto de Carga
content_hash: b20b577bd6244ed2634aabc0dd05d829bbe609824b37075315ac03d824645cc8
fetched_at: '2026-06-28T22:40:08.089323+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos  - MDF-e - MANISFESTO
  DE CARGA DE ENTRADA'
type: support-article
updated_at: '2024-04-04T22:04:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043193774--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDF-e-MANISFESTO-DE-CARGA-DE-ENTRADA
---

**Dúvida**MDFE DE ENTRADA, QUAIS OS CAMPOS PRECISAM ESTA PREENCHIDOS  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Informar a ESPECIE=SPED no documento de entrada, e dessa maneira serão preenchidos os campos F1\_ESPECIE, F3\_ESPECIE e FT\_ESPECIE = SPED.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058396254)

2- Informar o veiculo em um desses campos : F1\_VEICUL1, F1\_VEICUL2, F1\_VEICUL3.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058396314)

3- Deve ser informada a Chave no campo F1\_CHVNFE,  dessa maneira será preenchida a Chave nos campos: FT\_CHVNFE e F3\_CHVNFE.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059299673)

 4- Informar o filtro de entrada na rotina SPEDMDFE

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058396694)

5- Na rotina SPEDMDFE deve ser informada o mesmo veiculo preenchido no campo F1\_VEICUL1   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059300193)
