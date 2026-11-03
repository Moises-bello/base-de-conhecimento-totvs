---
article_id: 4419709968023
category: RH - Definições de Cálculo
content_hash: 2918d910906cd9ceede22f393a7e495ff0b9e494eacad9d07819d2fa8aece345
fetched_at: '2026-06-28T22:43:22.438231+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Conceito do campo C.Agrup.Med - RV_GRAMED
type: support-article
updated_at: '2025-10-03T18:08:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419709968023-RH-Linha-Protheus-GPE-Conceito-do-campo-C-Agrup-Med-RV-GRAMED
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33056544041495)** Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o conceito e como funciona o campo **C.Agrup.Med - RV\_GRAMED** no cadastro de verbas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O campo **C.Agrup.Med -** **RV\_GRAMED**, é utilizado para agrupamento de valores no cálculo da média, isto é, as verbas recebidas pelo funcionário serão exibidas no relatório de médias no código de verba preenchido nesse campo.  
 **Exemplo**  
Há três verbas com configuração para média, sendo que duas delas tem o campo C.Agrup.Med (RV\_GRAMED), conforme tabela abaixo:

|  |  |
| --- | --- |
| **Código Verba** | **C.Agrup.Med.** |
| 207 |  |
| 208 | 065 |
| 209 | 065 |

   
Supondo que o funcionário tenha recebido as três verbas no período das médias, ao efetuar um cálculo que gere médias e ao emitir o relatório de médias serão exibidos apenas duas verbas:

1. 0207;
2. 0065.

Devido ao agrupamento, os valores recebidos nas verbas 208 e 209 serão exibidos na verba do código 065.  
  
É necessário que a verba preenchida no campo **C.Agrup.Med** também possua incidências para médias, caso contrário, não será considerado na composição das médias, nem será exibida no relatório.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias)   
[RH - Linha Protheus - GPE - Parâmetros e Mnemônicos utilizados para o cálculo de Média](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7011337477015-RH-Linha-Protheus-GPE-Par%C3%A2metros-e-Mnem%C3%B4nicos-utilizados-para-o-c%C3%A1lculo-de-M%C3%A9dia)
