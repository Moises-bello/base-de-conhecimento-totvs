---
content_hash: 913285f0df3cef64c05186c6ffc345c6e553865ae380d166837d9c432b2a261c
fetched_at: '2026-06-29T00:09:17.413173+00:00'
page_id: '421388585'
product: rm
source: tdn-rm
title: Layout Registro Online
type: documentation
url: https://tdn.totvs.com/display/LRM/Layout+Registro+Online
version: 4
---

O Layout Registro Online foi criado para cadastrar os dados do registro online dos boletos e enviar para o banco. Através desses layouts, é possível de uma forma mais flexível, definir as informações que serão enviadas, com a possibilidade de utilização de fórmulas.

Na visão de banco no menu Anexo | Layout Registro Online, realize o cadastro de um novo campo.

É necessário liberar permissão no perfil para o acesso a inclusão e exclusão da Associação dos campos do Registro Online.

O Item 'Campo' quando salvo, não poderá mais ser editado, tornando chave do cadastro, e irá salvar os dados que o banco disponibilizar.

**Obs**.: O campo deverá ser cadastrado conforme arquivo do banco.

O item 'Descrição' foi criado com a flexibilidade para permitir inserir qualquer informação para identificação do registro cadastrado.

Exemplo

Banco: 033 - Santander  
Ao realizar um novo cadastro preencher o 'campo' com 'TITULO.DT\_VENCTO' (conforme descrito no arquivo do banco)

**Observação**

Foi disponibilizado no sistema Conceitos do módulo de Integração para realizar a importação e exportação dos cadastros de Campos do Layout do Registro Online.

Veja também

* [Documentação técnica complementar](https://tdn.totvs.com/display/LRM/DT+Cadastro+de+Layout+do+Registro+Online)
