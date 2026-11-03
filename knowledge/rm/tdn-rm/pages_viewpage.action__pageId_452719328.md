---
content_hash: 69ae7368aecbf0dc7c937381740757e87f00a7e26d0482ee580d7196add11d78
fetched_at: '2026-06-29T00:10:06.681359+00:00'
page_id: '452719328'
product: rm
source: tdn-rm
title: Configurações Gerais 3/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719328
version: 20
---

Nesta aba é possível fazer as Configurações Gerais relacionadas ao eSocial:   
   
   
**Gerar Gatilhos Iniciais por Evento**  
Este parâmetro permite gerar carga inicial por eventos.   
   
Confirmando este parâmetro o usuário poderá selecionar os eventos no processo Gerar Gatilhos Eventos Iniciais na etapa do faseamento eSocial "1ª Fase e 2ª Fase".  
   
Atenção:

* O usuário deverá selecionar o tipo de faseamento a ser gerado e somente poderá ser definido uma fase por vez.
* O usuário poderá definir a forma de geração conforme abaixo:
  + Parâmetro marcado: O usuário poderá definir os eventos a serem considerados na geração.
  + Parâmetro Desmarcado: O usuário não poderá definir os eventos a serem considerados na geração, será gerado para todos os eventos. Por Default as informações serão visualizadas desabilitadas.
* Quando o processo for realizado em uma coligada que não esteja com parâmetro marcado e na etapa "Gerar Gatilho Eventos Iniciais eSocial" for selecionada uma coligada que esteja parametrizada para gerar "Gatilhos iniciais por eventos" será demonstrada a seguinte mensagem para o usuário: "Não será gerada a Carga Inicial Por eventos para a Coligada 'XXX'. Carga Inicial será gerada para todos os eventos. Confirma geração?  Caso selecione "Não" o sistema irá desmarcar a coligada e a mesma não será considerada na geração do processo.

Exemplo 1: Processo realizado na coligada 1.  
Coligada 1 - "Parâmetro Marcado" e Coligada 8 – "Parâmetro Desmarcado":  
Na etapa "Gerar Gatilhos iniciais por eventos": Selecionado o evento S-1030.  
Na etapa "Gerar Gatilho Eventos Iniciais eSocial": Selecionadas as coligadas 1 e 8.  
   
Resultado do exemplo 1:  
   
Coligada 1 - Será gerado apenas evento S-1030.  
Coligada 8 - Serão gerados todos os eventos de tabela incluindo S-2200 e S-2300.  
Exemplo 2: Processo realizado na coligada 8.  
   
Coligada 8 - "Parâmetro Desmarcado" e Coligada 1- "Parâmetro Marcado":  
Na etapa "Gerar Gatilhos iniciais por eventos": Essa etapa não será visualizada.  
Na etapa "Gerar Gatilho Eventos Iniciais eSocial": Selecionadas as coligadas 1 e 8.  
   
Resultado do exemplo 2:  
   
Coligada 1 – Será gerado os eventos conforme definido pelo usuário.  
Coligada 8 – Serão gerados todos os eventos de tabela incluindo S-2200 e S-2300.

**Não gerar aviso para registro não obrigatório quando desconsiderado no XML**  
Esse parâmetro fará com que o sistema desconsidere os grupos/registros não obrigatórios, ou seja, essas informações serão ocultadas do log.  
Exemplo: Dentro do cadastro de funcionário os campos referentes ao documento CNH não estão preenchidos, sendo assim, ao gerar o XML do evento/validador da base de dados, com o parâmetro desmarcado, será apresentado no log de aviso uma mensagem como:   
"Registro 'CNH' não foi gerado porque os campos obrigatórios ('categoriaCnh', 'dtValid', 'nrRegCnh', 'ufCnh') não estão preenchidos."  
Caso esse parâmetro seja marcado, avisos como o citado acima serão desconsiderados no log.

**Gerar erro quando houver registro não obrigatório com informações incompletas**  
Quando este parâmetro estiver marcado o sistema irá gerar erro para registros não obrigatórios quando tiver algum campo preenchido.   
Quando desmarcado, para os registros não obrigatórios que não estiverem com todos os campos obrigatórios preenchidos o sistema gera aviso informado que o registro não foi considerado no XML.  
   
   
**Desconsidera o campo anotações do cadastro de evento para o evento S-1010**  
Quando este parâmetro estiver marcado o sistema irá desconsiderar na geração de XML S1010 a TAG observação.   
Quando desmarcado ao gerar o XML a tag observação será preenchida com as informações contidas na aba anotações.  
 

**Considerar jornada mensal do funcionário para cálculo da média de horas da Jornada semanal (Tipo da Jornada: 3 e 9)**

Ao marcar este parâmetro serão habilitadas as opções abaixo para preenchimento da TAG "qtdHrsSem" na geração do XML [S-2200](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719244).

* **Divisor da Jornada Mensal**: Permitirá definir um valor para o cálculo da jornada semanal a ser utilizada para todos os funcionários (Jornada Mensal / Divisor da Jornada Mensal).
* **Formula do Divisor da Jornada Mensal:**Permitirá informar uma fórmula, flexibilizando utilizar divisor diferente por funcionário no cálculo da jornada semanal.

    **Atenção:** O resultado da formula deve ser um valor que na divisão da jornada mensal, o retorno atenda as definições manual/leiaute do eSocial.

**Observação:**Caso o parâmetro esteja desmarcado, o sistema irá considerar a soma das horas das jornadas de trabalho do horário, dividido pelos dias do horário (todos os índices, inclusive dias de descanso), multiplicado por 7(Fixo).

   
**Considerar Cadastro da Jornada na geração dos eventos (S-2200 e S-2206)**  
Com este parâmetro marcado, ao gerar o XML S-2200 e S-2206 o grupo "horario" será criado com base no cadastro de jornada do horário, considerando a vinculação das colunas Índice -> Dia.  
Com o parâmetro desmarcado, ao gerar o XML o grupo será criado com base na vinculação do Índice -> Dia da semana da "Data de admissão", data mais próxima do inicio de obrigatoriedade dos eventos não periódicos ou "Data da mudança".  
Para mais detalhes, veja o link do [TDN](http://tdn.totvs.com/pages/viewpage.action?pageId=370618011) .

Além disso, para orientações específicas sobre o cálculo do adicional noturno, acesse  o  link   
   
**Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS**  
Com este parâmetro marcado ao cadastrar afastamentos do tipo( P ou O) inferiores a duração estipulada no MOS não serão gerados gatilhos do evento S-2230 na fila de eventos.

**Não gerar gatilho para o evento S-2250**  
 Com este parâmetro marcado o sistema não irá gerar os gatilhos referentes aos cadastros de avisos prévios trabalhados.

**Considerar maior valor de salário-hora na tag vrSalFx para professores/horistas**  
 Com este parâmetro marcado o sistema passa a considerar o maior salário hora cadastrado conforme data do histórico salarial para a geração da tag vrSalFx dos eventos S-2200 e S-2206.  

**Desconsiderar o indicador de comercialização igual a 3 no evento S-1260****pessoa jurídica não inscrita no PAA**  
Ao ativar este parâmetro, os movimentos serão excluídos da geração do S-1260 nos casos em que a venda é feita para uma pessoa jurídica adquirente não optante pelo Programa de Alimentação do Trabalhador (PAA). Essa medida foi adotada para cumprir as orientações descritas no Manual de Orientação do eSocial (MOS), no item 1.4, conforme descrito abaixo:

**1.4. Quando o produtor rural pessoa física contribuinte individual e o segurado especial comercializarem produção rural isenta com adquirente produtor rural pessoa física ou segurado especial, os que comercializarem devem enviar o evento S-1260 com ({tpComerc}=7). Nesse caso, a responsabilidade pelo recolhimento do Senar é do produtor rural ou segurado especial que comercializa. Todavia, quando a comercialização de produção rural isenta ocorrer com empresa adquirente ou com intermediário Pessoa Física, o produtor rural pessoa física contribuinte individual não é obrigado a enviar este evento e o segurado especial que comercializar, caso opte por enviar este evento, deve fazê-lo usando ({tpComerc}=3. Nesses casos, a responsabilidade pela retenção e pelo recolhimento da contribuição para o Senar é do adquirente, que cumprirá suas obrigações por meio do envio do evento R-2055 na EFD-Reinf. "**

|  |  |
| --- | --- |
|  | Informações Complementares |

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)

[Qual a função do parâmetro" Não gerar gatilho para afastamento inferior a 3 dias" ?](http://tdn.totvs.com/pages/viewpage.action?pageId=440841026)
