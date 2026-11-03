---
article_id: 18065326097815
category: SIGAEST - SALDOS
content_hash: 990b1155c7fd96b1dbfa5a636a1700e6b2f0acaa5fb8a19f9c173b5fb8872539
fetched_at: '2026-06-28T22:39:14.946617+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Saldo de Poder de/em
  Terceiro quando empresa (CNPJ) não existe mais ou mudou o CNPJ como transferir?
type: support-article
updated_at: '2023-10-06T10:45:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18065326097815-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Saldo-de-Poder-de-em-Terceiro-quando-empresa-CNPJ-n%C3%A3o-existe-mais-ou-mudou-o-CNPJ-como-transferir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18065335687063) Tempo aproximado para leitura: **00:04:30 min** **Dúvida**

Quando uma empresa (CNPJ) **não existe mais** (encerrou atividades) ou mudou o CNPJ, quais as opções para transferir ou baixar o Saldo em Poder de Terceiro?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Nesse cenário, é possível de duas formas, vamos destacar por tópico abaixo:

**- 1ª - Mantendo o saldo Em terceiro para a mesma empresa (CNPJ) e a medida que tiver os retornos, pode efetuar o procedimento abaixo:**  
   
Na rotina **Documento de Entrada (MATA103)** pressione a **tecla F12** e habilite o parâmetro ***OPERAÇÃO TRIAGULAR*** para ***Sim***. Dessa forma permite amarrar a Nota Origem ainda do CNPJ que não foi baixado o saldo.

Esse cenário pode ser considerado, tanto para PODER DE TERCEIROS como para PODER EM TERCEIROS. Veja os prints abaixo do parâmetro e observe que tanto na Entrada como na saída de documentos tem esse parâmetro.   
 

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18065775298455)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18065763999895)**

***- 2ª - Não posso manter o saldo no CNPJ que não existe mais, preciso que o saldo em terceiro conste no novo CNPJ. Nesse caso é necessário efetuar os seguintes  passos:***

 - Primeiramente efetuar o **[retorno simbólico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010519121-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-um-retorno-simb%C3%B3lico-limpar-saldo-de-material-que-ficou-em-poder-de-terceiros-?source=search)** baixando o saldo em Poder de Terceiro do CNPJ que não existe mais;

 - Agora incluir a saída simbólica do saldo para o CNPJ existente, dessa forma vai atualizar o saldo em terceiro corretamente para o novo CNPJ.

   
***Observações*:** Para o controle de Poder de terceiros somente é possível através de movimentações por Notas Fiscais, não existe rotina para atualizar o saldo de terceiros. 

***Saiba Mais:***

[SIGAEST - Poder de/em terceiros. Como a tabela SB6 efetua o controle dos saldos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11700511412375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Poder-de-em-terceiros-Como-a-tabela-SB6-efetua-o-controle-dos-saldos-)

[Clique aqui e veja mais artigos sobre SALDOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)

[SIGAEST - Como efetuar um retorno simbólico (limpar saldo) de material que ficou em poder de terceiros?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010519121-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-um-retorno-simb%C3%B3lico-limpar-saldo-de-material-que-ficou-em-poder-de-terceiros-?source=search)
