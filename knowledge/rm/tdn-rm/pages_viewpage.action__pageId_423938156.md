---
content_hash: 666d5ed427ccd4d1f2da1d1c90251aa87bd452e0df56a848bd92a3584d7cbc8f
fetched_at: '2026-06-29T00:09:25.456598+00:00'
page_id: '423938156'
product: rm
source: tdn-rm
title: Importação/Exportação Automação Comercial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938156
version: 5
---

**Exportação**

O processo de Exportação de Automação Comercial consiste em copiar os registros de [Cupom Fiscal](http://tdn.totvs.com/display/LRM/Cupom+Fiscal) e [Redução Z](http://tdn.totvs.com/pages/viewpage.action?pageId=423938855)e seus relacionamentos, gerando um arquivo texto com um layout pré-definido. Este recurso está disponível através do TOTVS Business Conector | [Gerador de Saídas](http://tdn.totvs.com/pages/viewpage.action?pageId=237383341) | Layout | Importar Layout. Existem três tipos de layout pré-definidos:

**Layout 1**  
    
 Informações Redução Z  
    
   
    
 **Informações do Item de Redução Z**  
    
 Informações do Cupom Fiscal  
    
   
    
 Informações do Item de Cupom Fiscal  
    
   
   
 Informações do Pagamento de Cupom Fiscal  
    
   
    
 Informações de Relacionamento do Item de Cupom Fiscal X Item de Movimento  
    
   
    
 **Layout 2**  
    
 Informações Redução Z  
    
   
    
 Informações do Item de Redução Z  
    
   
   
Informações do Cupom Fiscal  
    
   
   
 Informações do Item de Cupom Fiscal  
    
   
   
 Informações do Pagamento de Cupom Fiscal  
  
   
    
Informações de Relacionamento do Item de Cupom Fiscal X Item de Movimento  
    
   
    
 **Layout 3**  
    
 Informações de Redução Z  
    
   
    
 Informações do Item de Redução Z  
    
   
    
 Informações de Cupom Fiscal  
    
   
    
 Informações do Item de Cupom Fiscal  
    
   
    
 Informações do Pagamento de Cupom Fiscal  
    
   
    
 Informações de Relacionamento do Item de Cupom Fiscal X Item de Movimento

Importação: Através do processo de importação é possível incluir novos cadastros de Cupom Fiscal e Redução Z e seus dados relacionados, a partir do arquivo texto gerado na exportação ou criado manualmente conforme layout.   
Para utilizar o processo de importação de Automação Comercial é necessário incluir um novo conceito através do TOTVS Business Conector.   
No processo de importação o usuário poderá informar o seguinte parâmetro:

* **Cliente\Fornecedor identificado por CPF/CNPJ**: Para buscar o código do cliente através do CPF/CNPJ informado no campo CODCFO.

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.
