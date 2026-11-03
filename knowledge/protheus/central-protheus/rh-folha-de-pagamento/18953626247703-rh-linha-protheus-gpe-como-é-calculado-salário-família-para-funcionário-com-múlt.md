---
article_id: 18953626247703
category: RH - Folha de Pagamento
content_hash: 4799963a077c030e9ea518147a1beb5ed9184f2004f8e39d1c7138696fa3a2af
fetched_at: '2026-06-28T22:44:13.388875+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como é calculado Salário Família para funcionário
  com Múltiplos Vínculos
type: support-article
updated_at: '2024-09-05T18:07:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18953626247703-RH-Linha-Protheus-GPE-Como-%C3%A9-calculado-Sal%C3%A1rio-Fam%C3%ADlia-para-funcion%C3%A1rio-com-M%C3%BAltiplos-V%C3%ADnculos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18953642788631) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como é calculado Salário Família para funcionário com Múltiplos Vínculos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.

**Solução**Para múltiplos vínculos que possuem salário família, o cadastro do dependente deverá ocorrer em todos os vínculos, porém a informação se é dependente ou não do salário família (Campo **RB\_TIPSF** e **RA\_DEPSF**) deverá ser informado apenas no **último vínculo a ser calculado**, para que o sistema possa calcular a base total e verificar o direito ou não ao recebimento.  
  
**Exemplo:**- Funcionário com dois vínculos, a informação do salário família deve ser inserida apenas na última matrícula a ser calculada, neste caso a **000955**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18953618137879)  
  
- Cadastro do funcionário, aba **Benefícios**, campo **RA\_DEPSF:  
Matrícula 000226:****![](https://centraldeatendimento.totvs.com/hc/article_attachments/18954254500247)**

**Matrícula 000955:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18954250136343)**

Cadastro do dependente, campo **RB\_TIPSF**: **Matrícula 000226:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18954250143127)**

**Matrícula 000955:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18954250154519)**

**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[Novo Cálculo MULTV - Multiplos Vinculos - DR](https://tdn.totvs.com/pages/releaseview.action?pageId=552575179)
