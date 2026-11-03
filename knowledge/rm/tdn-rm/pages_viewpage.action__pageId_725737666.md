---
content_hash: afed7ea885cae8f21c9155dbc33cc0a21ff477d9492236dbbe2666e33af99618
fetched_at: '2026-06-29T00:11:27.463342+00:00'
page_id: '725737666'
product: rm
source: tdn-rm
title: Configuração do RM para integrar ao Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=725737666
version: 9
---

# Introdução

---

O objetivo dessa página é mostrar como configurar o **RM** para integrar com o Smart View, possibilitando assim o acesso aos relatórios gerados no Smart View diretamente no RM.

A instalação do Smart View é demonstrada na página .

A integração com os relatórios do Smart View estará disponível no RM à partir da versão **12.1.2306.**

# Configurando o RM

---

### Configurando o DefaultDB

---

Em ambientes do RM que **NÃO** são **MULTI-TENANT**, para permitir a integração com o Smart View é necessário configurar o Alias padrão conforme detalhado em .

Em ambientes **MULTI-TENANT** não é necessário nenhuma configuração adicional no RM.

### Parametrizando URL Base

---

No RM, é necessário parametrizar a URL base do Smart View via Parâmetros Globais, conforme descrito abaixo:

1. Acessar o módulo "Serviços Globais"
2. Na aba "Ambientes", clicar em "Parâmetros" e em seguida em "Parâmetros Globais;
3. Navegar até a "Integração Smart View";
4. Preencher a URL base do Smart View e clicar em salvar.

Exemplo de configuração:

### Criando usuário RM

---

Verifique se o usuário RM existe no cadastro de usuários do seu sistema, caso não exista o mesmo deverá cadastrado.

Este usuário não precisa ter acesso a nada no sistema, inclusive pode estar inativo, mas precisa existir. Ele será utilizado internamente durante o processo de importação para criação do objeto.

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2306

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO

falseAutores
