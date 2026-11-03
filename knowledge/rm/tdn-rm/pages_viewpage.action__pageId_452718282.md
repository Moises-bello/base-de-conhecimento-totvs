---
content_hash: e7c7625e8cafd915a93784b85ed4714705eb5a96eb720770254f60ef1efac4c9
fetched_at: '2026-06-29T00:09:59.295075+00:00'
page_id: '452718282'
product: rm
source: tdn-rm
title: Histórico de Situação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718282
version: 2
---

Ao longo do vínculo empregatício o funcionário terá alterações na situação, ou seja, de ativo terá férias, poderá ser afastamentos e por fim demitido. O histórico de situação guardará as informações relativas a alterações de situação do empregado.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Através da integração com o módulo SigaMNT do Protheus será possível recuperar a situação atual dos funcionários no módulo TOTVS Folha de Pagamento da linha RM**, para isso, foi adicionado** um mapeamento de uma mensagem de requisição, para que o Protheus solicite a situação dos funcionários e o RM retorne.  
 Para o correto funcionamento da integração, o Protheus deverá enviar as informações obrigatórias para o RM:              
 ·         Código da empresa do funcionário  
 ·         Data início da situação  
 ·         Data fim da situação  
 ·         Coligada e Chapa do funcionário  
    
 Obs: No caso de ser apenas um dia, a data início deverá ter o mesmo valor que a data fim.  
 O RM retornará a situação atual do funcionário para o Protheus.  
  [Boletim técinico Integração SIGAMNT - Ler situação real do funcionario no RM](http://tdn.totvs.com/display/integracoes/TOTVS+RH)
