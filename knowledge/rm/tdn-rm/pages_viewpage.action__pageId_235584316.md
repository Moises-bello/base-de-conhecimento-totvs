---
content_hash: d3803ce836bdb84d20ccc1fdedb464343f28fbe575b6c1a1e76db6af0741a7a6
fetched_at: '2026-06-29T00:08:05.115844+00:00'
page_id: '235584316'
product: rm
source: tdn-rm
title: TTEWAC_DT_Exclui_Grau_Participação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235584316
version: 116
---

# Exclui Grau de Participação no XML TISS 3.02.01

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento para Convênios |  |  | | --- | | **Rotina(s) envolvida(s)** | | Condições Contratuais com Convênios | |
| **Parâmetro(s):** | **Cadastros / Faturamento / Condições Contratuais com Convênios**, aba **Eletrônico III - TISS**, parâmetro **Grau de Participação na guia SP/SADT - exames** |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER e ORACLE |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado parâmetro nas condições contratuais para que seja possível escolher se deseja omitir o grau de participação na guia SP/SADT para exames.

## Procedimento para Utilização

1. Acesse as **Condições Contratuais do Convênio**.
2. Na aba "**Eletrônico III - TISS**", marque o parâmetro "**Grau de Participação na guia SP/SADT - exames**" na caixa agrupadora "**Tags opcionais que não serão geradas no XML**".
3. Acesse o **Faturamento para Convênios** e gere uma fatura para guia de SP/SADT.
4. Selecione os pacientes desejados e fature.
5. Após gerar o XML, verifique que a tag <ans:grauPart> não foi gerada dentro da outra tag referente à equipe (<ans:equipeSadt>).

divs
