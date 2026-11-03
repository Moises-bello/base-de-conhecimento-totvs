---
article_id: 20980892258071
category: Financeiro - Movimentação Bancária
content_hash: 173551b6c2da805a900327474ad08e1eee7f86d39f78c83e22bf87c69b2eeb2b
fetched_at: '2026-06-28T22:38:19.510806+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713/FINA717 -
  Help: Operação não permitida pois o boleto não pertence ao convênio do usuário'
type: support-article
updated_at: '2024-01-30T17:58:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20980892258071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-FINA717-Help-Opera%C3%A7%C3%A3o-n%C3%A3o-permitida-pois-o-boleto-n%C3%A3o-pertence-ao-conv%C3%AAnio-do-usu%C3%A1rio
---

**Ocorrência**

Ao transmitir um borderô ao Banco do Brasil via API (FINA713), no monitor de boletos constam pendência, e o retorno "operação não permitida pois o boleto não pertente ao convênio do usuário".

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20980863242007)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir 12.1.2210  
  
**Causa**O banco poderá retornar a mensagem, ao validar algumas situações: 

**01** - Número do convênio enviado está divergência ao cadastrado cadastrado em parâmetro de banco

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20980892241559)

**02** - Banco está cadastrado com o digito e conta juntos, ficando a conta diferente do convênio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20982630965911)

**Solução**Validar com o banco se as informações cadastradas no **Cadastro Parâmetros Banco (FINA130),** estão em concordância com as informações disponibilizadas ao realizar o cadastro das credenciais.  
  
**Saiba mais**

[Banco do Brasil - Configuração Boletos - FINA713 (Contas a Receber)](https://tdn.totvs.com/pages/releaseview.action?pageId=673798283)

[Banco do Brasil - Configuração pagamentos - FINA717 (Contas a Pagar)](https://tdn.totvs.com/pages/releaseview.action?pageId=734394173)
