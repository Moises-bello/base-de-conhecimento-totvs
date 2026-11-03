---
article_id: 360049998474
category: RH - Desoneração
content_hash: 8a3e33590449cf407ebc05272c30b48087cfdb22a1ad2ed8bbaabe79ec65b429
fetched_at: '2026-06-28T22:43:42.180788+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Como não levar os estagiários no calculo da desoneração
type: support-article
updated_at: '2025-08-06T20:20:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049998474-RH-Linha-Protheus-GPE-Como-n%C3%A3o-levar-os-estagi%C3%A1rios-no-calculo-da-desonera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33987060420759) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como não considerar os estagiários ou categorias que não tenham recolhimento de INSS Empresa no calculo da desoneração da folha de pagamento?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**No Sistema, quando é calculada a desoneração da folha rateada por matricula é utilizada a seguinte formula :

Valor ID 0318-Base funcionário / Valor ID 0318-Base Total empresa \* desoneração total-Tabela S033 Coluna Contribuição Devida =  Valor ID 0973 por matricula no cálculo da folha. 

Pode ocorrer o erro de levar indevidamente os **estagiários** nessa formula, pois ele **possui o ID 0318** no seu calculo, porém o estagiário não tem recolhimento de INSS Empresa**,** ou seja, o ID 0973 não será rateado para essa matricula de Estagiário, mas será utilizado o valor da verba de ID 0318 do estagiário indevidamente.

Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Para que os estagiários ou categorias que não tenham recolhimento de INSS Empresa não sejam considerados no cálculo da Desoneração, na pergunta **Categorias a Gerar** não selecione as categorias em questão.  
No exemplo abaixo, não foi selecionada as categorias de estagiários, dessa forma o Sistema não vai usar o valor da Base salario ID 0318 da matricula de estagiário para compor a formula do rateio:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013468901)

**Saiba Mais**

[RH - Linha Protheus - GPE - Como conferir o cálculo da desoneração quando o sistema está definido para ratear o INSS sobre Faturamento ID 0973 na folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053045734)

[RH - Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)
