---
article_id: 360028234934
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a9d6188e87e0aa2399fc158d6c003b79a6ec25831a16e7bcae1531fe00013838
fetched_at: '2026-06-28T22:42:45.690039+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento de campos com o configurador
  de produtos
type: support-article
updated_at: '2021-08-13T11:12:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028234934-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-de-campos-com-o-configurador-de-produtos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min**  
**Dúvida**Ao utilizar o **MATA093 - Configurador de Produtos**, é possível fazer com que outros campos além de **B1\_COD - Código**, **B1\_DESC - Descrição**, **B1\_TIPO - Tipo**, **B1\_UM - Unidade** e **B1\_LOCPAD - Armazem Pad** sejam preenchidos?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para preencher outros campos além dos quatro descritos acima execute os passos abaixo:  
1. Acesse a rotina **MATA093**, selecione a **Família** e clique em **Alterar**;  
2. Altere o conteúdo do campo **BP\_CAMPAD - Campo Pad**. para **Não**, salve o cadastro e saia desta tela;  
3. Selecione novamente a **Família** e em **Ações Relacionadas** selecione **Descrição**;  
4. Na coluna **BY\_CAMPO - Campo** informe o nome do campo a ser preenchido e na coluna **BY\_EXPRESS** - **Expressão** informe o conteúdo a ser preenchido no campo, podendo esse campo ser preenchido com um conteúdo texto ou ser resultado da composição de variáveis sugeridas na tela. Nesse processo deve-se informar também o conteúdo a ser preenchido nos campos **B1\_DESC, B1\_TIPO, B1\_UM e B1\_LOCPAD**.
