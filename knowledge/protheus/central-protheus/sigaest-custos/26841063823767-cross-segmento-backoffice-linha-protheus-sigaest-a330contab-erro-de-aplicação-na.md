---
article_id: 26841063823767
category: SIGAEST - CUSTOS
content_hash: 7793b1fa5e4806dea6ef689a3d4ff6fb69e5dd0688715dd54d3535550bb210c5
fetched_at: '2026-06-28T22:39:00.576176+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - A330CONTAB - Erro
  de Aplicação na Thread de Contabilização
type: support-article
updated_at: '2026-02-11T15:10:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26841063823767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-A330CONTAB-Erro-de-Aplica%C3%A7%C3%A3o-na-Thread-de-Contabiliza%C3%A7%C3%A3o
---

O erro A330CONTAB ocorre durante a contabilização no TOTVS Protheus, relacionado a variáveis ou regras incorretas no Lançamento Padrão (LP). Para corrigir, localize o erro no console.log, identifique a LP acionada, analise as variáveis na STACK, ajuste a regra incorreta e reprocese a rotina. O problema geralmente envolve variáveis inexistentes ou mal configuradas no ADVPL.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26841063794583) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Durante o processamento da etapa de contabilização, ocorre o erro: **A330CONTAB****-****Erro****de****Processamento/Thread de Contabilização**como corrigir?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**  
O erro **A330CONTAB** está diretamente relacionado com o processo de **Lançamento Padrão (LP)**. Esse erro ocorre quando uma variável ou regra usada em um lançamento padrão está incorreta ou não foi encontrada no momento da execução, e pode retomar vários erros por exemplo:

*- variable does not exist*  
*- JOB threads doesn't support remote/visual componentes*  
*- type mismatch on +*

**Ou outros, não importa qual, se retornar A330CONTAB é um problema pontual no Lançamento.**

**Segue exemplos de como pode aparecer em seu sistema:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26841047595799)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37192356199191)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38327278384535)

**Solução**  
Quando o erro ocorre no processo de **Acompanha Custos**, ele é registrado no arquivo `console.log`, onde é possível realizar uma busca utilizando o título do erro: **"Sub-Processo: A330CONTAB"**. Esse filtro vai trazer o cabeçalho do erro, seguido de informações adicionais que ajudam a identificar o ponto exato da falha, como o campo **TRC\_LANTRC/CPADRAO**, que indica a última **LP** acionada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26841063800599)

`variable does not exist TESTE on DETPROVA(MATXFUNA.PRX)`

Isso significa que o sistema não encontrou a variável **TESTE** dentro da função **DETPROVA**, no código-fonte **MATXFUNA.PRX**.

O erro está relacionado com uma regra específica do **Lançamento Padrão** registrado no campo **TRC\_LANTRC**, que, neste caso, é o lançamento **666**. Assim, o próximo passo é investigar onde essa regra está definida e como ela está sendo utilizada na **LP**.

Após identificar a **LP** no **TRC\_LANTRC** (neste caso, a LP 666), filtre a STACK e verifique as condições usadas no código. Ao fazer isso, encontramos que a variável **CVALOR(C)** contém apenas o nome **TESTE**, exatamente a variável que causou o erro na chamada.

`STACK DETPROVA(MATXFUNA.PRX) 30/09/2024 10:30:01`

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26841047600535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26841047602071)

Isso ajuda a localizar onde o erro ocorreu durante o processamento.

Após identificar que a variável **TESTE** está incorretamente configurada, é necessário ajustar a regra de acordo com a programação em **ADVPL**. Verifique se a variável **TESTE** realmente existe e, se necessário, substitua-a pela variável correta.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26841047603479)

**Nota:** Neste exemplo, o uso incorreto da variável foi intencional para demonstrar o erro.

Depois de corrigir o erro na LP (Lançamento Padrão), processe novamente a rotina no sistema para verificar se o problema foi resolvido.

Pode ocorrer erro do tipo:

**A330CONTAB - JOB threads doesn't support remote/visual componentes**

A validação é a mesma, regra na LP ou até mesmo o acionamento de uma customização nas chamdas, que pode ser identificado pela inicial U\_ na tela ou no erro.

---

**Resumo do Processo:**

1. Localize o erro no arquivo `console.log` utilizando o filtro **"Sub-Processo: A330CONTAB"**.
2. Identifique a LP acionada através do campo **TRC\_LANTRC**.
3. Analise a chamada STACK e as variáveis utilizadas no código.
4. Corrija a regra incorreta no lançamento padrão, ajustando a variável que causou o erro.
5. Reprocessar a rotina para validar a correção.

**Outro tipo de erro comum que pode ocorrer na contabilização é o erro da inexistencia de variavel, por exemplo:**

**variable does not exist NOME\_DA\_VARIAVEL on CTRELATION(MATXFUNC.PRX)**

A sugestão, é buscar o nome da variavel em questão dentro do error.log, e caso seja um campo, valide se esse campo esta em um indice de forma incorreta, seja na tabela CT5/CTL ou propria tabela do campo.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro de aplicação na thread de Contabilização*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001884321-MP-SIGAEST-MATA330-Erro-de-aplica%C3%A7%C3%A3o-na-thread-de-Contabiliza%C3%A7%C3%A3o)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
