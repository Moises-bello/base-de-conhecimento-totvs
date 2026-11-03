---
content_hash: 704ee87d11f29ac0e52c3be45b338d1451d568b55a5a7e0a962df9a07e846604
fetched_at: '2026-06-29T00:08:05.376960+00:00'
page_id: '235594747'
product: rm
source: tdn-rm
title: TUOXZJ_DT_Lançamento_de_KIT_pelo_Prontuário_Eletrônico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235594747
version: 117
---

# Lançamento de KITs pelo PEP

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hopsitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | PEP | Avaliações complementares |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Faturamento | Elaboração de Contas | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle e SQL Server |

## Descrição

É necessário que ao lançar um exame pelo **Prontuário Eletrônico do Paciente**, se o exame estiver vinculado a um kit, os itens do kit sejam lançados na conta do paciente. Comportamento idêntico ao lançamento de honorários na conta do paciente.

Realizada melhoria no sistema para lançar os itens do kit de lançamento, quando incluído um exame na aba Avaliações Complementares do PEP e na aba diagnose e terapia na conta do paciente.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.10.007 do executável do RM Saúde.

## Procedimento para Utilização

1. Acesse o menu **Cadastros / Faturamento / Kit de lançamentos**.
2. Configure um kit e vincule um procedimento da faixa de diagnose e terapia.
3. Acesse o **Prontuário** e lance o exame na aba **Avaliações Complementares**.
4. Ao confirmar o exame o sistema informará ao usuário que o procedimento está vinculado a um Kit e se deseja incluir os itens na conta do paciente.
5. Acesse a conta do paciente e verifique se os itens foram lançados.

   Observação

   Esse comportamento também ocorrerá no lançamento do procedimento na aba Diagnose e Terapia da conta do paciente.

divs
