---
article_id: 16006925992855
category: Inspeção de Processos (SIGAQIP)
content_hash: 4c197ab7b82c75686f7f9a60787bb42df02df4e59fac553460fc9c63162a3425
fetched_at: '2026-06-28T22:42:25.723211+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Definir nível de usuário para emissão
  de laudo
type: support-article
updated_at: '2025-06-04T13:36:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16006925992855-Manufatura-Linha-Protheus-SIGAQIP-Definir-n%C3%ADvel-de-usu%C3%A1rio-para-emiss%C3%A3o-de-laudo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16006933982103) Tempo aproximado para leitura: **00:00:40 min** **Dúvida**Na rotina **QIPA215 - Resultados** como definir o **nível de usuário** para a emissão de **laudo**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**Para definir **nível de usuário** para emissão de laudo na rotina **QIPA215 - Resultados**, existe o parâmetro **MV\_QPLDNIV - Define o nível que o usuário deve possuir, para emitir os laudos de laboratório, operação e geral, respectivamente**.   
No padrão este parâmetro vem com o conteúdo igual 000 representando três posições. A primeira posição refere-se ao **Laudo do Laboratório**, a segunda ao **Laudo da Operação** e a terceira e última ao **Laudo Geral**. Por exemplo, se o conteúdo do parâmetro estiver 129, para emissão do Laudo do Laboratório o usuário precisa ter nível 1, para emissão do Laudo da Operação o usuário dever ter nível 2, e para emissão do Laudo Geral o usuário precisa ter nível 9.  
Os níveis devem ser definidos com **valor entre 0 e 9** no campo **Nível - QAA\_NIVEL** da rotina **QIEA050 - Usuários**.
