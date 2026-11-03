---
article_id: 18501085805463
category: REQUISIÇÕES
content_hash: 85a86d02c5c294da4cf10ad2042e60b4100d2d5f2d33e50e324e6e4d04701904
fetched_at: '2026-06-28T22:44:37.602190+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - Meu RH - Quais são os tipos de solicitações que o RH
  terá acesso para aprovação
type: support-article
updated_at: '2025-09-16T17:09:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18501085805463-RH-Linha-Protheus-Meu-RH-Quais-s%C3%A3o-os-tipos-de-solicita%C3%A7%C3%B5es-que-o-RH-ter%C3%A1-acesso-para-aprova%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18501054818967) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Quais são os tipos de solicitações que o RH terá acesso para aprovação  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Todas as solicitações que os funcionários realizam no App Meu RH, são levadas a três tabelas principais.  
  
São elas:  
RH3 -> solicitações do Portal ao RH  
RH4 -> Alterações cadastrais  
RGK -> Histórico de movimentação das solicitações  
  
No que diz respeito às solicitações, **a tabela RH3, especificamente no campo RH3\_TIPO**, na tabela genérica SX5, temos a tabela JQ que traz os tipos de solicitações que são levadas para aprovação.  
  
Para acessar a tabela, inicialmente entrar no Configurador - SIGACFG, com uma senha de administrador.  
Acessar a rotina de Base de Dados, no caminho abaixo no menu:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18519296721687)  
  
Clicar em Tabelas Genéricas e, localizar a tabela JQ.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18519283204119)  
  
Itens:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18501081093527)  
  
Para o App Meu RH, não são todas as solicitações que temos para efetivar a requisição, porém, cabe ressaltar que os tipos das requisições, são compostos **na tabela JQ da genérica SX5.**  
  
O *status* da solicitação é trazido **no campo RH3\_STATUS**, sendo:  
  
1=Em processo de aprovação;  
2=Atendida;  
3=Reprovada;  
4=Aguardando Efetivação do RH;  
5=Aguardando Aprovação do RH.  
  
Campos da tabela RH3:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18519296729367)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18519296731287)  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
