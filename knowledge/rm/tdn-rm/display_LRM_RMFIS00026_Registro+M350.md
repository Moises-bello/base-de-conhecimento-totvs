---
content_hash: cf7cf0aaa41ea74df0795de0f897d1dc9db1d38bcf6bacaa36bed7c46465a803
fetched_at: '2026-06-29T00:12:02.691053+00:00'
page_id: '90276835'
product: rm
source: tdn-rm
title: RMFIS00026_Registro M350
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00026_Registro+M350
version: 10
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.8x |
| **Processo** | **:** | EFD Contribuições - Registro M350 |
| **Subprocesso** | **:** | Parametrização |
| **Data da publicação** | **:** | 16/09/2014 |

**Parametrização do Aplicativo Gestão de Folha (RM Labore)**

Acesse: **Opções | Parâmetros | RM Labore ->  Outros Parâmetros - - Eventos Exclusão Base PIS**. Preencher com os eventos necessários a serem Excluídos da Base de Cálculo do PIS.

REGISTRO M350: PIS/PASEP – FOLHA DE SALÁRIOS

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo | "M350" |
| 02 | VL\_TOT\_ | Valor Total da Folha de Salários | Gerado com os dados do Aplicativo Gestão de Folha (RM Labore) Total de todos os proventos da Folha de pagamento – Valor por ser Conferido através do Relatório da Folha Analítica. |
| 03 | VL\_EXC\_BC | Valor Total das Exclusões à Base de Cálculo | Gerado com o Valor dos Eventos parametrizado no Aplicativo Gestão de Folha (RM Labore). |
| 04 | VL\_TOT\_BC | Valor Total da Base de Cálculo | Calculado Internamente   (VL\_TOT(02) – VL\_EXC\_BC(03)) |
| 05 | ALIQ\_PIS\_FOL | Alíquota do PIS/PASEP – Folha de Salários | Conforme o Layout do EFD o valor é fixo em "1%" |
| 06 | VL\_TOT\_CONT\_FOL | Valor Total da Contribuição Social sobre a Folha de   Salários | Calculado Internamente   (VL\_TOT\_BC \* ALIQ\_PIS\_FOL) |

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
