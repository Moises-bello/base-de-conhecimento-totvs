---
article_id: 360036365813
category: Recrutamento e Seleção de Pessoas (SIGARSP)
content_hash: 37525b3189b437eb016f69d979f74b2d387ddc7907897605e389f9701c6297bc
fetched_at: '2026-06-28T22:43:00.922189+00:00'
product: protheus
section_id: 206960907
source: central-protheus
title: RH - Linha Protheus - RSP - Exclusão de Vagas gera log - A chave a ser excluída
  está sendo utilizada
type: support-article
updated_at: '2021-04-06T19:39:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036365813-RH-Linha-Protheus-RSP-Exclus%C3%A3o-de-Vagas-gera-log-A-chave-a-ser-exclu%C3%ADda-est%C3%A1-sendo-utilizada
---

**Ocorrência**No módulo Recrutamento e Seleção de Pessoal, ao tentar excluir uma vaga, gera log de ocorrência:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047739333/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Recrutamento e Seleção de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois existe relacionamentos entre a tabela de Vagas (SQS), com a tabela de Currículos (SQG), ou com a Agenda do Candidato, relacionado a Vaga tabela (SQD).  
  
**Solução**Para solucionar essa ocorrência, deverá acessar o Módulo 20 (SIGARSP), no seguinte caminho: Atualizações > Cadastro > Vagas, selecionar a vaga que deseja excluir e selecionar  outras ações > excluir.  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084878913/mceclip6.png)  
  
O sistema apesentará a seguinte mensagem de log , deverá clicar em SIM.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083708534/mceclip1.png)  
  
Será apresentado a mensagem de geração de LOG clique em SIM para o sistema detalhar as possíveis amarrações com a vaga deverá ser desfeita para que possa ser excluído seu cadastro.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084878733/mceclip2.png)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084878753/mceclip3.png)  
  
Com a geração do LOG será apresentado maiores detalhes sobre o vinculo desta vaga. Cabe a empresa decidir se irá retirar todos os vínculos para conseguir realizar a exclusão.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084878773/mceclip4.png)  
  
Se optar pela exclusão acesse o seguinte caminho: Atualizações > Candidato > Agenda, selecione a vaga em questão e exclua sua agenda.  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084878853/mceclip5.png)

Selecione a opção Outras Ações> Consulta por Vaga> Selecione a vaga em questão.   
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083708734/mceclip7.png)  
  
Será apresentado os processos amarrados a vaga, delete a linha e clique em salvar.  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083708914/mceclip8.png)  
  
Após este processo realize a exclusão da vaga, o sistema irá realizar a verificação dos dados e se não houver nenhuma amarrações, será possível realizar sua exclusão.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083708974/mceclip9.png)

Poderá ser apresentado a mensagem abaixo na tentativa de exclusão.  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083708994/mceclip10.png)  
  
Deverá ser verificado no seguinte caminho: Atualizações > Candidato > Currículo.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083709014/mceclip11.png)  
  
Selecione o Currículo clique na opção Alterar, retire e informação de COD VAGA conforme campo em destaque. Salve o registro.  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084879333/mceclip12.png)  
  
Execute novamente a tentativa de exclusão da vaga para o sistema avaliar se existe algum outro vinculo. Caso não encontre será apresentado o cadastro da vaga com a opção excluir e basta confirmar o registro.  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084879393/mceclip13.png)  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[Central de Artigos Recrutamento e Seleção](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960907-RH-Recrutamento-e-Sele%C3%A7%C3%A3o-de-Pessoal)
