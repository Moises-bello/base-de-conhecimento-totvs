---
content_hash: 7a2fec1442bc284f7fec461525967375e703a361c7a88c7c6abf91d9b56ae5d9
fetched_at: '2026-06-29T00:08:20.812653+00:00'
page_id: '268588781'
product: rm
source: tdn-rm
title: DT_CPMOV001-661_Processo_Copia_Marcas_entre_Coligadas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-661_Processo_Copia_Marcas_entre_Coligadas
version: 116
---

# Processo de Cópia de Marcas entre Coligadas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Copiar Marcas entre Coligadas* | *EstProcCopyMarca* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Marca* | *EstMarcaAction* | |  |  | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Consultar documento: [DT\_CPMOV001-452\_Marca](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca)* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | CPMOV001-661 |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server* |
| **Tabelas Utilizadas:** | *TMARCA* |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Processo para que seja permitido realizar a Cópia de Marca entre Coligadas. Este processo ficará disponível no cadastro de Marca quando o perfil do usuário possuir permissão para Incluir Marca.

## Procedimento para Utilização

Para utilizar o processo é necessário acessa-lo através do cadastro de Marca que está localizado em BackOffice/Gestão de Estoque, Compras e Faturamento/Cadastros/Estoque, Compras e Faturamento/Mais/Tabelas Auxiliares/Marca.

1. Acessar a opção de Menu "Copiar Marca entre Coligadas" em Processos.

2. Serão atualizadas todas as marcas selecionadas na visão nas Coligadas selecionadas,  conforme selecionado no parâmetro do processo.

Caso, o registro exista na Coligada destino é necessário marcar a opção do processo "Substitui registros no destino se eles já existirem".

divs
