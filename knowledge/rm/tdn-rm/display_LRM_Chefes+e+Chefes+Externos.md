---
content_hash: 7dbab4565d1c8f7f3f5a4018f0fff6692076901f81bf10ebf4a0326d278b84fa
fetched_at: '2026-06-29T00:10:09.949895+00:00'
page_id: '452719750'
product: rm
source: tdn-rm
title: Chefes e Chefes Externos
type: documentation
url: https://tdn.totvs.com/display/LRM/Chefes+e+Chefes+Externos
version: 4
---

O novo chefe e seu substituto terão permissão sobre os subordinados de acordo com o cadastro dentro da hierarquia de seção, a cada nível de seção superior que o funcionário for chefe os funcionários cadastrados nos níveis abaixo serão considerados subordinados.  
   
Caso o campo coligada  no cadastro do chefe estiver vazio o sistema retornará funcionários de todas as coligadas. Ao escolher o funcionário o campo coligada será preenchido automaticamente com a coligada em que o funcionário estiver cadastrado.  
   
A data final somente será habilitada se o parâmetro "Sempre Válido" estiver desmarcado.  
   
Se o parâmetro "Sempre Válido" estiver marcado significará que o Chefe terá a data de término ilimitado ficando o campo "Data Final" desabilitado. Caso contrário, o sistema exigirá a informação de uma data no campo "Data Final".  
   
O chefe definido com "Master" poderá designar substitutos de chefes.  
   
**Observação:**  
O sistema permite que um externo seja associado como chefe/supervisor uma única vez dentro da mesma seção.  
Caso seja necessário utilizar o externo mais vezes deverá ser alterada a data de término do chefe/supervisor.

## Informações adicionais

* Disponível a partir das versões:

  + 12.1.2410.297
  + 12.1.2502.202
  + 12.1.2506.146  
    *(Necessário executar o RM.Atualizador para atualização dos scripts)*
* Quando a base estiver integrada com o **RM x Feedz**, ao cadastrar um substituto, o registro será criado com a flag **"Chefe/Supervisor Substituto"** ativada no cadastro de chefes e supervisores.

Para mais informações sobre o uso deste campo, consulte a documentação [**da Integração RM x Feedz.**](https://tdn.totvs.com/pages/releaseview.action?pageId=785614408#1-1)
