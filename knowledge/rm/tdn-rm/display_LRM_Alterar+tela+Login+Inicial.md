---
content_hash: f497e41558fd96a7130f081121e5ec45671dabbc966ec300d43e6ae983fb822a
fetched_at: '2026-06-29T00:08:36.044455+00:00'
page_id: '284334296'
product: rm
source: tdn-rm
title: Alterar tela Login Inicial
type: documentation
url: https://tdn.totvs.com/display/LRM/Alterar+tela+Login+Inicial
version: 7
---

# Alterar tela Login Inicial

|  |  |
| --- | --- |
| **Produto:** | RM |
| **Versões:** | 12.1.16 ou Superiores |
| **Ocorrência:** | Alterar tela Login Inicial |
| **Ambiente:** | RM Portal |
| **Passo a passo:** | Introdução Neste manual iremos mostrar procedimento para alterar tela de login inicial do portal.  Passo a Passo  1 - Alterar Ordem. **1.1 -** Através da MDI acesse o contesto “Gestão de Conteúdo”        **1.2 -** Acesse o menu “Menu Portal”      **1.3 -** Através do menu aberto adicionar um novo registro        Através da tela é possível selecionar a tela inicial do portal.  **2 -** No Exemplo abaixo iremos realizar configuração para tela ser aberta diretamente no “Educacional”    **2.1 -** Adicionar novo registro na opção “Identificador do Menu Pai”    Iremos selecionar o menu “Educacional”      Após selecionar basta alterar a “Ordem de apresentação” para ‘1’. Desta forma registro irá se tornar o primeiro da lista. Quando portal for aberto irá cair diretamente na página do Educacional    **2.2  –** Salvar registro      **3 –** No servidor que portal estiver instalado, editar o arquivo “Web.config” localizado na pasta (COPORE.NET)  No Arquivo localizar a tag (<add key="LoadDefaultMenuOnLogin" value="false" />)  Na tag alterar o valor de false para “true”  Antes da alteração  <add key="LoadDefaultMenuOnLogin" value="false" />    Após alteração  <add key="LoadDefaultMenuOnLogin" value="true" />    **4 –** Aplicação no portal  Com registro salvo basta entrar no portal para que sistema abre diretamente no módulo selecionado.  Antes do registro salvo      Depois do Registro Salvo |
| **Observações:** | Não é possível configurar os módulos **Automação de Ponto**, **Folha de Pagamento**, **Gestão Bibliotecária** e **Gestão de Estoque, Compras e Faturamento** para abrir como default pois os mesmos estão associados à outros módulos.  Somente é possível adicionar o módulo associado para ser aberto como default.  Automação de Ponto e Folha de Pagamento estão associados ao **Gestão de Pessoas**.  Gestão Bibliotecária está associado ao **Educacional.**  Gestão de Estoque, Compras e Faturamento está associado ao **Gestão Financeira.  Por exemplo:** Caso o cliente deseje configurar o Gestão de Estoque, Compras e Faturamento para abrir como default, será possível apenas configurar o Gestão Financeira, acessando esse aplicativo será possível acessar o contexto do Gestão de Estoque, Compras e Faturamento, conforme exemplo no print abaixo:  Somente é possível adicionar o módulo Gestão Financeira:  Após a configuração, ao acessar o RM Portal será apresentado o módulo Financeiro e à partir dele poderá realizar o acesso ao Gestão de Estoque, Compras e Faturamento: |
