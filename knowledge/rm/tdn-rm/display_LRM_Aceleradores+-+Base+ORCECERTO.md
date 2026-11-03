---
content_hash: 52610be258f61c2a92d7c7bb35c33dd63d37769c36ba981162065a54600b124f
fetched_at: '2026-06-29T00:05:53.986827+00:00'
page_id: '1072712334'
product: rm
source: tdn-rm
title: Aceleradores - Base ORCECERTO
type: documentation
url: https://tdn.totvs.com/display/LRM/Aceleradores+-+Base+ORCECERTO
version: 2
---

Para testar o acelerador de implantação **Base ORCECERTO**, pode ser necessário fazer algumas alterações na base exemplo.

Ao acionar o menu "Projeto | Aceleradores de Implantação | Base ORCECERTO", se for apresentado o banner abaixo, significa que a base não tem esta integração ativa.

A solução é rodar o script abaixo:

*update mpar*  
*set LOGINPINI = '11444777000161',*  
*SENHAPINI = '02B73FC798E933EA2C647486D4561F75',*  
*WEBSERVICEPINI = '<http://webservice.orcecerto.com.br/WebService.asmx?WSDL>',*  
*TIPOINTEGRACAORECURSOS = 0;*

O conteúdo do campo LOGINPINI é um CNPJ que deve estar em uma das filiais cadastradas na base. Se não estiver, é necessário incluir ou alterar uma delas, preenchendo este CNPJ.

Após logar no sistema novamente e acionar o menu, esta tela deverá ser exibida:

Informe a senha "senha-testesenha-teste3"
