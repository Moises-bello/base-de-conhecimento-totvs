---
content_hash: 1274de6ae3a5dff9bb0d8cfb2093721fc3522133ca86867be73e6470f4d982e4
fetched_at: '2026-06-29T00:06:03.241179+00:00'
page_id: '198951974'
product: rm
source: tdn-rm
title: TSTWO2_DT_Funcao_Valorfuncperc_Nao_Retorna_Valor
type: documentation
url: https://tdn.totvs.com/display/LRM/TSTWO2_DT_Funcao_Valorfuncperc_Nao_Retorna_Valor
version: 2
---

# FUNÇÃO DE FÓRMULA VALORFUNCPERC NÃO RETORNA VALOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Função de fórmula VALORFUNCPERC.* |
| **Situação/Requisito:** | *Função de fórmula VALORFUNCPERC não está retornando valor, mesmo existindo o registro do valor associado no anexo do funcionário.* |
| **Solução/Implementação:** | *Ajustar a função de fórmula VALORFUNCPERC para não fazer a multiplicação por zero, e assim retornar o valor correto, que é o resultado da multiplicação dos valores associados ao funcionário, dentro do período das datas informadas.*  *VALORFUNCPERC(‘02’, ‘01/08/2015’, ‘31/08/2015’) -> Será retornado o resultado da multiplicação dos valores associados de código '02' entre 01/08/2015 a 31/08/2015.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSTWO2* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
