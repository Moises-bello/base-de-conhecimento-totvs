---
article_id: 1500001532761
category: RH - PPP ( Perfil Profissiográfico Previdenciário)
content_hash: 681f0ce738979d3a434f982bfea7c6637245835f82dfe0b2e22a263105709e06
fetched_at: '2026-06-28T22:43:25.094975+00:00'
product: protheus
section_id: 360011909673
source: central-protheus
title: RH - Linha Protheus - GPE - PPP - Campo 14.2 - Descrição de Atividades do PPP
type: support-article
updated_at: '2025-07-17T11:55:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001532761-RH-Linha-Protheus-GPE-PPP-Campo-14-2-Descri%C3%A7%C3%A3o-de-Atividades-do-PPP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22711299289623) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Qual é a origem das informações do campo 14.2 - Descrição de Atividades do PPP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**As informações são extraídas do campo **Ds. Detalhada** - **Q3\_MEMO1**, disponível na rotina de **Cargos - GPEA370:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001507522)  
  
  
É necessário que o cargo esteja **atrelado ao Funcionário:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001561621)

No cadastro de funções, selecione **Sim** nos campos **Impr no PPP** - **PRJ\_PPPIMP** e **Func. Líder -** **RJ\_LIDER:**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001561761)  
  
  
Após os cadastros, gere os dados do PPP em **Atualizações > PPP - Perfil Profissiográfico Previdenciário** > **Período Profissiográfico (****GPEA360) >** **Gerar Dados:**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100398534)  
  
  
Faça a parametrização conforme necessidade e confirme:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22717492346519)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22717492373271)  
  
  
Ao final da geração, selecione o Funcionário e clique em **Manutenção,** será apresentada a tela com a função e cargo da matricula selecionada:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001508542)  
  
  
Em seguida, acesse **Atualizações > PPP - Perfil Profissiográfico Previdenciário > Impressão PPP** - **GPERPPP** e preencha os parâmetros de acordo a necessidade;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22717482267927)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22717482285463)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22717492424599)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22717492436631)  
  
  
As informações de **Descrição das Atividades** serão exibidas no campo **14.2:**  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102572473)  
  
  
**Saber Mais:**[RH - Linha Protheus - GPE - Como incluir o logo do INSS no PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14464011287063-RH-Linha-Protheus-GPE-Como-incluir-o-logo-do-INSS-no-PPP?source=search)  
[RH - Linha Protheus - GPE - Ao imprimir o PPP, não é levado as informações do bloco 13 - Lotação e Atribuição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053018434-RH-Linha-Protheus-GPE-Ao-imprimir-o-PPP-n%C3%A3o-%C3%A9-levado-as-informa%C3%A7%C3%B5es-do-bloco-13-Lota%C3%A7%C3%A3o-e-Atribui%C3%A7%C3%A3o?source=search)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
