---
content_hash: 0e0ccd73093995a88410c427c5c6effe7cc794feb621a30d109737fa1d393e28
fetched_at: '2026-06-29T00:08:33.038785+00:00'
page_id: '274003859'
product: rm
source: tdn-rm
title: 636655 FINANCEIRO01-109 Integração Bancária - Retorno de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274003859
version: 109
---

# Integração Bancária - Retorno de Pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financiera |
| **Função:** | Integração Bancária - Retorno de Pagamento |
| **Situação/Requisito:** | Ao importar arquivo de retorno de pagamento do banco Deutsche – 487 é apresentado o erro abaixo: “Nenhum registro foi importado para o banco 487”. Geralmente esse erro ocorre quando o tamanho da linha no arquivo é diferente de 240, porém todas as linhas possuem tamanho 240. |
| **Solução/Implementação:** | Otimização no processo de importação de arquivo de retorno de pagamento. Agora o sistema importa e interpreta arquivos de retorno que possuem assentos do banco Deutsche - 487. Os arquivos são convertidos para o formato UTF-8 (Tabelas código "65001") para tratamento de acentuação e caracteres especiais. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000171 |

divs
