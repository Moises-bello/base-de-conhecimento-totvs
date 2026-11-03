---
article_id: 360050762134
category: RH - Ponto Eletrônico
content_hash: bb42e31a24de4f9de2d13a84b3b4257352aae39aaf2e91e05c422adbafb9e2f2
fetched_at: '2026-06-28T22:44:58.289738+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar um Abono Coletivo no Ponto Eletrônico
type: support-article
updated_at: '2021-08-11T23:27:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050762134-RH-Linha-Protheus-PON-Como-efetuar-um-Abono-Coletivo-no-Ponto-Eletr%C3%B4nico
---

**Dúvida**Como efetuar um abono coletivo no Ponto Eletrônico?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O **Abono Coletivo** é utilizado nos casos onde existe um volume grande de incidências no mesmo dia para muitos funcionários e todos terão o abono do período. Para a utilização, é necessário que exista um Motivo de Abono cadastrado para ser utilizado no Abono Coletivo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098586474/mceclip0.png)  
  
Depois, verifique exatamente o código do evento que será abonado, neste exemplo, será o evento 010 - Falta:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100823333/mceclip1.png)  
  
Acesse Miscelânea - Cálculos - Abono Coletivo e preencha os parâmetros:  
  
- **Data De/ Data Até?**: devem ser datas dentro do período de apontamento que estão informando no MV\_PONMES  
- **Eventos Abonados?**: lançar o código do evento que será abonado de forma coletiva  
- **Sobrepor Abonos?**: se esta pergunta estiver como Sim, caso já exista uma abono lançado para qualquer dia em que exista o evento gerado, ele será sobreposto pelo que será informado na rotina de Abono Coletivo  
- **Tipo de Abono?**: informar se será Integral ou Parcial. Para a primeira opção, todas as horas geras para o evento informado serão abonadas. Se for selecionada a segunda opção, apenas uma quantidade de horas informadas pelo usuário no próximo parâmetro serão abonadas  
- **Horas Abono Parcial?**: esta pergunta só será validada caso a pergunta anterior esteja como Parcial. Neste caso, o usuário deve informar a quantidade de horas que serão abonadas  
  
Após o preenchimento dos parâmetros, o sistema mostrará uma outra janela com todos os funcionários que dentro do intervalo de datas informado, tem o evento apontado. Nesta janela, informe qual o código do motivo de abono que será utilizado:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100823453/mceclip2.png)  
  
Após confirmar, os abonos serão lançados de forma coletiva, não sendo necessário reapontar as marcações.
