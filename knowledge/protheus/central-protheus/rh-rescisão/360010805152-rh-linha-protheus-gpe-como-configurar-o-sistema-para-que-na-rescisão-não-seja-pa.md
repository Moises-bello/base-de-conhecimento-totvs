---
article_id: 360010805152
category: RH - Rescisão
content_hash: 928de9510d6b83e7a2cb1524f825750341bc8c8df14c01a2acf421b04028e654
fetched_at: '2026-06-28T22:43:48.634665+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o Sistema para que na rescisão
  não seja pago saldo de salário
type: support-article
updated_at: '2025-09-11T00:57:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010805152-RH-Linha-Protheus-GPE-Como-configurar-o-Sistema-para-que-na-rescis%C3%A3o-n%C3%A3o-seja-pago-saldo-de-sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34843846129175) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como configurar o Sistema para que na rescisão não seja pago saldo de salário, quando o mesmo foi pago na folha, por exemplo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Quando o funcionário é demitido no final do mês possivelmente o salário do mesmo foi pago na folha.

Ao processar a rescisão, o sistema calcula novamente como saldo de salário pois não há como entender que já foi pago como salário mensal.

Para não pagar saldo de salário na rescisão, em **Atualizações > Definições de Calculo > Manutenção de tabela > S043 - TIPO DE RESCISÃO,** coloque N na coluna Saldo Salário para o Tipo de rescisão que será calculada:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9319737159191)

**Saiba mais**

[RH - Linha Protheus - GPE - Como parametrizar a tabela S043 para cadastrar um novo tipo de rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004395831-RH-Linha-Protheus-GPE-Como-parametrizar-a-tabela-S043-para-cadastrar-um-novo-tipo-de-rescis%C3%A3o?source=search)
