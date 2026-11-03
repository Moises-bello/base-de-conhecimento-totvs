---
article_id: 360026117092
category: Atualização
content_hash: c5074c5471a90e44683256b7a8640a4935d55b63bf236eedd676d4972a2d6c06
fetched_at: '2026-06-28T22:42:21.297666+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus - Ambiente com Empresa Teste e Dicionário no Banco
type: support-article
updated_at: '2024-03-26T12:59:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026117092-Framework-Linha-Protheus-Ambiente-com-Empresa-Teste-e-Dicion%C3%A1rio-no-Banco
---

**Dúvida**  
Como acessar um novo ambiente para testes com Dicionário de Dados no Banco de Dados?  
  
**Ambiente**  
Protheus - AppServer - Versão 12  
  
**Solução**  
Para acessar um ambiente com a Empresa Teste (99) com Dicionário de Dados no Banco de Dados, siga os passos abaixo:  
1. Para utilização do ambiente com o **Dicionário de Dados no Banco de Dados**, é necessário o apontamento para um **License Server Virtual**(igual ou superior a 01.03.013). No caso de utilização da Empresa Teste (99), basta apenas que o License Server Virtual seja instalado e não configurado.  
  
2. Ao instalar o License Server Virtual, no momento da configuração do Totvs ID **cancele** a tela e **finalize** o Wizard de Configuração.  
  
3. Neste cenário, o ambiente Protheus com Dicionário de Dados no Banco de Dados irá utilizar o LS Virtual, porém **não validara as licenças**, e assim poderá acessar o ambiente com a Empresa 99 com **dois acessos simultâneos**.
