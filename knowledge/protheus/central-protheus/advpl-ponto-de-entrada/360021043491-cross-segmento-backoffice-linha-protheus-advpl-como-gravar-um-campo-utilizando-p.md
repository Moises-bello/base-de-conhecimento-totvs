---
article_id: 360021043491
category: ADVPL - Ponto de Entrada
content_hash: 9ccb4203c110a713d3fe18bf9ae127e659fa5b9d7f5c7b3908f38946993a1b60
fetched_at: '2026-06-28T22:40:11.492722+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Como gravar um campo utilizando
  ponto de entrada em MVC
type: support-article
updated_at: '2023-10-03T19:02:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021043491-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Como-gravar-um-campo-utilizando-ponto-de-entrada-em-MVC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:00 min  
  
Dúvida**Como gravar um campo em rotina MVC, utilizando ponto de entrada da rotina?  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Para gravar a informação em um determinado campos através da rotina MVC é necessário, acessar o objeto, carregar a grid e atribuir o valor ao campo, a tabela é identificada pela propriedade ***ADEPENDENCY*** , mas é preciso verificar o momento que está atribuindo o valor ao campo, pois o sistema existem validações que podem impedir a gravação.

Sugerimos que faça no momento da  validação total do formulário (***ModelPos***), caso não seja permitido somente após a gravação.   
  
Exemplo da Rotina OMSA010

```
oModelx := FWModelActive()->Carregando Model Ativo  
oModelxDet := oModelx:GetModel('DA1DETAIL') ->Carregando grid de dados a partir o ID que foi instanciado no fonte.  
oModelxDet:SetValue('DA1_DESCRI','TESTE')-> Utilizando função para atribuir valor ao campo em tempo de execução  
Para obter DA1DETAIL verifique a propriedade ADEPENDENCY   
omodelx:ADEPENDENCY
```
