---
content_hash: e941d02574a4d28668d98e2ccd13d2bc1e20c53b799de7a7a6fbadecda31735c
fetched_at: '2026-06-29T00:08:11.197404+00:00'
page_id: '241701715'
product: rm
source: tdn-rm
title: TUPCOY_DT_BUSCAR_CODIGO_VERIFICACAO_GERAR_NFSE_NUMERO_PREFEITURA
type: documentation
url: https://tdn.totvs.com/display/LRM/TUPCOY_DT_BUSCAR_CODIGO_VERIFICACAO_GERAR_NFSE_NUMERO_PREFEITURA
version: 110
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | NF.01.0054 | NFS-E GERAR MOVIMENTO COM NUMERO DA PREFEITURA | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | TUPCOY |
| **Requisito (ISSUE):** | MOV000103 - Cópia de movimento |
| **País(es):** | *-* |
| **Banco(s) de Dados:** | *SQL Server* |
| **Tabelas Utilizadas:** | *TNFEMUNICIPAL* |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Melhoria para que quando realizar processo de "Gerar NFS-e com o número da Prefeitura", seja levado o código de verificação para o movimento de destino para fins de escrituração e geração de rotinas fiscais.

## Procedimento para Implantação

 O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.11.108 ou superior*

## Procedimento para Utilização

       1.   Gere uma cópia, onde o movimento de origem esteja parametrizado para uso de NFE MUNICIPAL, e verifique que o campo código de verificação (TNFEMUNICIPAL.PROTOCOLO) é levado para o campo chave de acesso do movimento de destino.

divs
