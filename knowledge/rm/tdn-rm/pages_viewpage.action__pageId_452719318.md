---
content_hash: 3a180b2ae98bc80e86cbf6644fa8f136fb114e2d1687dca345a66bce64096e4b
fetched_at: '2026-06-29T00:10:06.586049+00:00'
page_id: '452719318'
product: rm
source: tdn-rm
title: Rescisão Coletiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719318
version: 7
---

A Rescisão Coletiva é o cadastro e cálculo da rescisão de um ou mais funcionários por motivo único.

É aconselhável utilizar quando o processo de rescisão é para mais de uma chapa com a mesma parametrização.   
É apresentada a opção de utilizar filtro para seleção de funcionários que entrarão no processo de demissão.  
   
No LOG serão informados todos os funcionários que foram demitidos e os funcionários que não foram e o motivo da não demissão, por exemplo, funcionário que atende a fórmula de estabilidade no sindicato.  
   
No processo de rescisão individual existe a possibilidade do cadastramento anterior ao cálculo da rescisão.   
No processo de rescisão coletiva são feitos o cadastramento e o cálculo no mesmo momento, com exceção de quando houver restrições.  
   
Antes de executar o processo de rescisão coletiva deverá verificar se existem integrações com outros módulos.  
   
Exemplo: Se no módulo Educacional já foi efetuado o lançamento das horas aulas, ou se no módulo de Automação de Ponto já foi feito o lançamento do ponto. Caso haja uso da licença para estes módulos.  
   
Possíveis integrações:

* Gestão de Pessoas
  + Utiliza estabilidade para membro da CIPA.
  + Utiliza benefícios.
  + Tem requisição de desligamento.
  + Habilitar LOG de empréstimo EPI.

* Educacional
  + Utiliza lançamento das horas aulas.

* Automação de Ponto
  + Utiliza lançamento da movimentação do ponto.

No processo de rescisão coletiva, existindo algum funcionário vinculado à requisição de desligamento, este não será demitido e serão registrados no log da rescisão os funcionários que se encontram nesta situação. O mesmo ocorrerá com funcionários que possuem estabilidade devido à participação na CIPA e para funcionários que possuem EPI´s vinculados.

Quando o parâmetro 'Considerar o cadastro de estabilidades do funcionário' estiver marcado será verificado o cadastro de estabilidade do funcionário e retornará mensagem de aviso. A Rescisão será realizada.

**Observação**

Para as estabilidades de CIPA ou representantes dos empregados abaixo, somente irá retornar mensagem se a rescisão for do tipo 2 e M.

* + 7 - Candidato CIPA
  + 8 - Eleito Titular CIPA
  + 9 - Eleito Suplente CIPA
  + 14 - Candidato Representante dos Funcionários
  + 15 - Eleito Titular Representante dos Funcionários
  + 16 - Eleito Suplente Representante dos Funcionários

A página "Parâmetros da Rescisão Coletiva Informados" agora resume os dados das páginas "Dados do Aviso Prévio", "Dados da Rescisão", "Parâmetros de Cálculo da Rescisão" e "Parâmetros/Dados da Transferência" separando cada página para uma aba. No Tipo de Rescisão 6, aparecerão as quatro abas  "Dados do Aviso Prévio", "Dados da Rescisão", "Parâmetros de Cálculo da Rescisão" e "Parâmetros/Dados da Transferência", pois apesar de ser transferência, contém alguns ônus que deverão ser informados na página de "Parâmetros de Cálculo da Rescisão". No Tipo de Rescisão 5, aparecerão as abas  "Dados do Aviso Prévio", "Dados da Rescisão" e "Parâmetros/Dados da Transferência". E nos demais Tipos de Rescisão, aparecerão as abas  "Dados do Aviso Prévio", "Dados da Rescisão" e "Parâmetros de Cálculo da Rescisão"  
   
**Dados de Aviso Prévio**  
Os tipos de rescisão 2 ,4, e V (Comum Acordo), onde o aviso prévio não é indenizado/descontado, será considerado na execução do processo apenas os funcionários que possuem aviso prévio cadastrado. Caso a data não seja informada, deverá retornar a informação "Filtro não utilizado" no campo "Filtro Período Aviso Prévio Trabalhado" na aba "Dados de Aviso Prévio", da página "Parâmetros da Rescisão Coletiva Informados". Caso seja marcada a opção "Tem aviso prévio indenizado", será desabilitado o campo "Filtro Período Aviso Prévio Trabalhado", voltando a ser editável na página  "Dados de Aviso Prévio" e visível a informação "Filtro não utilizado" no campo "Filtro Período Aviso Prévio Trabalhado" na aba "Dados de Aviso Prévio", da página "Parâmetros da Rescisão Coletiva Informados" apenas quando marcada a opção "Tem Aviso Misto" estiver marcada. Para auxiliar na seleção dos funcionários, através do agrupador "Filtro Período Aviso Prévio Trabalhado" poderá ser informado um intervalo de datas, onde apenas os funcionários que possuírem aviso cadastrado dentro do intervalo pré-determinado serão considerados.  
   
Para rescisões de Comum Acordo, no campo Dias de Aviso Prévio Indenizado deve ser informada a metade da quantidade de dias total a ser indenizado. Quando a metade destes dias resultar em decimal, por exemplo 33 dias de aviso prévio indenizado deveria ser 16.5 dias de aviso prévio indenizado, o valor a ser informado no campo será o valor arredondado, no caso do exemplo 17 dias de aviso prévio indenizado. No momento do cálculo, ou seja, quando clicar em "Calcular Rescisão", deverá ser marcado ou não um parâmetro "Aviso Prévio Indenizado abate 0.5 dia" de acordo com o entendimento do usuário e essa informação de Sim ou Não só deve ser exibida no Tipo de Rescisão V.  
**Atenção:** Este parâmetro influenciará apenas no cálculo do aviso prévio indenizado e no cálculo das médias de aviso prévio indenizado. Para o cálculo da projeção em férias indenizadas e 13º salário indenizado será considerado o valor inteiro informado no campo "Dias de Aviso Indenizado" na pasta Aviso Prévio do cadastro de Rescisão.

Quando os Tipos de Rescisão forem 2, 3, 4, C, V e N, o campo "Tipo de Redução do Aviso e Forma de Redução" poderá ser marcado e informada a opção. Quando não informado nenhuma opção, deve retornar no label: 'Opção não informada'.

Quando as Datas de Aviso Prévio e suas variações (datas de aviso prévio trabalhado ou indenizado) não forem informadas, serão mantidos os labels sem nenhuma informação, independente do motivo.

Caso queira que o processo considere automaticamente a data de desligamento cadastrada dentro do aviso prévio, deverá ser marcado o parâmetro "Considerar data de demissão prevista informada no aviso prévio".  
**Observação:**   
Caso seja marcado o parâmetro citado acima, os campos abaixo serão desabilitados:  
·         Data de Demissão/Cálculo  
·         Data de Desligamento  
·         Período  
·         Data Último Movimento  
   
**Atenção:**  
Para atender ao leiaute do eSocial evento S-2299 -Desligamento, foi criado o campo Indicador de cumprimento Parcial de Aviso Prévio.  

**Dados da Rescisão**  
Na aba Dados da Rescisão, na parte de Seleção de Funcionários, se no campo Chapa não forem informadas as chapas a serem consideradas, retornará a mensagem "Será considerada todas as chapas". No campo Filtro, deverá retornar o código do filtro, mas caso não seja informado, deverá retornar a mensagem "Nenhum". No campo Fórmula, deverá retornar o código do fórmula, mas caso não seja informado, também deverá retornar a mensagem "Nenhum".

As datas informadas na página de "Dados da Rescisão" devem apresentar o formato DD/MM/AAAA e quando não forem solicitadas (quando se marca a opção "Considera data de demissão aviso prévio trabalhado"), devem manter os labels sem nenhuma informação na aba "Dados da Rescisão" da página "Parâmetros da Rescisão Coletiva Informados".

O campo Situação geralmente retorna informações quando selecionada uma chapa. Quando não retornar a situação, deverá apresentar a mensagem "Conforme a seleção de Funcionários"

**Parâmetros de **Cálculo Rescisão (esta aba não deve ser exibida se o tipo de rescisão for 5)****Na aba Parâmetros de Cálculo Rescisão, haverá comportamento distinto em três campos:  
· Lança salário composto: se a resposta for Sim, os labels "Lança eventos que tomam por base" e "Lança eventos relacionados" serão exibidos. No entanto, se a resposta for não, estes mesmos labels não serão exibidos;  
· Lança eventos de integração: se a resposta for Sim, o label "Comportamento" será exibido. No entanto, se a resposta for não, este label não será exibido;  
· Lança eventos da produção agrária: o campo na página de "Parâmetros de Cálculo Rescisão" só será exibido se a base estiver configurada para utilizar a Folha Agrária. Caso positivo, se a resposta ao campo "Lança eventos da produção agrária" for Sim, o label "Comportamento" será exibido. No entanto, se a resposta for não, este label não será exibido.

**Parâmetros de **Transferência****Existe a possibilidade de transferir os funcionários para a mesma coligada ou para coligada distinta de forma coletiva.  
   
Ao informar o tipo de demissão **5-Transferência sem ônus p/ Cedente** ou **6-Transferência com ônus p/ Cedente** será obrigatório o preenchimento dos campos que seguirão no wizard. Em especial, haverão três campos na aba de "Parâmetros/Dados de Transferência" cujo comportamento merece atenção:  
· No campo "Transfere Movimentação atual do mês atual", se a resposta for Sim, deve exibir o label "Desconsidera período da ficha financeira quando a data de pagamento for igual a demissão". Em caso de resposta negativa, não deve exibir o label;  
· No campo "Realiza transferência mesma coligada", se a resposta for Não, deve exibir os labels "Nova Coligada" e "Transfere históricos". Em caso de resposta Sim, não deve exibir os labels;  
· No campo "Realiza transferência para outra base", se a resposta for Sim, deve exibir apenas a informação de "Motivo de Transferência".  As demais informações desta aba devem ser ocultadas.

Observações  
·         Quando chegar à tela "Parâmetros da Rescisão Coletiva Informados", é possível retornar às telas anteriores, alterar as informações e as informações alteradas serão atualizadas e apresentadas na tela "Parâmetros da Rescisão Coletiva Informados", em suas respectivas abas;

·         Ainda na tela "Parâmetros da Rescisão Coletiva Informados" é possível cancelar o processo sem alterar as características e status dos funcionários e sem executar a finalização do processo de Rescisão Coletiva;

·         Quando a Transferência é do tipo 5 (Transferência sem ônus p/ Cedente) e mesma coligada ou o usuário desmarca o parâmetro 'Realiza Transferência para mesma coligada' e informa a nova coligada com o CNPJ com a mesma raiz da coligada de origem, o processo desabilita as opções de Motivo da Transferência para o usuário selecionar e por default deixa o Motivo da Transferência 'Estabelecimentos da própria empresa' selecionado. Com este motivo de Transferência, o processo não irá gerar para a Chapa ativa do Funcionário uma nova Matrícula eSocial.  
   
·         Quando a Transferência é do tipo 5 (Transferência sem ônus p/ Cedente) e o usuário desmarca o parâmetro 'Realiza Transferência para mesma coligada' e informa a nova coligada com o CNPJ com raiz diferente da coligada de origem, o processo habilita as opções de Motivo da Transferência para o usuário selecionar, podendo ser 'Sucessão, incorporação, cisão ou fusão' ou 'Empresa do mesmo Grupo Econômico'. O Motivo da Transferência 'Estabelecimentos da própria empresa' fica desabilitado para ser selecionado. Com estes motivos de Transferência, o processo irá gerar para a Chapa ativa do Funcionário uma nova Matrícula eSocial, conforme a Máscara para Matrícula do Trabalhador configurada em Configurações | Parâmetros | Parametrizador | 06.07- eSocial | Configurações Gerais.  
   
·         Quando a Transferência é do tipo 6 (Transferência com ônus p/ Cedente) as opções de Motivo da Transferência ficam desabilitadas para o usuário selecionar. Com este tipo de transferência o processo irá gerar para a Chapa ativa do Funcionário uma nova Matrícula eSocial, conforme a Máscara para Matrícula do Trabalhador configurada em Configurações | Parâmetros | Parametrizador | 06.07- eSocial | Configurações Gerais.  
   
**Atenção:**  
Somente será permitido o cadastramento de transferência retroativa se o parâmetro "**Permite realizar rescisão por transferência com data retroativa à competência atual"** estiver marcado no parametrizador.  
   
 A transferência coletiva dentro da mesma coligada só poderá ser realizada se no parametrizador do módulo Folha de Pagamento os parâmetros "Cadastro automático de chapas sequenciais (Exclusivamente numéricas)" e "Número de Ficha de Registro gerado pelo sistema" estiverem habilitados.  
   
A Transferência Coletiva foi idealizada para copiar exatamente todos os dados do funcionário de uma coligada para outra. As únicas mudanças são os motivos e o tipo de admissão no novo registro do funcionário transferido. Até mesmo a chapa é copiada no ato da transferência coletiva entre coligadas. É necessário verificar se os dados a serem preenchidos nos campos Seção, Função, Sindicato, Banco de Pagamento, Agência, Horário e Banco FGTS já foram previamente cadastrados na coligada de destino.  
   
A informação da Nova Coligada será para onde serão transferidos os funcionários e serão apresentadas todas as coligadas que estão como o mesmo mês e ano de competência da coligada de origem.  
   
Na seleção da Nova Seção de destino dos funcionários transferidos serão apresentadas todas as seções da coligada informada no campo anterior.

**Observações:**

1. Os funcionários demitidos para o próximo mês ficarão na situação A – Ativo até a liberação de competência com o envelope de pagamento bloqueado pelo motivo de rescisão calculada para o próximo mês;
2. Para realizar transferência apenas para um funcionário deverá ser feito via rescisão individual. Mesmo selecionando apenas um funcionário via rescisão coletiva serão seguidos os mesmos parâmetros mencionados anteriormente:
3. Caso haja histórico salarial futuro no momento da transferência do funcionário veja informações na aba Transferência de Funcionários do TDN [Histórico Salarial Futuro](https://tdn.totvs.com/pages/viewpage.action?pageId=687158765) .
4. Ao realizar a transferência de um funcionário com férias marcadas e data de pagamento anterior a data de demissão, será apresentado a mensagem "**Existem férias calculada e não finalizada para o período {0} a {1}. A rescisão não foi processada para a chapa {xxxx}**", quando:

I. Há férias marcadas com o início de gozo das férias posterior a data de demissão;

II. O pagamento das férias é até a data de demissão;

III. O parâmetro Configurações / Folha de pagamento / Rescisão / Transferência /  "**Permite transferência tipo 5 de funcionário afastados ou de férias**" está desmarcado.

 **Dados da Admissão**

* O Tipo de admissão será preenchido com o tipo T quando o tipo de demissão for 5 e será preenchido com o tipo E quando o tipo de demissão for 6.
* O novo motivo da admissão poderá ser informado conforme opções apresentadas, ou ser criado um novo motivo no Cadastro de Tabelas Dinâmicas, selecionando o código INT22.
* O novo motivo da mudança de seção poderá ser informado conforme opções apresentadas, ou ser criado um novo motivo no Cadastro de Tabelas Dinâmicas selecionando o código INT24.
* O novo motivo da mudança de função poderá ser informado conforme opções apresentadas, ou ser criado um novo motivo no Cadastro de Tabelas Dinâmicas selecionando o código INT25.
* O novo motivo da mudança de salário poderá ser informado conforme opções apresentadas, ou ser criado um novo motivo no Cadastro de Tabelas Dinâmicas selecionando o código INT26.
* O funcionário transferido com data do próximo mês competência ficará na situação Z - Admissão prox.mês até a liberação de competência.

**Gerar Gatilho para eSocial**  
·         A transferência tipo "5-Transferência sem ônus p/ Cedente" tem o seguinte comportamento:  
   
Entre coligadas: Gera um gatilho S-2299 na coligada origem e um gatilho S-2200 na coligada destino;  
   
Na mesma coligada: Gera um gatilho S-2206 na própria coligada.  
   
Motivo de Desligamento: Caso o tipo de demissão seja "5 - Transferência sem ônus p/ Cedente" retorna "11 - Transferência de empregado para outra empresa do mesmo grupo empresarial que tenha assumido os encargos trabalhistas, sem que tenha havido rescisão de contrato de trabalho";  
   
Outros casos deverá informar no parametrizador do eSocial De/Para de desligamento, Caso não exista nada no De/Para retornará vazio.  
   
**Gerar Log Consolidado**  
Existe a possibilidade de gerar um log consolidado com as informações de todos os funcionários processados. Para isto, basta marcar o parâmetro 'Gerar Log Consolidado'. Será habilitado o campo 'Salvar o(s) arquivo(s) na pasta' onde deve ser informado o caminho da pasta onde o log será salvo.   
**Observação**  
Caso o usuário queira que o arquivo gerado seja aberto no final do processo, basta marcar o parâmetro 'Abrir o arquivo ao final da execução'.
