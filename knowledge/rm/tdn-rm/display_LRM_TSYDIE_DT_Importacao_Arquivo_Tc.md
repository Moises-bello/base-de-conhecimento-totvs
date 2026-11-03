---
content_hash: 8620d927a2bf70be6169bd1358290d85f0124a778de7430f37c3575491539612
fetched_at: '2026-06-29T00:06:03.481091+00:00'
page_id: '198955089'
product: rm
source: tdn-rm
title: TSYDIE_DT_Importacao_Arquivo_Tc
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYDIE_DT_Importacao_Arquivo_Tc
version: 1
---

# Importação de Arquivo

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Importação de Arquivo - TOTVS Colaboração 2.0* |
| **Situação/Requisito:** | O Sistema está importando o arquivo XML para a coligada incorreta no TOTVS Colaboração 2.0. |
| **Solução/Implementação:** | Melhorias nas regras de seleção da Filial e Coligada com base nas informações do XML durante o processo de recebimento de NF-e. O Ajuste foi realizado para impedir que a  coligada corrente fosse utilizada durante a importação do XML quando o CNPJ contido no mesmo não for encontrado na base de dados, nesta situação o Arquivo será movido para o  diretório "RM/Error" e no log do processo será informado o motivo. |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não se Aplica* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.7* |
