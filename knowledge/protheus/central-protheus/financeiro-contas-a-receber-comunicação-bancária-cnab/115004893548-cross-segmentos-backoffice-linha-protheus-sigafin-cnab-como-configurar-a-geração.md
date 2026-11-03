---
article_id: 115004893548
category: Financeiro - Contas a Receber - Comunicação Bancária CNAB
content_hash: 78c704adc40ce5e26462cd300d3c03e9a7a380f35df2dfcc3d395381624edd0e
fetched_at: '2026-06-28T22:37:47.965764+00:00'
product: protheus
section_id: 26656449081111
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  CNAB - Como configurar
  a geração do nosso número
type: support-article
updated_at: '2025-11-12T17:46:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004893548-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-configurar-a-gera%C3%A7%C3%A3o-do-nosso-n%C3%BAmero
---

**Dúvida**  
Como configurar a geração do nosso número?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**  
Quando a empresa realiza emissão de boleto para o cliente, é necessário enviar o nosso número em cada título enviado ao banco.

O campo referente ao nosso número (**E1\_NUMBCO**) é preenchido conforme a configuração dos campos faixa início (**EE\_FAXINI),** faixa fim (**EE\_FAXFIM**) e faixa atual (**EE\_FAXATU**) no cadastro de Parâmetros Bancos (**FINA130**).

Para acessar a documentação da configuração do processo, acesse: [FIN0022\_CNAB\_Geração\_do\_nosso\_número](http://tdn.totvs.com/pages/viewpage.action?pageId=233764450)

É importante destacar que o **Nosso Número** é um requisito específico do layout de cobrança definido por cada instituição bancária. Assim, caso o campo **E1\_NUMBCO** seja ampliado no Protheus sem o devido ajuste no layout do **CNAB**, o arquivo de remessa poderá ser rejeitado pelo banco.

Antes de proceder com qualquer alteração, recomenda-se confirmar junto à instituição bancária o tamanho exato do **Nosso Número** exigido, de forma que esse mesmo tamanho seja configurado no campo **E1\_NUMBCO**.

**Veja mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
