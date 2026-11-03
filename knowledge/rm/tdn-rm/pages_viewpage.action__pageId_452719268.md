---
content_hash: 45be024bee19a5a8fa4a3fb60448cc7a76cb1e2be1f68c35645805b67aad4af3
fetched_at: '2026-06-29T00:10:04.974411+00:00'
page_id: '452719268'
product: rm
source: tdn-rm
title: Termo Rescisão Contrato de Trabalho (Portarias MTE)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719268
version: 8
---

O novo Termo de Rescisão do Contrato de Trabalho (TRCT) foi instituído pela portaria 1.621/2010 do Ministério do Trabalho e Emprego (MTE) e atualmente, está alterada pela portaria [MTE 1057 de 06 de julho de 2012.](http://portal.mte.gov.br/data/files/8A7C816A36A27C1401389A26D1F73CB8/Portaria%201.057%20unificado.pdf)

Em virtude da [Lei nº 14.553/23](http://www.planalto.gov.br/ccivil_03/_Ato2023-2026/2023/Lei/L14553.htm#:~:text=LEI%20N%C2%BA%2014.553%2C%20DE%2020,raciais%20no%20mercado%20de%20trabalho) passou a ser obrigatório que o Termo de Rescisão de Contrato de Trabalho (TRCT), informe a Raça/cor do funcionário. Para mais informações, acesse [DT - TRCT - Inclusão campo Cor/Raça - Lei nº 14.553/23](https://tdn.totvs.com/pages/viewpage.action?pageId=770944722).  
   
No TOTVS Folha de Pagamento, através deste módulo será gerado para os funcionários demitidos o termo de rescisão no padrão definido pela portaria.  
   
Ao iniciar a parametrização do processo de geração do TRCT, será necessário gravar um Perfil de Parâmetros para que todos os parâmetros definidos fiquem "salvos" para futuras gerações do relatório TRCT.  
Para gravar o perfil, na primeira tela do wizard deverá inserir uma descrição no campo "Perfil de Parâmetros" e clicar no Box "Salvar perfil ao concluir".  
   
Se desejar, poderá informar uma Descrição do Processo, para que no histórico de processo executados seja identificado com a descrição.   
   
Na geração do TRCT deverá definir: Quebra de seção e a grade de Seleção de Funcionários. Esta parametrização servirá como filtro, ou seja, serão gerados TRCT cujas seções dos funcionários correspondam à quebra informada e os funcionários tenham dados compatíveis com a grade de seleção definida.  
   
**Atenção I:**

* No campo "Chapa" da "Seleção de Funcionários", serão listados os funcionários que estão na situação demitidos ou com rescisão calculada para próximo mês.
* As datas dos campos Início e Término da grade "Período de Demissão" são obrigatórias, e determinarão um intervalo para que somente funcionários demitidos dentre o intervalo, tenham o TRCT gerado.
* Os campos que indicam a grade "Competência do Movimento", Mês, Ano e Período respectivamente, deverão ser informados obrigatoriamente para referenciar o movimento de rescisão que será considerado no TRCT.

**Atenção II:**

* Os campos que indicam a grade "Ordem", Dt.De Admissão, Nome e Chapa,  será definida pelo usuário no  momento da geração.Por default virá marcado o campo Dt.de Admissão.

   
**Exemplo de Rescisão:**  
   
O funcionário Chapa 0001 – ITAMAR teve cálculo de rescisão em 20/08/2011, na Competência do Movimento foi: Mês 8, Ano 2011, Período 3.  
   
Parametrização para gerar o relatório TRCT do ITAMAR  
   
Período de Demissão: Início: 01/08/2011    Término: 31/08/2011  
   
Competência do Movimento:  
Mês: 08              Ano: 2011                  Período: 3  
   
   
**Exemplo de Rescisão Complementar:**  
   
O funcionário Chapa: 0002 – João teve cálculo de rescisão em 10/12/2010.  
Houve cálculo de rescisão complementar para o João em 15/07/2011 na Competência do Movimento:  
Mês: 07     Ano: 2011      Período:5  
   
   
Parametrização para gerar o relatório TRCT da rescisão complementar do JOAO  
   
Período de Demissão: Início: 01/12/2010    Término: 31/12/2010  
   
Competência do Movimento:  
Mês: 07              Ano: 2011                  Período: 5  
   
   
   
O Módulo de geração do Termo de Rescisão funcionará com a utilização relatório "FOPREL0001 – Termo de Rescisão – Anexo I da Portaria 1621 – 2010.TotvsReport", que deverá estar importado na base de dados.  
   
No campo "Código do Relatório" deverá ser referenciado o relatório padrão do TRCT.  
   
Caso necessite importar no RM Reports o relatório do TRCT, proceda os passos:  
   
1)      Acesse Relatórios .net (Gerador .Net)  
2)      Clique no botão importar e localize na sua maquina o arquivo do relatório.  
3)      Conclua a importação.  
   
Obs.: O relatório estará disponível na pasta "Objetos Gerenciais" no local de instalação do sistema.  
   
No campo "Fórmula para Saldo de Salário (Campo 50)" deverá referenciar uma fórmula que tenha como retorno o valor do "Saldo de Salário Líquido" pago na rescisão.  
   
**Observação**  
É necessário informar a fórmula para cálculo do Campo 50, porque não existem rubricas padrão pré-definidas pelo MTE para representar Faltas, DSR Perdido, Reflexo de DSR Perdido e etc.  
   
Exemplificamos abaixo uma estrutura de fórmula a ser utilizada:  
   
(MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0001') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0002')) - (MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0008') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0182') + MV(PARMQRY('MESCOMP'), PARMQRY('ANOCOMP'), '0070'))   
   
Detalhando a fórmula, temos:  
   
MV = função de fórmula que retornará o valor de um evento. Os parâmetros desta função são: Mês Competência, Ano Competência, Código do Evento.  
PARMQRY('MESCOMP'), retornará o mês competência informado na geração do TRCT.  
PARMQRY('ANOCOMP'), retornará o ano competência informado na geração do TRCT.  
'0001' é o código do evento Horas Normais, da base exemplo.  
   
            Para obtenção do "Saldo de Salário Líquido" a fórmula utilizada na base exemplo considerou:  
   
Para a soma, os valores dos eventos:   
0001 – Horas Normais  
0002 – Dias Trabalhados  
   
Para subtração, os valores dos eventos:  
0008 – Faltas  
0182 – Horas de Faltas (atraso)  
0070 – DSR Perdido  
   
**Observação**  
A fórmula acima contempla o cálculo de Saldo de Salário da base Exemplo. Desta forma o usuário deverá verificar os códigos de eventos a considerar no cálculo do Líquido Salarial pago na Rescisão e adequar à fórmula.  
   
Existem alguns parâmetros na geração do TRCT que ficará a cargo e entendimento do cliente para sua utilização. São eles:

* **TRCT de rescisão complementar**
* **Campo 66 e 67 Forçar valor do envelope:**Quando este parâmetro estiver marcado, no campo 66 os valores de férias vencidas serão considerados de acordo com o valor lançado no envelope de pagamento, ou seja o valor total dos períodos aquisitivos vencidos para férias em dobro por exemplo. E o valor das férias em dobro informado no campo 67 incluindo as médias caso os parâmetros "Não somar média de férias vencidas (Campo 66)" e/ou "Não somar média de férias prop. (campos 65 e 71)" não estejam marcados. Caso estes parâmetros estejam marcados serão considerados com prioridade. Nesse último caso será separado o campo 66 por período aquisitivo e sem médias conforme indicado abaixo.
* **Data Aviso Prévio Indenizado igual à data de demissão**
* **Não somar média de férias vencidas (Campo 66):**Quando esse parâmetro for marcaso o valor do campo 66 será impresso sem o valor das médias. Neste caso, o usuário deverá parametrizar para que as médias de férias vencidas na rescisão sejam separadas, e os eventos de média existentes no envelope de rescisão estejam com rubricas para serem impressos do relatório do TRCT em outros campos.
* **Não somar média de férias prop. (campos 65 e 71):** Quando este parâmetro for marcado, o valor dos campos 65 e 71 serão impressos sem o valor das médias. Neste caso, o usuário deverá parametrizar para que as médias de férias vencidas e proporcionais na rescisão sejam separadas, e os eventos de média existentes no envelope de rescisão estejam com rubricas para serem impressos do relatório do TRCT em outros campos.
* **Informar o Número de dias no campo 65:** Com este parâmetro marcado será informado no campo 65 a quantidade de dias de férias proporcionais devidos pagos na rescisão. Desmarcado será informado somente a quantidade de avos devidos de férias proporcionais pagos na rescisão.

No TOTVS Folha de Pagamento, o TRCT será gerado a partir das referencia das Rubricas em cada campo correspondente, com exceção do campo 50 que como citado acima, é calculado por fórmula.  
   
Nos cadastros dos eventos deverão existir as rubricas correspondentes a cada evento, sendo as rubricas pré-definidas pelo MTE que tem faixa de código 001 a 036, e as rubricas criadas pelo usuário a partir do número 100, de acordo com a necessidade.  
   
As rubricas pré-definidas pelo MTE estão especificadas no [manual 2.10 do Sistema HomologNet](http://portal.mte.gov.br/data/files/8A7C816A2E7311D1012EFC5F01A5639F/LAYOUT%20ARQUIVO%20IMPORTA%c3%87%c3%83O%20Vers%c3%a3o%202%2010%2011_02_2011%20site.pdf) instituído pela Portaria Nº 1.620, de 14/07/2010, disponível no site do MTE.  
   
   
O Cadastro de Rubricas no TOTVS Folha de Pagamento está localizado em Cadastros | Tabelas Dinâmicas | 'HOMOLOGRUB'. Nesta tabela poderá verificar as rubricas pré-definidas pelo MTE e cadastrar as rubricas que forem necessárias a partir do número 100.   
   
   
Na geração do TRCT, para relacionar as rubricas aos campos correspondentes do relatório, marque o Box "Alterar Rubricas" e clique em "Avançar".  
   
Será exibida a Tela "Edição das Rubricas", divididas em duas páginas Proventos e Desconto, com todos os campos do relatório que deverão ter relacionada sua respectiva rubrica.  
Por existir rubricas pré-definidas pelo MTE, os campos de Rubricas para a geração do relatório TRCT que são correspondentes as estas rubricas, estarão desabilitados.   
   
Os campos desabilitados são: 51, 52, 53, 54, 55, 56, 57, 60, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93 e 98.  
   
Os campos que não são correspondentes as rubricas pré-definidas pelo MTE, estarão habilitados e neles deverão ser informadas as rubricas correspondentes que foram cadastradas pelo usuário a partir do número 100.   
   
**Observações**   
1)   A associação de rubricas aos eventos que são utilizados no sistema para movimentação da Folha de Pagamento é de responsabilidade do usuário.  
2)   Os campos de Rubricas habilitados na geração TRCT que devem ter Rubricas relacionadas, serão os campos que o usuário verificará que existem eventos pagos na movimentação da Folha de Pagamento sendo de responsabilidade do usuário identificar qual rubrica deverá estar relacionada aos eventos e qual rubrica referenciar aos campos.  
   
   
Na tela de Parametrização de Geração do TRCT existe o parâmetro "Imprimir verbas rescisórias pré-definidas quando valor igual a zero". Este parâmetro quando marcado, irá imprimir todos os campos de verbas rescisórias que estão definidos no Anexo I, da Portaria Nº1.621 de 14/07/2010, mesmo que algum tenha valor igual zero.  
   
Com o parâmetro desmarcado, serão impressos os campos definidos no Anexo I, que o valor for maior que zero.  
   
Quando algum campo de Rubrica poderá apresentar valor igual zero?  
   
1)   Campos de Rubricas do TRCT que têm código de Rubrica associado, mas na movimentação de Rescisão não existe evento que possua a rubrica associada, serão gerados no Termo de Rescisão com valor zerado.  
   
2)   Campos que não possuem código de Rubrica relacionada serão gerados com valor zerado.  
   
3)   Evento lançado na movimentação de rescisão com valor zero, mesmo que exista código de rubrica relacionado ao campo correspondente, fará com que o campo seja gerado com valor zero.  
   
   
A tabela abaixo detalha os campos de Verbas Rescisórias do TRCT com a relação das rubricas pré-definidas e a indicação dos campos que terão rubricas criadas pelo usuário a partir do número 100.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campos 50 a 99 – Informação de verbas rescisórias provento** | | | |
| **Campos de Rubricas e Descrições** | | **Rubricas do HomologNet Correspondente** | Rubricas relacionadas a eventos Provento |
| Campo 50 | Saldo de Salário; | FÓRMULA CAMPO 50 |
| Campo 51 | Comissão; | 007 - Comissão |
| Campo 52 | Gratificação; | 017 - Gratificação |
| Campo 53 | Adicional de Insalubridade; | 013 - Insalubridade |
| Campo 54 | Adicional de Periculosidade; | 014 - Periculosidade |
| Campo 55 \* | Adicional Noturno; | 012 - Horas adicional Noturno |
| Campo 56 \*\*\* (caso exista mais de uma verba diversa, criar os subitens 56.1, 56.2, 56.3...); | Horas - Extras | 004 - Hora Extra |
| Campo 57 | Gorjetas; | 011 - Gorjetas |
| Campo 58 | Descanso Semanal Remunerado (DSR); | Rubricas criadas pelo usuário a partir do número 100 |
| Campo 59 | Reflexo do DSR sobre Salário Variável; |  |
| Campo 60 | Multa Art. 477, § 8º/CLT; | 009 - Multa Art. 477 |
| Campo 61 | Multa Art. 479/CLT; | Rubricas criadas pelo usuário a partir do número 100 |
| Campo 62 | Salário –Família; |  |
| Campo 63 | Décimo –Terceiro Salário Proporcional; |  |
| Campo 64 \*\*\* – (caso exista mais de uma verba diversa, criar os subitens 64.1, 64.2, 64.3...) | Décimo –Terceiro Salário Exercícios Anteriores |  |
| Campo 65 *(Dica Blog)* | Férias Proporcionais; |  |
| Campo 66 \* – (caso exista mais de uma verba diversa, criar os subitens 66.1, 66.2, 66.3...); *(Dica Blog)* | Férias Vencidas |  |
| Campo 67 \* – (caso exista mais de uma verba diversa, criar os subitens 67.1, 67.2, 67.3...); | Férias Vencidas (Reflexo/Dobra) |  |
| Campo 68 | Terço Constitucional de Férias; |  |
| Campo 69 | Aviso –Prévio Indenizado; |  |
| Campo 70 | Décimo –Terceiro Salário (Aviso–Prévio Indenizado); |  |
| Campo 71 *(Dica Blog)* | Férias (Aviso–Prévio Indenizado); |  |
| Campo 72 | Percentagem; | 006 - Percentagem |
| Campo 73 | Prêmios; | 008 - Prêmios |
| Campo 74 | Viagens; | 010 - Viagens |
| Campo 75 | Sobreaviso; | 015 - Sobreaviso |
| Campo 76 | Prontidão; | 016 - Prontidão |
| Campo 77 | Adicional por Tempo de Serviço; | 018 - Adicional Tempo de Serviço |
| Campo 78 | Adicional por Transferência de Localidade de Trabalho; | 019 - Adicional Por Transferencia de Localidade de Trabalho |
| Campo 79 | Salário Família Excedente ao Valor Legal; | 020 - Salario Familia no que exceder o valor legal obrigatorio |
| Campo 80 | Abono/Gratificação de Férias Excedente 20 Dias Salário; | 021 - Abono ou gratificacao de férias |
| Campo 81 | Valor Global Diárias para ViagemExcedente 50% Salário; | 022 - Diarias para viagem |
| Campo 82 | Ajuda de Custo Art. 470/CLT; | 023 - Ajuda de custo |
| Campo 83 | Etapas Marítimos; | 024 - Etapas Maritimo |
| Campo 84 | Licença –Prêmio Indenizada; | 025 - Licenca Premio |
| Campo 85 | Quebra de Caixa; | 026 - Quebra de caixa |
| Campo 86 | Participação nos Lucros ou Resultados; | 027 - Participacao nos lucros/resultados |
| Campo 87 | Indenização a Título de Incentivo à Demissão; | 028 - Indenizacao recebida |
| Campo 88 | Bolsa Aprendizagem; | 029 - Bolsa Aprendizagem |
| Campo 89 | Abonos Desvinculados do Salário; | 030 - Abonos Desvinculados |
| Campo 90 | Ganhos Eventuais Desvinculados do Salário; | 031 - Ganhos eventuais |
| Campo 91 | Reembolso Creche; | 032 - Reembolso Creche |
| Campo 92 | Reembolso Babá; | 033 - Reembolso baba |
| Campo 93 | Gratificação Semestral; | 034 - Gratificacao Semestral |
| Campo 94 | Salário do Mês Anterior à Rescisão; | Rubricas criadas pelo usuário a partir do número 100 |
| Campo 95 \* - (caso exista mais de uma verba diversa, criar os subitens 95.1, 95.2, 95.3...); | Outras Verbas |  |
| Campo 96 | Indenização Art. 9º, Lei n.º 7.238/84; |  |
| Campo 97 | Indenização Férias Escolares; |  |
| Campo 98 | Multa do Art. 476–A, § 5º, da CLT; | 036 - Multa do Art. 476-a, § 5º, da CLT |
| Campo 99 | Ajuste do saldo devedor. | Rubrica criada pelo usuário a partir do número 100 |

|  |  |  |  |
| --- | --- | --- | --- |
| **Campos 100 a 116 – Informação de verbas de deduções** | | | |
| Campo 100 | Pensão Alimentícia; | Rubricas criadas pelo usuário a partir do número 100 | Rubricas relacionadas a eventos Desconto |
| Campo 101 | Adiantamento Salarial; |
| Campo 102 | Adiantamento de 13º Salário; |
| Campo 103 | Aviso –Prévio Indenizado; |
| Campo 104 | Indenização Art. 480 CLT; |
| Campo 105 | Empréstimo em Consignação; |
| Campo 106 | Vale –Transporte; |
| Campo 107 | Reembolso do Vale –Transporte; |
| Campo 108 | Vale –Alimentação; |
| Campo 109 | Reembolso do Vale –Alimentação; |
| Campo 110 | Contribuição para o FAPI; |
| Campo 111 | Contribuição Sindical Laboral; |
| Campo 112.1 | Previdência Social; |
| Campo 112.2 | Previdência Social13º Salário; |
| Campo 113 | Contribuição Previdência Complementar; |
| Campo 114.1 | IRRF; |
| Campo 114.2 | IRRF sobre 13º Salário; |
| Campo 114.3 | IRRF sobre Participação nos Lucros ou Resultados; |
| Campo 115{**}**\* - (caso exista desconto não especificado nos campos acima; havendo mais de um desconto, criar os subitens 115.1; 115.2...); | Outros Descontos |
| Campo 116 | Desconto de Valor Líquido de TRCT QuitadoDecisão Judicial. |

*Dica Blog:* Acesse o blog TOTVSConnect e veja [dicas para parametrizar a geração dos campos 65, 66 e 71](http://tdn.totvs.com/pages/viewpage.action?pageId=36309636).

**Atenção** (Campos da tabela com )

Quando houver que informar subitens para os campos 55, 56, 64, 66, 67, 95 e 115, o sistema irá criá-los automaticamente, respeitando a parametrização das rubricas relacionadas aos eventos, conforme exemplos abaixo:  
  
**Exemplo 1**  
  
Campo 56 – Hora Extra  
  
O Campo 56 possui relação com a Rubrica 004 – Hora Extra, definida pelo MTE.  
  
Os eventos de Horas Extras são pagos correspondendo às diferentes faixas:  
Hora Extra 50%  
Hora Extra 100%  
Hora Extra 150%  
  
Desta forma, no cadastro de cada um dos eventos acima, deverá estar informada a rubrica 004 – Hora Extra.  
  
Conforme este exemplo, no TRCT será gerado:  
  
Campo 56 – Hora Extra 50%  
e os subitens:  
  
Campo 56.1 – Hora Extra 100%  
Campo 56.2 – Hora Extra 150%  
  
  
**Exemplo 2**  
  
Campo 115 – Outros Descontos  
  
Para este campo, deverá criar uma rubrica a partir do número 100, pois não existe correlação com rubricas pré-definidas pelo MTE. Como exemplo, vamos supor que foi criada a rubrica:  
  
154 – Outros descontos.  
  
Os eventos de descontos listados abaixo foram lançados na rescisão do funcionário.  
  
Assistência Médica  
Cesta Básica  
  
No cadastro dos respectivos eventos, deverá ser relacionada a rubrica 154 – Outros Descontos.  
  
Conforme este exemplo, no TRCT será gerado:  
  
Campo 115 – Assistência Médica  
Campo 115.1 – Cesta Básica  
  
  
**Observação**  
Nas descrições dos campos do TRCT em que é exigido o preenchido da quantidade de horas dos eventos, o sistema irá persistir nestes campos as horas da seguinte forma:

1) Eventos do tipo HORA: A quantidade de horas constante no evento será persistida diretamente no TRCT, nos respectivos campos de rubricas;

2) Eventos do tipo Referência: A quantidade de horas será obtida através da conversão da referência decimal do evento para horas. O valor obtido será persistido nos respectivos campos de rubricas.

|  |  |
| --- | --- |
|  | Veja Também |

---

[Portarias, manuais, layout do TRCT e HomologNet](http://portal.mte.gov.br/ass_homolog/assistencia-e-homologacao-de-rescisao-de-contrato-de-trabalho.htm)
