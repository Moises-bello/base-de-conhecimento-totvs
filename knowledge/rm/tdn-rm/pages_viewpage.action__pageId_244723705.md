---
content_hash: 0550d8abc28422d28e3b32ea6cbc13af4d801dcd23d2568e5433b2f1ffceecda
fetched_at: '2026-06-29T00:08:14.983215+00:00'
page_id: '244723705'
product: rm
source: tdn-rm
title: TVFSEZ_DT_Parâmetro_BI_e_Descritivo_Cirurgia_Função_Cirurgião
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244723705
version: 122
---

# Parâmetro para BI de Procedimento Cirúrgico e Descritivo de Cirurgia Exibir Corretamente as Funções do Cirurgião

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Controle de Infecção Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | BI de Procedimento Cirúrgico | | Descritivo de Cirurgias | |
| **Parâmetro(s):** | Permite Somente Cirurgião Principal BI e Descritivo de Procedimento Cirúrgico |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado um novo parâmetro para ao gerar o BI de Procedimento Cirúrgico o usuário pode gerar apresentando somente as informações de cirurgião principal ou com informação de auxiliar e cirurgião principal.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Controle de Infecção Hospitalar (RM Janus)**, acesse **Utilitários/Parâmetros**. Configure  o parâmetro a seguir:

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| **Nome:** | Permite Somente Cirurgião Principal BI e Descritivo de Procedimento Cirúrgico |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | Marcado |

## Procedimento para Utilização

       1.            No **TOTVS Controle de Infecção Hospitalar** (RM Janus), acesse **Apoio Gerencial / Procedimento Cirúrgico**.

O sistema apresenta a janela de BI de **Procedimento Cirúrgico**.

       2.            Selecione uma data e clique em **Atualizar**.

       3.            Verifique que no cubo de Função traz também a informação de Cirurgião e Auxiliar quando o parâmetro está desmarcado.

       4.            Com o parâmetro (**Permite Somente Cirurgião Principal BI e Descritivo de Procedimento Cirúrgico**) marcado o sistema apresenta somente a função Cirurgião.

divs
