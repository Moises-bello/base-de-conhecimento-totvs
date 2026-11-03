---
content_hash: ea02e1f5620b2c186b2df237084fabd746a9d388b8aeaf8ca5bd4d2eca9dec06
fetched_at: '2026-06-29T00:11:26.479668+00:00'
page_id: '717715207'
product: rm
source: tdn-rm
title: Planilha Executiva (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=717715207
version: 18
---

**Passo 1: Marcar o parâmetro que ativa a planilha:**

O parâmetro "Utiliza Planilha Executiva" por default vem desabilitado nos parâmetros do projeto.

Ao habilitá-lo o sistema passa permitir o uso da .

Nessa visão dos parâmetros além de permitir ativar o uso, pode-se também personalizar o nome da planilha executiva, desde que respeite o tamanho de caracteres. Caso não preencha este campo e o deixe em branco o sistema sempre deixará default o nome "Planilha Executiva"

No campo máscara não será permitido informar números e espaço conforme a mesma regra para máscara de planilha de atividades/serviço.

Permitirá informar apenas # e . respeitando os níveis definidos.

**Observação:**Em uma estrutura com múltiplos níveis, apenas o item de último nível exibirá as abas 'Vínculos' e 'Planejamento / Avanço Físico'. Além disso, apenas neste item, os campos 'Quantidade', 'Unidade' e 'Valor Unitário' serão obrigatórios.

É possível fazer com que um item seja considerado de último nível, mesmo que não seja o último item na hierarquia da máscara. Para isso, basta preencher o campo 'Quantidade' com um valor maior ou igual a zero. Ao fazer isso, as abas 'Vínculos' e 'Planejamento / Avanço Físico' serão exibidas, e os campos 'Unidade' e 'Valor Unitário' se tornarão obrigatórios. No entanto, é importante observar que não é possível transformar um item com subitens em um item de último nível, nem adicionar subitens a um item de último nível, mesmo que a máscara permita mais itens.

É importante destacar que o nome definido nesse parâmetro é o nome que aparecerá na visão principal da planilha.

**Passo 2: Liberar acesso no perfil do usuário:**

Além de habilitar o parâmetro do projeto para poder utilizar a planilha executiva e personalizá-la, será necessário também dar permissão ao usuário:

**Atenção** : Somente depois que ativar o parâmetro "Utiliza Planilha Executiva" e a permissão concedida no perfil, é que será possível visualizar a mesma no menu do sistema.
