---
article_id: 360022440852
category: Materiais - Compras (SIGACOM)
content_hash: 503c8f31ceda2a8a79cf2ca4509f9522c2fc27fcb9db318af6e54cc54009fc51
fetched_at: '2026-06-28T22:41:10.341576+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais os Pontos de
  Entrada da rotina MATA140 (Pre-Nota de Entrada) ?
type: support-article
updated_at: '2025-06-10T18:21:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022440852-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-os-Pontos-de-Entrada-da-rotina-MATA140-Pre-Nota-de-Entrada
---

**Dúvida**Quais os Pontos de Entrada da rotina MATA140 (Pre-Nota de Entrada) ?  
  
**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**

Relação de pontos de entrada disponíveis na rotina de Pré-nota:

MT140FIL - [Adição de filtro na chamada mBrowse](https://tdn.totvs.com/pages/releaseview.action?pageId=6085667)

MT140COR - [Novas regras de cores das legendas](https://tdn.totvs.com/display/public/PROT/MT140COR+-+Adiciona+novas+regras+de+cores+na+Mbrowse)

MT140CPO -  [Informar os campos na GetDados que poderão ser alterados](https://tdn.totvs.com/display/public/PROT/TVLBKD_DT_PONTO_DE_ENTRADA_MT140CPO)

A140ALT - [Valida a alteração de uma pré-nota de entrada](https://tdn.totvs.com/pages/releaseview.action?pageId=6085270)

MT140CAB - [Ponto de entrada que permite o preenchimento automático dos dados do cabeçalho da pre-nota e define se continua a rotina](https://tdn.totvs.com/pages/releaseview.action?pageId=38240313)

A140EXC - [Valida a exclusão de uma pré-nota](https://tdn.totvs.com/pages/releaseview.action?pageId=6085271)

MT140SAI - [Responsável por controlar a interface de um pre-documento de entrada](https://tdn.totvs.com/display/public/PROT/MT140SAI)

MT140PC - [Manipula parâmetros MV\_PCNFE](https://tdn.totvs.com/pages/releaseview.action?pageId=6085510)

MT140LOK - [Valida informações no pré-documento de entrada](https://tdn.totvs.com/pages/releaseview.action?pageId=6085509)

MT140TOK - [Validacao da TudoOk](https://tdn.totvs.com/pages/releaseview.action?pageId=6085513)

MA140BUT - [Adiciona botoes do usuario na EnchoiceBar](https://tdn.totvs.com/pages/releaseview.action?pageId=6085354)

MT140APV - [Alterar grupo de aprovação](https://tdn.totvs.com/pages/releaseview.action?pageId=6784340)

MT140ACD - [Atualizacao da conferencia fisica](https://tdn.totvs.com/display/public/PROT/MT140ACD+-+Atualizacao+da+conferencia+fisica)

SD1140E - [No momento da exclusão/deleção da pré-nota](https://tdn.totvs.com/display/public/PROT/TTEN24_DT_PONTO_ENTRADA_SD1140E)

SD1140I - [Utilizado na atualização das linhas do Pré-Documento de Entrada](https://tdn.totvs.com/display/public/PROT/SD1140I)

SF1140I - [Utilizado na atualização do cabeçalho do Pré-Documento de Entrada.](https://tdn.totvs.com/pages/releaseview.action?pageId=6085617)

Este Ponto de Entrada não exibe campos customizados no cabeçalho da pré nota.

Hoje, no sistema não possuimos um PE para essa funcionalidade.

MTA140MNU - [Adicionar botões ao Menu Principal através do array aRotina](https://tdn.totvs.com/pages/releaseview.action?pageId=6085799)

***Obs:***

No estorno da classificação na rotina MATA140, a rotina verifica a função A103NFISCAL, nessa função, temos o PE ***MT100GRV***, o qual pode ser utilizado na MATA140 no estorno da classificação, para estabelecer regras onde a nota pode ou não ser estornada.

[***MT100GRV*** - https://tdn.totvs.com/pages/releaseview.action?pageId=6085394](https://tdn.totvs.com/pages/releaseview.action?pageId=6085394)

***Saiba Mais :***

[MP - SIGACOM - Pontos de Entrada - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000169747-MP-SIGACOM-Pontos-de-Entrada-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
