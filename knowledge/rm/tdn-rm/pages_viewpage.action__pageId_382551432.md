---
content_hash: 29ca39301b35ef85f7432b552b73ed735f6ec8ddd288cfc7d779424ef964da09
fetched_at: '2026-06-29T00:09:04.119731+00:00'
page_id: '382551432'
product: rm
source: tdn-rm
title: 197952 DSAUGCIH-17 DT Atualização diária do parcial de cultura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382551432
version: 3
---

# Continuidade de Afastamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Controle de Infecção Hospitalar (CIH) |
| **Função:** | Cadastro de cultura parcial. |
| **Situação/Requisito:** | O cliente necessita de ajuda com a atualização diária do parcial de cultura. O sistema deve trazer todas as informações já alimentadas nos campos de 'Gram', 'Andamento' e 'Parcial' da 'Atualização' imediatamente anterior.  **Critérios de Aceite:** 1. Campos texto; 2. Quando 1º parcial sugerir para o campo 'Andamento" negativo até o momento; |
| **Solução/Implementação:** | Para acessar o recurso dentro do módulo CIH acessar o menu: Pacientes >> Internações >> Cultura Parcial (Imagem em anexo)  Implementação realizada conforme solicitação do cliente:  Ao realizar o primeiro registro de cultura parcial o campo "Andamento" será carregado com o valor padrão "Negativo até o momento.".  Durante a criação de novos registros as informações anteriores do ultimo registro serão carregadas para o novo registro. |
