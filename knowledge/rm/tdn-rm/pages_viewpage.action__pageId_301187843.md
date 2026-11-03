---
content_hash: 5822ab4fcc42135cb41f40fb91ee3241265030fa6b759653d1a7ec0f6a600fc9
fetched_at: '2026-06-29T00:08:43.065242+00:00'
page_id: '301187843'
product: rm
source: tdn-rm
title: RMFIS00004_Alterar Máscara do Número do Lançamento/Documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301187843
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.x |
| **Ocorrência:** | Alterar a máscara do número de documento do lançamento fiscal. |
| **Ambiente:** |  |
| **Passo a passo:** | Acesse Ambiente →   PARÂMETROS  →  TOTVS Gestão Fiscal →   IDENTIFICAÇÃO DE REGRAS DE APURAÇÃO – ICMS – AVANÇAR – ETAPA LANÇAMENTO FISCAL 1/7, campo "Máscara do número do documento".           Atenção aos caracteres válidos exibidos:          O sistema emitirá uma mensagem de aviso ao processo:      **Apenas orientando que em rotinas fiscais que consideram apenas seis caracteres (tamanho do nº documento), será consistido os números da direita para a esquerda.**    **Exemplo: 123456789 - será considerado "456789".** |
| **Observações:** | Operando com o TOTVS Gestão de Compras, Faturamento e Estoque, orienta-se a manter a mesma máscara definida no Gestão Fiscal.  **Para que o sistema grave a alteração realizada, é necessário avançar etapa por etapa dos parâmetros até conclusão do processo, inclusive as etapas por Filial.** Saia e entre no sistema novamente. |
