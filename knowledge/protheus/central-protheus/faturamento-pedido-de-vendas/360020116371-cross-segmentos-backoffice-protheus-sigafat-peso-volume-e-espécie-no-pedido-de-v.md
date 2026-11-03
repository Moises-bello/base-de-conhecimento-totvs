---
article_id: 360020116371
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f7e13aabdd44e143eff380405d47baffdfefea15c85cf08b47e0cf2d8ff4340b
fetched_at: '2026-06-28T22:38:39.951897+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Peso, volume e espécie no
  pedido de venda e ao faturar
type: support-article
updated_at: '2026-05-13T21:21:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020116371-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Peso-volume-e-esp%C3%A9cie-no-pedido-de-venda-e-ao-faturar
---

**Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**

Qual a tratativa do sistema para o preenchimento e a integração dos campos de Peso, Volume e Espécie entre o Pedido de Venda e o Documento de Saída?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Para que os dados de **Peso, Volume e Espécie** sejam levados ao **DANFE**, é necessário que os campos `F2_PLIQUI`, `F2_PBRUTO`, `F2_VOLUME1` e `F2_ESPECI1` estejam preenchidos no Documento de Saída.

Existem duas formas principais para a gravação dos campos de peso (`F2_PLIQUI` e `F2_PBRUTO`):

**1. Pelo Cadastro do Produto:** Nesta configuração, os campos do cabeçalho do pedido de vendas (`C5_PESOL` e `C5_PBRUTO`) não terão o preenchimento. A nota será alimentada da seguinte forma:

* O campo `F2_PLIQUI` é gravado de acordo com o campo `B1_PESO` (multiplicado pela quantidade `D2_QUANT`).
* O campo `F2_PBRUTO` é gravado de acordo com o campo `B1_PESBRU` (multiplicado pela quantidade `D2_QUANT`).

**2. Pelo Pedido de Vendas:** Os campos `C5_PESOL` e `C5_PBRUTO` não têm preenchimento automático.

* Caso preenchidos manualmente no Pedido de Venda, o sistema irá sobrepor esses conteúdos nos campos `F2_PLIQUI` e `F2_PBRUTO` do Documento de Saída.

**Tratativa de Volume e Espécie:** Os campos destinados ao preenchimento de Volume (`C5_VOLUME`) e Espécie (`C5_ESPECI`) não possuem preenchimento automático, mesmo com o preenchimento de embalagens no cadastro.

**Esses campos, também, não diminuem automaticamente, são sempre fixos, se preciso for, podem ser alterados conforme as liberações vão acontecendo, antes de faturar para sair certo na nota.**

* **Com Aglutinação de Pedidos habilitada:** Os volumes correspondentes a espécies iguais serão somados. Espécies diferentes serão distribuídas nos campos `F2_VOLUME'x'` e `F2_ESPECI’x’` conforme a ordem de processamento.
* **Com Aglutinação de Pedidos desabilitada:** Haverá correspondência direta. Exemplo: `C5_VOLUME1` preenche `F2_VOLUME1`, `C5_ESPECI1` preenche `F2_ESPECI1`, e assim sucessivamente até o volume/espécie 4.

> **Importante: XML / DANFE com múltiplos volumes e espécies** No XML da Nota, as informações de Peso Líquido e Peso Bruto serão levadas **apenas para a primeira tag** de Volume 1 (`F2_VOLUME1`) e Espécie 1 (`F2_ESPECI1`). Os campos referentes aos Volumes e Espécies 2, 3 e 4 não possuirão as tags de peso líquido e peso bruto. Para tratar esta situação utilize o link do Ponto de Entrada listado no final deste artigo.

---

##### **Observações:**

* Caso os campos estejam devidamente preenchidos na Tabela SF2, mas não sejam impressos na DANFE, consulte a Equipe de Suporte SPED/TSS.
* O conteúdo do campo `B1_PESO` também é levado para o campo `FT_PESO` (referente ao item da nota fiscal, gravado sempre com o peso real do produto).

**Saiba mais:**

* [**Peso, Volume e Espécie no Pedido de Vendas e Documento de Saída**](https://tdn.totvs.com/x/Z0NtDQ)
* [**DT\_PE\_PE01NFESEFAZ\_Peso\_Líquido\_e\_Peso\_Bruto\_por\_Espécie\_e\_Volume\_na\_DANFE**](https://tdn.totvs.com/x/3lYMEQ)
