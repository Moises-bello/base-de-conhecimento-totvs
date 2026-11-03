---
article_id: 360029298831
category: Configurador
content_hash: 137c9b38ff6a9ac0347f76eac8c09285883a937b00a3029c55567d68c0a9a399
fetched_at: '2026-06-28T22:42:19.274305+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Usuário com configuração de diretório de impressão
  inválida
type: support-article
updated_at: '2025-10-22T12:39:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029298831-Framework-Linha-Protheus-Usu%C3%A1rio-com-configura%C3%A7%C3%A3o-de-diret%C3%B3rio-de-impress%C3%A3o-inv%C3%A1lida
---

**Dúvida**  
O que devo fazer quanto aparecer mensagem de configuração inválida de diretório de impressão?  
  
**Ambiente**  
Protheus - Configurador - Todas as versões  
  
**Solução**  
Na configuração do usuário, quando o Ambiente de impressão padrão estiver definido como Servidor, a pasta indicada no Diretório de impressão padrão deverá indicar um caminho da estrutura de pastas do Protheus, mais especificamente abaixo da RootPath. Já quando o Ambiente de impressão padrão estiver definido como Cliente, a pasta indicada no Diretório de impressão padrão deverá indicar um caminho absoluto do computador, como por exemplo C:\Spool\.  
![2019-06-07_1053.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030439091)  
  
Na configuração do usuário, se tentar utilizar o Ambiente de impressão padrão como Servidor e a pasta indicada for um caminho local, será exibido o alerta abaixo e não permitirá confirmar:  
![2019-06-07_1052.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030439291)  
  
Se tentar utilizar o Ambiente de impressão padrão como Cliente, e a pasta indicada for um caminho relativo da RootPath, o Configurador permitirá Confirmar, porém ao acessar o Protheus com este usuário, será exibida a mensagem abaixo, e no momento da impressão será perguntada qual pasta do computador quer que seja utilizada para a impressão:  
![2019-06-07_1051.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030439311)  
  
As configurações deverão ser analisadas tanto no usuário quanto nos grupos nos quais ele eventualmente esteja vinculado.
