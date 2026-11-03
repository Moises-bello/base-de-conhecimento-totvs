---
content_hash: 84c3991c11ebb54ca74195425422ef309a3e368474ecf71420d33bc506f7dfbe
fetched_at: '2026-06-29T00:06:26.240874+00:00'
page_id: '224455221'
product: rm
source: tdn-rm
title: TUFPQA_DT_Libera_Bloqueio_Ordem_Producao
type: documentation
url: https://tdn.totvs.com/display/LRM/TUFPQA_DT_Libera_Bloqueio_Ordem_Producao
version: 120
---

# Liberação Bloqueio Ordem de Produção

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão Planejamento e Controle da Produção* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Libera Bloqueio Ordem Produção* | *Informe o nome técnico da rotina.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Baixa de materiais e Empenho de Materiais*.* | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | |
| **Cadastros Iniciais:** | *Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito.* |
| **Parâmetro(s):** | *Informe os parâmetros utilizados.* |
| **Ponto de Entrada:** | *Menu* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *Informe o requisito relacionado (Issue).* |
| **País(es):** | *Informe o(s) Pais(es).* |
| **Banco(s) de Dados:** | *Informe o(s) Banco(s) de Dados utilizado(s).* |
| **Tabelas Utilizadas:** | * *KORDEM* |
| **Sistema(s) Operacional(is):** | *Informe o(s) sistema(s) operacional(is) utilizados.* |

|  |  |
| --- | --- |
| **Versões/Release:** | *Informe as versões.* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

## Descrição

Implementado recurso de segurança relacionando a utilização dos serviços de empenho e baixa de materiais de uma ordem de produção por dois usuários simultâneos, nessa situação a quantidade baixada ou empenhada pode ser realizada em dobro.

Com o novo recurso quando um usuário está atuando no processo de empenho ou baixa de uma ordem ela fica bloqueada para outros usuários impedindo que ocorra o problema de duplicação, a ordem é liberada logo após o processo seja finalizado ou abandonado pelo usuário.

Ocorrendo fechamento forçado do sistema como no caso de queda de energia a ordem de produção pode ficar bloqueada, a ordem de produção pode ser liberada manualmente através do menu da nova MDI. Acesse a página “Controle de Produção” -> “Liberar Bloqueio Ordem de Produção”. As ordem de produção com bloqueio vão ser listadas, basta selecionar as que deseja liberar e em processos -> “Liberar bloqueio Ordem de Produção”.

Para usar dê permissão para o usuário no perfil do mesmo.

Na versão 11.82 o recurso precisa ser liberado por script, na versão 12.1.10 já é ativado através do conversor.

Escreva aqui a descrição da nova implementação ou melhoria.

divs
