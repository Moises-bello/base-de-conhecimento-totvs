---
content_hash: 54265a97a71c59cd89ed26814639e35e77be8d53ef9a5b2d87d661f9ce11f107
fetched_at: '2026-06-29T00:08:05.486656+00:00'
page_id: '235595669'
product: rm
source: tdn-rm
title: TUQVSK_DT_Referencia_EventoCC38_Com_FormulaValor
type: documentation
url: https://tdn.totvs.com/display/LRM/TUQVSK_DT_Referencia_EventoCC38_Com_FormulaValor
version: 1
---

# REFERÊNCIA VINDO ZERADA QUANDO O EVENTO COM CC 38 POSSUI FÓRMULA VALOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias* |
| **Situação/Requisito:** | *Quando os eventos de CC's 2 (Dias Trabalhados), 17 (Salário Maternidade), 24 (Férias Indenizadas), 25 (Férias Proporcionais) e 38 (Ferias Recibo) possuem fórmula valor, o campo referência não é calculado, retornando o valor zerado.* |
| **Solução/Implementação:** | *No caso da existência de fórmula do usuário, todo o controle relacionado ao código de cálculo é ignorado no processamento.*  *Foi tratado para que somente a parte do cálculo da referência do evento seja executada, mesmo na existência de fórmula valor no evento.* |
| **Chamados   relacionados:** | *TUQVSK* |
| **Versões/Release:** | *12.1.11* |
