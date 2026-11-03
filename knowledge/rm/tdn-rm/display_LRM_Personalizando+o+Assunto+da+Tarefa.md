---
content_hash: e766b69ba4cdec5e3f07af9153f9335832ab34dc59efcf22bc7d3491bac9e0c7
fetched_at: '2026-06-29T00:11:06.355405+00:00'
page_id: '634036772'
product: rm
source: tdn-rm
title: Personalizando o Assunto da Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Personalizando+o+Assunto+da+Tarefa
version: 2
---

Segue abaixo um exemplo de duas tarefas, uma criada com uma fórmula de personalização do assunto (código 331) e outra com o texto padrão (Nome do Tipo de Atendimento)   
  
Tarefa de código 331 com personalização.

Tarefa de código 330 sem personalização.

O uso de fórmula para definir o repasse de uma etapa, é uma ferramente poderosa e de comum uso no sistema TOTVS Aprovações e Atendimento, da mesma forma, essa ferramenta também pode ser usada no aplicativo Minhas aprovações, segue abaixo alguns exemplos uteis:

**Fórmula para alterar o assunto (ou outro campo) do atendimento**

Para isso, os seguintes passos devem ser seguidos:

1 - Criar 3 funções de fórmula conforme imagens abaixo:

2 - Criar uma sentença SQL que traga as informações desejadas, ela deve conter a tabela HATENDIMENTOBASE filtrada pelas formulas anteriores, essa SQL pode conter qualquer tabela relacionada com a atendimentos, nesse exemplo, iremos acrescentar o id do movimento ao assunto:

SELECT TMOV.IDMOV   
FROM HATENDIMENTOBASE (NOLOCK)   
LEFT JOIN TMOVATEND (NOLOCK) ON (HATENDIMENTOBASE.CODCOLIGADA = TMOVATEND.CODCOLIGADAATEND AND   
HATENDIMENTOBASE.CODLOCAL = TMOVATEND.CODLOCAL AND  
HATENDIMENTOBASE.CODATENDIMENTO = TMOVATEND.CODATENDIMENTO)  
LEFT JOIN TMOV (NOLOCK) ON (TMOVATEND.CODCOLIGADA = TMOV.CODCOLIGADA AND   
TMOVATEND.IDMOV = TMOV.IDMOV)  
WHERE HATENDIMENTOBASE.CODCOLIGADA = :FRM\_COLIGADA  
AND HATENDIMENTOBASE.CODLOCAL = :FRM\_CODLOCAL  
AND HATENDIMENTOBASE.CODATENDIMENTO = :FRM\_CODATEND

3 - Criar a fórmula que irá alterar o assunto do atendimento e atribui-la a primeira etapa do fluxo, caso a primeira etapa já possua uma fórmula, esses comandos podem ser acrescentado à fórmula existente sem influenciar no seu funcionamento, seguem os comandos:

DECL IDMOV;  
DECL NOVOASSUNTO;  
EXECSQL( 'SQL\_002' );  
SETVAR( IDMOV, CONCATENA('Gerado pelo movimento:', RESULTSQL( 'SQL\_002', 'IDMOV' ), ''));  
SETVAR( NOVOASSUNTO, CONCATENA(IDMOV, CAMPOSATENDIMENTO('ASSUNTOOC'), ' - '));  
ALTERARCAMPOATENDIMENTO(CONCATENA('ASSUNTOOC', NOVOASSUNTO, '='));

Ao utilizar mais de uma sentença sql com o mesmo código e vincular a mesma no parâmetro "Consulta SQL a ser utilizada para recuperar os registros para a visão de atendimentos" é importante que os campos sejam informados em ordem , e não é recomendado o uso do \* .
