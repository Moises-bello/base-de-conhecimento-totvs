---
article_id: 360053001473
category: Financeiro - Contas a Pagar
content_hash: 5a7cd06bdf1469d5f7e7fa9b3c1ef2ba7d656d6b7ea78de9d90d1c1bb1849643
fetched_at: '2026-06-28T22:38:09.759398+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Help:  TITNAOXADO
  ao cancelar a baixa do título'
type: support-article
updated_at: '2026-03-16T17:46:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053001473-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Help-TITNAOXADO-ao-cancelar-a-baixa-do-t%C3%ADtulo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21013750450455)**Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Ao realizar o cancelamento da baixa do título na rotina **FINA750/ FINA740** ou na rotina **FINA080/FINA070** ocorre o **Help**: **TITNAOXADO**  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084251134)**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**  
Esse incidente ocorre, pois possui divergência entre os tamanhos de campos nas tabelas **SE2** e **SE5**  
Exemplo: Na tabela **SX3 (dicionário)** o campo **E2\_PARCELA** está com tamanho = 2 e na **E5\_PARCELA** está com tamanho = 3  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084249914)

**Ou**

O tamanho dos campos da chave de identificação do título está diferente no banco de dados.

Exemplo:

Na imagem abaixo podemos ver que na tabela de dicionário SX3 o tamanho do campo parcela tem tamanho 2

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/32096988528023)](https://centraldeatendimento.totvs.com/hc/article_attachments/32096988528023)

Na imagem abaixo podemos abrir o banco de dados e consultar para ver se o tamanho do campo parcela na SE2 possui o mesmo tamanho de campo.

Devemos abrir a tabela SE2 ao invés da SX3

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/32096955619223)](https://centraldeatendimento.totvs.com/hc/article_attachments/32096955619223)

Caso tenha diferença de tamanho, irá apresentar o problema de relacionamento entre a tabela SE1/SE2 e a tabela SE5 e, ao tentar estornar, irá apresentar o help TITNAOXADO.

Essa consulta deverá ser feita entre as tabelas SE1/SE2 e SE5 referentes às chaves de identificação do título, que são:

filial + prefixo + número + parcela + fornecedor + loja 

**Solução**  
No configurador existe o grupo de campos **Parcela,** no padrão do sistema, os tamanhos de campos deve estar iguais no dicionário e banco de dados. Solicite ao seu executivo de soluções de negócio (ESN) a visita de um analista in loco para avaliar e corrigir a estrutura do seu ambiente.   
A chave de identificação do título é composta pelos campos **FILIAL** + **PREFIXO** + **NUMERO** + **PARCELA** + **FORNECEDOR** + **LOJA**. Temos esta chave nas tabelas (**SE1**/**SE2**/**SE5**).  
Se "o tamanho" de algum desses campos estiver diferente entre essas tabelas, o incidente será apresentado.  
Outro problema que pode gerar o help seria a sequência de baixa no campo **E5\_SEQ**,  caso a próxima baixa esteja com a mesma sequência da primeira, o help também é apresentado. Toda vez que realiza uma baixa e um cancelamento, o sistema grava uma sequência conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21013065934743)

**Importante**

Os parâmetros **MV\_BX10925 e MV\_BR10925****n****ão devem ser alterados, uma vez que, no momento da implantação do*****Protheus*****, foi definido como a empresa irá tratar o imposto.**

**A alteração dos parâmetros mencionados resultará na exibição da mensagem de erro, pois modifica o comportamento do sistema na geração dos impostos.**

**A manipulação da base de dados não é contemplada em nosso escopo de atendimento de Suporte Técnico; esse tipo de procedimento é efetuado apenas por analista in loco. Confira nosso Escopo -**  [https://tdn.totvs.com/pages/releaseview.action?pageId=547876496](https://www.google.com/url?q=https://tdn.totvs.com/pages/releaseview.action?pageId%3D547876496&sa=D&source=hangouts&ust=1597871158503000&usg=AFQjCNF21LurfJgG0snU2MvgXxh34R8MCw)

[Como consultar o tamanho de campos no banco de dados + E5\_SEQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18890795067927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Contabiliza%C3%A7%C3%A3o-duplicando-ou-gerando-grava%C3%A7%C3%A3o-incorreta-do-campo-da-tabela-Sequ%C3%AAncia-de-Baixa-E5-SEQ)
