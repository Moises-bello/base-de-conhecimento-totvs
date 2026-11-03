---
content_hash: d7aae7b6cc5dfe81edce4aced145ce5a1fe9aba8ba0b12ce1d98b66e9e582d80
fetched_at: '2026-06-29T00:09:50.680636+00:00'
page_id: '435106700'
product: rm
source: tdn-rm
title: FISCAL01-6998 DT Inclusão de lançamento - Carregar Defaults de Ajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435106700
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Inclusão de lançamento |
| **Situação/Requisito:** | Tratar o serviço de inclusão de lançamento para carregar os defaults de ajuste automaticamente. |
| **Solução/Implementação:** | Ao incluir um lançamento fiscal ou item do lançamento, os defaults associados à natureza devem ser carregados automaticamente |

**Inclusão do lançamento fiscal**

Ao selecionar a Natureza (CFOP) do lançamento, o sistema carregará os ajustes associados à natureza pelo processo "Associação Códigos de Ajuste SPED Fiscal":

Neste momento, os valores estarão zerados e as fórmulas só serão executadas para o cálculo dos mesmos ao salvar.   
Atenção: Caso o usuário edite algum valor, o sistema não executará as fórmulas para o ajuste correspondente.

**Inclusão do item do lançamento fiscal**  
Os ajustes serão carregados na inclusão do item. De forma equivalente, os mesmos serão recuperados zerados e as fórmulas só serão executadas após salvar o lançamento fiscal.  
Atenção: Caso o usuário edite algum valor, o sistema não executará as fórmulas para o ajuste correspondente.

**Edição do lançamento/Item do lançamento**Ao alterar um registro de código de ajuste de lançamento/item, os valores serão zerados.   
Os mesmos serão recalculados com as respectivas fórmulas, após salvar o lançamento:

O mesmo ocorre se os valores forem zerados manualmente. Assim, caso seja necessário executar novamente as fórmulas, basta zerar todos os valores.

**Escrituração Fiscal**

Ao escriturar um lançamento fiscal, o sistema também carregará os ajustes associados à natureza, já com os valores calculados pelas respectivas fórmulas.
