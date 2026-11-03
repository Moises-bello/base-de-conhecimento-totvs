---
content_hash: f08828005813b6d98005d7bf22ed38e7669afa519ed4bf3dc2a4211a69ed6d71
fetched_at: '2026-06-28T21:35:19.329943+00:00'
page_id: '201735552'
product: fluig
source: tdn-fluig
title: DES - Determinando campos invisíveis no formulário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201735552
version: 10
---

# Índice

4.\*ndicenone

# Plataforma

**Produto:**Fluig Studio

# Ocorrência

Método "setVisible=false" não executado na visualização do formulário através dos eventos de formulário (displayFields).

java


]]>java

# 

**Figura 1 - Criação de novo registro de formulário, contendo apenas o campo desejado visível para inserção.**

**Figura 2 - Visualização do formulário do novo registro inserido, exibindo também o campo que fora definido como invisível.**

# Causa

É uma característica do sistema mostrar todos os campos existentes no formulário, independente de métodos executados nos eventos.   
  
Estes eventos somente são considerados nas inclusões/modificações do formulário.

# Solução

Para setar a não visibilidade de determinado campo (setVisible=false), fora adequado para input type igual a "hidden" ao invés de "text" para o campo desejado.   
  
Desta forma, o campo permanecerá invisível para todas as etapas (inclusão/consulta e modificação).

java


]]>

# Observações

Para o evento displayFields, existe o método setShowDisabledFields, pela qual, serve para renderizar a visualização do formulário em seu formato original com os campos desabilitados, porém este não inclui a visualização de campos invisíveis.

java

**Figura 3 - Visualização de formulário com o método setShowDisabledFields ativo.**

java

**Figura 4 - Visualização de formulário sem o método setShowDisabledFields ativo.**
