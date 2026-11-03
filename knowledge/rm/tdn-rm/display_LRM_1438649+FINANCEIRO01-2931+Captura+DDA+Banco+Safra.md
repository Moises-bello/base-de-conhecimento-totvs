---
content_hash: 64853551e449a028728d1a29f8a4745c772788ed0156e4db61bd0b1173743984
fetched_at: '2026-06-29T00:08:46.365620+00:00'
page_id: '317003410'
product: rm
source: tdn-rm
title: 1438649 FINANCEIRO01-2931 Captura DDA Banco Safra
type: documentation
url: https://tdn.totvs.com/display/LRM/1438649+FINANCEIRO01-2931+Captura+DDA+Banco+Safra
version: 97
---

# REGISTRO DE CAPTURA DE COBRANÇA SAFRA (DDA - DÉBITO DIRETO AUTORIZADO)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Captura de Título de Cobrança (DDA - Débito Direto Autorizado). |
| **Situação/Requisito:** | O processo de Captura de Título de Cobrança para o Banco Safra apresentava inconsistência na criação do registro no banco (tabela FCAPTURACOB). Se o formato da data (Vencimento ou Emissão) no layout bancário do banco para DDA (Débito Direto Autorizado) está parametrizado como DDMMAA o sistema não lia corretamente a data informada no arquivo no processo de Captura de Títulos em Cobrança. Exemplo: 201017 era transformada em 20/10/0017 ao invés de 20/10/2017. |
| **Solução/Implementação:** | Ajustada a leitura de dados dos arquivos de captura de títulos de cobrança tratando datas no formato DDMMAA.  No processo **Captura de Título de Cobrança** para o Banco Safra o REGISTRO DE CAPTURA DE COBRANÇA SAFRA (CAB) VARREDURA DE SACADOS / (DDA) DÉBITO DIRETO AUTORIZADO do layout de retorno tem o campo Código de Barras com tamanho 45 mas o sistema só permitia 44 caracteres. O tamanho foi alterado nos campos das tabelas de Lançamento (FLAN) e Reg. de Captura de Títulos em Cobrança (FCAPTURACOB), sendo tratado apenas na alteração do lançamento chamada pelo processo de conciliação dos títulos (a pagar cujo convênio vinculado a banco com código Febraban 422). Nos processos de inclusão de lançamento, importação via arquivo texto e alteração (para lançamento a pagar de banco que não o Safra) a consistência continua exigindo código de barras de tamanho 44. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1438649. |
| **Requisito:** | FINANCEIRO01-2931. |

divs
