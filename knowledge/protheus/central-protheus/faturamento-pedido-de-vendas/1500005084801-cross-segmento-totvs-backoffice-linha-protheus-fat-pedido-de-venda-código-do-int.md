---
article_id: 1500005084801
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: c69a652d8e484fb579e67d4644a1d7e5c00fac8edf363def23ee30128d8f331f
fetched_at: '2026-06-28T22:38:38.380985+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - Pedido de Venda
  - Código do Intermediador (Validações e Emissão da NF)
type: support-article
updated_at: '2021-09-06T20:47:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005084801-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Pedido-de-Venda-C%C3%B3digo-do-Intermediador-Valida%C3%A7%C3%B5es-e-Emiss%C3%A3o-da-NF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como utilizar o Código do Intermediador no Pedido de Vendas/Nota Fiscal?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - A partir da versão 12  
  
**Solução**Em atendimento à legislação da Nota Técnica 2020.006,  foi adicionado um tratamento do campo do "**Código do Intermediador"** nas rotinas do **Pedido de Venda** e na **Emissão do Documento Fiscal de Saída.**

Para isso foram criados os campos **C5\_INDPRES** e **C5\_CODA1U** no pedido de vendas, e o campo **F2\_CODA1U** no Documento de Saída, além do parâmetro **MV\_NT2006I**.

Para criação dos campos e parâmetro, além das tabelas envolvidas no processo, é necessário executar o **UPDDISTR** com o **SDFBRA** (Pacote de Dicionário) disponível em: <https://suporte.totvs.com/portal/p/10098/download?e=1013133>

```
OBS: A opção 4=NFC-e em operação com entrega a domicílio, não foi incluída no C5_INDPRES, pelo motivo: Pelo modulo do faturamento não é emitida operação de NFCE -Nota fiscal de cupom.
```

**Saiba mais**: <https://tdn.totvs.com/x/ZIZjIw>

**Saiba mais a respeito da NT2020.006 - Indicativo de presença e intermediador nos links abaixo:**<https://tdn.totvs.com/x/KmsIJ>  
<https://tdn.totvs.com/x/sb0oJ>
