---
article_id: 360046082294
category: Inspeção de Processos (SIGAQIP)
content_hash: 23ab5d561da7066215cf43756d4dab2d088df9ce19e3811df12ef320a0bc666c
fetched_at: '2026-06-28T22:42:25.894043+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Origem da informação gravada nos campos
  QPK_CLIENT e QPK_LOJA
type: support-article
updated_at: '2021-10-01T13:09:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046082294-Manufatura-Linha-Protheus-SIGAQIP-Origem-da-informa%C3%A7%C3%A3o-gravada-nos-campos-QPK-CLIENT-e-QPK-LOJA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:00 min**  
**Dúvida**Qual a origem da informação gravada no campo **QPK\_CLIENT - Cliente** e **QPK\_LOJA - Loja**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**A gravação dos campos **QPK\_CLIENT** e **QPK\_LOJA** tem relação com o parâmetro **MV\_QINTPC - Apresenta tela de relacionamento entre Produto x Cliente**.  
Se este parâmetro estiver como **T**, e os campos **QPK\_CLIENT** e **QPK\_LOJA** em **branco/vazio**, quando clicar em **Resultados** na tela da rotina **QIPA215 - Inspeção de Processos**, será aberta uma tela para poder informar qual é o **cliente** e **loja** que serão registrados nestes campos.  
Esses campos são gravados apenas neste momento, onde é aberta uma tela para seleção do cliente e loja. Os dados exibidos nesta tela, são com base no relacionamento entre **produto x cliente**, realizado na rotina **QIPA070 - Inspeção de Processos**, onde serão gravados os registros nas tabelas **QQ4 - Relacionamento Prod x Cliente** e **QQ7 - Amarr Prod x Clientes - Ensaios**.
