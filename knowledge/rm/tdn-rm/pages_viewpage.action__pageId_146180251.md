---
content_hash: 1d82babefc8f74fe61c9be94a303d56c59952787c07d84e21a7224b698160ab6
fetched_at: '2026-06-29T00:05:55.751510+00:00'
page_id: '146180251'
product: rm
source: tdn-rm
title: Conversor da Compensação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146180251
version: 21
---

Importante

Este processo deverá ser executado apenas quando for solicitado pela Equipe do Suporte.

**INFORMAÇÕES ADICIONAIS:**

Foi criado um novo modelo de banco de horas e desta forma durante a conversão da base para versão 11.50 ou superior o sistema convertia os dados das tabelas antigas de banco (ABANCOHORFUN ou ACOMPFUN) para a tabela nova (ABANCOHORFUNDETALHE).

O conversor de compensação foi liberado dentro da aplicação porque em bases inconsistentes esta conversão não foi realizada durante a conversão da Base.

**Exemplo:**

1º) Existir dados ao mesmo tempo nas tabelas ABANCOHORFUN e ACOMPFUN. A tabela ABANCOHORFUN guarda informações do banco diário e ACOMPFUN do banco por período. Quando o usuário decide trabalhar com outra parametrização de banco de horas é preciso que antes o banco de horas seja zerado é só depois altere o tipo de banco. Se na tua base existir esta inconsistência é preciso avaliar qual é a informação correta e zerar a informação inconsistente.

 2º) Existirem informações no banco de horas de faltas, atrasos e extras (todas as faixas e tipos) e não existir o evento correspondente informado no sindicato do funcionário.

Observação

Antes de executar o conversor é preciso que as situações citadas acima estejam corrigidas na base. Caso a equipe de Suporte tenha solicitado o processo de **Conversão da compensação**, siga as instruções abaixo para executá-lo:

1. Acesse o gerenciador de banco de dados.
2. Execute as sentenças SQL a seguir para remover os dados das novas tabelas de banco de horas

`DELETE ABANCOHORFUNDETALHE` `WHERE CHAPA='INFORME AQUI O CÓDIGO DA CHAPA' AND` `CODCOLIGADA='INFORME AQUI O CÓDIGO DA COLIGADA'`

`DELETE ASALDOBANCOHORFUNDETALHE WHERE CHAPA='INFORME AQUI O CÓDIGO DA CHAPA'` `AND CODCOLIGADA='INFORME AQUI O CÓDIGO DA COLIGADA'`

`Exemplos:  
   DELETE ABANCOHORFUNDETALHE WHERE CHAPA ='00001' AND CODCOLIGADA = 1\  
   DELETE ASALDOBANCOHORFUNDETALHE WHERE CHAPA ='00001' AND CODCOLIGADA = 1`

     3. Para executar o Conversor da Compensação, deverá :

     a) Acessar o RM e clicar sobre a aba **"**Executar"**.**

  b) No campo "Localizar", pesquise por Conversor da compensação.

c) Na seção **Ponto**, clique sobre o Conversor da Compensação.

d) Será demonstrada o Conversor da compensação. O usuário poderá selecionar um ou mais funcionários e informar uma quebra de seção.

.

e) Ao selecionar "**Executar**" , iniciará a execução do processo, e no fim irá aparecer a mensagem que foi o mesmo foi concluído.

Finalizado o processo, acessar a aba Banco de horas e Saldo do banco de horas para fazer as devidas conferências.

Para maiores informações sobre banco de horas em geral, acesse [Banco de Horas: Conceito e tipos de banco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045694133-RH-RM-PTO-Banco-de-Horas-Conceito-e-tipos-de-banco).
