---
article_id: 115015967548
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 71d2184fa36b761ecbfb12c3483baa8a66582f7767ebe948088a35f977abc96c
fetched_at: '2026-06-28T22:40:32.464306+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 Tipos de Saldos
  Contábeis
type: support-article
updated_at: '2023-07-19T18:24:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015967548-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Tipos-de-Saldos-Cont%C3%A1beis
---

**Dúvida**Quais os tipos de saldo contábeis?  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.8 **Solução**Conceito:

O ambiente Contabilidade Gerencial permite que sejam controlados até 36 tipos de saldos diferentes para análises gerenciais, orçamentárias etc.

Para fins fiscais, todos os lançamentos contábeis gerados deverão obrigatoriamente utilizar o “1=Saldo Real".  
Para fins de análise gerencial, poderão ser utilizados todos os demais tipos de saldo (exceto o tipo Pré-Lançamento, porque este não grava Saldos).

O ambiente já possui 6 tipos pré-configurados (que podem ser identificados na tela de Lançamento Contábeis através de legenda própria). O tipo "Orçado" não é exibido no Lançamento Contábil.

* Orçado (este tipo é utilizado somente na rotina de Orçamentos)
* Real
* Previsto
* Gerencial
* Empenhado
* Pré-Lançamento (este tipo não movimenta saldos)

A manutenção nos tipos de saldos pode ser feita de duas formas:

1- Através do módulo SIGACFG na opção Cadastros -> Tabelas na tabela SL segue exemplo no padrão do sistema:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057299794)

2- Através da rotina CTBA130, opção Saldos contábeis:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11466844580759)

Para incluir por exemplo, selecione a opção incluir:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11466875130263)

Preencha as informações e confirme:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11466878612631)

Utilização:O ambiente Contabilidade Gerencial permite que o usuário utilize vários tipos diferentes de saldos, que posteriormente serão utilizados na emissão de relatórios e consultas

Casos as legendas não sejam apresentadas seguir os passos abaixo para criação da tabela responsável por apresentação das legendas:

Via configurador realizar os passos abaixo:  
   
Base de Dados -> Dicionario -> Base de dados:  
![](https://totvssuporte.zendesk.com/attachments/token/jQya4p0xsE8pnyujDOgLhphv4/?name=image.png)  
   
Em base de dados acessar as tabelas genéricas e buscar por tabela SM:  
![](https://totvssuporte.zendesk.com/attachments/token/ibFskMqUDeRYWO4HcW0WstkbZ/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/2LwP1XP84nqPqlUMvjxKppbgv/?name=image.png)  
   
Caso não exista esta tabela devera criar conforme abaixo:  
   
Selecionar Incluir:  
   
![](https://totvssuporte.zendesk.com/attachments/token/XOGJ7FT54idFQJuTsJjwESP0k/?name=image.png)  
   
E após inserir as informações conforme abaixo.  
![](https://totvssuporte.zendesk.com/attachments/token/xCsbw0t4MZlBHxahAUBB45oqW/?name=image.png)  
   
Após inserir as informações salve a criação.

Após os ajustes acima as legendas dos saldos serão apresentados corretamente.

Saiba mais:

https://tdn.totvs.com/pages/releaseview.action?pageId=648024154
