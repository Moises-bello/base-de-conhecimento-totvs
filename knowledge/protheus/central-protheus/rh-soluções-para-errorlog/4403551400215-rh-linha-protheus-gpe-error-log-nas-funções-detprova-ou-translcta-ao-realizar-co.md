---
article_id: 4403551400215
category: RH - Soluções para error.log
content_hash: 47ae20e0a46f3d751515bb745469c44be7e63d184ab9014af534470521ee21b8
fetched_at: '2026-06-28T22:44:09.101445+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Error log nas funções DETPROVA ou TRANSLCTA ao
  realizar Contabilização
type: support-article
updated_at: '2025-09-22T20:00:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403551400215-RH-Linha-Protheus-GPE-Error-log-nas-fun%C3%A7%C3%B5es-DETPROVA-ou-TRANSLCTA-ao-realizar-Contabiliza%C3%A7%C3%A3o
---

**Ocorrência**Ao realizar a **Contabilização**, através da rotina **GPEM110**, é apresentado *error log*nas funções **DETPROVA** ou **TRANSLCTA**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Erros na função **DETPROVA** ou **TRANSLCTA** normalmente são erros de configuração do **Lançamento Padrão** do cliente. Este é causado devido à **informações errôneas** dentro do cadastro de integração  
  
**Solução****1.** Localize em seu system (PROTHEUS) o arquivo **ERROR.LOG**  
**2.** Abra com um editor de texto e localize pela palavra **CPADRAO**.  
**Obs.: CPADRAO** é o código do Lançamento Padrão que está com problema. Normalmente existem 3 referências desta variável, dentro do arquivo de *error log*, onde a primeira referência é vazia e a segunda e a terceira são preenchidas com o código do Lançamento Padrão.  
  
**3.** Após encontrar, abrir o ERP, no módulo de SIGAGPE, a rotina em **Atualizações/Cadastros/Lançamento Padrão**  
**4.** Realizar a busca do Lançamento Padrão correspondente ao conteúdo de **CPADRAO** informado no *error log*  
**5.** Avalie todos os campos de fórmula do cadastro do Lançamento Padrão, seguindo a seguinte sequência:  
**a.** Verifique se as expressões utilizadas estão corretas  
**b.** Caso esteja utilizando customizações nestes campos, verifique se estão compiladas dentro do seu RPO e/ou se estão habilitadas dentro do cadastro de personalizações (dentro do menu cadastro no configurador (SIGACFG))  
**c.** Caso esteja referenciando um campo do sistema, verifique se o mesmo está como usado e/ou disponível para utilização.  
  
**6.** Após ajuste, realize o processo de Contabilização novamente e verifique se o erro será sanado.  
  
**Obs.:** Caso o erro ainda ocorra, refaça todos os processos novamente, validando se após o ajuste, o novo *error log* aponta para **outro** Lançamento Padrão que também está configurado incorretamente e, neste caso, será necessário ajuste também deste Lançamento Padrão e de todos os demais que apresentarem erros.  
  
**Informações complementares**Pacote de Expedição Contínua do Gestão de Pessoal: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)
