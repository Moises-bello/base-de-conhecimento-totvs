---
article_id: 12042426679191
category: SIGAEST - CUSTOS
content_hash: 89e935e98659a430725751810944339873294905ad64bb3415db303438256c22
fetched_at: '2026-06-28T22:39:02.239350+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330/MATA331/MATA038
  - Invalid column name 'CT2_MSUIDT'
type: support-article
updated_at: '2023-03-24T18:23:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12042426679191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-MATA331-MATA038-Invalid-column-name-CT2-MSUIDT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:30 min****Ocorrência**Ao executar as rotinas de Custo Médio ou Contabilização do Custo Médio ocorre o error.log: "***Invalid column name 'CT2\_MSUIDT'****"*  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir do release 12.1.33  
**Causa**O erro em questão ocorre devido ao sistema tentar posicionar em um novo campo do arquivo CT2 que o ambiente não possui no Dicionário (SX3) ou dentro da tabela no Banco de Dados.

**Solução**

Foi criada uma proteção na rotina para não apresentar o erro descrito. Sendo assim, não há a obrigatoriedade de atualização de UPDDISTR para que o Dicionário passe a ter o campo CT2\_MSUIDT.

O campo é o CT2\_MSUIDT foi criado para o Conciliador Contábil. Caso sua empresa faça uso do Conciliador Contábil, basta pular para o passo 2.

**1.** Aplique o  Pacote de Correção abaixo, efetuando o Download conforme a sua release. **[Patch de correção para a 12.1.33](https://suporte.totvs.com/portal/p/10098/download?e=1094013)** | **[Patch de correção para a 2210](https://suporte.totvs.com/portal/p/10098/download?e=1094014)**

Observação: Para qualquer aplicação de pacote é recomendável que o faça primeiro em ambiente de homologação.

**2.** Caso a empresa realmente tenha a necessidade de ter o campo no dicionário pois usa o Conciliador Contábil, efetue o processo do minuto 2:45 até o 07:36 do vídeo abaixo (Esse trecho ensina como efetuar a criação dos campos necessários):

Para maiores detalhes sobre a configuração e informações do Conciliador Contábil, veja abaixo a documentação:  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA940 - Conciliador Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451317698583-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-Cont%C3%A1bil?source=search)

|  |
| --- |
| **Observação importante:** Caso os passos acima tenham sido feitos e o error.log persistir **ou caso tenha dúvidas sobre o Conciliador Contábil** ou o processo de configuração do mesmo, recomendamos fortemente que acione o Suporte Técnico da equipe **Protheus Ativo e Contábil** |

**Saiba mais**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
