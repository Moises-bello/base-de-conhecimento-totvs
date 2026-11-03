---
content_hash: 9f9d0b1a8bf1c0cbbe9afed96e177ff3605fc482611d1bb89f357187c014a8ab
fetched_at: '2026-06-29T00:05:51.635642+00:00'
page_id: '1052744485'
product: rm
source: tdn-rm
title: Grupo ZF - Informações de Produtos da Agricultura, Pecuária e Produção Florestal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1052744485
version: 7
---

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | | | |  |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Observação** | **Campo de Origem** |
| 423k | ZF01 | agropecuario | Informações de produtos da agricultura, pecuária e produção Florestal | G | A01 | - | 0-1 | Gerado à partir das informações da pasta "Agro Negócio" do movimento. Esta pasta ficará visível apenas se o parâmetro "Informar dados agrícolas" estiver habilitado. |  |
| 423k.1 | ZF02 | defensivo | Defensivos Agrícolas | CG | ZF01 | - | 1-20 | Gerado à partir das informações de Defensivos Agrícolas informados no movimento. |  |
| 423k.2 | ZF03 | nReceituario | Número da receita ou receituário do agrotóxico / defensivo agrícola | E | ZF02 | C | 1-1 | Informar o número da receita ou receituário de aplicação do defensivo | TMOVDEFENSIVOAGRO.NUMRECEITA |
| 423k.2a | ZF03a | CPFRespTec | CPF do Responsável Técnico pela emissão do receituário | E | ZF02 | N | 1-1 | Informar o CPF do Responsável Técnico legalmente habilitado para emissão do receituário agrícola, conforme exigências federais e estaduais, como engenheiro agrônomo, engenheiro florestal ou técnico agrícola. | TMOVDEFENSIVOAGRO.CPFRESPONSAVEL |
| 423k.3 | ZF04 | guiaTransito | Guia de Trânsito | CG | ZF01 |  | 1-1 | Gerado à partir das informações de Guia de Trânsito informados no movimento. |  |
| 423k.4 | ZF05 | tpGuia | Tipo da Guia | E | ZF04 | N | 1-1 | 1 - GTA - Guia de Trânsito Animal;  2 - TTA - Termo de Trânsito Animal;  3 - DTA - Documento de Transferência Animal;  4 - ATV - Autorização de Trânsito Vegetal;  5 - PTV - Permissão de Trânsito Vegetal;  6 - GTV - Guia de Trânsito Vegetal;  7 - Guia Florestal (DOF, SisFlora - PA e MT ou SIAM - MG). | TMOV.TIPOGUIATRANSITO |
| 423k.5 | ZF06 | UFGuia | UF de emissão | E | ZF04 | C | 1-1 | UF de emissão da guia | TMOV.CODUFEMISSAOGUIATRANSITO |
| 423k.6 | ZF07 | serieGuia | Série da Guia | E | ZF04 | C | 0-1 | Informar sempre que houver a série da guia | TMOV.SERIEGUIATRANSITO |
| 423k.7 | ZF08 | nGuia | Número da Guia | E | ZF04 | N | 1-1 | Número da Guia | TMOV.NUMGUIATRANSITO |
