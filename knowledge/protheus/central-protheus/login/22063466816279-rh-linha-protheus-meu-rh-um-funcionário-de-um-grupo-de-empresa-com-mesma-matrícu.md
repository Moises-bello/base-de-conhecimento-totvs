---
article_id: 22063466816279
category: LOGIN
content_hash: daabf6379d8a68582eee8d648ca719fbe01f878dba631ae010c4375df449c9f5
fetched_at: '2026-06-28T22:44:40.425038+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - Meu RH - Um funcionário de um Grupo de Empresa, com mesma
  matrícula, consegue acessar dados do outro
type: support-article
updated_at: '2025-11-06T20:37:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22063466816279-RH-Linha-Protheus-Meu-RH-Um-funcion%C3%A1rio-de-um-Grupo-de-Empresa-com-mesma-matr%C3%ADcula-consegue-acessar-dados-do-outro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22063482686999) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Um funcionário de um Grupo de Empresa, com mesma matrícula, consegue acessar dados de um outro funcionário, de um outro Grupo de Empresa.  
**Ambiente**TOTVS RH Linha Protheus - Meu RH – Todas as versões  
  
**Causa**Este incidente pode ocorrer, pois **dois funcionários que possuem o mesmo código de matrícula**, **entre Grupos de Empresas diferentes**, possuem também o **mesmo código de participante** e o **mesmo código de filial**, e **não realizam o *logout*** para invalidar o *Token* de acesso.  
  
**Solução**Entre Grupos de Empresas diferentes, quando **dois funcionários com a mesma matrícula**, **mesmo código de participante** e o **mesmo código de filial**, utilizam o App Meu RH e, **sem realizar *logout***, fecham a página, o *Token* de acesso não era invalidado, por isso, um conseguiria acessar o Meu RH do outro só alterando a *URL* de acesso ao Meu RH.  
  
Cenário entre dois Grupos de Empresas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22063466804759)  
  
Tendo mais confiabilidade no App Meu RH, foi implementado **mais um mecanismo de segurança** para, obrigatoriamente, *deslogar* o usuário da página, **mesmo que este não acione o botão Sair**, basicamente, se o App Meu RH identificar que houve troca de Grupo de Empresa por alguma alteração na *URL*, **o Meu RH forçará o *logout* deste funcionário**, para que um novo *token* de acesso seja gerado e o *token* antigo seja invalidado.  
  
Para que, **o ambiente esteja preparado à essa nova ferramenta de segurança**, é obrigatório a **atualização dos arquivos de *front* do App Meu RH**, seguindo nossa **[documentação oficial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034).**  
  
Para melhor desempenho, é altamente recomendado que seja realizado, periodicamente, a limpeza do cache do navegador, procedimentos esse **para que o *endpoint* seja carregado sem o cache, visando a sua devida atualização.**  
  
**Saiba Mais**  
**[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**  
**[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
