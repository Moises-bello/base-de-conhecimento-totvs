---
article_id: 360010863672
category: Folha Mensal
content_hash: 972503de17b123f22345a16c4db01cd340a815e285106baf07b6521c1cce63c7
fetched_at: '2026-06-28T22:47:00.309706+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RM - FOP - Parametrização do INSS empresa na folha analítica
type: support-article
updated_at: '2025-02-27T17:45:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010863672-RM-FOP-Parametriza%C3%A7%C3%A3o-do-INSS-empresa-na-folha-anal%C3%ADtica
---

**Dúvida**Como parametrizar o percentual do INSS empresa na geração do relatório de folha analítica?  
  
**Ambiente**RM - Folha de pagamento - Todas as versões  
  
**Solução**O campo INSS empresa é o imposto relacionado a base da folha de pagamento que normalmente é 20% do total das remunerações pagas.  
Durante a geração da folha analítica é necessário informar o percentual de recolhimento do INSS empresa no campo **% Empresa**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30285912380695)  
  
Se na seleção de coligadas seja habilitado a parâmetro **Utiliza parâmetros específicos** é necessário informar o percentual novamente nesta tela, no campo **% Empresa**, conforme abaixo:  
  
![Tela2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008439871)

**Observação:** Se mesmo com as parametrizações acima o INSS empresa não for calculado, acesse em **Administração de pessoal | Cadastros globais | Coligadas**, acesse o cadastro da coligada onde ocorre a divergência e verifique se a flag **Produtor rural** está habilitada:

![flag.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042640834)

Com esta flag habilitada, o sistema não irá calcular o INSS empresa no relatório.   
  
Atualmente é necessário também verificar se o campo "Habilita histórico de INSS no cadastro de seção" está marcado, no caminho: **Configurações | Parametrizador | Folha normal | Encargos Sociais:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23454920658455)

Caso esse campo esteja marcado é necessário verificar dentro do cadastro da seção centralizadora, no caminho: Anexos | Histórico de percentuais para INSS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23454912105239)

Se os percentuais estão devidamente preenchidos, no caso da empresa deve estar preenchido no campo a baixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23454912120727)

**Saiba mais**

**[RH - RM - FOP - Folha Analítica: cadastro e parametrização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416042752151-RH-RM-FOP-Folha-Anal%C3%ADtica-cadastro-e-parametriza%C3%A7%C3%A3o)**
