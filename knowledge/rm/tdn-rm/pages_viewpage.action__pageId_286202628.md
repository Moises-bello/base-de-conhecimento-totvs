---
content_hash: f29ff8331c68fd047e8cf7b97535c5a1b702ad0984c75db7bf10f34fd1400867
fetched_at: '2026-06-29T00:08:40.039287+00:00'
page_id: '286202628'
product: rm
source: tdn-rm
title: 1042867 MSAU-11863 DT Tela Registro de Atendimento na Classificação de Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286202628
version: 105
---

# Tela Registro Atendimento na Classificação de Risco

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Painel de Classificação de Risco | |
| **Parâmetro(s):** | Exibe por padrão senha de Todas Unidades no Registro de Atendimento |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZUNIDATEND, SZSENHACLASSIF, SZCLASSIFICACAORISCO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Criado um filtro na tela de registro de atendimento "Exibir senha de todas unidades", ao marcar esse filtro e atualizar o sistema irá pesquisa por senha de todas as unidades de atendimento. Foi adicionado também uma nova coluna na grid de Unidade de Atendimento, para que o usuário possa se localizar com as senhas da unidade.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.17 deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Gestão Hospitalar (RM Saúde)**, acesse **Opções/Parâmetros/Parâmetros Gerais**. Na aba de Classificação de Risco o(s) parâmetro(s) a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Exibe por padrão senha de Todas Unidades no Registro de Atendimento |
| **Tipo:** | *Checkbox (Opcional)* |
| **Cont. Por.:** | Desmarcado |
| **Descrição:** | Exibe por padrão senha de Todas Unidades no Registro de Atendimento |

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Saúde), acesse o Toten de Pronto Atendimento.

                      Chame várias senhas para várias unidades de atendimento diferentes.

       2.            Após chamar as senhas, acesse o Painel de Classificação de Risco.

       3.            Selecione uma unidade com senhas chamadas ou não, na aba de registro de atendimento possui uma nova opção de filtro "Exibir senha de todas unidades"

                      Se o parâmetro "Exibe por padrão senha de Todas Unidades no Registro de Atendimento", estiver marcado, o filtro informado já virá marcado por padrão.

       4.            Ao marcar o filtro será exibido a senha de todas as unidades de atendimento e não somente a unidade selecionada no painel.

divs
