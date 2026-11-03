---
content_hash: 7a08149303c6f1b3e4368db4f6dd415f64454bfce6bc78870f472d71f0688ecf
fetched_at: '2026-06-29T00:09:16.256797+00:00'
page_id: '421385495'
product: rm
source: tdn-rm
title: Parâmetros Geral
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385495
version: 2
---

**Geral**   
 A aba **Geral** é composta pelos campos abaixo:  
 **Integração com Suprimento/Faturamento:** Este campo deve ser habilitado para que a integração seja ativada.  
 **Utiliza rateio por centro de custo:** Este campo é habilitado quando a integração irá utilizar rateio por centro de custo.  
 **Arredondar quantidade na conversão de unidades:** Este campo é habilitado quando a integração utilizar arredondamento de quantidade de unidade.  
 **Possíveis situações de conversão:**  
 A unidade do insumo pode ser igual à unidade de compra. O sistema não modifica a quantidade.  
 A unidade do insumo pode ser incompatível com a unidade de compra do Gestão de Estoque Compras e Faturamento. O sistema informa que a unidade é incompatível e não gera o movimento para o Gestão de Estoque Compras e Faturamento  
 A unidade do insumo pode ser uma e a do produto outra (Kg para Sc, por exemplo, onde uma é unidade base da outra). O sistema converte de acordo com a unidade base e o fator de conversão  
 A unidade do insumo pode ser uma e a do produto outra, sendo que ambos têm a mesma unidade de conversão (T para mg, onde a unidade base de ambos é Kg).  
 **Enviar descrição completa do insumo para requisição de materiais:** Este campo é habilitado quando a integração utilizar descrição completa do insumo na requisição.  
 **Considerar contratos na requisição de materiais:** Este campo é habilitado quando a integração utilizar contratos na requisição de materiais.   
 **Campo referência data apropriação no movimento:** Este campo define referência da data da apropriação no movimento.  
 **Condição de Pagamento:** Condição de pagamento default para integração com o Suprimento e Faturamento.  
 Para Adiantamento de Contratos existem quatro campos que devem ser parametrizados:  
 **Tipo do movimento contratos a pagar:** Onde se informa o tipo de movimento que será utilizado para contratos a pagar.  
 **Tipo do movimento contratos a receber**: Onde se informa o tipo de movimento que será utilizado para contratos a receber.  
 **Produto padrão contratos a pagar:** Onde se define o produto padrão do contrato a pagar.  
 **Produto padrão contratos a receber:** Onde se define o produto padrão do contrato a receber.
