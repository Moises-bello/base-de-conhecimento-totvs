---
article_id: 360021428711
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 75d47a9977b9563b06831c20a11148995a69be8601d481db43719c18e0dbeb1f
fetched_at: '2026-06-28T22:39:07.881368+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro THREAD ERROR:
  Nome de coluna ''CDV_PRODUT'' inválido.'
type: support-article
updated_at: '2021-11-15T13:04:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021428711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-THREAD-ERROR-Nome-de-coluna-CDV-PRODUT-inv%C3%A1lido
---

**Dúvida**Erro "THREAD ERROR: Nome de coluna 'CDV\_PRODUT' inválido" ao tentar excluir um produto no Cadastro de Produtos.  
  
**Ambiente**  
Microsiga Protheus –  Estoque – A partir da versão 12.1.17  
  
  
**Solução**

Em **Ambiente de Homologação,** efetue o procedimento abaixo.  
  
Retire o relacionamento da tabela CDV com a SB1 na SX9 pois no padrão não consta.  
  
    Index (0) :I\_RECNO    
    Index (1) :\*\*SX90101  X9\_DOM  
    Index (2) :SX90102  X9\_CDOM+X9\_DOM  
    Field 1: D\_E\_L\_E\_T\_E\_D(C) :   
    Field 2: R\_E\_C\_N\_O(N) :13767  
    Field 3: X9\_DOM(C) :**SB1**  
    Field 4: X9\_IDENT(C) :001  
    Field 5: X9\_CDOM(C) :**CDV**  
    Field 6: X9\_EXPDOM(C) :B1\_COD  
    Field 7: X9\_EXPCDOM(C) :**CDV\_PRODUT**

**Caso mesmo após realizar o procedimento acima o erro persista, siga os passos abaixo:**  
  
**1.** Criar o campo CDV\_PRODUT via configurador com as mesmas configurações do campo B1\_COD  
![](https://totvssuporte.zendesk.com/attachments/token/fpW7Ab1TPjDnugKa29Vl2yRzw/?name=inline1174003326.png)​![](https://totvssuporte.zendesk.com/attachments/token/ojictB24NfXOUeeM3WvnDkcgQ/?name=inline2085943114.png)​![](https://totvssuporte.zendesk.com/attachments/token/t820N4GJ9RLrfHIhC29M77JeJ/?name=inline304959759.png)​![](https://totvssuporte.zendesk.com/attachments/token/HY0mk27djTGEJKNziGO5zXUe4/?name=inline1218229649.png)​![](https://totvssuporte.zendesk.com/attachments/token/sTlkiXUvlEKCc9p5it5ZyBhN9/?name=inline-936278163.png)​![](https://totvssuporte.zendesk.com/attachments/token/xD6aC1jgVNslc2J0fNZYrXpfE/?name=inline-1537061242.png)​![](https://totvssuporte.zendesk.com/attachments/token/SsDQH4VTSSKuWWkHB7bYJAnbk/?name=inline-1853676196.png)

Desta forma, não ocorrerá mais o error.log.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
