---
article_id: 7221979681303
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: f4c8985a07878e30e3f3e19553c935b85c23018388f86cfdd82ac7bd3f6c59bd
fetched_at: '2026-06-28T22:40:54.184279+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA020 - Erro ManagerialAccountingEntityPolicy
type: support-article
updated_at: '2023-11-14T15:18:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7221979681303-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Erro-ManagerialAccountingEntityPolicy
---

**Ocorrência**Ao cadastrar ou alterar uma conta contábil via **CTBA020** quando possui **integração EAI** da mensagem **AccountantAccount** do Protheus para outro produto(exemplo RM), temos a mensagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7220834242839/mceclip1.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - A partir da versão 12  
  
**Causa**A mensagem acontece pois o outro produto TOTVS está exigindo o envio da tag **ManagerialAccountingEntityPolicy** dentro do XML que o Protheus está encaminhando, mas o Protheus não está enviando-a.

Essa Tag é referente a **entidade adicional** no Protheus, podendo ser da **05 até a 09**, conforme explica a documentação: [Cross Segmento - Backoffice Linha Protheus - SIGACTB - Entidades adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013316351-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Entidades-adicionais?source=search)

**Solução**Primeiramente o cliente precisará verificar se possui entidade adicional em seu ambiente, caso não possua deverá contatar o suporte do outro produto para verificar o motivo da exigência da Tag **ManagerialAccountingEntityPolicy** e saber se a mesma cabe ao negócio do cliente ou se precisa retirar a obrigatoriedade da mesma.

Agora caso o cliente deseje que o Protheus envie na mensagem EAI a Tag **ManagerialAccountingEntityPolicy**, deverá realizar os passos abaixo:

**Passo 1:** Garanta que os campos da entidade adicional desejada estejam criados em seu ambiente e que ela esteja cadastrada em sua tabela CT0.

Se não estiver precisará rodar o Wizard **U\_CTBWIZENT** para a criação dos componentes.

Para criar novas entidades contábeis:

1. Acesse a tela de abertura do Protheus Remote e informe no campo **Programa inicial**, **U\_CTBWIZENT**.
2. O Sistema exibe a tela com as orientações para execução da rotina. Clique em **Avançar**.
3. Informe:

* A quantidade total de Entidades para criação.
* A numeração da primeira entidade.
* Os módulos para criação dos campos

|  |
| --- |
| ***Importante:***  Os módulos indicados para criação dos campos não podem ser alterados posteriormente. |

     4. Clique em **Avançar**.

     5. Confira e confirme a parametrização da(s) nova(s) entidade(s).

     6. Clique em **Avançar**.

     7. O Sistema cria a(s) nova(s) entidade(s) e exibe os campos criados.

     8. Clique em **Finalizar**.

**Passo 2:**Preencha o parâmetro **MV\_CTBCGER** indicando uma entidade adicional desejada. O conteúdo do parâmetro pode ser de 05 até 09, mas ao preencher por exemplo com o conteúdo 05, os campos da entidade adicional 05 devem estar criados e o cadastro da entidade adicional deverá estar na CT0 senão a TAG não será gerada.

Definição do parâmetro **MV\_CTBCGER**:

![](https://totvssuporte.zendesk.com/attachments/token/uLBA27WlTJRrxlc5mLdPfovqR/?name=inline-538510608.png)  
 

**Passo 3:**Inclua ou altere a conta contábil normalmente e veja se a Tag ManagerialAccountingEntityPolicy será gerada.
