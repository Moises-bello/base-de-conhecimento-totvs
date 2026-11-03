---
content_hash: 6fba62acb96c50db966102e85caaf54cd8325e3c7a0a773c01b096c0c39da450
fetched_at: '2026-06-29T00:12:01.622843+00:00'
page_id: '896384665'
product: rm
source: tdn-rm
title: 7 – Base de dados de automação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=896384665
version: 4
---

Compreender como funciona a base de automação e qual a melhor forma de utilizá-la, é primordial para a criação dos testes automatizados.  
A base de Automação é a base de dados do sistema que queremos testar. Se iremos automatizar testes do sistema RM, criamos um backup da base de produção do RM para se tornar a base de automação.

Base Fixa de Automação

Base de dados Fixa de Automação é quando utilizamos somente uma base predefinida para as execuções das automações. Esta base nunca será substituída por outra, mas ela pode ser atualizada de acordo com a necessidade.  
Optar por uma base fixa é uma prática que reduz o risco de falhas nos testes, especialmente para aqueles que dependem de dados específicos. Caso a base seja alterada ou substituída, os testes podem parar de funcionar, comprometendo a confiabilidade da automação. Para evitar a necessidade de uma base fixa, recomenda-se criar testes independentes de dados específicos. Esses testes devem ser capazes de configurar seus próprios cenários e dados de teste dinamicamente.

Base Temporária de Automação

Base temporária é a restauração do backup da base fixa de automação, onde os testes automatizados serão executados e após execução a mesma será descartada.  
A base temporária sempre é descartada pois não é possível executar os testes novamente nesta base após uma execução já realizada.

## 7.1 – Comportamento da base de automação no processo de execução de testes automatizados

Quando executamos um teste automatizado, temos os seguintes passos:

* Restauramos o backup da **Base Fixa de Automação;**
* Esta base restaurada será a **Base Temporária;**
* Executamos os testes automatizados na **Base Temporária;**
* Excluímos a **Base Temporária.**

## 7.2 – Evolução da Base Fixa de Automação

Quando adotamos o uso de uma **Base Fixa de Automação**, não quer dizer que ela não possa evoluir.   
Se for implementado uma nova fórmula Visual, algum parâmetro precisa ser alterado ou for necessário criar novos dados na minha base fixa de automação,  podemos sim evoluir a base  de Automação. Para isso, restauramos a **Base Fixa de Automação**, realizamos as alterações, criamos um backup desta base e substituímos o backup da **Base Fixa de Automação**.

O Armazenamento e backup da **Base Fixa de Automação** é de fundamental importância pois seus testes automatizados utilizam dados que estão nesta base. A perda desta base acarretará na manutenção das automações existentes.

[← Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=896383882) | [Próximo →](https://tdn.totvs.com/pages/viewpage.action?pageId=896384883)
