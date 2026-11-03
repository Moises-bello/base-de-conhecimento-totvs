---
content_hash: c9f1ae05695bdc3968328a6f6226e49c53491cb4d07f030f532c22c891ebc55c
fetched_at: '2026-06-29T00:11:55.603239+00:00'
page_id: '862597885'
product: rm
source: tdn-rm
title: 2.6 - Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862597885
version: 6
---

# Índice

[2.6.1 - Soap](https://tdn.totvs.com/x/KHv_K)

[2.6.2 - Http](https://tdn.totvs.com/x/LHv_K)

# Preparando seu ambiente para testar WebServices e API'S

Preparação do ambiente.Preparação do Ambiente.

1. Atualize o RM na versão desejada;
2. Procure pelo arquivo **RM.Host.exe.config**, ele encontra-se na pasta bin do RM em questão;
3. Edite esse arquivo, inserindo as seguintes keys necessárias para uso de WebService e API'S;

]]>

4. Salve o arquivo;

Caso realize alterações no arquivo com o **RM.Host.exe** em execução, lembre-se de reiniciar a aplicação para que as mudanças sejam aplicadas.

É obrigatório existir um Alias com o nome **CorporeRM** que aponte para uma base válida do RM. Clique  [aqui](https://tdn.totvs.com/display/SUI/Configurando+o+alias) para mais informações de como criar um Alias no seu RM.
