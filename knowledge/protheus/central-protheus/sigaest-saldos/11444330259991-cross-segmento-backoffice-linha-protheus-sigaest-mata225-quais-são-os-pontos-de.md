---
article_id: 11444330259991
category: SIGAEST - SALDOS
content_hash: c4bf982a552f24e47fa958106b17124ee1d4ce103144f26ef4c40b2d13b138eb
fetched_at: '2026-06-28T22:39:14.891764+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA225 Quais são
  os Pontos de entrada da rotina Saldo Atual
type: support-article
updated_at: '2025-10-01T17:47:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11444330259991-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA225-Quais-s%C3%A3o-os-Pontos-de-entrada-da-rotina-Saldo-Atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35335610288791) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais são os Pontos de Entrada da rotina MATA225 - Saldo Atual?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Abaixo lista com todos os pontos de entrada disponíveis na rotina de Saldo em Estoque (MATA225)

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada:** | **Título:** | **Descrição:** |
| [M225FILB](https://tdn.totvs.com/x/aiAaDg) | Verificação de filtros na Mbrowse da Função MATA225 | Este ponto de entrada tem como objetivo permitir que o usuário filtre os dados a serem exibidos. Utilização: Ao executar a rotina, o usuário poderá especificar através deste ponto de entrada, uma expressão Advpl para filtrar os registros. |
| [MT225GRV](https://tdn.totvs.com/x/NuRc) | Grava campos ou aquivos de usuário | O ponto de entrada MT225GRV é chamado ao final da gravação e pode ser utilizado para gravar campos ou arquivos do usuário. |
| [MT225STAT](https://tdn.totvs.com/x/axKqC) | Alteração de Status | o ponto de entrada MT225STAT complementa a atualização do status do saldo atual do produto. |
| [MTA225MNU](https://tdn.totvs.com/x/Xw7DLw) | Adiciona opções ao menu do mBrowse | Este Ponto de Entrada permite adicionar novas opções ao menu do mBrowse da rotina MATA225 (Slado Atual). |
| [MT225FIL](https://tdn.totvs.com/x/NeRc) | Insere novas opções no array | Este ponto de entrada pode ser utilizado para inserir novas opções no array aRotina. Eventos |
| [MT225TIP](https://tdn.totvs.com/x/vwrBD) | Alterar o tipo do armazém com o saldo ainda em movimentação. | Permite alterar o tipo do armazém (Próprio, padrão ou terceiros) mesmo que o saldo em estoque ainda esteja em movimentação. |
| [MT225COR](https://tdn.totvs.com/x/NORc) | Manipula apresentação das cores no Array | Ponto de entrada para inclusão de nova COR da legenda |

Saiba Mais:

*[Clique aqui e veja mais artigos sobre Saldos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)*
