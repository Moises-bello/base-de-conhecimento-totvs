---
article_id: 360052458813
category: RH - Leitura e Apontamento
content_hash: d2c155c9854039adf32d7dbc4915dd199b38788fd95afdc64eae24a28d1df653
fetched_at: '2026-06-28T22:44:46.006555+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Quando funcionário registra o ponto em outras filiais,
  as marcações não são lidas
type: support-article
updated_at: '2025-11-10T19:48:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052458813-RH-Linha-Protheus-PON-Quando-funcion%C3%A1rio-registra-o-ponto-em-outras-filiais-as-marca%C3%A7%C3%B5es-n%C3%A3o-s%C3%A3o-lidas
---

**Ocorrência**  
Quando funcionário registra o ponto em outras filiais da empresa, diferente da que está alocado no cadastro de Funcionário, ao processar a rotina de Leitura/Apontamento, as marcações não são lidas.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
Este problema ocorre quando o compartilhamento das tabelas **SP0** (Cadastro de Relógios) e **SPE** (Crachás Provisórios) está como **EXCLUSIVO**.  
  
**Solução**  
Para solucionar o problema, o compartilhamento das tabelas **SP0** (Cadastro de Relógios) e **SPE** (Crachás Provisórios) deve ser alterado para **COMPARTILHADO:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35446243940759)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35446275641111)  
  
**Importante*****:***  
**1.** Se as tabelas estiverem populadas (com informações), será necessário efetuar Backup das mesmas, deletar os registros da tabela. Somente com a tabela criada no banco e sem registros que será possível,via configurador, alterar o compartilhamento;  
**2.** Após isso, retornar as informações nas tabelas;  
\*\*Atenção: Se atente que para o campo **Filial** das tabelas:  
Estas tabelas SP0 e SPE só pode constar totalmente exclusiva ou totalmente compartilhada. Uma vez que:  
- se total compartilhada: o campo **Filial** deve ficar em branco;   
- se total exclusiva: o campo Filial deve estar preenchido com a Empresa/filial correspondente.  
  
**Informações complementares**  
[Manual Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua do RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
