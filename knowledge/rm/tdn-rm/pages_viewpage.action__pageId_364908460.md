---
content_hash: b8832b3ba249d5c8dcf4c2bf4374aed5adeb1999e8e574ccdaeaced25037d36d
fetched_at: '2026-06-29T00:08:59.601765+00:00'
page_id: '364908460'
product: rm
source: tdn-rm
title: S-2210 - Comunicação de Acidente de Trabalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908460
version: 11
---

A finalidade da CAT é comunicar acidentes de trabalho envolvendo empregados e/ou trabalhador avulso, mesmo que não haja afastamento do trabalhador. O envio ao eSocial é feito através do evento S-2210.  A CAT deve ser enviada até 1 dia útil ao da ocorrência e em caso de morte, o envio deve ser imediato. O envio ao eSocial só será possível após o envio dos eventos S-2200 e S-2300.

Os eventos de Saúde e Segurança do Trabalhador (S-2210, S-2220 e S-2240) ainda não estão disponíveis no ambiente de produção, pois o governo ainda não está apto a recebe-los devido ao faseamento. Caso esteja em ambiente diferente do tipo “1-Produção”, será possível realizar todos os processos independente da data de obrigatoriedade.

Os gatilhos para o evento S-2210, serão gerados a partir da criação de uma ocorrência de trabalho. As ocorrências podem ser inseridas através do Prontuário Médico, pelo módulo de CAT do Segurança e Saúde Ocupacional e também através do anexo do cadastro do funcionário.

**Procedimentos para geração do gatilho para o evento S-2210-Comunicação de Acidente de Trabalho.**

**1º **Passo: Cadastro da Ocorrência****

**Através do Prontuário Médico:**

Totvs Segurança e Medicina do Trabalho | PCMSO | Prontuário Médico.

Será gerado gatilho para o evento S-2210 com status 0-Pendente. O Usuário poderá visualizá-lo através do menu Folha de Pagamento | eSocial | Fila de eventos.

**Através do módulo da CAT**

Segurança e Saúde Ocupacional | CAT | Ocorrências Acidente Trabalho.

Gatilho:

**Através do anexo no cadastro do funcionário.**

Gatilho:

**2º Passo: Gerar XML:**

Após o cadastro da CAT, o processo de Geração do  XML deve ser executado para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Gerar XML

**Fila de Eventos.**

Para a correta geração do XML é necessário observar os campos que são obrigatórios para o envio.

**3º Passo:-Integrar evento com TAF:.**

Para isso deverá selecionar o evento e clicar Integrar TAF.

Neste momento o status do evento será alterado para 3-Enviado  para o TAF.

4º Passo: Enviar os eventos gerados na fila para o TOTVS Automação Fiscal (TAF):

Acesse o produto Totvs Automação Fiscal (TAF)  e realize  o processamento para envio das informações do Totvs Folha de pagamento para o TAF.

5º Passo: Atualizar status integração TAF:

 Para atualizar o status da integração do TAF terá as seguintes opções:

* Na fila de eventos selecionar   " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

Veja mapeamento dos campos que serão informados:
