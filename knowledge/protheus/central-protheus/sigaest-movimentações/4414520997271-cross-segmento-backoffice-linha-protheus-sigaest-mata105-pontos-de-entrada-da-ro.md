---
article_id: 4414520997271
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 592f2b945a821d966966af31aed8110143472e25297fff0d542b81a92170f172
fetched_at: '2026-06-28T22:38:55.704663+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Pontos de
  Entrada da rotina Solicitação ao Armazém
type: support-article
updated_at: '2026-03-06T15:47:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414520997271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Pontos-de-Entrada-da-rotina-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

**Dúvida**Quais são os Pontos de Entradas da rotina MATA105?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Segue abaixo a relação dos Pontos de Entrada disponíveis na rotina MATA105:

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada:** | **Título:** | **Descrição:** |
| **[MT105FIL](https://tdn.totvs.com/pages/releaseview.action?pageId=6087699)** | Solicitação ao almoxarifado | Ponto de entrada para filtragem da Mbrowse |
| **[MT105COR](https://tdn.totvs.com/display/public/PROT/MT105COR+-+Manipula+itens+da+legenda)** | Manipula itens da legenda | Permitir que itens da legenda possam ser manipulados (modificados ou excluídos) ou que novos itens sejam adicionados. |
| **[MT105MNU](https://tdn.totvs.com/pages/releaseview.action?pageId=6087703)** | Adiciona botões ao menu principal | Este Ponto de Entrada é utilizado para adicionar itens no menu principal da rotina de solicitação ao armazém Eventos |
| **[MT105QRY](https://tdn.totvs.com/display/public/PROT/MT105QRY+-+Filtro+de+dados+da+Mbrowse+para+ambiente+Top)** | Filtro de dados da Mbrowse para ambiente Top | Permite Filtrar os dados da Mbrowse para o ambiente Top. |
| **[M105BUT](https://tdn.totvs.com/pages/releaseview.action?pageId=647444724)** | Monta array com botões nas rotinas de inclusão. | O Ponto de Entrada M105BUT e utilizado para montar um array com botões a serem visualizados nas rotinas de inclusão, exclusão e visualização das solicitações ao armazém. |
| **[MT105SCR](https://tdn.totvs.com/pages/releaseview.action?pageId=6087704)** | Objeto para manipulação de usuário | Encontra-se dentro da rotina que monta a dialog da Solicitação ao Almoxarifado; Disponibiliza como parâmetro o Objeto da dialog; 'oDlg' para manipulação do usuario e a opção selecionada (inclusão/ alteração/ visualização/ exclusão ) |
| [**MT105COP**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087696) | Acrescenta campos do usuário que não devem ser copiados para a nova SA | Na rotina de inclusão da Solicitações ao Almoxarifado A105INCLUI. |
| [**A105DELOK**](https://tdn.totvs.com/pages/releaseview.action?pageId=235597587) | Exclusão de Solicitações de Compra. | Ponto de entrada localizado após a confirmação da exclusão e antes de executar a rotina de exclusão da solicitação ao armazém. Tem retorno lógico para validação da exclusão da S.A. |
| [**MTA105LIN**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087791) | Valida os dados na linha da solicitação ao almoxarifado digitada | Pode ser utilizado para validar os dados na linha da solicitação ao almoxarifado digitada. |
| **[MTA105OK](https://tdn.totvs.com/pages/releaseview.action?pageId=6087792)** | Confirma a gravação da solicitação ao almoxarifado | Ao confirmar a solicitação ao almoxarifado. Pode ser utilizado para confirmar ou não a gravação da Solicitação ao Almoxarifado. |
| **[MT105GRV](https://tdn.totvs.com/pages/releaseview.action?pageId=6087701)** | Solicitações ao Almoxarifado | Este Ponto de Entrada e chamado após a inclusão ou alteração de dados no arquivo SCP. |
| **[MT105FIM](https://tdn.totvs.com/pages/releaseview.action?pageId=6087700)** | Solicitação ao Almoxarifado A105GRAVA | Encontra-se no final da função de gravação da tabela SCP. |
| **[MT105LEG](https://tdn.totvs.com/pages/releaseview.action?pageId=6087702)** | Manipulação de itens da legenda | Permitir que itens da legenda possam ser manipulados (modificados ou excluídos) ou que novos itens sejam adicionados. |
| **[MT105EXP](https://tdn.totvs.com/display/public/PROT/MT105EXP+-+Manipula+os+itens+carregados+no+acols)** | Manipula os itens carregados no acols | O ponto se encontra no final da função após a carga do acols com os produtos da estrutura/e ou OP e sua utilização é disponibilizar ao usuário a possibilidade de manipular os itens carregados no acols. |

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Movimentações](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
