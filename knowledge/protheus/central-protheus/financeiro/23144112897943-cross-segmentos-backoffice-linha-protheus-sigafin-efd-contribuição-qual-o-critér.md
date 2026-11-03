---
article_id: 23144112897943
category: Financeiro
content_hash: 98d68beb0ee31b7306508c51205b206b3a67c140b53e5b7d77877c6df2442d3d
fetched_at: '2026-06-28T22:38:02.945067+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - EFD Contribuição -
  Qual o critério para agrupar o valor do bloco F525 na apuração do EFD contribuição
type: support-article
updated_at: '2024-08-01T20:32:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23144112897943-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-EFD-Contribui%C3%A7%C3%A3o-Qual-o-crit%C3%A9rio-para-agrupar-o-valor-do-bloco-F525-na-apura%C3%A7%C3%A3o-do-EFD-contribui%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23144089709079) Tempo aproximado para leitura: **00:06:00 min** **Dúvida**Qual o critério para agrupar o valor do bloco F525 na apuração do EFD contribuição?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – Todas versões  
  
**Solução**O critério para agrupar estes valores é feito através da rotina de Apuração, através das perguntas inicias da rotina:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23152746420887)

Se escolhido o indicador da **receita por Cliente**, então o campo **04–CNPJ\_CPF** será preenchido com o CNPJ do cliente da operação, o campo **02–VL\_REC** será o somatório das receitas dos clientes, e o campo **07–VL\_REC\_DET** será o somatório das receitas do cliente cujo CNPJ foi incluído no campo **04-CNPJ\_CPF**

Se escolhido o indicador da **receita por Título/Duplicata**, então o campo **05–NUM\_DOC** será preenchido com o número do título, o campo **02-VL\_REC** será o somatório das receitas dos títulos, e o campo **07–VL\_REC\_DET** será o somatório das receitas do título que foi informado no campo **04 – NUM\_DOC**

Se escolhido o indicador da **receita por Documento Fiscal**, então o campo **05–NUM\_DOC** será preenchido com o número da Nota Fiscal, o campo **02-VL\_REC** será o somatório das receitas das notas fiscais, e o campo **07-VL\_REC\_DET** será o somatório das receitas da nota fiscal que foi informada no campo **04-NUM\_DOC**

Se escolhido o indicador da **receita por Item Vendido**, então o campo **06–COD\_ITEM** será preenchido com o código do produto ou serviço, que deverá constar no **registro 0200**, o campo **02-VL\_REC** será o somatório das receitas dos produtos/serviços, e o campo **07-VL\_REC\_DET** será o somatório das receitas do produto/serviço que foi informado no campo **06-COD\_ITEM**

**Importante**  
O **campo 02–VL\_REC** é gravado com a somatória da receita e não individual, o comportamento do sistema segue as **regras do layout do EFD Contribuições**, pois a soma das receitas informadas no campo **02**, deverá corresponder a receita total informado no **registro F500**

**Saiba mais:**[EFD Contribuições - Registro F500/525 - Reconhecimento da Receita fato gerador PIS/COFINS](https://tdn.totvs.com/pages/releaseview.action?pageId=436273261)
