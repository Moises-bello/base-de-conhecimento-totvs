---
content_hash: 2a4023d087455733ce0596f3bd8cff8c7ef1c6d92568bd254a9be46f282ce7a9
fetched_at: '2026-06-29T00:10:32.058895+00:00'
page_id: '525028260'
product: rm
source: tdn-rm
title: '[LGPD] - Log de Auditoria RM'
type: documentation
url: https://tdn.totvs.com/display/LRM/%5BLGPD%5D+-+Log+de+Auditoria+RM
version: 7
---

Em atenção às responsabilidades atribuídas pela LGPD ( Lei Geral de Proteção de Dados) o Log de Auditoria passou por melhorias, facilitando a rastreabilidade de alterações referentes a campos pessoais e/ou sensíveis.

### Implementação

A partir da versão 12.1.27 da Linha RM, ao ativar o Log de Auditoria todas as tabelas que possuam campos classificados como "Pessoal" serão automaticamente auditadas. Clientes que já utilizam esta ferramenta também terão suas configurações migradas automaticamente, garantindo a auditoria destas tabelas.

Campos classificados como "Pessoal" nas configurações do Dicionário de Dados não poderão ser selecionados no cadastro de "Exceções". Caso haja algum campo pessoal cadastrado como exceção, este será automaticamente desconsiderado durante a migração ou ativação do Log de Auditoria.

### Configuração de campos pessoais

A configuração dos campos pessoais/sensíveis é realizada a partir da rotina "Configurar Dicionário de Dados", disponível

### Comportamento esperado

O exemplo abaixo apresenta o comportamento esperado do Log de Auditoria ao parametrizar um campo como pessoal.

Na tela a seguir serão cadastrados quais os campos que são pessoais e, com  isso, a tabela será auditada automaticamente.

A partir da marcação acima, informando que o campo é pessoal, a tabela TUND será automaticamente auditada e assim não sendo possível ao usuário modificar este comportamento. Na tela de configuração os campos ficarão marcados e desabilitados, conforme imagem a seguir.

Quando um campo da tabela é classificado como pessoal, este mesmo campo também não poderá ser excepcionado.

Na rotina referente a exceções os campos pessoais estarão desmarcados e desabilitados.

### Referências

Documentação do Log de Auditoria: 

Configurar Dicionário de Dados:
