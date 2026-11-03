---
article_id: 16636068190487
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 49f0bd1a8a65bf1eaea54830a8ba8ef54d69890872d82243440215119cf2a033
fetched_at: '2026-06-28T22:42:44.452991+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Mensagem de erro array out of bounds
  ... on WSPCP:RECEIVEMESSAGE(WSPCP.PRW) '
type: support-article
updated_at: '2023-08-10T11:24:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16636068190487-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-de-erro-array-out-of-bounds-on-WSPCP-RECEIVEMESSAGE-WSPCP-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16636112198679) Tempo aproximado para leitura: **00:01:24 min****Ocorrência**Ao integrar um arquivo **XML** do **TOTVS MES** com o Sistema, ocorre o *error.log* **array out of bounds** ... **on WSPCP:RECEIVEMESSAGE(WSPCP.PRW)**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Esse erro ocorre quando o parâmetro **MV\_TWSPCP - Definição dos parâmetros utilizados na função ManualJob chamada na função WSPCP. Na seq: nInactive, nMax,nMinFree e nIncr** não possui os quatro valores numéricos que especificam o tempo e números de threads separados por vírgula.  
  
**Solução**Preencher no parâmetro **MV\_TWSPCP** os valores pertinentes ao cenário, onde no primeiro valor deve-se informar o tempo de inatividade das threads em segundo, no segundo valor, o número máximo de threads abertas simultaneamente, no terceiro valor o número mínimo de threads livres e no quarto valor o número de threads acrescidas quando a quantidade livre for atingida.  
  
**Exemplo****MV\_TWSPCP** = 20,10,2,3  
  
**Saiba mais**No *link* [serviço do MES com diversas conexões simultâneas](https://tdn.totvs.com.br/pages/viewpage.action?pageId=654486548) temos a documentação a respeito desse parâmetro.
