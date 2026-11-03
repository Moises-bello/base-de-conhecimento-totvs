---
article_id: 9223850384791
category: Contabilidade Gerencial - Lançamento Padrão e Ponto de Lançamento
content_hash: 0e64291d8f4b858c03bd1fcd5e65770f610cef5cb4707e3f1b0fc6964f3bf6f0
fetched_at: '2026-06-28T22:40:34.155782+00:00'
product: protheus
section_id: 1500001549002
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA940 - Conciliador
  Contábil não traz dados.
type: support-article
updated_at: '2024-02-21T20:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9223850384791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-Cont%C3%A1bil-n%C3%A3o-traz-dados
---

**Dúvida**  
Conciliador não traz dados com os filtros informados.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - a partir da release 12.1.33

**Causa**

A rotina pode não apresentar dados por alguns motivos mencionados abaixo:

* O campo de ID não esta preenchido no lançamento que esta realizando o filtro, um exemplo abaixo do lançamento contábil com o campo CT2\_MSUDIT preenchido:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9221901492887)

Então, caso os dados não apresentem na tabela de origem ou no destino, o primeiro passo e verificar se os campos de ID estão preenchidos corretamente.

* A informações inseridas no filtro, para que a rotina realize a busca correta das informações, devera sempre preencher os campos "De" e "Até ", com a informação que deseja filtrar ou informar de "Branco" a "ZZZZZ".

Os campos que são únicos não é necessários serem todos preenchidos, porem para um filtro mais assertivos inserir informações relevantes para os lançamentos que esta buscando.

Para os campos que não são "De" "Até", caso queira inserir mais de uma informação poderá utilizar o separador "," inserindo mais de uma informação no campo.

Exemplo abaixo, dos filtros para conciliação do Contas a Pagar (SE2) com contábil (CT2) :

![Projeto-sem-T_tulo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/9223786336151)

* Caso os dados não tenham sido apresentados na aba Dados da Conciliação:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9223035018007)

Verificar na aba dados não encontrados:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9223039228055)  
  
Os dados apresentados nesta aba são os lançamentos que não realizaram Match automático, será necessário realizar o Match Manual, ou seguir a verificação abaixo cara correção deste, caso.

* Verifique os compartilhamento das tabelas CT2 e CV3, pois as duas deve conter o mesmo compartilhamento

**Solução:**

Caso tenha identificado que os campos de ID não estejam populados poderá rodar o WIZARDUUID na opção 3 (Popular os campos de ID), para a data em questão assim o campo será populado, seguir as orientações do passo 3 da documentação abaixo para o wizard.

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736>

POPULAR OS CAMPOS DE ID

O objetivo da opção Popular os campos de ID é preencher o código de ID único nos registros já gravados do sistema.

Caso não estejam apresentando as informações na Aba Dados da conciliação, significa que na CV3 os campos de ID para estes lançamentos não foi populado ou o lançamento não possui o par para realizar o Match.

Nesse caso poderá rodar a quarta opção do WIZARDUUID para a data em questão, assim o sistema ira preencher os campos de ID com as informações do rastreio.

Se mesmo assim o sistema não realizar o Match automático destes lançamentos, será necessário verificar o rastreio contábil do lançamento para verificar se esta apontando para seu documento de origem correto.

Poderá utilizar a documentação abaixo para verificação do rastreio:

[Cross Segmentos - Backoffice Linha Protheus - SIGACTB - CTBA102 - Exclusão de lançamento contábil gera error.log : Invalid data type on (F3\_DTLANC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9144446577687-Cross-Segmentos-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Exclus%C3%A3o-de-lan%C3%A7amento-cont%C3%A1bil-gera-error-log-Invalid-data-type-on-F3-DTLANC-)  
  
Verificar se o compartilhamento das tabelas CT2 e CV3 estão com o mesmo nível de compartilhamento, pois caso não esteja, o sistema poderá apresentar informações incorretas ou até mesmo gerar erros. Portanto, essa prática não é recomendada.  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB: Como realizar compartilhamento de tabelas no Contabilidade Gerencial (SIGACTB)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032)

**Documentação complementar:**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736>

[Conciliador Genérico - CTBA940 - P12 - Contabilidade Gerencial](https://tdn.totvs.com/pages/releaseview.action?pageId=648811255)

[Instalação Conciliador Contábil CTBA940](https://youtu.be/haI8PfjMspg)

[Como Utilizar o Conciliador Contábil](https://youtu.be/H8dS30e1dL8)

[Como o Conciliador Valida as Contabilizações](https://youtu.be/QQkHHUvT6CA)

Setup - <https://tdn.totvs.com.br/display/public/PROT/Setup+-+Conciliador+-+CTBA940+-+Contabilidade+Gerencial+-+P12>
