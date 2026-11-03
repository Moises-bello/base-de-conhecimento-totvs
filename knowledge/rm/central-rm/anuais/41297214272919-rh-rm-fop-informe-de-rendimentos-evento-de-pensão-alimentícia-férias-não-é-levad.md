---
article_id: 41297214272919
category: Anuais
content_hash: 5715caa4e5d0717ae5a40fd53a87eea2988de331f42a75c77f83fdd6fbd6ab60
fetched_at: '2026-06-28T22:46:50.924292+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - Informe de Rendimentos - Evento de pensão alimentícia férias,
  não é levado no Informe de Rendimentos
type: support-article
updated_at: '2026-06-22T16:45:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41297214272919-RH-RM-FOP-Informe-de-Rendimentos-Evento-de-pens%C3%A3o-aliment%C3%ADcia-f%C3%A9rias-n%C3%A3o-%C3%A9-levado-no-Informe-de-Rendimentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41297214247319) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Na geração do Informe de Rendimentos a linha **4. Pensão Alimentícia (inf beneficiário no campo 7)** do campo **3- Rendimentos tributáveis, deduções e imposto**  está sendo considerado o evento de pensão Alimentícia de férias. Porém o campo 7 - Informações complementares não apresenta o valor da pensão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297214248087)![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297222960663)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
O incidente pode ocorrer devido a divergências de informações entre o recibo de férias, envelope de pagamento onde ocorreu o lançamento e registro do movimento de pensão. Conforme exemplificado no material de apoio (print):

Acesse administração de pessoal | funcionário | férias cadastrada, podemos verificar o lançamento de pensão de férias dentro do mês 03/2025:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297214250007)

Dentro do cadastro de **Dependentes | Anexo** , acessamos o **Movimento da Pensão de Dependente**s :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297222963351)

Vemos dois registro para o mês competência 3:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297222964759)

O Registro de férias é o de valor 255,24 o mesmo está apontando para o **tipo de movimento 0** o correto seria apontar para o **tipo de movimento 1** com as informações de data de pagamento das férias e data de vencimento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297214252823)

Dessa forma ao gerar o informe de rendimento as informações serão levadas corretamente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297222969623)![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297214255255)

**Importante:**

##### *04 – Pensão Alimentícia (beneficiário informado no campo 7)*

##### *Considera os códigos de cálculo:*

##### *(13 + 113 + 53 + 195 + 197 + 319 + 326 + 320 + 386) – (199 + 201 + 327)*

O informe de rendimentos segue a seguinte validação das informações conforme código de calculo e movimento da pensão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297214258327)

**Saiba mais:**

[FOP\_0002\_Emissão DIRF/Informe de Rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=208347682#1-2)

[RH - RM - FOP - DIRF/Informe de Rendimentos: Ficha Financeira divergente do movimento de Pensão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007117092-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Ficha-Financeira-divergente-do-movimento-de-Pens%C3%A3o)
