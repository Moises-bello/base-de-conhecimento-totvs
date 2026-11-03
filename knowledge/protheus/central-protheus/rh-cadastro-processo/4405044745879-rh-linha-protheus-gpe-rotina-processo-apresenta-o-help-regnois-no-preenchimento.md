---
article_id: 4405044745879
category: RH - Cadastro Processo
content_hash: acbae7f948d0c2cee87a111231cf639f650e64a7a8e886203d6abdb6f73a242a
fetched_at: '2026-06-28T22:44:10.694847+00:00'
product: protheus
section_id: 206971467
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina Processo apresenta o help Regnois no preenchimento
  do campo Tipo Desp
type: support-article
updated_at: '2026-06-24T19:27:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405044745879-RH-Linha-Protheus-GPE-Rotina-Processo-apresenta-o-help-Regnois-no-preenchimento-do-campo-Tipo-Desp
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33449846435479) Tempo aproximado para leitura: **00:02:00****min**

**Ocorrência**Rotina Processo - APTA100 apresenta o *help* **Regnois** no preenchimento do campo Tipo Desp. utilizando a lupa para busca de dados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13957838236823)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Causa**Esse help é apresentado devido a divergência de tamanho dos campos  **Categoria - RE5\_TABELA** e **Categoria -REK\_TABELA**, que obrigatoriamente devem estar parametrizados com o mesmo tamanho.  
  
**Solução**

1. Acesse no módulo SIGACG - Configurador em **Base de Dados** > **Dicionário** > **Base de Dados**;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076870313/mceclip0.png)  
  
2. Em seguida, localize as tabela **RE5 - Tipos das Tabelas** e clique em **Editar**;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405037665559)  
  
3. Após isso, selecione o campo **RE5\_TABELA** e clique em **Editar** novamente;  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405037746455)  
  
4. Verifique se o **Tamanho** do campo consta conforme padrão do Sistema (4) e clique em **Salvar**.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405037774103)  
  
5. Após Salvar, execute o mesmo procedimento com a tabela REK e confirme novamente através do Ícone ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076887893/mceclip0.png)  
  
6. Clique em Atualizar base de dados - Ícone do Disquete, para que a alteração feita no campo seja atualizada efetivamente no dicionário

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como cadastrar um processo trabalhista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050723993-RH-Linha-Protheus-GPE-Como-cadastrar-um-processo-trabalhista)  
[RH - Linha Protheus - GPE - eSocial - Como se adequar ao eSocial leiaute S-1.1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8658568031127-RH-Linha-Protheus-GPE-eSocial-Como-se-adequar-ao-eSocial-leiaute-S-1-1?source=search)  
[RH - Linha Protheus - GPE - Qual a referência/cadastro do Protheus para apresentar o cadastro de Reclamante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13163454046871-RH-Linha-Protheus-GPE-Qual-a-refer%C3%AAncia-cadastro-do-Protheus-para-apresentar-o-cadastro-de-Reclamante)
