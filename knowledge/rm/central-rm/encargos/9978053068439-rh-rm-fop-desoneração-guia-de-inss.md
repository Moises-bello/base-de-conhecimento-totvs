---
article_id: 9978053068439
category: Encargos
content_hash: 3e476ec0200796b1ad5015e447a586a1517a90e9d39e40b85c1deddfca9f1c23
fetched_at: '2026-06-28T22:46:52.406902+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Desoneração Guia de INSS
type: support-article
updated_at: '2025-03-11T10:37:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9978053068439-RH-RM-FOP-Desonera%C3%A7%C3%A3o-Guia-de-INSS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como fazer desoneração da Guia de INSS?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Foi criado a tela de cadastro **Parâmetros da Guia de INSS Desoneração** disponível na geração da Guia de INSS, que deve ser abastecida antes da sua geração para empresas que possuem o percentual redutor para aplicar no campo parte empresa da guia.

Portanto acesse: Encargos | Guia de INSS | Parâmetros da Guia de INSS Desoneração

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977731084183)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977836087703)

Na tela acima devem ser informados os valores da receita bruta com desoneração e receita bruta de demais atividades. O percentual redutor será calculado automaticamente com base nestes valores. O cálculo será realizado conforme abaixo:

**PercentualRedutor = (ReceitaBrutaDemaisAtividades /( ReceitaBrutaDemaisAtividades + ReceitaBrutaDesoneracao)) \* 100**

**Importante:** Caso o valor do campo receita bruta de demais atividades esteja zerado e o campo receita bruta com desoneração for informado, o campo parte Empresa da Guia de INSS será zerado.

Uma vez informados os valores acima, o recolhimento da parte empresa será feito da seguinte forma:

a) O recolhimento referente à receita bruta com desoneração deverá ser feito através de relatório DARF com código 2985.

b) O recolhimento referente à receita bruta das demais atividades será feito na própria GPS, utilizando para isto o percentual redutor calculado acima.

Na guia de INSS foi criado o parâmetro

**Utilizar percentual redutor (Lei 12.546/2011)’**para correto cálculo da parte empresa. O parâmetro **Por filial** busca os valores do novo cadastro de acordo com a quebra de CNPJ.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977831430807)

O parâmetro **Por Empresa** busca o valor do novo cadastro de acordo com a seção informada na guia. O percentual definido na Empresa informada será utilizado para as demais Empresas.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977859723927)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9977934663703)

**Saiba mais:**  
[Desoneração Guia de INSS](https://tdn.totvs.com/pages/releaseview.action?pageId=118883664)
