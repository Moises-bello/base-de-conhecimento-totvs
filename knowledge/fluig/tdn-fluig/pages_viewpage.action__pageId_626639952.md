---
content_hash: a6a2b1d98548aeec1f6301474d6acfcb22015a7050f8f06799f24b73fb83fcc0
fetched_at: '2026-06-28T21:35:28.260138+00:00'
page_id: '626639952'
product: fluig
source: tdn-fluig
title: Logoff automático por inatividade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626639952
version: 10
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar os procedimentos necessários para a configuração de um Logoff automático por inatividade no TOTVS Fluig Plataforma.

# Considerações iniciais

Nativamente, o TOTVS Fluig Plataforma não possui logoff automático, pelo contrário, uma sessão permanece válida enquanto uma página do produto estiver aberta no navegador.

Porém é simples de implementar, utilizando uma customização.

# Implementando Logoff automático

O  logoff automático demonstrado aqui utiliza a técnica de .

false0.5falseLogoff automaticofadetrue1Passo 1

Baixe o arquivo  e procure a seguinte linha:

var TEMPO\_EM\_MINUTOS = 30;

Altere o valor para o tempo (em minutos) desejado. Por padrão, o tempo de vida da sessão vem configurado como 30 minutos.

2Passo 2

Por padrão também, quando o usuário estiver visualizando um documento, o logoff nunca será feito. Se desejar mudar esse comportamento também para efetuar o logoff mesmo quando visualizando documento, procure pela seguinte linha:

var NAO\_EXPIRAR\_VISUALIZANDO\_DOCUMENTO = true;

e altere o valor de true para false:

var NAO\_EXPIRAR\_VISUALIZANDO\_DOCUMENTO = false;

3Passo 3

Copie o arquivo para a pasta **[diretório\_instalação]/repository/wcmdir/custompage,** mantendo o nome custompagehead.ftl.

**Obs:** Não é necessário reiniciar a plataforma. A alteração entra em vigor imediatamente.
