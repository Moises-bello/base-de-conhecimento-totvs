---
article_id: 28149640390167
category: Inspeção de Processos (SIGAQIP)
content_hash: 570d8a6f7062dd1d9862b0d8ede85afd2f263bc31e03a9eeb1cb418e5385e070
fetched_at: '2026-06-28T22:42:25.849506+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Mensagem integração com Metrologia
  no APP Minha Produção
type: support-article
updated_at: '2024-11-29T14:01:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28149640390167-Manufatura-Linha-Protheus-SIGAQIP-Mensagem-integra%C3%A7%C3%A3o-com-Metrologia-no-APP-Minha-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28149640382103) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**Ao utilizar **SIGAQIP - Inspeção de Processos** no **APP Minha Produção** ocorre a mensagem **Integração com Metrologia ativa. Utilize o Protheus para informar os Instrumentos utilizados e preencher ou editar o laudo.**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**A mensagem ocorre quando o parâmetro **MV\_QIPQMT - Integração do SIGAQIP com o SIGAQMT** tem o conteúdo igual a **S - Sim**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Para **manter a integração**, o parâmetro **MV\_QIPQMT** deverá ser mantido com conteúdo igual a **S - Sim**, e a tratativa de preenchimento de **Instrumento e Laudo** ocorrerá no **Protheus;**

2. Para **não manter a integração**, altere o conteúdo do parâmetro **MV\_QIPQMT para N - Não**. Esta alteração somente terá validade para nova revisão da especificação na rotina **QIPA010 - Especificação de Produto** e que esta especificação não tenha mais o instrumento preenchido, além de gerar nova inspeção relacionada a esta mesma numeração de revisão;  
  
**Saiba mais**  
Atualmente, conforme documentação [Manufatura - Linha Protheus - SIGAQIP - Funcionalidade e Interface do SIGAQIP no APP Minha Produção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16255926887575-Manufatura-Linha-Protheus-SIGAQIP-Funcionalidade-e-Interface-do-SIGAQIP-no-APP-Minha-Produ%C3%A7%C3%A3o) esta funcionalidade não faz parte do escopo do **SIGAQIP** no **APP Minha Produção**.
