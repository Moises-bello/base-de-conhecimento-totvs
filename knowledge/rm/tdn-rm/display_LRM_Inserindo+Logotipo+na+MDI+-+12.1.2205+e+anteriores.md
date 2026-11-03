---
content_hash: 996bcb32e48529f71872e921404b0e364181602775bb5e8acf76815363c48980
fetched_at: '2026-06-29T00:11:18.101823+00:00'
page_id: '683181047'
product: rm
source: tdn-rm
title: Inserindo Logotipo na MDI - 12.1.2205 e anteriores
type: documentation
url: https://tdn.totvs.com/display/LRM/Inserindo+Logotipo+na+MDI+-+12.1.2205+e+anteriores
version: 2
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

A nova MDI tem diversas funcionalidades, uma delas é a opção de colocar a Logotipo da empresa, porém, a partir da versão 12.1.X o botão Esquema de cores não está disponível, por padrão, no menu do sistema devido a otimizações de desempenho.

A inclusão de uma imagem ou logomarca na visão do RM só é possível utilizando o Esquema de Cores **Sample** de acordo com a versão do sistema. E necessária permissão de **LEITURA** e **GRAVAÇÃO** no **DIRETÓRIO** onde se encontra a imagem.

## **02. EXEMPLO DE UTILIZAÇÃO**

**Atividade:**

1. **Acesse:** Serviços Globais | Administração | Configurações

2. Vá para a aba personalizar e clique em "Carregar...".

Observação

Se a aba personalizar não estiver disponível, vá nas configurações globais e habilite os temas da MDI.

**Acesse:** Serviços Globais | Ambiente | Parâmetros | Parâmetros Globais | Performance

   

3. Após clicar em "Carregar...", selecione a imagem desejada e clique em "Aplicar".

4. Confira se a imagem escolhida passou a ser exibida.

Atenção!

Esta configuração **não** é possível de uso quando acessado o sistema por meio de **conexão remota** ou **TS**. Para habilitá-la é necessário adicionar a tag "**enableskin**" no atalho do aplicativo RM.exe

Para mais informações sobre a nova MDI .
