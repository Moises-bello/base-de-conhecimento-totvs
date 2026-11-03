---
content_hash: a53d12481ca079ac4e0366692fd81bd70a9030d8c4c008cbb7680a898f03a77e
fetched_at: '2026-06-29T00:09:01.225283+00:00'
page_id: '372559399'
product: rm
source: tdn-rm
title: 1754713 DSAUGCIH-48 DT Diferenciação de acento no cadastro de antibiótico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372559399
version: 2
---

# DIFERENCIAÇÃO DE ACENTO NO CADASTRO DE ANTIBIÓTICO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Controle de Infecção Hospitalar |
| **Função:** | Cadastro de Antibiótico |
| **Situação/Requisito:** | O campo Código Externo do registro de antibiótico não está realizando a diferenciação entre caracteres com ou sem acento em ambiente de banco de dados SQL Server no Ambiente Oracle esse comportamento é realizado como padrão. |
| **Solução/Implementação:** | O método de validação do campo Código Externo foi corrigido de forma a permitir a diferenciação de entradas de texto com e sem acento. |
