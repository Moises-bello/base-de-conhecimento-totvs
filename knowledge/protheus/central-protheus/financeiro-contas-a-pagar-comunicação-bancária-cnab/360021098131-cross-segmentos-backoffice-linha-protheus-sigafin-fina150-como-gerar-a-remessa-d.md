---
article_id: 360021098131
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 8f7cc5de76643f1276c0ff7443d7c67c7dd00328b92c6239d26444a355db450a
fetched_at: '2026-06-28T22:37:55.052659+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA150 - Como gerar
  a remessa de cobrança calculando o desconto
type: support-article
updated_at: '2025-01-31T20:21:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021098131-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA150-Como-gerar-a-remessa-de-cobran%C3%A7a-calculando-o-desconto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24267960149783)** Tempo aproximado para leitura:**00:05:00min  
  
Dúvida**Como gerar a remessa de cobrança calculando o desconto?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA150 - Todas as versões

**Solução**Primeiramente, precisa saber como o banco deve receber as informações referente ao banco do título. Pois cada banco possui alguma particularidade. Tem bancos que deve ser gerado o valor do título considerando o desconto e este valor do desconto deve ser informado na posição: "Valor Desconto". Outros bancos solicitam encaminhar apenas o valor do título na posição: "Valor Titulo" e na posição: "Valor Desconto" e informar o valor do desconto. Neste caso, deve sempre consultar o layout do banco.  
  
No exemplo abaixo, está sendo apresentado uma tela da rotina **Cnab Receber** localizado: Configurador > Ambiente > Cadastros. Através desta rotina é possível configurar layout de remessa em modelo 1 (400 posições):  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017572391)

Nesta posição, que será gerado na remessa e enviado para banco, deve informar o valor original do título e caso houver juros, multa ou desconto, será nessa posição que poderá informar a fórmula  para calcular o valor do título que o banco necessita.  
O valor do desconto pode ser informado no campo: "Desc. Fin"(E1\_DESCFIN) que está em destaque abaixo. Este campo calcula o desconto diariamente. Algumas empresa aplicam desconto dependendo da quantidade de dais de antecipação do pagamento, neste caso poderá utilizar o campo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017573091)

Sendo assim, visto que o valor do desconto encontra-se no campo **Desc Financ**, caso o Layout do banco esteja afirmando para informar o o desconto na posição do: "Valor Desconto", poderá informar no arquivo de configuração de remessa:

![sigacfg_descfin.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017694912)

Caso o valor do desconto seja um valor fixo, poderá utilizar o campo: **Descrescimo (E1\_DECRESC)**. Onde o valor do desconto está definido e não há alterações, caso seja este cenário poderá utilizar este campo: **(E1\_DECRESC)** e da mesma forma do exemplo acima informe este campo na posição: Valor Desconto.  
  
**Saiba mais  
MP - SIGAFIN - CNAB - Como configurar CNAB a Receber**[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Como configurar CNAB a Receber](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006976531-MP-SIGAFIN-CNAB-Como-configurar-CNAB-a-Receber)  
  
[How to | SIGAFIN | Remessa CNAB Contas a Receber FINA150 | #TOTVS\_Backoffice\_Linha\_Protheus](https://www.youtube.com/watch?v=KEzY7O79xlw)
