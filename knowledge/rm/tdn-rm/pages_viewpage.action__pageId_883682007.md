---
content_hash: ffa7e0eed3277608f3663dc271864bcae22eb9fb6dd2a56f1856c0dcac7c030d
fetched_at: '2026-06-29T00:12:00.689739+00:00'
page_id: '883682007'
product: rm
source: tdn-rm
title: Utilitários - Conversores - Limpeza de Tabelas de Log
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883682007
version: 3
---

A ferramenta de ***Limpeza de Tabelas de Log*** é essencial para manter o banco de dados sempre eficiente, evitando problemas de performance e armazenamento.

O uso desta ferramenta garante uma boa performance no *reajuste das venda*s e na geração da *ficha financeira*, entre outros.

Ao acessá-la, o TCGI exibe uma tela inicial para que seja informada a *descrição* do processo, caso o usuário julgue necessário.

Após clicar no botão avançar, o sistema exibe a tela do *Termo de Responsabilidade* com as informações abaixo e a opção para *concordar* com ele:

*"Atenção:*

*Este processo apagará os registros antigos de forma **irreversível** das seguintes tabelas de log:*

*- XLOGVENDAPARCELA*  
*-FTRBLANHST*  
*-FLANINTEGRACAOHST*  
*-FLANRATCCUHST*  
*-FLANRATDEPHST*  
*-FRELLANHST*  
*-FRETENCAOACUMULADARATEIOHST*  
*-FRETENCAOACUMULADAHST*  
*-FRETENCAOIRRFHST*  
*-FLANBAIXAINTEGRACAOHST*  
*-FLANBAIXARATCCUHST*  
*-FLANBAIXARATDEPHST*  
*-FLANBAIXATRBHST*  
*-FLANBAIXAHST*  
*-FHISTVALORESINTEGRACAOHST*  
*-FLOGVALORESHST*  
*-FLANHST*

*Sugerimos um "backup da base de dados" antes da execução do processo."*

Importante!

Por segurança, os valores apagados das tabelas citadas no termo de aceite acima, são transferidos para uma outra tabela o mesmo nome com o seguinte formato de nome: [*nome\_da\_tabela*]\_backup.

As informações preservadas nestas novas tabelas não será mais utilizadas por nenhum processo do RM e caso seja necessário verificar alguma informação nelas, essa ação deverá ser realizada via banco de dados.

Na tela seguinte o sistema apresenta a *Configuração de Limpeza das Tabelas de Log*, para que o usuário parametrize ou não, conforme permissão definida no parâmetro de [*Log da Venda*](https://tdn.totvs.com/pages/viewpage.action?pageId=435104754), o tempo em anos, que os logs serão mantidos, por cada situação da Venda:

A execução deste processo será realizada em segundo plano e conforme a quantidade de logs nas tabelas citadas acima, pode demorar para ser executado na primeira vez. Por este motivo, recomendamos que seja realizado um agendamento de execução do mesmo, para um horário em que o acesso a banco tenha menos concorrência.

Recomendamos também o agendamento periódico de execução da ferramenta, para manter a performance do sistema.

Após a conclusão, o job de execução exibirá a quantidade de logs excluídos, conforme exemplo abaixo:

*Total de registros de log excluídos: [35464]*

É importante parametrizar também a opção ***Limitar o tamanho do log do reajuste por data base***, nos parâmetros do *[Reajuste Monetário](https://tdn.totvs.com/pages/viewpage.action?pageId=435105185)***.**

Boas Práticas!

Tabelas de log tendem a acumular um volume grande de dados que com o tempo, o que podem:

1. **Impactar a Performance**: Tabelas de log muito grandes tornam as consultas mais lentas, especialmente as que realizam varreduras completas (full scans) nessas tabelas. Isso afeta diretamente os processos que dependem dos dados de log, como auditorias e relatórios, e pode sobrecarregar o banco, prejudicando operações em tempo real.
2. **Consumo de Espaço em Disco**: Logs grandes ocupam espaço em disco de maneira exponencial. Sem limpeza, o banco pode atingir o limite de armazenamento, resultando em custos maiores com infraestrutura ou, no pior caso, interrupções nas operações até que haja espaço liberado.

Assim, implementar políticas de retenção e limpeza periódica nas tabelas de log é uma prática recomendada para manter o banco de dados performático e o uso de disco sob controle.
