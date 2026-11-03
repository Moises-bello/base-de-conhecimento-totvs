---
content_hash: 3dee2563b2c416df0966de424e1fc0cab563071415499709221f5f3e4239a95b
fetched_at: '2026-06-29T00:08:04.156983+00:00'
page_id: '235569713'
product: rm
source: tdn-rm
title: TQUQX3_DT_Alterar_CID_de_Alta
type: documentation
url: https://tdn.totvs.com/display/LRM/TQUQX3_DT_Alterar_CID_de_Alta
version: 116
---

# Permissão de Acesso para Alterar CID após a Alta do Paciente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Alta |  |  | | --- | | **Rotina(s) envolvida(s)** | | Segurança / Perfis | |
| **Cadastros Iniciais:** | **Cadastros / Segurança / Perfis,** selecionar um perfil, aba **"Acesso a Menus"*****.***  **TOTVS Hospitalar > [03] Atendimento > [03.03] Internação > [03.03.11] Alta.** Conceder acesso ao item **[03.03.11.01]  Permite Alterar CID(Alta)** |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER e Oracle |
| **Tabelas Utilizadas:** | SZATENDIMENTO, SZPACIENTE, SZLOGCIDALTA |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada permissão de acesso por perfil de usuário, para que este possa alterar o CID de Alta após o paciente ter recebido alta pelo sistema, bem como um histórico para que seja possível verificar alterações anteriores para o mesmo paciente.

## Procedimento para Utilização

1. Acesse **Cadastros / Segurança / Perfis**.
2. Selecione um perfil, vá até a aba **Acesso a Menus**.
3. Na árvore de menus acesse o caminho: TOTVS Hospitalar/ [03] Atendimento / [03.03] Internação / [03.03.11] Alta. Permita acesso ao item [03.03.11.01] Permite Alterar CID(Alta).
4. Após a permissão, selecione novamente a coligada para que o sistema atualize as permissões do usuário.
5. O usuário poderá acessar a tela de alta e alterar o CID(Alta) do paciente sem ter que cancelar a alta do mesmo.
6. Foi implementado um botão ao lado do botão de busca do CID(Alta) que irá exibir o histórico de alterações de CID para aquele paciente em questão.

divs
