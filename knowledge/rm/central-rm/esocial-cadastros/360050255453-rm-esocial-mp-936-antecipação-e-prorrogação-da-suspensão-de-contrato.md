---
article_id: 360050255453
category: eSocial - Cadastros
content_hash: 39ad4e958503c8606fd99e6fe0e857616b38c619d40cc8ae1ee3a73b8282e7bb
fetched_at: '2026-06-28T22:47:14.581885+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RM - eSocial - MP 936 -  Antecipação e prorrogação da suspensão de contrato
type: support-article
updated_at: '2021-03-31T16:49:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050255453-RM-eSocial-MP-936-Antecipa%C3%A7%C3%A3o-e-prorroga%C3%A7%C3%A3o-da-suspens%C3%A3o-de-contrato
---

**Dúvida**Como gerar informações ao eSocial sobre antecipação e prorrogação da suspensão temporária do contrato de trabalho (MP 936)?  
  
 **Ambiente**RM - eSocial - A partir dos *Patches*12.1.26.233, 12.1.27.203 e 12.1.28.125  
  
**Solução**   
Para enviar ao eSocial a antecipação ou prorrogação da suspensão temporária de trabalho, siga os passos abaixo:

1. No módulo **Folha de Pagamento,** acesse**Administração de Pessoal | Funcionários | Registro | B.E.M**e preecha o campo **Data da Antecipação** ou **Dias de Prorrogação** conforme a sua necessidade. O campo **Data Prorrogação BEM** deverá ser preenchido quando se tratar de prorrogação. O campo **Data do acordo** não deve ser alterado.

![teste.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098376174/teste.png)

2. Ainda no cadastro do funcionário, acesse o anexo **Históricos |****Histórico de Afastamento** e informe a nova data de término da suspensão. no campo **Data Fim Afastamento**;

![rrrrrrrrrr.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074552074/rrrrrrrrrr.png)

3. Caso ainda não tenha realizado a integração do S-2230 com a data anterior, após a alteração supracitada o status voltará para **Pendente**, sendo considerada na geração do XML a nova data de término da suspensão. Já se o evento tiver sido integrado anteriormente, será gerado um novo gatilho do S-2230 do tipo **Retificação**, ajustando a data de término da suspensão.

**Importante**  
O cadastro do B.E.M. poderá ser alterado de forma global (vários funcionários de uma vez), acessando o menu **Administração de Pessoal | Alteração Campos do Cadastro,**aplicando a seleção de funcionários e utilizando uma fórmula para alterar o campo desejado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075785734/mceclip0.png)

**Saiba Mais**  
Para maiores informações, acesse:

      • [Alteração Contratual para o eSocial referente a Prorrogação/Antecipação/Cancelamento - MP 936/2020](https://tdn.totvs.com/pages/releaseview.action?pageId=556391463#1-2)  
      • [MP 936 - Suspensão Temporária do Contrato de Trabalho](https://tdn.totvs.com/pages/releaseview.action?pageId=545621865)  
      • [S-2230 - Afastamento Temporário](https://tdn.totvs.com/pages/releaseview.action?pageId=364908488)
