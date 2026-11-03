---
article_id: 115015809548
category: RH - Períodos de Apontamento
content_hash: 83440e88ff2f241d038c47a1fb0ecb99b22386e66cd7bf70dcf397f3a59746b7
fetched_at: '2026-06-28T22:44:45.125270+00:00'
product: protheus
section_id: 32419304439959
source: central-protheus
title: 'RH - Linha Protheus - PON - Período de ponto desconfigurado: como ajustar
  os parâmetros MV_PAPONTA e MV_PONMES'
type: support-article
updated_at: '2025-10-13T17:45:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015809548-RH-Linha-Protheus-PON-Per%C3%ADodo-de-ponto-desconfigurado-como-ajustar-os-par%C3%A2metros-MV-PAPONTA-e-MV-PONMES
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35601067186455) Tempo aproximado para leitura: 00:02:00 min**  
Dúvida**  
Como ajustar os parâmetros MV\_PAPONTA e MV\_PONMES no cadastro de períodos de apontamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O período do ponto fica desconfigurado quando mostra em 4 campos ao consultar no Período de Apontamentos em Modificar período > Apenas visualizar.   
  
Isto geralmente ocorre quando o período é alterado manualmente e não foi seguido a parametrização abaixo para deixá-lo configurado de forma correta. Caso seu período seja o mês completo, exemplo de 21/02 a 20/03 o parâmetro MV\_PAPONTA deve ser configurado como 21/20.  
  
Para ajustar o período, é necessário realizar o passa a passo abaixo em **Atualizações > Cadastro do Ponto >  Períodos de Apontamentos**:  
  
1. **Modif. Per. Apont. - Dia Inicial/ Final - Salvar**: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/31469975021463)**

2. No campo em destaque abaixo, informar o período do ponto, **ex: 21/20** e salvar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31469975023639)

3. Informar o último dia do período do ponto atual e clicar em **Ok**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31469997718551)

4. O período **foi alterado com sucesso** – mensagem apenas de alerta para reapontar o novo período:![](https://centraldeatendimento.totvs.com/hc/article_attachments/31469975025687)

5. Conferir se ficou correto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31469975028119)

6. Período deve mostrar o **MV\_PAPONTA e MV\_PONMES** em somente 3 campos, conforme abaixo:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31469997724695)

**IMPORTANTE**: Na tela inicial da rotina de períodos de apontamentos obrigatoriamente deverá ter somente períodos fechados. Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31469975029655)

**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
