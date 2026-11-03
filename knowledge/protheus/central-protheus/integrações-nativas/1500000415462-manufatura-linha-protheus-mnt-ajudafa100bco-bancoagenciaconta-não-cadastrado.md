---
article_id: 1500000415462
category: Integrações Nativas
content_hash: 2dd3ff9ea153e1bdf63bbe0d5e92bcbd5ff6c63ea893886de22ea2048fbaf1c5
fetched_at: '2026-06-28T22:42:35.298074+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - AJUDA:FA100BCO Banco/Agencia/Conta não
  cadastrado
type: support-article
updated_at: '2021-06-02T14:39:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000415462-Manufatura-Linha-Protheus-MNT-AJUDA-FA100BCO-Banco-Agencia-Conta-n%C3%A3o-cadastrado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Na integração do **Manutenção de Ativos** com o **RM**, ao fazer a baixa do lançamento no **RM** a mensagem está sendo enviada ao **Protheus** e no retorno está apresentando a mensagem **AJUDA:FA100BCO Banco/Agencia/Conta não cadastrado**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Causa**Esse incidente ocorre, pois está faltando o cadastro do **Banco Agência** e **Conta** no **SIGAGPE - Gestão de pessoal** do **Protheus**.  
  
**Solução**Para solucionar essa ocorrência, acesse no **Protheus** o módulo **SIGAGPE** em **Atualizações - Cadastros - Banco/Agências - MATA070** e inclua:

* **Código** igual a **001**
* **Agência** igual a **0001**
* **Nro. conta** igual a **00001**.
