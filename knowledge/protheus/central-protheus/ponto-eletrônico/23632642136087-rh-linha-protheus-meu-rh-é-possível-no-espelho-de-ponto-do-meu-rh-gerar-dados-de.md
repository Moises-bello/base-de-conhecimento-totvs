---
article_id: 23632642136087
category: PONTO ELETRÔNICO
content_hash: 1700e7307f915e9c6735a33550ee4eb39c3f204441e5b4eb5c6d6b3123140661
fetched_at: '2026-06-28T22:44:36.490918+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - É possível no Espelho de Ponto do Meu RH, gerar
  dados de Geolocalização das marcações
type: support-article
updated_at: '2026-06-22T17:31:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23632642136087-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-no-Espelho-de-Ponto-do-Meu-RH-gerar-dados-de-Geolocaliza%C3%A7%C3%A3o-das-marca%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23632642105751) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
É possível no Espelho de Ponto do Meu RH, gerar dados de Geolocalização das marcações ?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
No App Meu RH, é possível registrar **marcações** ***online*** **com o indicativo da geolocalização** que, o funcionário se encontra naquele momento, sendo referenciada a **latitude e longitude** do registro.  
  
Para ter acesso à Geolocalização, a premissa é ter o **protocolo seguro configurado no appserver.ini** do Meu RH, ou seja, o App precisa ser **acessado em ambiente HTTPS**.   
Para saber mais sobre essa configuração, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042649133).  
  
Também será necessário, ter as **permissões do Meu RH habilitadas para aquele usuário genérico do portal, vinculado ao Cadastro de Participante**.   
Para saber mais sobre como habilitar, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050355093).  
  
Com as duas premissas, na **rotina Ponto > Bater Ponto**, abrirá um mapa da localização via *web* ou celular.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23632642109975)  
  
Essas informações, serão gravadas nas tabelas **RS3 e SP8 do Protheus**, nos campos abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23632647673367)  
  
Porém, quando o Espelho de Ponto é gerado pelo App Meu RH, as marcações por Geolocalização, **não possuirão nenhuma informação impressa.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23632642114583)  
  
É possível realizar a customização do ***RDMake IMPESP*** e, compila-lo no RPO do Meu RH, para isso, há necessidade de um conhecimento técnico no processo.  
  
Para ter acesso ao ***RDMake***, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10548416826775).  
  
No artigo abaixo, documentamos um pouco sobre como gerar um relatório das marcações, feitas por Geolocalização, com as informações de Latitude e Longitude, via Protheus.  
[RH - Linha Protheus - Meu RH - É possível gerar um relatório com as marcações registradas por Geolocalização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18922934482071)  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI**para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
