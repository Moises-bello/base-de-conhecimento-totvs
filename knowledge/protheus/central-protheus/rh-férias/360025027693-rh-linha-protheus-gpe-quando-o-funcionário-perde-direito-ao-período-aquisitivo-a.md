---
article_id: 360025027693
category: RH - Férias
content_hash: e9e5c765b30771a17527959b68d23e4aee9424dcf0b2a97802e6fee756d92cf5
fetched_at: '2026-06-28T22:43:59.163134+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Quando o funcionário perde direito ao Período Aquisitivo
  após o retorno do Afastamento
type: support-article
updated_at: '2025-04-11T17:42:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025027693-RH-Linha-Protheus-GPE-Quando-o-funcion%C3%A1rio-perde-direito-ao-Per%C3%ADodo-Aquisitivo-ap%C3%B3s-o-retorno-do-Afastamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31349348158231) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Quando o funcionário perde direito ao Período Aquisitivo após o retorno do afastamento?  
Orientações relacionadas a perda do período aquisitivo de férias quando funcionário teve afastamentos que a soma é superior a 180 dias.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O funcionário **perde** direito ao Período Aquisitivo de Férias após o Retorno do Afastamento, quando os dias de **ausência ultrapassam** a quantidade de dias determinados no campo **Tip. Aus. Feri** (RCM\_FERIAS) do Cadastro do Tipo de ausência, desconsiderando os dias que foram pagos pela empresa.  
  
**Exemplo****1** - Funcionário afastado por Doença, com Afastamentos não Sequenciais.  
Afastamentos Sem Sequência (Com códigos de CID Diferentes): 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038373054)

Período Aquisitivo : 22/12/17 á 21/12/18 Ativo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038373934)

Cadastro de Ausência:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039209893)

Neste exemplo temos um total de 208 dias de Ausência, sendo que a cada afastamento, a empresa pagou os 15 primeiros dias.  
Neste caso, o funcionário **Não perde Direito** ao Período Aquisitivo de Férias, pois desconsiderando os 45 dias pagos pela empresa, o funcionário ficou 163 dias afastado, e **não ultrapassou os 180 dias** determinados no Cadastro de ausência.

**Exemplo 2** - Funcionário afastado por Doença, com Afastamentos Sequenciais.

Afastamentos Em Sequência (Com códigos de CID iguais): 

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039211973)

Período Aquisitivo : 22/12/17 á 21/12/18 Prescrito:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039211653)

Cadastro de Ausência:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039209893)

Neste outro caso temos um total de 211 dias de Ausência, sendo que somente no primeiro e segundo, empresa pagou os 15 primeiros dias.  
Neste caso, o funcionário **Perde** Direito ao Período Aquisitivo de Férias, pois desconsiderando os 30 dias pagos pela empresa, o funcionário ficou 181 dias afastado, quantidade que **ultrapassa os 180 dias** determinados no Cadastro de ausência.

**Saiba Mais**[RH - Linha Protheus - GPE - Como informar data fim de afastamentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006476621-RH-Linha-Protheus-GPE-Como-informar-data-fim-de-afastamentos?source=search)[RH - Linha Protheus - GPE - Como Lançar Ausências para um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011457651-RH-Linha-Protheus-GPE-Como-Lan%C3%A7ar-Aus%C3%AAncias-para-um-Funcion%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Prorrogação de afastamento de um funcionário emitindo alerta: Help: Nr. Sequencia Problema: O tipo de ausência e regras de cálculo da sequência informada são diferentes da sequência atual. Altere o cadastro antes de continuar.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058499454-RH-Linha-Protheus-GPE-Prorroga%C3%A7%C3%A3o-de-afastamento-de-um-funcion%C3%A1rio-emitindo-alerta-Help-Nr-Sequencia-Problema-O-tipo-de-aus%C3%AAncia-e-regras-de-c%C3%A1lculo-da-sequ%C3%AAncia-informada-s%C3%A3o-diferentes-da-sequ%C3%AAncia-atual-Altere-o-cadastro-antes-de-continuar-?source=search)
