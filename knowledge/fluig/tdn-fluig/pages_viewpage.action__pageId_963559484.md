---
content_hash: 01a8f046a012deb342a0e9a9132e8d8dd39ee96e61a2de2fe44fbc84b64dfd39
fetched_at: '2026-06-28T21:35:31.696843+00:00'
page_id: '963559484'
product: fluig
source: tdn-fluig
title: Desenvolvendo formulários compatíveis com modo escuro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963559484
version: 19
---

# Visão geral

---

O Fluig agora oferece suporte nativo ao modo escuro, proporcionando uma experiência visual mais confortável em ambientes com pouca luz.

Essa funcionalidade já está disponível nos formulários da plataforma e é habilitada automaticamente de acordo com o tema escolhido pelo usuário no Fluig.

Importante:

Para que seu formulário fique compatível com o modo escuro, é fundamental seguir as orientações abaixo, principalmente se o formulário possui estilos customizados ou utiliza plugins de terceiros.

## Como o modo escuro funciona internamente

---

O modo escuro é ativado automaticamente pela plataforma quando o usuário escolhe esse tema. Internamente, isso é feito adicionando a classe `theme-dark` na tag `<html>` do formulário.

Com essa classe presente, o navegador passa a utilizar as variáveis CSS definidas dentro do seletor `html.theme-dark { ... }`, substituindo as definidas em `:root`.

**Exemplo simplificado:**

cssRDark

Quando o modo escuro está ativo, os componentes e estilos que utilizam variáveis CSS (como `var(--fs-color-neutral-light-00)`) automaticamente herdam os valores definidos dentro de `html.theme-dark`.

Informação:

Isso permite alternar entre temas sem precisar alterar nenhuma estrutura de código no formulário — basta usar as variáveis CSS corretamente.

## Boas práticas

---

✔ Priorize sempre o uso dos componentes e estilos do Style Guide Fluig.  
✔ Evite o uso de cores fixas ou hardcoded no CSS.  
✔ Teste o formulário tanto no tema claro quanto no modo escuro antes de publicar.  
✔ Consulte periodicamente o Style Guide para novas variáveis e atualizações.

## O que já funciona automaticamente

---

* **Componentes padrão do Style Guide Fluig:**  
  Todos os componentes visuais do Style Guide já estão preparados para o modo escuro. Se seu formulário utiliza apenas esses componentes, **nenhuma ação é necessária**.
* **Ativação automática:**  
  O modo escuro do formulário acompanha automaticamente o tema selecionado pelo usuário no Fluig. Não é necessário alterar código para detectar ou ativar o tema.

## Como adaptar um formulário customizado para o modo escuro

---

### 1. **Revisão do CSS Customizado**

Caso seu formulário tenha estilos próprios definidos via CSS, é necessário substituir cores fixas por variáveis CSS disponibilizadas pela plataforma.

### **Exemplo de substituição:**

**Antes:**

cssRDark

**Depois (compatível com modo escuro):**

cssRDark

### 2. **Onde encontrar as variáveis CSS**

Todas as variáveis disponíveis estão documentadas no **Fluig** **Style Guide**, na seção: **CSS > Themes - https://<SEU\_DOMINIO>/style-guide/css.html#themes**

Ali você encontra a lista completa de variáveis para cores, sombras, bordas, backgrounds e outros aspectos visuais.

Caso seja necessário definir cores manualmente, **siga estas diretrizes:**

**Direcionamentos Gerais**

| Tipo de Cor | Variável CSS a Utilizar |
| --- | --- |
| Cor de texto "padrão" | var(--fs-color-neutral-dark-90) |
| Cor de texto "padrão" hover ou focus | var(--fs-color-neutral-dark-95) |
| Cor de fundo (geralmente branco) | var(--fs-color-neutral-light-00) |
| Cor de fundo cinza claro | var(--fs-color-neutral-light-05) ou var(--fs-color-neutral-light-10) |
| Cor de fundo cinza com destaque maior | var(--fs-color-neutral-light-20) |
| Cor de borda "padrão" | var(--fs-color-neutral-light-20) ou var(--fs-color-neutral-light-30) |

## Atenção com plugins de terceiros

---

Se o formulário utiliza bibliotecas ou plugins visuais de terceiros, é necessário:

* Verificar se o plugin suporta tema escuro nativamente.
* Caso não suporte, sobrescrever os estilos do plugin utilizando as variáveis CSS do Fluig.

## Exemplo de formatação customizada compatível

---

**HTML:**

xmlRDark

# Meu Formulário
