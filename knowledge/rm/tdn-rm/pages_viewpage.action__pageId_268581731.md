---
content_hash: 91ef3abb0cb4f80e842d0ae850b2648f61799b3e3dc1ec2d76813384c0a083cc
fetched_at: '2026-06-29T00:08:20.626860+00:00'
page_id: '268581731'
product: rm
source: tdn-rm
title: TTQNG9_DT_Emissão_Boleto_Pelo_RMReport_Guardando_Binário_Rel_Gerado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268581731
version: 123
---

# Emissão do Relatório de Boleto

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Emissão de Boleto | Emissão de Boleto |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Visão de Boleto | Emissão do Relatório de Boleto (Visão de Boleto) | | Contrato | Emissão do Relatório de Boleto (Anexo Contrato) | | Matricular Aluno | Emissão do Relatório de Boleto (Matricula Aluno Período Letivo) | | Portal - Matricula online | Emissão do Relatório de Boleto (Portal - Matricula online) | | Portal - Histórico Financeiro | Emissão do Relatório de Boleto (Portal - Histórico Financeiro) | | Portal - Atendimento/Solicitações | Emissão do Relatório de Boleto (Portal - Atendimento/Solicitações) | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Chamados Relacionados** | TTQNG9 |
| **Requisito (ISSUE):** |  |
| **País(es):** | Todos |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |

## Descrição

Evolução na emissão de relatório de boleto do educacional para que as informações binárias do relatório gerado sejam armazenadas no banco de dados.

Esta evolução impactará na emissão do relatório de boleto dos seguintes cadastros/processos:

* Visão de Boleto (Financeiro/Contábil -> Boletos)
* Contrato (Financeiro/Contábil -> Contrato)
* Matricular Aluno (Currículo/Ofertas -> Aluno -> Anexo Cursos/Habilitações -> Processo Matricular Aluno)
* Portal - Matricula Online
* Portal - Histórico Financeiro
* Portal - Atendimento/Solicitações

Iremos evoluir também a tela de seleção e emissão  do relatório de boleto para que fique mais simplificada e apresente somente os relatórios criados a partir do RM [Report.net](http://Report.net).

**Observação:**

Este novo recurso somente será acionado se o educacional estiver parametrizado (Educacional >> Tesouraria >> Relatórios) para que o tipo de relatório seja igual a "RM Reports", se o educacional estiver parametrizado para o tipo de relatório "Gerador de Relatório (Antigo)" o comportamento continuará o mesmo antes desta evolução, ou seja, não irá gravar o binário do relatório e continuará apresentando a tela de emissão de relatório antiga.

**Comportamento:**

* Ao ser apresentada a tela de emissão do relatório de boleto o sistema preenchera automaticamente o campo de relatório com o relatório de boleto default parametrizado no educacional (Educacional >> Tesouraria >> Relatórios), sendo possibilitado ao usuário selecionar outro relatório se preferir.
* Sempre que um usuário emitir o boleto pelo RM Educacional ou RM Portal o sistema armazenará no banco de dados as informações binárias do relatório do boleto que foi gerado, ou seja, se o usuário emitir o boleto 10 vezes iremos armazenar todas as emissões.

As informações do boleto poderão ser acessadas e consultadas posteriormente no módulo TOTVS Gestão Financeira.

Para maiores informações veja em:

* <http://tdn.totvs.com/pages/releaseview.action?pageId=211063088>
* <http://tdn.totvs.com/pages/releaseview.action?pageId=211063413>

divs
