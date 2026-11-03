---
content_hash: 755e6fc98fa5f3e1ec0f7f38ad84d9042bf36cf764fa10317acdc70112108152
fetched_at: '2026-06-29T00:11:03.322816+00:00'
page_id: '620774786'
product: rm
source: tdn-rm
title: Sistema - Campos Obrigatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=620774786
version: 7
---

### Introdução

---

Através desta visão é possível configurar e customizar todos os campos relacionados à pessoa, de modo que os mesmos possam ser bloqueados ou liberados de acordo com a parametrização.

### Controle de permissão por etapas da proposta

---

Será possível também, a partir da **versão 12.1.33,** fazer um controle de permissão baseado em etapas no botão **Selecionar Etapas**, onde todas as etapas serão exibidas. Ou seja, caso o usuário deseje avançar uma proposta para determinada situação o sistema irá primeiro verificar quais campos são obrigatórios em quais etapas para que se possa então avançar a proposta.

O Portal de Imóveis irá mostrar ao usuário numa mensagem de alerta, todos os campos que deverão ser preenchidos antes do avanço da etapa. Mostrará também de qual tabela o campo pertence, facilitando o ajuste por parte do usuário.

O sistema permite a seleção de várias etapas e permite também a copia das seleções para todos os outros campos.

Importante: Para a validação dos campos obrigatórios funcionarem é necessário que o parâmetro global "**Ativar validação de campos obrigatórios customizados**" esteja definido como **SIM.**

**Nota Importante sobre Campos Obrigatórios (Proposta vs. Pessoa)**

É crucial que a configuração de campos obrigatórios por etapa da "Proposta" considere apenas os campos disponíveis na tela de "Proposta".

Evite marcar como obrigatório qualquer campo que seja exclusivo da tela de "Pessoa" (como, por exemplo, o campo "Forma de Contato").

**O que pode ocorrer:** Se um campo exclusivo de "Pessoa" for exigido na "Proposta", o usuário enfrentará um bloqueio ao tentar criar um *novo prospect*. O sistema irá validar a obrigatoriedade do campo (ex: "Forma de Contato"), mas não fornecerá o referido campo na tela de "Proposta" para que ele seja preenchido, impedindo o avanço do processo.
