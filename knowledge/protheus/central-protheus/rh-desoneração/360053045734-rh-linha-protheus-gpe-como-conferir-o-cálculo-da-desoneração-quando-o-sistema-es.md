---
article_id: 360053045734
category: RH - Desoneração
content_hash: 6e6c49fee45b84cf2b369d9e621f282b79f259fd4a88747ed8fbf50b7b2215bc
fetched_at: '2026-06-28T22:43:42.172285+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir o cálculo da desoneração quando o
  sistema está definido para ratear o INSS sobre Faturamento ID 0973 no cálculo do
  funcionário
type: support-article
updated_at: '2023-04-14T20:52:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053045734-RH-Linha-Protheus-GPE-Como-conferir-o-c%C3%A1lculo-da-desonera%C3%A7%C3%A3o-quando-o-sistema-est%C3%A1-definido-para-ratear-o-INSS-sobre-Faturamento-ID-0973-no-c%C3%A1lculo-do-funcion%C3%A1rio
---

**Dúvida**Como conferir o cálculo da desoneração quando o sistema está definido para ratear o INSS sobre Faturamento ID 0973 no cálculo do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**O sistema irá ratear o valor do ID 0973 por funcionário na folha de pagamento quando o parâmetro **MV\_RAT0973** estiver habilitado:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088864673/mceclip0.png)

Para calcular o valor do ID 0973 rateado por funcionário (valor individual) na folha de pagamento, o Sistema utiliza a seguinte fórmula:

**Valor ID 0318 Funcionário / Valor ID 0318 Total do Resumo \* Valor Total ID 0973**

Conferencia da folha na verba com ID 0973, após executar a desoneração:  
  
- Resumo da folha  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087842794/mceclip2.png)

- Folha individual por funcionário  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087842934/mceclip3.png)

**Regra de cálculo:  
Valor ID 0318 Funcionário / Valor ID 0318 Total do Resumo \* Valor Total ID 0973**  
Valor ID 0318 Funcionário = 1800,00  
Valor ID 0318 Total do Resumo = 5.400,00  
Valor Total ID 0973 = 2.521,41  
  
Então temos o cálculo abaixo:**1.800,00 / 5.400,00 \* 2.521,41 = 840,47****IMPORTANTE:** Caso o valor apresentado na verba com ID 0973 rateado por funcionário esteja errado, deve-se atentar nas categorias informadas na geração da desoneração GPEM013. Só devem ser consideradas  no cálculo as categorias que possuem contribuição previdenciária. O estagiário é uma categoria que não possui recolhimento de INSS, mas se estiver na seleção da geração da desoneração, ele será considerado para o rateio, fazendo com que o valor fique errado entre os funcionários.

A distribuição/rateio da desoneração por matricula não é obrigatória por lei, o parâmetro MV\_RAT0973 foi apenas uma melhoria, para ter a ideia do calculo por matricula dos funcionários (clt, pró-labore e etc). Assim não existe um embasamento legal para ratear para funcionário ou contribuinte individual.   
  
**Saiba mais:**  
Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:  
[RH - Linha Protheus - GPE - Qual o processo completo da Desoneração da Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053866933-RH-Linha-Protheus-GPE-Qual-o-processo-completo-da-Desonera%C3%A7%C3%A3o-da-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Como ratear o valor da desoneração entre os funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008542221)  
[RH - Linha Protheus - GPE - Como não levar os estagiários no calculo da desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049998474)
