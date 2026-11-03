---
article_id: 360005090232
category: SIGAEST - PODER DE TERCEIROS
content_hash: c46d68fd942647c685c5b99febf0b5d49ecee800f171bd84f530e47ed374ede8
fetched_at: '2026-06-28T22:39:03.119127+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar o Controle
  de Poder De/Em Terceiros?
type: support-article
updated_at: '2026-06-03T14:16:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005090232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-Controle-de-Poder-De-Em-Terceiros
---

O Protheus permite controlar o poder de terceiros em movimentações de estoque entre empresas via documentos MATA103 e MATA410. O controle varia conforme o TES utilizado, que pode ou não atualizar estoque, registrando quantidades nas tabelas SB2 e SB6. Para ajustes, pode-se usar o retorno simbólico, eliminando saldos sem movimentar estoque. Recomenda-se que remessa e devolução tenham o mesmo parâmetro "Atualiza Estoque" no TES.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40939246851479) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**  
Como efetuar o controle de poder De/Em terceiros no *Protheus*?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todos os Módulos - Todas as versões  
  
**Solução**  
O Poder de Terceiros consiste em movimentações de estoques, normalmente remessas/devoluções das remessas, que são realizadas via Documento de Entrada MATA103 e Pedido de Venda MATA410 entre empresas.

Portanto, o Protheus permite ao cliente efetuar todo o controle destas remessas de produtos que podem ir para um terceiro, ou produtos de um terceiro que ficarão em seu poder.

**Entendendo o controle DE/EM terceiros quando utilizar uma TES que NÃO atualiza Estoque:**

* Ao enviar produtos para terceiros (nosso em poder de terceiros), o sistema armazena na tabela de "**Saldos Físico e Financeiro" (SB2)**, no campo **"Saldo Pod.3 " (B2\_QTER)** a quantidade enviada, gravando também na tabela de **"Saldo em Poder de Terceiros" (SB6)**, o registro do movimento com tipo "R" (remessa) no campo **"Poder Terc." (B6\_PODER3)**;
* Ao receber produtos de terceiros (de terceiros em nosso poder), o sistema apenas armazena, na tabela de **"Saldo em Poder de Terceiros" (SB6)**, o registro do movimento com tipo "R" (remessa) no campo **"Poder Terc." (B6\_PODER3).** Nesta situação o sistema **não movimenta custos**, pois não houve movimento de estoque;
* Na devolução o sistema gera novo registro na tabela de **"Saldo em Poder de Terceiros" (SB6)** com tipo "D" no campo **"Poder Terc." (B6\_PODER3)** e baixa a quantidade devolvida  na tabela de "**Saldos Físico e Financeiro" (SB2)** no campo **"Saldo Pod.3" (B2\_QTER)**;

**Entendendo o controle DE/EM terceiros quando utilizar uma TES que ATUALIZA Estoque:**

* Ao enviar produtos a terceiros (nosso em poder de terceiros), o sistema armazena na tabela de "**Saldos Físico e Financeiro" (SB2)**, no campo **"Qt.Ns.Pd.Ter" (B2\_QNPT)**, a quantidade enviada e grava, na tabela de **"Saldo em Poder de Terceiros" (SB6)**, o registro do movimento com tipo "R" (remessa) no campo **"Poder Terc." (B6\_PODER3)**;
* Ao receber produtos de terceiros (de terceiros em nosso poder), sistema armazena na tabela de "**Saldos Físico e Financeiro" (SB2)**, no campo **"Qt.Ter.Ns.Pd" (B2\_QTNP)**, a quantidade recebida e grava, na tabela de **"Saldo em Poder de Terceiros" (SB6)**, o registro do movimento com tipo "R" (remessa).
* Na devolução o sistema gera novo registro na tabela de **"Saldo em Poder de Terceiros" (SB6)** com tipo "D" e baixa a quantidade devolvida na tabela de "**Saldos Físico e Financeiro" (SB2)**, no campo **"Qt.Ns.Pd.Ter" (B2\_QNPT)** para produtos em poder de terceiros, e **"Qt.Ter.Ns.Pd" (B2\_QTNP)** para produtos de terceiros em nosso poder.

**Nota Fiscal de Retorno Simbólico**

Para situações pontuais onde o saldo precisa ser eliminado, uma alternativa é realizar o Documento de Entrada / Documento de Saída que caracterize um **Retorno Simbólico**, com o TES devidamente configurado para promover a baixa de Poder de Terceiros, para fins de ajuste nos saldos do ERP, mantendo o registro da Nota como referência da movimentação. Para mais informações, consulte a documentação:

* [**Como eliminar saldo em Poder de terceiro (retorno simbólico)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010519121-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-eliminar-saldo-em-Poder-de-terceiro-retorno-simb%C3%B3lico)

**Exemplo da operaçãos com poder de terceiros:**

|  |  |
| --- | --- |
| **Operação** | **Processo sugerido** |
| Envio de Demonstração | **Tipo de Pedido Venda:** N  **TES Poder Terceiros:** R  **TES Atualiza Estoque:** S |
| Devolução de Demonstração | **Tipo de Documento de Entrada**: B  **TES Poder Terceiros:** D  **TES Atualiza Estoque:** S |
| Envio para Conserto | **Tipo de Pedido Venda:** B  **TES Poder Terceiros:** R  **TES Atualiza Estoque:** S |
| Devolução de Conserto | **Tipo de Documento de Entrada:** N  **TES Poder Terceiros:** D  **TES Atualiza Estoque:** S |

**Observação:** Ao fazer controle DE/EM terceiros de Remessa/Devolução, recomendamos que ambos os movimentos respeitem o campo "Atualiza Estoque" (F4\_ESTOQUE) no cadastro do TES.   
Ou seja, se uma remessa for feita com um TES com o campo **"Atualiza Estoque" (F4\_ESTOQUE)** como **"Sim"**, é recomendado que a Devolução seja realizada com um TES com o campo **"Atualiza Estoque" (F4\_ESTOQUE)** também como **"Sim"**.

Abaixo disponibilizamos o vídeo do Webinar sobre o Controle de Poder de Terceiros para maior detalhamento dos processos:

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar um retorno simbólico de um saldo que ficou em poder de terceiros?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010519121-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-um-retorno-simb%C3%B3lico-de-um-saldo-que-ficou-em-poder-de-terceiros-)

[*MP - SIGAEST - É possível fazer o retorno (devolução) de remessa de Poder de Terceiros com custo diferente da remessa?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004896162-MP-SIGAEST-%C3%89-poss%C3%ADvel-fazer-o-retorno-devolu%C3%A7%C3%A3o-de-remessa-de-Poder-de-Terceiros-com-custo-diferente-da-remessa-)

[*Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)
