---
article_id: 1500000387001
category: PONTO ELETRÔNICO
content_hash: 97c59b38823522b38aa6e592d92c8c05780d4f641368b41bc1cb7ad046d3987b
fetched_at: '2026-06-28T22:44:36.729188+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Período de apontamento atual encontra-se fechado
  para manutenção de batidas
type: support-article
updated_at: '2023-11-21T16:50:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000387001-RH-Linha-Protheus-MEU-RH-Per%C3%ADodo-de-apontamento-atual-encontra-se-fechado-para-manuten%C3%A7%C3%A3o-de-batidas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19225845606167) Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Ao incluir ou fazer manutenção de batidas aparece a mensagem, Período de apontamento atual encontra-se fechado para manutenção de batidas.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH – todas as versões  
  
**Solução**Verificar se os parâmetros **MV\_DABERTO**, **MV\_PAPONTA** e **MV\_PONMES** estão preenchidos corretamente.   
  
A tabela SPO é responsável pelos **períodos fechados** em seu ambiente. Nesta tabela somente poderão ter os período já fechados e **nunca**, os que ainda encontram-se abertos.  
  
Esta tabela deve ser **Compartilhada** no cadastro das tabelas, sendo consultadas via SIGACFG, com C C C ou **Exclusiva** E E E, não podendo ter compartilhamento diferente de um desses dois.  
  
Se a SPO for C C C, no cadastro dos parâmetros, que são visualizados no Configurador, deverá haver **apenas um parâmetro MV\_PAPONTA e um MV\_PONMES** com **filial em branco,** porém se a SPO for E E E deverá haver **APENAS** parâmetros **MV\_PAPONTA e MV\_PONMES com filial preenchida** e não haver em branco.  
  
A tabela SPO e os períodos de apontamento já fechados, poderá ser verificada no módulo 16 - SIGAPON, rotina **Atualizações > Cadastro de Ponto > Períodos de Apontamentos**.  
  
Os períodos abaixo, já estão fechados efetivamente (legenda vermelha)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19225845612951)  
  
Nesta mesma tela, em **Outras Ações > Modificar Período > Apenas Visualizar**, é possível verificar o período aberto das marcações naquele momento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19225820336663)  
  
Ou seja, as marcações só poderão ser incluídas, alteradas ou excluídas a partir deste período aberto.  
  
**Saiba mais**[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
