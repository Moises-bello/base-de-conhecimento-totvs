---
article_id: 17734289158935
category: RH - Benefícios
content_hash: 8df0de568d7dd3eb9735326507b0f9cbde22b24c0c3003b4a633a59085373cf1
fetched_at: '2026-06-28T22:44:03.399322+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE -  Ao tentar realizar o processo de Cálculo dos benefícios
  VT/VR/VA é apresentado log de cálculo informando que foi calculado, porém o cálculo
  fica zerado
type: support-article
updated_at: '2025-09-05T19:13:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17734289158935-RH-Linha-Protheus-GPE-Ao-tentar-realizar-o-processo-de-C%C3%A1lculo-dos-benef%C3%ADcios-VT-VR-VA-%C3%A9-apresentado-log-de-c%C3%A1lculo-informando-que-foi-calculado-por%C3%A9m-o-c%C3%A1lculo-fica-zerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17734298245527) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao tentar realizar o processo de Cálculo dos benefícios VT/VR/VA é apresentado log de cálculo informando que foi calculado, porém o cálculo fica zerado. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733347645207)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733382769943)**

**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da release 12.1.2310.   
  
**Causa**Esse incidente ocorre, pois a pergunta **Complemento HE** nos parâmetros do cálculo de **VT/VR/VA** está preenchida com **Sim**. Dessa forma o sistema busca informações da tabela **S151 - Complemento de Benefícios**, como não existe informações de preenchimento na tabela, o cálculo é gerado em branco.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733474125335)  
  
**Solução**Para solucionar essa ocorrência, realize novamente o cálculo dos benefícios **VT/VR/VA** preenchendo a pergunta **Complemento HE** com **Não**.   
  
**1.** Acesse a rotina Cálculo em **Atualizações>** **Benefícios> VT/VR/VA> Cálculos.**  
**2.** **Preencha** os parâmetros para cálculo deixando a pergunta **Complemento HE** com **Não**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733662044311)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733680373143)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733681869207)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733688406935)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733702008855)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733701576727)  
  
  
3. Verifique o cálculo na rotina de **Atualizações de Vales** em **Atualizações> Benefícios> VT/VR/VA> Atualização**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17733756550551)

**Saiba Mais**

[Complemento de Beneficios VT/VR/VA por horas extras](https://tdn.totvs.com/pages/viewpage.action?pageId=776129138)  
[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029037011-RH-Linha-Protheus-GPE-Como-Cadastrar-e-Calcular-o-Vale-Transporte?source=search)  
[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Refeição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028852992-RH-Linha-Protheus-GPE-Como-Cadastrar-e-Calcular-o-Vale-Refei%C3%A7%C3%A3o?source=search)  
[RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028910152-RH-Linha-Protheus-GPE-Cadastro-e-C%C3%A1lculo-do-Vale-Alimenta%C3%A7%C3%A3o?source=search)
