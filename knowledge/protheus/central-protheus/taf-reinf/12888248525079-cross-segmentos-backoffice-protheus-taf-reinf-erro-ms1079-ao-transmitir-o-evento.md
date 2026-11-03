---
article_id: 12888248525079
category: TAF - REINF
content_hash: 95304fd33109d152f7cc12d0b50e2cd5937dcd769ecdda88211adc475a2d6cd2
fetched_at: '2026-06-28T22:41:33.561789+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Erro MS1079 ao transmitir
  o evento R-1000 ambiente homologação  layout 2.1
type: support-article
updated_at: '2023-11-22T18:38:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12888248525079-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-MS1079-ao-transmitir-o-evento-R-1000-ambiente-homologa%C3%A7%C3%A3o-layout-2-1
---

**Dúvida**Como corrigir a rejeição MS1079 - Registro não existe na tabela com a mesma chave e período de validade informados no evento?  
  
**Ambiente**Microsiga Protheus - SIGATAF - A partir de 12.1.27  
  
**Solução** O novo envio do evento R-1000 deve ocorrer porque o banco de dados utilizado pela receita para o layout 2.1 é diferente do banco utilizado para o layout 1.5, desta forma não existe a informação para transmissões do novo layout.   
   
MS1079 - O erro ocorre devido ao envio do seu R-1000 está sendo feito como alteração aonde o correto é inclusão, o envio esta gerando dessa forma(alteração) porque há informações transmitida do R-1000 do layout 1.5 no seu banco de dados. 

Para correção faça uma limpeza da suas tabelas de apurações para que ao apurar o seu R-1000 o mesmo seja enviado como inclusão. 

1° Atualize o seu ambiente do TSS.

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)  
   
**A funcionalidade abaixo é criada exclusivamente para ambientes teste!**  
   
Miscelânia > Funcionalidade >Exclusão por período fiscal.    
![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12888034807319)

Selecione somente a opção REINF.

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12888061177111)

Insira o período que deseja fazer a exclusão  e realize a exclusão, serão excluídas todas informações gravadas nas tabelas espelho do seu ambiente.

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12888094695319)

   
**Recomendamos que seja feito um back-up do banco de dados, mesmo que as informações gravadas são em ambiente teste.**  
   
  Após limpeza do ambiente é necessário fazer a remoção do contribuinte na receita, procedimento enviado pela opção abaixo.

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12888188277911)

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12888242567447)

Remoção realizada com sucesso você pode refazer a transmissão do seu R-1000,**Lembrando que todas orientações passadas nesse chamado são para ambiente em homologação.**
