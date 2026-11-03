---
article_id: 360016524552
category: RH - Lançamentos
content_hash: fc07b669b136e9e498cee8f2c1fbb88571881c343d3be8ea4749015c48359067
fetched_at: '2026-06-28T22:43:31.194353+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar os lançamentos de empréstimo consignado
  na folha de pagamento
type: support-article
updated_at: '2025-07-24T17:19:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016524552-RH-Linha-Protheus-GPE-Como-gerar-os-lan%C3%A7amentos-de-empr%C3%A9stimo-consignado-na-folha-de-pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26103015559063)** Tempo aproximado para leitura:**00:02:30 min**

**Dúvida**Como gerar os lançamentos de empréstimo consignado na folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE - Gestão de Pessoal - A partir da versão 12  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

O sistema realiza o controle do desconto de empréstimos consignados na folha de pagamento, divide em parcelas e quita lançamentos a partir da data inicial de vencimento.

1. Cadastre uma verba **sem id** p/ cálculo de empréstimo consignado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012769751)

2. Faça o lançamento em valores futuros (**Atualizações > Lançamentos > Valores Futuros**);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012768912)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012769512)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012770631)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012770651)

**Campos importantes:**

**Código de verba**: Verba cadastrada como empréstimo consignado;

**Valor Principal:** Valor total do empréstimo;

**Numero de parcelas**: Numero de parcelas para quitação do empréstimo;

**Num. parcelas pagas**: Caso o empréstimo já esteja em andamento é necessário preencher este campo com o numero de parcelas já pagas ao banco;

**Data do próximo vencimento**: Este campo precisa ser preenchido para que o sistema tenha uma base de quando iniciará o pagamento;

**Emp. Consig**: Este campo é preenchido de forma automática caso o campo **Emp. Consig.** do cadastro de verbas esteja preenchido.

**Per. Inicio**: É o período inicial do desconto, a folha em aberto.

**Situação**: Informa se aquele lançamento este ativo e deve ser calculado na folha.  
**Regra de Desconto:** Nesse campo é possível selecionar a regra de desconto para o empréstimo. Por exemplo, se **selecionado Folha ou deixar em branco** o sistema sempre descontará da folha de pagamento, portanto nos meses de férias, onde o funcionário não tenha saldo, o desconto ocorrerá e a verba saldo insuficiente será demonstrada no valor como provento e no próximo mês o sistema lança automaticamente essa verba como desconto (quando houver saldo).

Se **selecionado Férias**, o sistema irá descontar na folha de pagamento normalmente e quando houver Férias, o sistema desconta das férias e não da folha.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046988613)

3. Calcule a folha:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012769632)  
  
Após gravar o lançamento em **Valores futuros**, qualquer **alteração** deve ser feita em **Conta Corrente Valores Futuros**. Segue documentação para auxiliar: [RH - Linha Protheus - GPE - Como controlar as movimentações de Lançamentos Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006568592-RH-Linha-Protheus-GPE-Como-controlar-as-movimenta%C3%A7%C3%B5es-de-Lan%C3%A7amentos-Valores-Futuros)

**Saiba Mais**

[RH - Linha Protheus - GPE - Como suspender valores lançados na rotina de Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017555452-RH-Linha-Protheus-GPE-Como-suspender-valores-lan%C3%A7ados-na-rotina-de-Valores-Futuros)

[RH - Linha Protheus - GPE - Lançamento de Valores Futuros não é carregado para a folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14175822567447-RH-Linha-Protheus-GPE-Lan%C3%A7amento-de-Valores-Futuros-n%C3%A3o-%C3%A9-carregado-para-a-folha)

[RH - Linha Protheus - GPE - Sistema permite deletar lançamento futuro que ainda não foi feito o pagamento de nenhuma parcela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13491090836119-RH-Linha-Protheus-GPE-Sistema-permite-deletar-lan%C3%A7amento-futuro-que-ainda-n%C3%A3o-foi-feito-o-pagamento-de-nenhuma-parcela)

[RH - Linha Protheus - GPE - Como gerar lançamentos de empréstimo consignado nas Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053128314-RH-Linha-Protheus-GPE-Como-gerar-lan%C3%A7amentos-de-empr%C3%A9stimo-consignado-nas-F%C3%A9rias)
