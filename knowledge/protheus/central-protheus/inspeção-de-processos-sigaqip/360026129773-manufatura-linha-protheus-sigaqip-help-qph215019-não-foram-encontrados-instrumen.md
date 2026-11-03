---
article_id: 360026129773
category: Inspeção de Processos (SIGAQIP)
content_hash: 48969c501a9f129e536cc0f556fa502e2f91cf5ce5ada9b178b3c0c4dcc2299e
fetched_at: '2026-06-28T22:42:25.778989+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help QPH215019 - Não foram encontrados
  instrumentos
type: support-article
updated_at: '2021-10-01T13:13:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026129773-Manufatura-Linha-Protheus-SIGAQIP-Help-QPH215019-N%C3%A3o-foram-encontrados-instrumentos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Na rotina **QIPA215 - Resultados**, ao selecionar um instrumento é retornada a mensagem **QPH215019 - Não foram encontrados instrumentos!**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**A mensagem ocorre quando o instrumento não foi localizado na tabela **QM2 - Instrumentos** ou o mesmo não está calibrado.  
  
**Solução**  
Na rotina **QMTA010 - Instrumentos**, verifique se o instrumento existe na filial em questão e se o mesmo está com o status **Calibrado e Ativo**.   
  
**Importante**  
Caso desejar que o instrumento não seja validado ao realizar o preenchimento do laudo, altere o parâmetro **MV\_QPVLIN - Indica se irá validar o instrumento no momento na medição** para **N**.  
  
Para que não seja obrigatório o preenchimento de instrumento, configure o parâmetro **MV\_QPINSOB - Define se é obrigatória a especificação do instrumento para a gravação dos resultados** como **N**.
