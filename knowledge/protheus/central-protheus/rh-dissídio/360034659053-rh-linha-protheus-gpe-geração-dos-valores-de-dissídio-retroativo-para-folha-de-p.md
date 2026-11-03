---
article_id: 360034659053
category: RH - Dissídio
content_hash: e846e243eb20c1c2420c496094fc39442fd2a00628686204f434a77b4036a858
fetched_at: '2026-06-28T22:43:43.592334+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Geração dos valores de dissídio retroativo para
  folha de pagamento
type: support-article
updated_at: '2021-04-30T00:23:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034659053-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-dos-valores-de-diss%C3%ADdio-retroativo-para-folha-de-pagamento
---

**Dúvida**Como gerar valores do cálculo de dissídio retroativo para folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Após calcular o dissídio retroativo e conferir os valores, será necessário gerar as diferenças para folha de pagamento, conforme passo a passo abaixo:  
  
**1.** Na rotina Dissidio Retroativo, clique em >Outras Ações >Geração:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091686894/mceclip0.png)  
  
**2.** Na tela abaixo, clique em Perguntas:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093846873/mceclip1.png)  
  
**3.** Preencha as perguntas abaixo de acordo com os parâmetros do seu cálculo e sua necessidade de geração:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044153214/mceclip1.png)  
  
- Quando desejar parcelar o valor da diferença de dissidio, deve-se preencher o campo **Número de Parcelas e Atualiza Lançamentos** com conteúdo igual a **Lançamentos Futuros.** Dessa maneira o sistema carregará as parcelas e seus valores para tabela SRK, e após cálculo da folha de pagamento os valores serão migrados para SRC.- Para pagamento em uma única vez, o campo **Número de Parcelas** deve ficar com **1** e o campo **Atualiza Lançamentos** com conteúdo igual a **Mensais**. Assim o sistema lança os valores para tabela RGB e após calcular a folha de pagamento, serão levados para SRC.  
  
- Utilizar o campo **Atual. Histor. Salar**. para atualizar os campos de salário na **SRA** (RS\_SALARIO e RA\_ANTEAUM).  
  
**4.** Confirme os parâmetros e clique no botão abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091687014/mceclip2.png)  
  
Sistema gerará os valores do dissídio para a Folha de Pagamento, conforme parâmetros preenchidos.  
  
**OBS.: Após gerar os valores do dissidio para a folha, não é possível desfazer esse processo. Portanto, é de extrema importância que os valores sejam conferidos corretamente antes dessa geração para a folha.**  
  
  
**Saiba mais:** [MANUAL GPE - Dissídio Retroativo](https://tdn.totvs.com/pages/releaseview.action?pageId=220889925)  
[MP - GPE - Exclusão do cálculo de dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037259774-MP-GPE-Exclus%C3%A3o-do-c%C3%A1lculo-de-diss%C3%ADdio-)
