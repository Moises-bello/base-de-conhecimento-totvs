---
article_id: 38838452208407
category: SIGAEST - INTEGRAÇÕES
content_hash: bfbdae3748e8c1c5b2211633054d4a9ab9a2114ed91b41cb9dd3ef365fcac888
fetched_at: '2026-06-28T22:38:46.145993+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração EAI: tabelas
  XX3 e XXF'
type: support-article
updated_at: '2026-03-24T13:56:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38838452208407-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-EAI-tabelas-XX3-e-XXF
---

Nas integrações Protheus via EAI, as tabelas XX3 e XXF são essenciais para rastrear mensagens. A XX3 registra tentativas de comunicação dos Adapters, armazenando funções, arquivos de envio e resposta, e versão do Adapter. A XXF mapeia os registros integrados, associando valores externos e internos. Juntas, elas funcionam como log e controle de De/Para, indicando se a integração é alteração ou inclusão de registros.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38838467997975) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como rastrear as ocorrencias no envio e recebimento de mensagens na Integração EAI?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
Nas integrações do Protheus via **EAI (Enterprise Application Integration)**, as tabelas **XX3** e **XXF** são o controle e mapeamento de como os dados trafegam pelo sistema. Elas trabalham como um direcionador e um log de transações.

Veja um vídeo do Processo:

[![De-Para de Mensagem Única.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39256759670423)](https://youtu.be/ssOYCKqj9fI?si=a8mglIdQkeM-JzA4)

---

## 1. Tabela XX3 – Cadastro de Adapters

A **XX3** é a tabela que registra os as tentativas de comunicação dos **Adapters**.

* **O que ela guarda:**

  + **Função (XX3\_FUNCOD):** O nome da mensagem única (ex: `STOCKLEVEL`, `ITEM`).
  + **Arquivo de Envio (XX3\_TRANS):** Arquivo XML ou Json utilizado na integração.
  + **Arquivo de Resposta (XX3\_RETURN):** Arquivo XML ou Json de retorno indicando se a integração gerou erros ou não.
  + **Versão do Adapter (XX3\_VERSAO):** Versão da mensagem integrada pelo sistema.

## 2. Tabela XXF – De/Para de Mensagens (Mapeamento)

A **XXF** é a tabela de **De/Para dos registros integrados**. Ela registra os dados dos registros informando o identificador interno e externo.

* **O que ela guarda:**

  + **Tabela Integrada (XXF\_ALIAS):** Indica em qual tabela do Sistema a informação foi gravada;
  + **Valor Externo (XXF\_EXTVAL):** Indica o valor recebido pelo outro sistema;
  + **Valor Interno (XXF\_INTVAL):** Indica o valor interno correspondente ao valor externo recebido.

---

## Como elas se relacionam na prática?

Imagine que a integração de um registro foi executada pelo sistema:

1. Na **XX3**, você terá uma espécie de "Log de registro", indicando qual registro foi integrado e qual a resposta do sistema de destino.
2. Na **XXF**, você terá um De/Para dos registros integrados, sempre que uma nova integração for realizada, o Protheus vai verificar se este registro já existe na XXF, definindo assim se a integração será uma alteração de um registro já existente ou se será a inclusão de um novo registro.

## Resumo Técnico:

| **Tabela** | **Nome** | **Função Principal** |
| --- | --- | --- |
| **XX3** | Transações EAI | Registra os dados integrados pelo sistema. |
| **XXF** | De/Para de Mens. Única | Indica o De/Para dos registros recebidos associando com os registros internos do Protheus. |

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
