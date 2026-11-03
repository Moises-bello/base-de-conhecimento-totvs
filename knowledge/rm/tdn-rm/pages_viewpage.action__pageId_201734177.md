---
content_hash: 401bc9d966e8b764513f6fb2b887effa840ded67e056a7af06c03705405b496c
fetched_at: '2026-06-29T00:06:06.997921+00:00'
page_id: '201734177'
product: rm
source: tdn-rm
title: DT_Anexar_Relatório_para_Impressão_Painel_de_Classificação_de_Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201734177
version: 6
---

# Anexar relatórios para impressão no painel da classificação de risco

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | Atendimento - Painel Classificação de Risco |
| **Requisito (ISSUE):** | PCREQ-6796 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

Implementação possibilita que ao selecionar um registro na lista que contém informações do paciente, o médico inclua um relatório para o paciente.

Para o médico anexar um relatório basta clicar "**Imprimir**", ele visualizará os dados do paciente em uma tela para anexar o relatório desejado. Na tela de visualização o médico poderá incluir o relatório na opção de menu **Anexos / Relatórios**. Ao realizar a vinculação do relatório o anexo ficará cadastrado no registro do atendimento do paciente.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.7.

1. Aplique o patch do chamado e execute uma vez a rotina **Painel de Classificação de Risco**.

## Procedimento para Utilização

1. Acesse o menu **Atendimento**.
2. Selecione a opção a **Pronto Atendimento/ Ambulatório/ Painel de Classificação de Risco**.
3. Selecione um registro em atendimento.
4. Clique em **Imprimir**.
5. Selecione o registro na tela de visualização.
6. Clique no menu **Anexos / Relatórios**.
7. Inclua o relatório desejado.
