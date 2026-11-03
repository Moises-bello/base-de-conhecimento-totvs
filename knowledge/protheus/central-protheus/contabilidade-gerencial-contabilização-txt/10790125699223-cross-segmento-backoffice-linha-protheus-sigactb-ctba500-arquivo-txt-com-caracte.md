---
article_id: 10790125699223
category: Contabilidade Gerencial - Contabilização txt
content_hash: 5d197591dd907854357d6c67e81b15f51627a7fa96100b8c33f10a445a491937
fetched_at: '2026-06-28T22:40:55.446269+00:00'
product: protheus
section_id: 1500001537521
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA500 - Arquivo TXT
  com caracteres especiais
type: support-article
updated_at: '2022-12-07T18:19:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10790125699223-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA500-Arquivo-TXT-com-caracteres-especiais
---

**Dúvida**Como importar arquivo TXT com caracteres especiais no campo de histórico do lançamento.

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

#### **Solução:**

No sistema existe o parâmetro MV\_ACENTO que permite a utilização de letras com acentos.  
  
Na rotina de contabilização TXT alguns tipos de formatação(Caracteres especiais ou acentos em letras) podem gerar uma mensagem impeditiva de erro na estrutura do arquivo e com isso não permitindo a sua importação.

![](https://tdn.totvs.com/download/attachments/657221568/image2021-12-28_10-19-8.png?version=1&modificationDate=1640697548320&api=v2)

Isso pode acontecer caso a estrutura de campos no txt possa estar incorreta ou se existirem algum caractere especial em que não é permitido e ocasiona a mensagem no txt lido.

E caso seja desejado utilizar na descrição algum caractere especial de acento por exemplo ?

**Nesse caso temos dois comportamentos:**  
  
Caso queira contabilizar o TXT com o caractere especial ele será exibido da seguinte forma:

![](https://tdn.totvs.com/download/attachments/657221568/image2021-12-28_10-29-14.png?version=1&modificationDate=1640698154810&api=v2)

Vale ressaltar que caso seja ocasionado erro de estrutura em arquivos que contenham esses caracteres deve-se formatar o arquivo para o formato **ANSI** e verificar os caracteres especiais contidos nele.

É importante também verificar se o parâmetro **MV\_ACENTO** esta como **"S"**, caso esteja como N o lançamento será realizado sem os acentos e se estiver com a formatação **ANSI**:

![](https://tdn.totvs.com/download/attachments/657221568/image2021-12-28_11-1-17.png?version=1&modificationDate=1640700077423&api=v2)

Arquivos em formato UTF podem ser lidos normalmente, mas dependendo do caractere especial contido podem ocasionar a mensagem de erro na estrutura, assim tornando-se necessário verificar a estrutura e/ou alterar sua formatação.

**Formatação do arquivo TXT:**

Para formatação no modelo ANSI, seguir os passos abaixo para Bloco de Notas e NotPAd++

Caso utilize o **Bloco de Notas** padrão poderá alterar a codificação no momento de salvar o arquivo:  
![](https://totvssuporte.zendesk.com/attachments/token/6CMzAfOuGYVrRQkPRRHAWz4Un/?name=image.png)  
  
Caso utilize o **NOTEPAD++** poderá alterar a codificação no menu formatar:  
  
![](https://totvssuporte.zendesk.com/attachments/token/FBIutQUWCiqPcs42gqhNPynQ0/?name=image.png)

**Saiba mais:**

<https://tdn.totvs.com/display/public/PROT/CTBA500+Arquivo+txt+com+acentos>

[Cross Segmento - Backoffice Linha Protheus SIGACTB - CTBA500 CONTABILIZAÇÃO TXT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007149031--Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA500-CONTABILIZA%C3%87%C3%83O-TXT)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA500 Configuração para contabilização TXT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018285051-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA500-Configura%C3%A7%C3%A3o-para-contabiliza%C3%A7%C3%A3o-TXT)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB :CTBA500 - Contabilização TXT com mais de uma Filial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021556152-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA500-Contabiliza%C3%A7%C3%A3o-TXT-com-mais-de-uma-Filial)

[Cross Segmento - Backoffice Linha Protheus - CTBA500 - Contabilização TXT com mais de uma data](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021561512-Cross-Segmento-Backoffice-Linha-Protheus-CTBA500-Contabiliza%C3%A7%C3%A3o-TXT-com-mais-de-uma-data)
