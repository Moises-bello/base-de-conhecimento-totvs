---
content_hash: c5a84e0807fab16b537228d6ad26f43326f63ca37eba9ed06ccd176ceda61aa8
fetched_at: '2026-06-29T00:09:32.683749+00:00'
page_id: '425458900'
product: rm
source: tdn-rm
title: Layout de Importação de Gabarito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458900
version: 2
---

Segue o layout da Importação de Gabaritos respostas de **questões fechadas**:

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Obrigatório?** |
| INDICADOR | Indicador de tipo de arquivo. Para esse layout trará sempre o valor "P" | Sim |
| CODCOLIGADA | Código da coligada | Sim |
| IDPS | Código do processo seletivo | Sim |
| IDETAPA | Código da etapa | Sim |
| NUMERO\_CARTAO | Número do cartão de repostas | Não |
| NUMERO\_INSCRICAO | Número da inscrição | Sim |
| RESPOSTA\_CANDIDATO | Seqüência de respostas do candidato.  Respeita a ordem das questões no caderno de prova. Poderá conter:   1 - alternativas à A,B,C,D...;   2 - asterisco "\*" à Quando o candidato marcar mais de uma alternativa para a questão, ou seja, anulou a questão;   3 - espaço em branco à O candidato não marcou nenhuma das alternativas, ou seja, anulou a questão.   Exemplo de conteúdo:   "B \*EEEEDECA BAACBCBEE" | Sim |
| QTD\_QUESTÕES | Quantidade de questões | Sim |

**Ex.:**  
 INDICADOR;CODCOLIGADA;IDPS;IDETAPA;NUMERO\_CARTAO;NUMERO\_INSCRICAO;RESPOSTA\_CANDIDATO;QTD\_QUESTOES P;1;29;40;1;1;ABCDEABCD;10  
 Segue o layout da Importação de Gabaritos respostas de **questões abertas**:

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Obrigatório?** |
| INDICADOR | Indicador de tipo de arquivo. Para esse layout trará sempre o valor "R" | Sim |
| CODCOLIGADA\_1 | Código da coligada | Sim |
| IDPS\_1 | Código do processo seletivo | Sim |
| IDETAPA\_1 | Código da etapa | Sim |
| NUMERO\_CARTAO\_1 | Número do cartão de respostas | Não |
| NUMERO\_INSCRICAO\_1 | Número da inscrição | Sim |
| C\_1\_R\_1 | Nota da prova aberta número 1 | Sim |
| C\_1\_R\_2 | Nota da prova aberta número 2 | Não |

**Ex.:**  
    
 INDICADOR;CODCOLIGADA\_1;IDPS\_1;IDETAPA\_1;NUMERO\_CARTAO\_1;NUMERO\_INSCRICAO\_1;C\_1\_R\_1;C\_1\_R\_2; R;1;29;39;1;1;1;5;
