---
article_id: 360008920172
category: RH - Dissídio
content_hash: 2aff1756037adf60d5806642d8e08aa6cb0017abbfb146e2d230112b6cc284d1
fetched_at: '2026-06-28T22:43:43.404933+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - O que analisar quando sistema gera valores negativos
  para verbas de encargos no cálculo do dissídio retroativo
type: support-article
updated_at: '2025-08-20T12:30:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008920172-RH-Linha-Protheus-GPE-O-que-analisar-quando-sistema-gera-valores-negativos-para-verbas-de-encargos-no-c%C3%A1lculo-do-diss%C3%ADdio-retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34313965167767) Tempo aproximado para leitura: 00:00:30 min**

**Dúvida**O que analisar quando sistema gera valores negativos para verbas de encargos no cálculo do dissídio retroativo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Primeiramente verifique se toda parametrização necessária foi realizada, para isso consulte o manual do dissídio retroativo, através do *link* abaixo:  
[MANUAL GPE - Dissídio Retroativo](http://tdn.totvs.com/pages/releaseview.action?pageId=220889925)   
  
**Valores negativos de encargos provém de bases de cálculo atuais menores que as originais**, então confira se a base de cálculo atual está deixando de contemplar algum valor (confira o cálculo da época com o atual), para isso, valide se todas as verbas que na época do cálculo da folha faziam base para os encargos atualmente estão fazendo base para os encargos também:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10844759957783)

Valide também se todas as verbas que fazem base para os encargos e foram calculadas na folha estão sendo calculadas na rotina de dissídio, mesmo que essas não tenham que sofrer reajuste elas devem ser calculadas para não negativar os encargos.  
  
**Após verificação**, caso o erro persista, por gentileza nos envie as **evidências** abaixo (selecione um funcionário de exemplo para enviar as informações)  
  
- Cadastro do funcionários (pasta funcionais);  
- Cadastro do sindicato (pasta dissídio);  
- Acumulado GPEA120 (*print* de tela referente aos meses que estão com valores incorretos);  
- Parâmetros de cálculo completo (*print* de tela);  
- Relatório de dissídio da matricula de exemplo  
  
  
**Saiba mais**  
Para adquirir maior conhecimento acesse os *links* abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>
