---
content_hash: 66d485aad0f27f10d64a3b733edad57436eeb24e4d2c91003d1b0f6135e43ab0
fetched_at: '2026-06-29T00:11:55.922530+00:00'
page_id: '864983749'
product: rm
source: tdn-rm
title: Plugin Winforms - Download
type: documentation
url: https://tdn.totvs.com/display/LRM/Plugin+Winforms+-+Download
version: 17
---

## O que são?

**WinForms Plugins** são componentes fundamentais que permitem a renderização de interfaces gráficas do RM, proporcionando uma interação com os elementos visuais do sistema. Esses plugins viabilizam a automação no TOTVS Automação de Testes de fluxos de trabalho e a simulação da navegação e as ações do usuário, como cliques e entradas de dados, em diversas telas do RM.

## Para que servem?

Os **WinForms Plugins** são utilizados para que o TOTVS Automação de Testes consiga renderizar corretamente os componentes de interface do RM, possibilitando a execução de automações **WinForms**. Dessa forma, para realizar qualquer teste automatizado nas telas do RM através do TOTVS Automação de Testes, é imprescindível que esses plugins estejam incluídos na pasta Bin do RM. A presença desses plugins é essencial para garantir que o TOTVS Automação de Testes interaja com os elementos visuais do sistema.

# Exemplo de Uso

Como Baixar e Executar.Como Baixar e Extrair Arquivos

1. Navegue no menu TOTVS Automação de Testes e clique em **Downloads** → **WinFormsPlugin**e faça o download da versão dos Plugins de acordo com a versão do RM, após clicar na versão desejada, o arquivo .**zip** contendo o Plugin será baixado automaticamente.
   1. Plugin para a versão **RM 12.1.2410.x** ou **anterior.**
   2. Plugin para a versão **RM 12.1.2502.x** ou **superior.**
2. Após o download, Extraia o arquivo zip que deve conter uma pasta **TestFlow.**
3. Mova a pasta **TestFlow** para a pasta **TOTVS/CorporeRM/RM.Net** na qual você deseja executar a automação do **Winforms**.
5. Acesse a pasta e desbloqueie todos os arquivos com o seguinte comando:

5. Dê permissão FULL para o usuário **Everyone** na pasta.

---

# Saiba mais

Verifique se o usuário Everyone tem permissão Full na pasta.

Após baixar os plugins sempre conferir se os arquivos estão desbloqueados.

Caso você precise atualizar esses plugins, basta baixá-los novamente e substitua os antigos pelos novos.

---

# FAQ

**P:  Qual a finalidade dos WinForms Plugin?**

R:Esses plugins renderizam os componentes do RM, para que ele possa executar ações de usuário

**P: Recebi o seguinte log ao rodar minha automação Winforms: Não foi encontrado uma aplicação para teste.**

R: A pasta **TestFlow** não existe no diretório **TOTVS/CorporeRM/RM.Net**.
