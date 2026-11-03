---
article_id: 32755384304535
category: eConsignado (Crédito do Trabalhador)
content_hash: ca65226513639e0ddceed5e63671dc48a5531295cc5ccfd69d663fb606c3b56c
fetched_at: '2026-06-28T22:43:07.142861+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH  - Linha Protheus - GPE - Smartview - Relatório de Saldo Devedor econsignado
type: support-article
updated_at: '2026-06-22T18:04:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32755384304535-RH-Linha-Protheus-GPE-Smartview-Relat%C3%B3rio-de-Saldo-Devedor-econsignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32755384295831) Tempo aproximado para leitura: **02:00:00min**  
  
**Dúvida**  
Como gerar o relatório de saldo devedor eConsignado - Credito do trabalhador - para verificação de desconto parcial/ saldo devedor por falta de margem na folha de pagamento

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2310  
  
**Solução**  
**1. Passo**  
O relatório será adicionado ao menu na release 12.1.2510, então, para usar ele nas release 12.1.2410 ou 12.1.2310, é necessário adicionar a função **GPERSV079**no menu, para saber mais acesse:   
[RH - Linha Protheus - GPE - Como excluir ou incluir rotinas no menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013342191-RH-Linha-Protheus-GPE-Como-excluir-ou-incluir-rotinas-no-menu)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33399563883415)

2. Passo  
No relatório de saldo devedor, será possível filtrar os funcionários que tiveram empréstimos lançado nos valores futuros, seja, o crédito do trabalhador ou outro consignado.  
Foi realizado a inclusão da coluna '**Vlr. Não Pago**', que exibe o valor do novo campo **RCK\_NPAG**, correspondente ao valor não quitado da parcela do crédito do trabalhador.  
Exemplo;   
**Conta Corrente - Após calculo e fechamento da competência 05/2025**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32755370938135)

**3. Passo**  
Após incluir na rotina, acesse o relatório ;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32764898372759)

**- Clique em imprimir**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32764898373527)

**- Preencha os parâmetros e na pergunta - Somente eConsignado deixe = SIM**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32764883671831)

**- No Relatório serão apresentados apenas empréstimos da categoria Credito do Trabalhador demonstrando o Vlr Não Pago**  
Obs.: **O valor demonstrado sempre será o ultimo valor do campo RCK\_NPAG para o eConsigando gerado após o fechamento da folha.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32755384296599)  
  
**Observações**: O Sistema não possui um "ID" (campo ou mnemônico) padrão que traga o saldo devedor instantâneo pré-fechamento.

Para melhor entendimento assista aos videos HOW TO

**Saiba Mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=904052273>  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
