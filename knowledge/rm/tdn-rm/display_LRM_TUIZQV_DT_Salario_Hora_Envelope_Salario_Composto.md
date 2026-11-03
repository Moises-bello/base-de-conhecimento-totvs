---
content_hash: 43121caa3c771ed99034c179bc961afb08675a58642cea7e1ebaeb56242ec70f
fetched_at: '2026-06-29T00:08:03.491555+00:00'
page_id: '235323108'
product: rm
source: tdn-rm
title: TUIZQV_DT_Salario_Hora_Envelope_Salario_Composto
type: documentation
url: https://tdn.totvs.com/display/LRM/TUIZQV_DT_Salario_Hora_Envelope_Salario_Composto
version: 2
---

# SALÁRIO HORA INCORRETO NO ENVELOPE DE MESES ANTERIORES QUANDO USA SALÁRIO COMPOSTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Envelope* |
| **Situação/Requisito:** | *Na tela do envelope de funcionário com salário composto, o valor do salário hora não está ficando correto quando é selecionado meses anteriores à competência.*  *No momento de dividir o salário pela jornada mensal, não está sendo considerado o decimal.* |
| **Solução/Implementação:** | *Ajuste na tela do envelope para tratar o somatório da jornada do salário composto como um valor decimal, ao invés de inteiro.*  *Para assim exibir o valor do salário hora correto.* |
| **Chamados   relacionados:** | *TUIZQV, TUOYNC* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
