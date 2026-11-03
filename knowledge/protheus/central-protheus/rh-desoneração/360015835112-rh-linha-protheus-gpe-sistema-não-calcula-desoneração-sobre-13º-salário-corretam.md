---
article_id: 360015835112
category: RH - Desoneração
content_hash: 2c7f0be03978734ef81b7f42b676fd7c8fe4a6e07aad6d3dd1d32e0cbe1cd877
fetched_at: '2026-06-28T22:43:42.253276+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não calcula desoneração sobre 13º salário
  corretamente
type: support-article
updated_at: '2026-03-25T13:28:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015835112-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-desonera%C3%A7%C3%A3o-sobre-13%C2%BA-sal%C3%A1rio-corretamente
---

**Ocorrência**  
No módulo **Gestão de Pessoal**, após realizar c**álculo do 13º** sistema **não calcula desoneração**.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12  
  
**Solução**  
De acordo com o item 3.8 da consultoria de segmentos, a desoneração de 13º salário não deve ser realizada até 2027.  
 [Orientação Consultoria de Segmentos - Reoneração da Folha de Pagamento](https://tdn.totvs.com.br/pages/releaseview.action?pageId=874192035#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosReonera%C3%A7%C3%A3odaFolhadePagamento-3.4ComoficaaReonera%C3%A7%C3%A3oapartirde2025)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39282672539031)

O sistema **não apresentará a verba de id 0973**, como também **não precisará gerar a DARF PIS** de contribuição previdenciária, pois a contribuição devida nesse cálculo já é realizada ao decorrer do ano, mês a mês.

Caso entenda que a desoneração deve ser realizada, altere o campo **Cálculo % Empresa 13º** da tabela **S037** para **S** em **Atualizações > Definições de Cálculos > Manutenção de Tabelas (GPEA320)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39282685724567)

**Saiba Mais**  
[RH - Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)
