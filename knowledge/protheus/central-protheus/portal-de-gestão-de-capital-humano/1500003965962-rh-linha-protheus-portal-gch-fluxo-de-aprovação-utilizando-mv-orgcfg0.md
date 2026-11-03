---
article_id: 1500003965962
category: Portal de Gestão de Capital Humano
content_hash: fb8b8d7588a74f64f8ca54dd39bd4a3751298aa3a286e3f9e753f156d86a443f
fetched_at: '2026-06-28T22:43:00.062162+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Fluxo de aprovação utilizando MV_ORGCFG=0
type: support-article
updated_at: '2021-04-07T12:37:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003965962-RH-Linha-Protheus-PORTAL-GCH-Fluxo-de-aprova%C3%A7%C3%A3o-utilizando-MV-ORGCFG-0
---

**Dúvida**Como configurar o Fluxo de aprovação utilizando **MV\_ORGCFG=0**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão Capital Humano – Todas as versões  
  
**Solução**Importante ressaltar que quando o conteúdo do parâmetro **MV\_ORGCFG =0**, no cadastro de departamento (**CSAA100**), deve ser apontado a, **Matricula Responsável** e **Departamento Superior** , apenas no ultimo nível, quando não houver superior aquela aprovação deve ter o campo departamento superior em Branco, qualquer informação indevida em seu cadastro poderá comprometer a chave de busca, utilizada no fluxo de aprovação. Entendendo o conceito do sistema poderá ser aplicada para a montagem hierárquica, conforme necessidade da empresa.  
   
Ire demonstrar a composição de um exemplo simples onde: o  **Funcionário** solicita, direcionar ao **Líder** do departamento ( **matricula responsável**), e após aprovação direciona ao **Superior** deste Líder, (**Departamento Superior**).  
  
No módulo 07 (**SIGAGPE**), acesse: **Atualizações > Cadastro > Departamento.**Em meu exemplo definirei o Departamento de Código 000000001 Superior ao Departamento de Código 000000002.  
  
Todas as matriculas alocadas no Departamento **000000002** - **DEP RH** - Irão fazer parte na composição da equipe, sendo subordinados da matricula apontada como responsável, no meu exemplo matrícula: **000002 - Líder.**Por sua vez esta matricula responsável, deve estar alocada no departamento apontado como superior.  
  
Todas as matriculas alocadas no Departamento **000000001 - DEP. SUP. GERENCIA** - Irão fazer parte na composição da equipe, sendo subordinados da matricula apontada como responsável, no meu exemplo matrícula **000004 - Gerente.**  
**1.** Acesse o cadastro do **Departamento Superior** e Defina uma **Matricula Responsável**. (Neste exemplo este será meu ultimo nível de aprovação portanto neste cadastro o meu campo Departamento Superior permanecerá em branco).   
Importante ressaltar que todas as matriculas alocadas neste departamento, serão subordinados da Matricula responsável apontada, compondo assim sua equipe.  
  
**2.** Acesse o(s) departamento(s) conforme necessidade estrutural da empresa e preencha os campos necessários para correta montagem de busca sendo: Matricula responsável e departamento superior.  
Importante ressaltar que todas as matriculas alocadas neste departamento, serão subordinados da Matricula responsável apontada, compondo assim sua equipe.  
  
Exemplo de cadastro:  
  
![CW1FPz39DO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004615441/CW1FPz39DO.gif)  
  
Os as matriculas responsáveis apontadas no cadastro de departamento ao acessar o portal deverá visualizar sua equipe.  
**Matricula 000002 - Líder,** visualiza sua equipe, e visualiza seu superior em seu cadastro**.**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004617221/mceclip1.png)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103287114/mceclip2.png)  
  
**Matricula 000004- Gerente,** visualiza sua equipe, e não visualiza seu superior pois não existe pessoa superior a ele na definição estrutural.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103287234/mceclip3.png)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004476182/mceclip4.png)

Neste exemplo usarei a solicitação de Justificativa Pré Abono, para desenhar o fluxo de aprovação no portal. Entendendo o conceito do sistema poderá ser aplicada para qualquer solicitação.  
  
![51TNuoIt4r.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004476842/51TNuoIt4r.gif)  
  
**Saiba Mais**  
[Artigos Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano#)
