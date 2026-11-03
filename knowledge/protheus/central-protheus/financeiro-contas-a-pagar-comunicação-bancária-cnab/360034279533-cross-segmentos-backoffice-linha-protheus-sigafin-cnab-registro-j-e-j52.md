---
article_id: 360034279533
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 76522e71bcbf9aff4203b4dff9b106fec42516ff57b40d0db17394b9ac884d95
fetched_at: '2026-06-28T22:37:55.042309+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - REGISTRO J e
  J52
type: support-article
updated_at: '2026-05-13T17:01:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034279533-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-REGISTRO-J-e-J52
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37445720811927)**Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
A partir do dia 01/09/2019 por determinação da FEBRABAN/BANCO CENTRAL o registro J52 será obrigatório independente de valor, além de ter o seu sequencial, colunas 009 a 013, modificados.   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões

**Solução**  
**Como é atualmente:**

titulo 1 - sequencia 1 para J

titulo 1 - sequencia 1 para J52

titulo 2 - sequencia 2 para J

titulo 2 - sequencia 2 para J52

Sintax utilizada na posição 009 a 013: **PADL(INT(INCREMENTA()-1),5,"0")**

**Como deve ficar?**

titulo 1 - sequencia 1 para J

titulo 1 - sequencia 2 para J52

titulo 2 - sequencia 3 para J

titulo 2 - sequencia 4 para J52

Sintax utilizada na posição 009 a 013: **STRZERO(F420SEQLOT(),5)**

**Na recepção do arquivo modelo 2, utilize na posição****018 a 019****a função SEGJ52:**

1. Crie ou Restaure o arquivo de configuração (\*.2PR)
2. No segmento J-52 pressione a tecla **[F4]** para acessar os detalhes
3. Configure o segmento conforme o manual do banco
4. Na linha que identifica o segmento J-52, preencha a coluna conteúdo com o valor **SEGJ52**.
5. Confirme a operação e salve o arquivo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37445720817303)

**Informações Adicionais:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA300 - O que é necessário para gerar o registro J-52 na remessa do SISPAG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019519972-MP-SIGAFIN-FINA300-O-que-%C3%A9-necess%C3%A1rio-para-gerar-o-registro-J-52-na-remessa-do-SISPAG-?source=search)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como utilizar o segmento J-52 no SISPAG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018663271-MP-SIGAFIN-Como-utilizar-o-segmento-J-52-no-SISPAG?source=search)

<http://tdn.totvs.com/display/public/PROT/CNAB>

[Gerar arquivo de Retorno (CFGX049 - SIGACFG)](https://tdn.totvs.com/pages/releaseview.action?pageId=306855592)

**Para tratativa do CEDENTE/BENEFICIÁRIO:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Segmento J-52 – Identificação do Cedente/Beneficiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035158573/)
