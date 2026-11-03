---
content_hash: 0e6226c64e4dea6bdbf3805df08a162cc3f8b92222fb448721f924014277653c
fetched_at: '2026-06-29T00:08:15.438576+00:00'
page_id: '244733980'
product: rm
source: tdn-rm
title: TVBHA0_DT_GRRF
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBHA0_DT_GRRF
version: 114
---

# GRRF

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | Folha de pagamento |
| **Função:** | *GRRF* |
| **Situação/Requisito:** | Ao importar o arquivo GRRF.RE está dando erro conforme abaixo:  REGISTRO CONTEÚDO DO CAMPO  LINHA DO ERRO CÓDIGO - DESCRIÇÃO DO ERRO  TRABALHADOR PIS/PASEP ADMISSÃO CAT  10 00025326252600  00002 18 - CEI da Empresa inválido. Verifique se o campo está preenchido corretamente.  40 3  00003 129 - Tipo de Inscrição da Empresa inválido (1 - para CNPJ, 2 - para CEI). |
| **Solução/Implementação:** | Ajuste realizado na GRRF, de forma que, no caso em que a base esteja parametrizada para usar CEI e no cadastro da coligada seja informado um CPF no campo "CNPJ / CPF / CEI", o sistema informe no arquivo GRRF o CEI de acordo com a quebra de CEI informada no parametrizador, item máscaras e quebras |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVBHA0 TVMTOZ |
| **Requisito (ISSUE):** |  |

divs
