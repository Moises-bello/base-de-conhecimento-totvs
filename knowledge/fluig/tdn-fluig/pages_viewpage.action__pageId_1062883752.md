---
content_hash: 77d3cb7680e5e66c0934302ca2c3d0e058526a0909688f788ddac49c16b13411
fetched_at: '2026-06-28T21:35:17.444480+00:00'
page_id: '1062883752'
product: fluig
source: tdn-fluig
title: Guia de atualização front-end da 1.8.2 para a 2.0.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1062883752
version: 18
---

2.\*ndice

## TL;DR - Atualização do Fluig 1.8.2 (Mist) para 2.0.0 (Voyager)

### O que mudou

* Toda interface do Fluig foi reconstruída utilizando o **Animalia Design System**
* Uso massivo de **Design Tokens (CSS variables – `var(--...)`)** ao invés de cores fixar em hexadecimais
* Suporte a **tema claro/escuro (dark mode)**
* Alterações em **classes CSS, estrutura HTML e comportamento de componentes**

### O que mais impacta nas customizações

* CSS com **cores fixas (hex/rgb)**
* **Override de classes padrão** (`.btn`, `.panel`, etc.)
* Uso excessivo de `!important`
* Dependência de **estrutura HTML interna**
* Scripts que manipulam DOM de componentes Fluig

### O que você precisa fazer

* Substituir valores fixos por **tokens (`var(--fs-...)`)**
* Evitar override global, **isolar CSS no seu widget ou formulário**
* Não depender de classes/HTML internos do Fluig
* Revisar JS que manipula elementos diretamente
* Testar customizações em **tema claro e escuro**

### Comece por aqui

1. Procure por cores fixas no seu CSS
2. Identifique overrides de classes padrão
3. Revise scripts que acessam DOM diretamente
4. Teste sua customização na 2.0 (tema claro + escuro)

## Contexto

A versão 2.0.0 (Voyager) do Fluig trouxe uma evolução significativa na camada visual da plataforma, com a adoção do [Animalia Design System (design system oficial da TOTVS)](https://doc.animaliads.io/), alinhado ao [PO UI](https://po-ui.io/), biblioteca de componentes Angular, Open Source da TOTVS.. Essa mudança introduziu um novo padrão de estilos baseado em design tokens (CSS variables), além de melhorias em usabilidade, acessibilidade e suporte a temas (como modo claro e escuro).

Como parte dessa evolução, diversos componentes do Style Guide foram revisados, incluindo estrutura HTML, classes CSS e comportamento visual.

Customizações desenvolvidas na versão 1.8.2, principalmente aquelas que sobrescrevem estilos diretamente (CSS) ou dependem da estrutura interna dos componentes, podem sofrer impactos na versão 2.0.0, resultando em diferenças visuais ou funcionais.

Este guia tem como objetivo auxiliar na identificação e adequação dessas customizações, tanto em widgets quanto em formulários, reduzindo os impactos e facilitando o processo de atualização.

## Principais mudanças que causam quebra

A versão 2.0.0 introduziu mudanças estruturais na forma como os estilos e componentes são definidos e aplicados na plataforma. Essas mudanças impactam diretamente customizações existentes, principalmente aquelas que dependem de comportamento interno do Style Guide.

Abaixo estão os principais pontos de atenção:

### Adoção de Design Tokens (CSS Variables)

Os estilos passaram a ser controlados por variáveis CSS (`var(--...)`), centralizando cores, espaçamentos, tipografia e demais propriedades visuais.

**Impacto:**

* Valores fixos (ex: `#fff`, `16px`) podem gerar inconsistências visuais
* Customizações deixam de acompanhar automaticamente mudanças de tema
* Overrides diretos tendem a perder prioridade ou não funcionar como esperado

### Suporte a temas (Claro / Escuro)

A plataforma agora suporta variações de tema, alterando dinamicamente cores e outros estilos.

**Impacto:**

* Customizações com cores fixas não se adaptam ao tema
* Problemas de contraste e legibilidade podem surgir
* Componentes customizados podem apresentar comportamento inconsistente

### Revisão de componentes do Style Guide

Diversos componentes (como abas, botões, formulários, tabelas, etc.) foram atualizados para aderir ao novo Design System.

**Impacto:**

* Alterações em classes CSS e estrutura HTML
* Mudança no comportamento visual de estados (hover, ativo, foco, etc.)
* Customizações baseadas em classes antigas podem deixar de funcionar

### Centralização e aumento de prioridade dos estilos padrão

Os estilos da plataforma passaram a ter maior controle e prioridade na aplicação, visando consistência visual.

**Impacto:**

* CSS customizado pode ser sobrescrito com mais frequência
* Necessidade de maior especificidade para aplicar customizações
* Uso de `!important` tende a gerar conflitos e efeitos colaterais

### Mudanças de escopo e aplicação global de estilos

Parte dos estilos que antes estavam limitados a contextos específicos passaram a ser aplicados de forma mais global (ex: via `:root`).

**Impacto:**

* Alterações no comportamento de herança de estilos
* Possíveis conflitos com CSS existente
* Customizações dependentes de escopo anterior podem não funcionar corretamente

### Evolução contínua dos componentes

Os componentes do Style Guide passam a seguir um modelo mais evolutivo, alinhado ao Design System.

**Impacto:**

* Customizações diretas podem sofrer impacto em atualizações futuras
* Maior necessidade de desacoplamento entre código customizado e componentes padrão

### Resumo

De forma geral, os impactos ocorrem quando a customização:

* Depende de valores fixos (cores, espaçamentos, etc.)
* Sobrescreve estilos padrão diretamente
* Utiliza classes ou estrutura interna dos componentes
* Não considera variações de tema

## Como identificar problemas na sua customização

Antes de iniciar os ajustes, é importante identificar se sua customização está utilizando padrões que podem ser impactados pelas mudanças da versão 2.0.0.

Use o checklist abaixo para avaliar rapidamente seus widgets e formulários:

### Estilos (CSS)

* Uso de cores fixas (`#fff`, `#000`, `rgb(...)`, etc.)
* Uso de valores fixos de espaçamento (`margin`, `padding`, `font-size`, etc.)
* Uso de `!important` para forçar estilos
* Override de classes padrão (ex: `.btn`, `.panel`, `.nav-tabs`, etc.)
* CSS aplicado de forma global (sem escopo de widget/formulário)

### Estrutura (HTML)

* Dependência de estrutura interna de componentes (ex: `.nav > li > a`)
* Uso de seletores muito específicos ou frágeis
* Alterações diretas em HTML gerado por componentes do Fluig

### Comportamento (JavaScript)

* Scripts que manipulam diretamente elementos do DOM de componentes do Fluig
* Uso de seletores baseados em classes internas do Style Guide
* Dependência de eventos ou comportamento não documentado

### Widgets

* CSS ou JS global afetando múltiplos widgets
* Falta de isolamento de estilos (escopo próprio)
* Customizações visuais aplicadas diretamente em componentes padrão

### Formulários

* Estilos definidos diretamente no HTML (`<style>`)
* Customizações replicadas em vários formulários (sem padronização)
* Dependência de comportamento visual específico (ex: abas com cor customizada)

### Sinais comuns de problema após a atualização

Se após a atualização você identificar algum dos comportamentos abaixo, é provável que sua customização esteja sendo impactada:

* Estilos não estão sendo aplicados como antes
* Cores ou espaçamentos foram alterados inesperadamente
* Componentes (abas, botões, inputs, etc.) mudaram de aparência
* Customizações funcionavam na 1.8.2 e não funcionam mais na 2.0.0
* Diferenças visuais entre tema claro e escuro

### Como usar este checklist

* Marque os itens que se aplicam ao seu cenário
* Priorize a correção dos itens mais críticos (CSS global, overrides, etc.)
* Utilize as próximas seções deste guia para adequar cada tipo de problema

**Dica importante**: Quanto mais sua customização depender de detalhes internos do Style Guide, maior a chance de impacto na atualização.

## Guia de adequação

Esta seção apresenta os principais cenários de impacto e como adequar suas customizações para a versão 2.0.0.

Cada exemplo segue o padrão:

* Problema
* Causa
* Como corrigir

### CSS / Estilo

#### Uso de cores fixas

**Problema**  
Customizações utilizam cores fixas (hex, rgb), que não se adaptam ao novo padrão visual e aos temas.

**Causa**  
Na versão 2.0, as cores são controladas por design tokens (`var(--...)`), permitindo variação por tema.

**Antes (1.8.2)**

cssExemplo uso de cores fixas - Antestrue

**Depois (2.0.0)**

cssExemplo uso de cores fixas - Depoistrue

#### Override de classes padrão

**Problema**  
Customizações sobrescrevem classes do Style Guide (ex: `.btn`, `.nav-tabs`), gerando conflitos.

**Causa**  
Componentes foram atualizados e passaram a ter maior controle de estilos.

**Antes (1.8.2)**

cssExemplo override de classes padrão - Antestrue

**Depois (2.0.0)**

cssExemplo override de classes padrão - Depoistrue

**Boa prática**

* Evitar override global
* Aplicar estilos dentro de um escopo próprio (ex: classe do widget)

#### Uso de `!important`

**Problema**  
Uso excessivo de `!important` para forçar estilos.

**Causa**  
Na 2.0, isso tende a gerar conflitos com o Design System.

**Como corrigir**

* Aumentar a especificidade do seletor
* Evitar uso de `!important` sempre que possível

#### Espaçamentos fixos

**Problema**  
Uso de valores fixos de espaçamento (`px`, `rem`, etc.)

**Causa**  
O Design System padroniza espaçamentos via tokens.

**Antes (1.8.2)**

cssExemplo espaçamentos fixos - Antestrue

**Depois (2.0.0)**

cssExemplo espaçamentos fixos - Depoistrue

### HTML / Estrutura

#### Dependência de estrutura interna

**Problema**  
Customizações dependem da estrutura HTML interna dos componentes.

**Causa**  
Essa estrutura pode ter sido alterada na 2.0.

**Antes (1.8.2)**

cssExemplo dependência de estrutura interna - Antestrue li > a {
color: yellow;
}]]>

**Depois (2.0.0)**

cssExemplo dependência de estrutura interna - Depoistrue

**Boa prática**

* Evitar seletores baseados em estrutura interna
* Criar classes próprias para estilização

### JavaScript

#### Manipulação direta de DOM

**Problema**  
Scripts manipulam diretamente elementos de componentes do Fluig.

**Causa**  
Mudanças internas podem quebrar seletores e comportamento.

**Antes (1.8.2)**

jsExemplo JavaScript - Antestrue

**Depois (2.0.0)**

jsExemplo JavaScript - Depoistrue {
tab.addEventListener('click', () => {
tab.classList.add('ativo');
});
});]]>

**Boa prática**

* Evitar dependência de classes internas
* Controlar comportamento via classes próprias

### Widgets

#### Falta de isolamento de estilos

**Problema**  
CSS global afeta múltiplos widgets.

**Causa**  
Mudanças globais agora têm maior impacto.

**Como corrigir**

cssExemplo Widgets - Como corrigirtrue

### Formulários

#### Customizações replicadas

**Problema**  
Mesma customização aplicada manualmente em vários formulários.

**Causa**  
Dificulta manutenção e adequação.

**Como corrigir**

* Centralizar estilos comuns
* Criar padrão reutilizável
* Evitar duplicação de código

#### Estilo inline no formulário

**Problema**  
Uso de `<style>` direto no HTML do formulário.

**Impacto**

* Difícil manutenção
* Maior chance de conflito

**Recomendação**

* Manter estilos organizados e padronizados
* Sempre que possível, isolar por contexto

### Resumo

As adequações seguem três princípios principais:

* **Evitar dependência de implementação interna**
* **Utilizar tokens e padrões do Design System**
* **Isolar e organizar customizações**

## Casos comuns

Esta seção reúne alguns dos cenários mais comuns encontrados após a atualização para a versão 2.0.0 e possíveis formas de adequação.

#ebecf0

#### @1 A cor da aba (tab) não está mais sendo aplicada

@1

---

### Sintoma

A aba ativa passa a utilizar a cor padrão do tema do Fluig, ignorando a customização existente.

### Causa

O componente de abas foi atualizado para aderência ao Animalia Design System e passou a ter maior controle sobre os estilos aplicados.

### Recomendação

* Revisar a especificidade do CSS customizado
* Evitar dependência apenas das classes padrão do componente
* Sempre que possível, aplicar estilos dentro de um escopo próprio do formulário/widget
#ebecf0

#### @2 Botões perderam customização visual

@2

---

### Sintoma

Botões passaram a utilizar cores, bordas ou espaçamentos diferentes da versão 1.8.2.

### Causa

Os estilos dos botões passaram a utilizar design tokens (`--btn-*`, `--fs-color-*`) e comportamento padronizado do Design System.

### Recomendação

* Evitar sobrescrever estilos globais como `.btn` ou `.btn-primary`
* Utilizar tokens CSS sempre que possível
* Aplicar customizações em escopo isolado
#ebecf0

#### @3 Campos de formulário ficaram diferentes visualmente

@3

---

### Sintoma

Inputs, selects e checkboxes apresentam diferenças de tamanho, borda, foco ou espaçamento.

### Causa

Os componentes de formulário foram revisados e passaram a utilizar novas variáveis de estilo (`--form-*`).

### Recomendação

* Revisar estilos fixos aplicados anteriormente
* Evitar dependência de estilos internos do componente
* Validar comportamento em diferentes temas
#ebecf0

#### @4 Customizações funcionavam na 1.8.2 e não funcionam mais na 2.0.0

@4

---

### Sintoma

Estilos ou scripts deixaram de funcionar após a atualização.

### Causa

A versão 2.0.0 introduziu mudanças estruturais em componentes, estilos e escopo de aplicação CSS.

### Recomendação

Verificar principalmente:

* Uso de classes internas do Style Guide
* Overrides globais
* Uso de `!important`
* Manipulação direta de DOM
#ebecf0

#### @5 Estilos estão sendo sobrescritos pelo tema do Fluig

@5

---

### Sintoma

Mesmo com CSS customizado, o visual continua seguindo o padrão do tema da plataforma.

### Causa

Os estilos padrão passaram a possuir maior controle e prioridade para garantir consistência visual.

### Recomendação

* Revisar especificidade dos seletores
* Evitar CSS global
* Isolar estilos no contexto do widget/formulário
#ebecf0

#### @6 Diferenças visuais entre tema claro e escuro

@6

---

### Sintoma

Componentes customizados apresentam problemas de contraste ou cores inadequadas em determinados temas.

### Causa

A plataforma passou a suportar temas dinâmicos utilizando design tokens e variações de cores.

### Recomendação

* Evitar cores fixas
* Utilizar variáveis CSS (`var(--...)`)
* Validar customizações nos diferentes temas disponíveis
#ebecf0

#### @7 Layouts e espaçamentos ficaram diferentes

@7

---

### Sintoma

Elementos apresentam alinhamento ou espaçamento diferente da versão anterior.

### Causa

A versão 2.0.0 introduziu novos tokens de espaçamento, borda e tipografia.

### Recomendação

* Revisar valores fixos (`margin`, `padding`, `font-size`)
* Utilizar tokens de spacing (`--fs-spacing-*`)
* Evitar ajustes visuais baseados em “compensação manual”
#ebecf0

#### @8 Uso excessivo de `!important`

@8

---

### Sintoma

Necessidade crescente de adicionar `!important` para manter customizações funcionando.

### Causa

Conflito entre estilos customizados e o novo padrão visual centralizado da plataforma.

### Recomendação

* Evitar escalada de especificidade
* Reestruturar CSS com escopo isolado
* Preferir seletores mais específicos ao invés de `!important`

## Documentações relacionadas

Além deste guia, recomendamos a consulta dos materiais abaixo para apoio no processo de adequação e migração para a versão 2.0.0 (Voyager):

### Desenvolvendo widgets compatíveis com modo escuro

Boas práticas e orientações para adaptar widgets ao suporte de temas (light/dark), utilizando design tokens e evitando problemas de contraste e estilização.

<https://tdn.totvs.com/pages/releaseview.action?pageId=965446583>

### Desenvolvendo formulários compatíveis com modo escuro

Guia com recomendações para desenvolvimento de formulários aderentes ao novo padrão visual da plataforma e compatíveis com os diferentes temas disponíveis.

<https://tdn.totvs.com/pages/releaseview.action?pageId=963559484>

### Principais mudanças de Front-end — Fluig Voyager 2.0.0

Documentação com visão geral das principais mudanças de front-end introduzidas na versão 2.0.0, incluindo alterações visuais, componentes e comportamentos da interface.

<https://tdn.totvs.com/pages/releaseview.action?pageId=976127718>

### Checklist de atualização Voyager (2.0)

Checklist com pontos importantes a serem validados durante o processo de atualização para a versão 2.0.0.

<https://tdn.totvs.com/pages/releaseview.action?pageId=963023914>
