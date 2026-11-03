---
content_hash: 233d1bda6817406a927bcf7f1e2cf1961ecdf8bf0ee1a32523abbbe159a1df20
fetched_at: '2026-06-29T00:10:13.935045+00:00'
page_id: '458771727'
product: rm
source: tdn-rm
title: Nota carioca
type: documentation
url: https://tdn.totvs.com/display/LRM/Nota+carioca
version: 11
---

Esta Rotina é utilizada para que seja feita a Declaração de Notas Convencionais Recebidas no Sistema de Notas Fiscais de Serviço Eletrônicas do município do Rio de Janeiro. O TOTVS Gestão Fiscal gera este arquivo obedecendo ao layout definido pela Prefeitura.

Para que a Rotina possa ser gerada o layout deve ser importado no Gerador de Saídas. O layout está disponível no diretório do Objetos Gerencias da instalação do RM (Geralmente instalado nesta estrutura C:\TOTVS\CorporeRM\ObjetosGerenciais\Layout)

**Registros gerados.**

**Tipo 010 - Cabeçalho**: Será gerado com os dados da Filial declarante

**Tipo 040 - Declaração de Notas Convencionais Recebidas:**Será gerado com informações das notas fiscais de serviço recebidas desde que não sejam NFS-e emitidas no município do Rio de Janeiro. Sendo assim, o sistema irá selecionar os lançamentos de entrada vinculados a natureza de operação não fiscal (pasta Outros Dados do Cadastro de Naturezas) e que possuam o Tributo ISS em suas Situações Tributárias.

**Tipo 50 - Declaração de Materiais (REMAS):**Será gerado com a carga das Notas de Entrada emitidas fora do município do Rio de Janeiro e que possuem Naturezas de Operação cuja  pasta DADOS C.CIVIL possuam a informação do Tipo de Nota (REMAS/RJ)  gravada.

Código da Obra Origem

Gerado com o Campo do Projeto -  Lançamento Fiscal – Pasta “Situação Tributaria”. -  Sub Pasta Prestação de Serviço – Código Projeto DLAF.IDPRJ – Lançamento de Entrada.

Campo Valor Incorporado

Valor Contábil da Situação Tributaria, do lançamento de Entrada, que no Cadastro da CFOP associado ao Lançamento, o Campo Classif.Operação Construção Civil diferente de “Uso e Consumo”, cadastro\Sub Pasta Dados Construção Civil. DLAF.VALORCONT.

Campo Valor Uso e Consumo

Valor Contábil da Situação Tributaria, do lançamento de Entrada, que no Cadastro da CFOP associado ao Lançamento, o Campo Classif.Operação Construção Civil igual a “Uso e Consumo”, cadastro\Sub Pasta Dados Construção Civil. DLAF.VALORCONT.

Campo Valor Total da Nota

Valor contábil do Lançamento Fiscal. DLAFAGRUP.VALORCONT.

**Tipo 90 - Rodapé:**Registro gerado automaticamente pelo processo da Rotina de acordo com a exigência do layout.
