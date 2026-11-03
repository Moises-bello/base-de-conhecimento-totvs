---
article_id: 360057999794
category: MDT - PCMSO
content_hash: a396c3b6032ba786dc3fffcc080317bf9e7af9977849c52a75f30c66ec00e411
fetched_at: '2026-06-28T22:44:28.326043+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Aviso O Funcionário XXXX não possui exames antes
  da data de inicio da programação para usar como referência ao gerar programação
  de exame (MDTA190)
type: support-article
updated_at: '2025-09-03T14:03:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057999794-RH-Linha-Protheus-MDT-Aviso-O-Funcion%C3%A1rio-XXXX-n%C3%A3o-possui-exames-antes-da-data-de-inicio-da-programa%C3%A7%C3%A3o-para-usar-como-refer%C3%AAncia-ao-gerar-programa%C3%A7%C3%A3o-de-exame-MDTA190
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27598273517463)**Tempo aproximado para leitura: 00:01:00 min **Dúvida**O que verificar quando ao gerar a programação de exames rotina (MDTA190) apresentar a mensagem:" O Funcionário XXXXXXX não possui exame antes da data de inicio da programação para usar como referência. Informe a data em que os primeiros exames dele serão programados.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098360014)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Por regra do produto o sistema sempre irá considerar a **data do resultado do exame anterior** e assim aplicar os meses definidos na faixa  periódica,  para então retornar com a **data do resultado**.

**Exemplo 1:**  
Tenho o exame hemograma  realizado com data de resultado em 02/08/2020.  
Na minha programação anual (12 meses) o exame de hemograma vira com data 02/08/2021.  
Ou seja pega a data do resultado anterior e aplica a faixa definida no meu caso 12 meses.

**Exemplo 2:**  
Não tenho nenhum exame realizado e consequentemente nenhuma data de resultado.   
Ao realizar a programação o sistema irá apresentar uma mensagem " O Funcionário XXXXXXX não possui exames antes da data de inicio da programação para usar como referência. Informe a data em que os primeiros exames dele serão programados. Caso a data de referência não for preenchida, será considerada a data de Vencimento do exame Médico, se este não estiver preenchido será considerada a Data de Admissão do Funcionário."

Caso não queira que seja gerado desta forma na programação  poderá utilizar o campo **(TMW\_BASEDT)** igual a "**data informada**" e no campo **(TMW\_DTREFE)** informe a data desejada. Sistema ira ignorar os exames já realizados e criara exame a partir da data informada. **(TMW\_DTREFE)**.  
  
Diferente disto apenas customizando o produto.  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos PCMSO](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945214-MDT-PCMSO)
