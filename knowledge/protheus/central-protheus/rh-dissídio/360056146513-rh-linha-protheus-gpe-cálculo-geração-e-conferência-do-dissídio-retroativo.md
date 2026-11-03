---
article_id: 360056146513
category: RH - Dissídio
content_hash: cd2c6d4032391ad363dc766d899c22d8298164afe5ffc6f063d475049591c395
fetched_at: '2026-06-28T22:43:43.234136+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo, geração e conferência do dissídio retroativo
type: support-article
updated_at: '2025-08-07T15:04:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056146513-RH-Linha-Protheus-GPE-C%C3%A1lculo-gera%C3%A7%C3%A3o-e-confer%C3%AAncia-do-diss%C3%ADdio-retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34015509334423)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como realizar o cálculo, conferir e gerar o dissídio retroativo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**1. Realize as configurações prévias:  
[MP - GPE - Qual a configuração que antecede o cálculo do dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054351414-MP-GPE-Qual-a-configura%C3%A7%C3%A3o-que-antecede-o-c%C3%A1lculo-do-diss%C3%ADdio-retroativo?source=search)  
  
2. Para o cálculo o sistema vai utilizar informações do cadastro de funcionário\*, cadastro de sindicato e folha de pagamento fechada, que pode ser visualizada através do recibo de pagamento:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094188773)

**\*Importante:** ao efetuar o cálculo , o sistema faz a validação do campo SRA\_ANTEAUM (salário Base dissídio , se ele estiver alinhado com o Histórico salarial (tabela SR3/SR7). Caso ocorra alteração salarial posterior ao período calculado no dissídio, a rotina passa a enxergar qual o salário base para pagamento das diferenças conforme ordem cronológica do históricos salarial.   
**Exemplo:**   
Cadastro do funcionário - R$ 2.500,00 - Salário Base para dissídio R$ 2.500,00  
Histórico Salarial com alteração em 01/09/2023 - Salário base para dissídio 2.500,00  
Histórico Salarial até 01/08/2023 - R$ 2.000,00 - Salário base para dissídio  
Se for efetuado o cálculo de dissídio retroativo ´para a competência 08/2023, o reajuste será aplicado sobre os R$ 2.000,00 pois a rotina respeitará qual o salário base de dissídio para a época do reprocessamento.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094188973)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094189413)  
  
3. Cálculo do dissídio:  
Miscelânea/ Reajuste/ Dissidio Retroativo/ Calcular  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091984674)  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094193033)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094193593)  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094194013)  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091987194)  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094200113)  
  
4. Conferência de dissídio:  
Miscelânea/ Reajuste/ Dissidio Retroativo/ Outras ações/ Impressão  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094204613)  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094204633)  
  
A conferência dos valores de dissídio retroativo deve ser realizada através da impressão do relatório, pois somente nele existe a totalização das diferenças geradas. Esses valores apresentados na totalização e sinalizado na imagem são exatamente os valores que serão apresentados na folha de pagamento do funcionário.   
  
5. Geração do dissídio:  
Miscelânea/ Reajuste/ Dissidio Retroativo/ Outras ações/ Geração  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094203833)  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091996934)  
  
6. Valores mensais do funcionário:  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094204693)  
  
**Saiba Mais:**

[Artigos Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
