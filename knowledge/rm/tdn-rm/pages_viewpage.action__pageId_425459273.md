---
content_hash: 833b1685684b7ff34d8cc77b5723fde4d021bfbc77bd2fb588094207c9747dbe
fetched_at: '2026-06-29T00:09:34.879856+00:00'
page_id: '425459273'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Moeda e Cotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459273
version: 2
---

**TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Moeda e Cotação**

---

As moedas e cotações são incluídas, alteradas e excluídas no Protheus. Os dados são automaticamente sincronizados para o TOP, onde pode ser realizada a consulta dos registros sincronizados.  
    
 Por padrão, o Protheus possui 5 moedas registradas, sendo necessário configurar os parâmetros referentes ao símbolo e a descrição da moeda.   
    
 Para configurar os parâmetros, acesse: Protheus | SigaCfg | Ambiente | Cadastro | Parâmetros  
 **Símbolo da moeda:** parâmetro MV\_SIMB1 referente a Moeda 1, parâmetro MV\_SIMB2 referente a Moeda 2, e assim por diante.   
 **Cotação da moeda:** parâmetro MV\_MOEDA1 referente a Moeda 1, parâmetro MV\_MOEDA2 referente a Moeda 2, e assim por diante.   
 As moedas devem ter os valores de cotação preenchidos para que sejam sincronizadas ao TOP. Para configurar a cotação acesse: Protheus | SigaCom (módulo padrão) | Atualizações | Cadastros | Moedas  
    
 No cadastro deve ser informado o valor da taxa da moeda, sempre em relação à Moeda 1. Os campos disponíveis são referentes a taxa da Moeda 2 até a taxa da última moeda cadastrada.  
    
 Para visualizar a Moeda/Cotação no TOP acesse: RM | BackOffice | Gestão Financeira | Movimentações Bancárias | Moedas e Índices  
   
 **Dados Sincronizados**  
    
 Os dados sincronizados do Protheus para o TOP referente ao cadastro Moeda e Cotação são:

* Símbolo da moeda
* Data da cotação
* Descrição da moeda
* Fator de conversão
* Quantidade de casas decimais
* Símbolo de referência
* Tipo

*Observação:*

O cadastro de índices/moedas disponível na abertura do Protheus é diferente da visão de cadastro dentro do Protheus. Ele não possui integração e não deve ser utilizado como cadastro de Moeda e Cotação.
