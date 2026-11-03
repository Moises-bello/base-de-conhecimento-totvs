---
article_id: 360004090071
category: eSocial - Cadastros
content_hash: 8beecc028a141323a8c6f7692c8054ada3a2cce3d3b9fba052546bad29930624
fetched_at: '2026-06-28T22:47:14.568043+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Zerar líquido da rescisão no eSocial
type: support-article
updated_at: '2024-06-17T12:35:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004090071-RH-RM-FOP-eSocial-Zerar-l%C3%ADquido-da-rescis%C3%A3o-no-eSocial
---

**Dúvida**Como zerar o líquido da rescisão com o código de cálculo **150 - Liquido da Rescisão** no eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O evento de código de cálculo [**150 - Liquido da Rescisão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415374884887-RH-RM-FOP-Lan%C3%A7amento-de-Liquido-de-Rescis%C3%A3o?source=search) tem um tratamento especial e diferente de outros eventos do tipo desconto pois, apesar de ser um desconto, deverá ser desconsiderado para envio ao eSocial.

Assim, siga os procedimentos abaixo para zerar o líquido da rescisão e enviar corretamente os eventos ao eSocial:  
1 Acesse **Configurações | Parametrizador | eSocial | Eventos a Desconsiderar** e inclua o evento com o código de cálculo 150;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043508753/mceclip0.png)

2. Após calcular a rescisão do funcionário, acesse **Rescisão | Lançamento do Líquido** para lançar o evento na movimentação;  
3. Após, gere normalmente o XML do **S-2299** para transmissão ao governo.  
  
**Saiba mais**  
Acesse os links abaixo para mais informações:  
   • [Código de Cálculo 150 - Zerar Rescisão](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452718710)  
   • [Diferença Processo de Rescisão Complementar - Retificação de Rescisão e Acordo Coletivo](http://tdn.totvs.com/pages/viewpage.action?pageId=419535691)
