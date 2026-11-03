---
article_id: 18143354886551
category: RH - Integração de Titulo
content_hash: e1e791034b041ca444f5fa9be4a76bddd0462d6f569d7850897a10dbd5787390
fetched_at: '2026-06-28T22:43:36.156332+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - AVISO: O vencimento do título deverá ser informado
  uma única vez'
type: support-article
updated_at: '2025-07-14T21:08:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18143354886551-RH-Linha-Protheus-GPE-AVISO-O-vencimento-do-t%C3%ADtulo-dever%C3%A1-ser-informado-uma-%C3%BAnica-vez
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18143323865751) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**

Ao tentar salvar o título na rotina Definição (GPEM640) é apresentado o seguinte AVISO, impedindo que as configurações sejam salvas:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18143354342935)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal - A partir da versão 12  
  
**Causa**

Título já possui configuração na opção Definição de relacionamento para busca do vencimento:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18143431578775)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1) Erro apresentado na tentativa de salvar as configurações definidas no título:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18143347401239)

2) Acessar a opção DEFINIR TÍTULO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18143443244951)

3) Acesse Outras Ações -> Informações para busca data de vencimento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18143483129623)

4) Exclua as informações de configuração para busca de acordo com a data gravada na tabela:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18143545308567)

Caso deseje realizar a busca de acordo com a data gravada na tabela de acordo com o cálculo realizado, mantenha essa opção da definição de relacionamento para busca do vencimento preenchida e no campo **DIA em Vencimento do título**, em branco conforme print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18143543112087)

Saiba Mais:  
[RH - Linha Protheus - GPE - Como criar e configurar um título de folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028042632-RH-Linha-Protheus-GPE-Como-criar-e-configurar-um-t%C3%ADtulo-de-folha-de-pagamento)
