---
article_id: 30908070019351
category: Materiais - Compras (SIGACOM)
content_hash: 8a0eec85ccca15586162f3fbb746ddf3b1f46146aba5e814bf65739fdcfcb264
fetched_at: '2026-06-28T22:41:17.619303+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Erro invalid typecast
  in file ao gerar cotação pelo NFC.
type: support-article
updated_at: '2025-03-25T17:40:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30908070019351-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Erro-invalid-typecast-in-file-ao-gerar-cota%C3%A7%C3%A3o-pelo-NFC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30908067930775) Tempo aproximado para leitura: **00:02 min****Ocorrência**

THREAD ERROR ([XXXXX], usuario, maquinaXXX)

invalid typecast in file D:\build-dir\TP11-OF20320-TECXWIN64\advpl\instrvar.inl at line 989   
on A131ADDFOR(MATA131.PRW) 06/03/2025 16:25:42 line : 3896

**Ambiente**

Protheus – Compras – A partir da versão 12

**Causa**Erro ocorre devido o parâmetro **MV\_PGCOBC1** estar com o Tipo **"C - carácter"** e o seu conteúdo Lógico.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30908067931415)

**Solução**

Neste caso é necessário alterar o parâmetro **MV\_PGCOBC1** para Tipo **"L - Logico"** e  seu conteúdo Lógico.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30908070003991)

Para maiores informações sobre o NFC acesse: [Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
