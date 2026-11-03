---
content_hash: cf35bcffd5ef9541d9160a90ebd409a770b7d595e82e4e31b50719ca7af59812
fetched_at: '2026-06-29T00:06:21.255545+00:00'
page_id: '223166647'
product: rm
source: tdn-rm
title: TTWNYN_DT_Saldo_Ferias_Coletivas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWNYN_DT_Saldo_Ferias_Coletivas
version: 1
---

# SALDO NAS FÉRIAS COLETIVAS DE FUNCIONÁRIO COM MAIS DE 1 ANO DE CASA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias Coletivas* |
| **Situação/Requisito:** | *Quando o parâmetro "Considera data de retorno para início do período aquisitivo quando < 1 ano" está marcado no Parametrizador, no processamento das férias coletivas considera o saldo até a data final do período de gozo.*  *Entretanto este comportamento só deve ocorrer para funcionário com menos de 1 ano de casa, que terão o período aquisitivo interrompido.*  *No caso de funcionários com mais de 1 ano de casa, deve sempre ser considerado o saldo somente até a data de início do período de gozo das férias coletivas.* |
| **Solução/Implementação:** | *Ajuste no lançamento das férias coletivas, para verificar o parâmetro "Considera data de retorno para início do período aquisitivo quando < 1 ano" somente no caso de funcionários com menos de 1 ano de casa.*  *Para funcionários com mais de 1 ano sempre será considerado o saldo até a data de início do período de gozo das férias coletivas.* |
| **Chamados   relacionados:** | *TTWNYN* |
| **Versões/Release:** | *12.1.9* |
