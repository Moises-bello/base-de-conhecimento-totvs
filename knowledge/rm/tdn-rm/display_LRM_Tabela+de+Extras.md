---
content_hash: 73c44dc40b27af8ff7412ef30d912eeabd284bdd3aba847b60fd887b26686358
fetched_at: '2026-06-29T00:10:11.270512+00:00'
page_id: '452720021'
product: rm
source: tdn-rm
title: Tabela de Extras
type: documentation
url: https://tdn.totvs.com/display/LRM/Tabela+de+Extras
version: 2
---

**Tabela de Extras**

Cadastro de intervalos diários que definem o tempo a ser considerado de extras no dia.  
**Atenção:** Para que este cálculo seja considerado, é necessário que a tabela de extras esteja  
definida como **Diário** na etapa de **Extra** no **Parametrizador do Sindicato**.

Exemplo:

Jornada Planejada: 08:00 12:00 14:00 18:00  
Jornada Executada: 07:50 12:00 14:00 18:00

Intervalos cadastrado na tabela de extras:

Início: 00:00 Fim: 00:10 Desconsiderar: 00:00

Cálculo das ocorrências:  
07:50 - 08:00 => Extra Normal Desconsiderada  
08:00 - 12:00 => Trabalho  
14:00 - 18:00 => Trabalho

Para o exemplo acima, o funcionário executou 10 min de extras no dia que serão consideradas  
no intervalo da tabela de extras cadastrada, portanto estes minutos serão desconsiderados,  
uma vez que no cadastro, foi informado o valor 00:00.

Caso o funcionário tivesse feito 11 minutos de extra neste dia, esta quantidade não se  
encaixaria em nenhum dos intervalos cadastrados na tabela de extras, e por este motivo,  
nada seria desconsiderado, ou seja, a extra seria calculada integralmente.
