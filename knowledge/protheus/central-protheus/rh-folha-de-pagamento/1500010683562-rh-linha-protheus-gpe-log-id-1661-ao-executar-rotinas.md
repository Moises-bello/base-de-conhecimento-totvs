---
article_id: 1500010683562
category: RH - Folha de Pagamento
content_hash: 5bec0d4b35ee3fa96c823d89d26164f34f64bb8bd6ae82e3cc321f347c58813a
fetched_at: '2026-06-28T22:44:15.053121+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Log ID 1661 ao executar rotinas
type: support-article
updated_at: '2024-09-04T20:10:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010683562-RH-Linha-Protheus-GPE-Log-ID-1661-ao-executar-rotinas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21305111427991) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao executar as rotinas, sistema apresenta log com a mensagem: Os identificadores abaixo são obrigatórios e não estão relacionados a uma verba: 1661-Base Dedutora INSS 13º  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**A mensagem ocorre pois não há verba relacionada ao ID 1661 na rotina **Verbas**.  
  
**Solução**

Acesse o cadastro de Verbas em **Atualizações/ Definições de Cálculo/ Verbas** e clique em **Incluir**Cadastre uma nova verba e relacione ao ID 1661, a nova verba deve ter as parametrizações abaixo:  
- Verba tipo **Base Desconto**  
- Natureza informativa **9989**  
- Campo **Cd. INC. CP** deve ficar com **12**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21305140645655)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21305111470231)

**Obs.:** A configuração restante é algo particular de cada empresa.

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - eSocial - S-2299 / S-1210 - Inss incorreto quando existe rescisão e 13º salário ou erro 726 no S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjFHlrVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBymh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA2MTczODY5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtZVNvY2lhbC1TLTIyOTktUy0xMjEwLUluc3MtaW5jb3JyZXRvLXF1YW5kby1leGlzdGUtcmVzY2lzJUMzJUEzby1lLTEzJUMyJUJBLXNhbCVDMyVBMXJpby1vdS1lcnJvLTcyNi1uby1TLTEyMTAGOwhUOg5zZWFyY2hfaWRJIik1NmJiMjgxYS0zZWIxLTRhNjMtOGU3NC01NzE3ZmRkNmM1MDIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgGEUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIGVTb2NpYWwgLSBTLTIyOTkgLyBTLTEyMTAgLSBJbnNzIGluY29ycmV0byBxdWFuZG8gZXhpc3RlIHJlc2Npc8OjbyBlIDEzwrogc2Fsw6FyaW8gb3UgZXJybyA3MjYgbm8gUy0xMjEwBjsIVDoScmVzdWx0c19jb3VudGkChAQ%3D--4bd69e5afde15ab9b243b7f184fe79686d4dfa19)
