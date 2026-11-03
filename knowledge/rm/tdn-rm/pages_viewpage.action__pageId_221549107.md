---
content_hash: fc5f2db85dbe19c9e9a597f3e14b5fbc6e8eda299c36b90ac6edc534c50d4829
fetched_at: '2026-06-29T00:06:20.191137+00:00'
page_id: '221549107'
product: rm
source: tdn-rm
title: TTTTR4_DT_Ajuste_Campos_Relatório_Book
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221549107
version: 126
---

# RELATÓRIO BOOK - FOPREL00038 AVISO PRÉVIO TRABALHADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Gerar relatório do book* |
| **Situação/Requisito:** | Ao realizar a geração do relatório FOPREL00038 Aviso Prévio Trabalhado o campo data está com a formatação do ano errada a mesma está apresentado a seguinte formatação Belo Horizonte ,\_\_\_\_ de\_\_\_\_de\_\_\_\_19\_\_. O mesmo relatório apresentada erro durante a impressão fazendo com que as informações fiquem fora da margem, somente é possível validar essa informação se realizar o comanda de impressão pois a exibição do mesmo está correta porém ao imprimir o mesmo está errado é não é possível alterar visto que o mesmo é um relatório padrão, assim que aciona a opção de imprimir é apresentado uma mensagem informando que a margem está fora da área de impressão. |
| **Solução/Implementação:** | Ajustado o campo Cidade que se encontra no cabeçalho, ajustado o campo "Nome da cidade \_\_\_\_\_ de \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_de  \_\_\_\_\_\_", ajustado a formatação do relatório para não cortar ao imprimir.Inserido as informações de Rua, Bairro e Cidade antes de cada informação no cabeçalho do rodapé. |
| **Chamados relacionados:** | TTTTR4 |
| **Versões/Release:** | *12.1.9* |

divs
