---
article_id: 12606996366743
category: Materiais - Compras (SIGACOM)
content_hash: 39857ea2d6f7893e7cea479664c894e3b4bcbc024006621050557dff114fa359
fetched_at: '2026-06-28T22:41:14.186459+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Após Eliminar Resíduos
  do Pedido de compras não é possível visualizar o registro de aprovação do Pedido
  que foi realizado antes da eliminação.
type: support-article
updated_at: '2026-03-31T17:23:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12606996366743-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ap%C3%B3s-Eliminar-Res%C3%ADduos-do-Pedido-de-compras-n%C3%A3o-%C3%A9-poss%C3%ADvel-visualizar-o-registro-de-aprova%C3%A7%C3%A3o-do-Pedido-que-foi-realizado-antes-da-elimina%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30708261911447) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Após Eliminar Resíduos do Pedido de compras não é possível visualizar o registro de aprovação do Pedido que foi realizado antes da eliminação, na opção na opção "Outras Ações->Aprovac" da visualização do pedido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39422857828375)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus compras - Todas as versões  
  
**Solução**

Ao eliminar resíduos utilizando o controle de alçadas, conceitualmente, os registros referente ao aprovador são deletados.

Conforme documentação: [Exibe Aprovação dos Documentos Eliminados como Resíduo](https://tdn.totvs.com/pages/viewpage.action?pageId=6085059) é possível visualizar os registros que foram deletados para fins de histórico habilitando o parâmetro **MV\_EXAPROV**.

O objetivo do parâmetro **MV\_EXAPROV** é definir se exibe ou não aprovação dos documentos eliminados como resíduo.

Se **.T.** exibe aprovação dos documentos eliminados como resíduo;  
Se **.F.** não exibe aprovação dos documentos eliminados como resíduo.

## **Parâmetro**

| Itens | Descrição |
| --- | --- |
| Nome | MV\_EXAPROV |
| Tipo | Lógico |
| Valor Padrão | **.T.** |
| Descrição | Exibe aprovação dos documentos eliminados como resíduo. |

***Obs:***

O parâmetro não se trata para deixar de deletar os registros da SCR na Eliminação de Residuos, mas sim para se conseguir visualizar/exibir os registros/logs de aprovação na opção "Outras Ações->Log Aprovação" da visualizaçao do Pedido/Solicitação de Compras com alçada.

Dessa forma, para que não haja perda do histórico dos aprovadores, utilizando o parâmetro **MV\_EXAPROV** igual a **.T.**, **não** se deve executar o processo de **PACK** na tabela **SCR**.

***Saiba Mais :***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a Funcionalidade da rotina Eliminar de Resíduo (MATA235)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024673534-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-Funcionalidade-da-rotina-Eliminar-de-Res%C3%ADduo-MATA235-?source=search)
* [MV\_EXAPROV - Exibe aprovação dos documentos eliminados como resíduo.](https://tdn.totvs.com/pages/releaseview.action?pageId=838681814)
* [PCOM18003 - Instrução sobre os registros da tabela SCR - Eliminação de Resíduos](https://tdn.totvs.com/pages/releaseview.action?pageId=510502977)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM)
