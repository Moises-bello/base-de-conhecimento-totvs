---
content_hash: be885cdcddb73252db17c8ea15a379478062de9ff8c2ad5786eae202ed9d429b
fetched_at: '2026-06-29T00:12:01.630623+00:00'
page_id: '896389211'
product: rm
source: tdn-rm
title: '10 - Validando seus testes: Como garantir que eles funcionam'
type: documentation
url: https://tdn.totvs.com/display/LRM/10+-+Validando+seus+testes%3A+Como+garantir+que+eles+funcionam
version: 7
---

Para todo teste automatizado criado, se faz necessário ter uma validação.   
Fazer esta validação é muito importante para conseguirmos realmente validar a eficácia do teste automatizado, garantindo que o mesmo foi bem-sucedido, verificando em diversos pontos do sistema onde o teste tem integrações. No TOTVS Automação de Testes, temos várias atividades para validar os testes automatizados como: Comparação de Arquivos, Comparação de diretórios, Comparação de Banco, API´s, Código C#.

## Utilizando o Mock

Mocks são objetos simulados que reproduzem o comportamento de objetos reais em um ambiente controlado.

Na atividade de Comparação de Banco de dados temos a opção de criar um Mock.  
(Saiba mais sobre esta atividade clicando [aqui](https://tdn.totvs.com.br/pages/releaseview.action?pageId=689067178#Comocadastrar-1381411668))

* Avalie o que será salvo no Mock e quais dados fazem sentido para o seu teste. Como o objetivo é a reexecução dos testes automatizados em diferentes datas, campos relacionados a data não podem estar no Mock, pois sempre apresentarão diferenças.Dica

Nunca utilize select \* from no Mock.

[← Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=896386855) | [Próximo →](https://tdn.totvs.com/pages/viewpage.action?pageId=896390218)
