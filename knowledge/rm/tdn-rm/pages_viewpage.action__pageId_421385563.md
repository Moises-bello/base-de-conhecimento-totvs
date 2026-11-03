---
content_hash: e0d1ec958259a159301732e56f409d6076f875e2069f64ec5977248bd55b0099
fetched_at: '2026-06-29T00:09:16.793961+00:00'
page_id: '421385563'
product: rm
source: tdn-rm
title: Rateio Default para Etapas/Obras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385563
version: 2
---

O rateio Default para Etapas/Obras define em um único processo os rateios para várias tarefas.  
    
 Como funciona:   
 Na opção de itens do contrato foi criado processo Rateio Default para Etapas/Obras. Selecione o Item de contrato, como a medição será distribuída entre produtos para geração de movimentos no sistema de Suprimentos/Faturamento.  
    
 Ao selecionar uma etapa/obra e definir um rateio, o mesmo é aplicado para todas as tarefas filhas que estão associadas à etapa/obra, automaticamente.  
    
 O processo contém as etapas:  
    
 Na primeira etapa são exibidas as etapas e obras do projeto:  
 As linhas com texto em azul são etapas/obras que possuem serviços associados ao contrato em questão. Para essas etapas/obras, é exibida entre parênteses a quantidade de serviços associados.  
 Deve-se selecionar apenas 1(um) registro e seguir para a próxima etapa.  
 A escolha irá refletir em todos os registros filhos da obra/etapa selecionada.  
 Na próxima etapa, é definido o rateio propriamente dito, através da seleção de produtos e definição do percentual de rateio:  
 Não é necessário definir 100% do rateio, pois o restante do rateio pode ser definido durante o processo de medição de períodos de contrato.  
    
 A opção de excluir, se marcado, exclui todo o rateio default já existente nas tarefas em questão e insere o rateio definido pelo usuário. Caso esteja desmarcado (padrão), o sistema ignora os rateios que já estejam definidos.  
    
 Se o usuário insere um percentual para um determinado produto mais de uma vez, o valor do rateio é substituído pelo valor informado pelo usuário.  
    
 Na última etapa, executa-se o processo que faz as seguintes validações:  
 Para cada item contido na listagem de tarefas associadas da obra/etapa é verificado se o mesmo já possui rateio default definido, caso exista e o parâmetro de sobrescrever rateios estiver habilitado o rateio anterior é excluído e o novo é salvo. Se o parâmetro de sobrescrever não estiver habilitado, o sistema não sobrescreve rateio definido para o item anteriormente. Se não existir rateio cadastrado para os itens vinculado ao contrato após o final do processo o rateio será salvo.
