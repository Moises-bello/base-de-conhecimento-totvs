---
article_id: 360052099654
category: RH - Dissídio
content_hash: bf3fdae38a2cd69def5440d2e303c66cf6c5109304ef96240642e806ccbfaa81
fetched_at: '2026-06-28T22:43:43.515518+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo do dissídio utilizando base de Horas Mensal
  errada
type: support-article
updated_at: '2024-04-01T21:04:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052099654-RH-Linha-Protheus-GPE-C%C3%A1lculo-do-diss%C3%ADdio-utilizando-base-de-Horas-Mensal-errada
---

**Ocorrência**Ao calcular o dissídio o sistema utiliza base de HORAS MENSAL de 220 horas, porém no cadastro do funcionário está configurado sobre 180 horas.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - A partir da versão 12.  
  
**Solução**Para o cálculo do dissídio o sistema verifica os dados contidos no Cadastro do Funcionário (tabela SRA) e tabela SR9, onde se tiver conteúdo ou datas diferentes entre o período do cálculo e tabela SR9 dará divergência.  
  
No exemplo abaixo nota-se que houve duas alterações no campo R9\_HRSMES e no cadastro do funcionário está sobre 180 horas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084890573/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083723514/mceclip1.png)  
Para o cálculo da folha de pagamento o sistema valida o cadastro do Funcionário (tabela SRA), mas para o dissídio olha as informações das duas tabelas, o correto é manter na SR9 o ultimo registro com a alteração devida, se foi alterado para 220 a partir de 01/05/2020 no cadastro do Funcionário (tabela SRA) deve conter a mesma informação, ficando também com 220, ou vice e versa.
