---
content_hash: 22e7d9db56da7d047cbf01bc10ac914cf835b503fae26124ee884ebd18bf0352
fetched_at: '2026-06-29T00:09:09.016666+00:00'
page_id: '390412443'
product: rm
source: tdn-rm
title: FISCAL01-5971 DT SPED Fiscal Registro G125
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-5971+DT+SPED+Fiscal+Registro+G125
version: 82
---

# SPED Fiscal Registro G125

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Serviços* |
| **Módulo:** | *Totvs Getsão Fiscal* |
| **Função:** | *Geração Sped Fiscal* |
| **Situação/Requisito:** | Refazer implementações da tarefa FISCAL01-5576/FISCAL01-5884  Após as alterações feitas na Issue FISCAL01-5576 o Layout do TAF  está apresentando advertências ao ser importado na versão 12.1.22: "Erro ao importar objeto: 1-234/C:\RM\Documentos\Fis-Fiscal\Rotinas Fiscais\TAF\Layouts\FISLAY0007 - TAF.TotvsGen  Erro: O campo 'COD\_IND\_BEM' da ligação não é válido. Registro: T050AA. Campo: COD\_IND\_BEM." |
| **Solução/Implementação:** | Ajuste na geração do registro G125 para voltar a utilizar o tipo original e assim  não causando erro na importação do Layout TAF e mantendo o ajuste da Issue: FISCAL01-5576/FISCAL01-5884 |

divs
