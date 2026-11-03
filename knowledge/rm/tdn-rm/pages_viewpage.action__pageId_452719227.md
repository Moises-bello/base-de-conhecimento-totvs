---
content_hash: b7c359b7990fcf7e25bccfa3f2cb809d4b77f5e838cee05f2bf03502a1a3242a
fetched_at: '2026-06-29T00:10:04.621030+00:00'
page_id: '452719227'
product: rm
source: tdn-rm
title: Lançamento Global de Abonos e Abonos futuros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719227
version: 4
---

**Lançamento Global de Abonos e Abonos futuros**

---

No processo de apuração de ponto, a movimentação pode registrar atrasos e/ou faltas que poderão ser abonadas ou canceladas conforme justificativa do empregado.  
Utilize este menu para fazer lançamento de abonos coletivos de faltas e/ou atrasos para o período atual e/ou um período superior ao atual do sistema.  
   
**Observação:**  
Para que o processo seja executado com sucesso, algumas pré e pós-condições devem ser atendidas:

1
incomplete
Um período deve estar ativo.

2
incomplete
Deve ter sido realizado o lançamento de faltas e atrasos.

3
incomplete
Deve ser parametrizado se o abono será por número de horas ou intervalo  
Após a execução deste processo,

As faltas e/ou atrasos compensados ou não do referente período devem ter sido abonadas de acordo com a parametrização feita pelo usuário.  
**Para o grupo de funcionários**  
**Código de quebra:** Informe o Código de quebra da seção a qual pertencem os funcionários que terão os dados alterados.  
**Seleção de Funcionários:** Clique no botão "Seleção de Funcionários" para acessar a janela que irá selecioná-los por situação, tipo, código de recebimento ou Chapa.  
   
**Perfil:**  
Este campo permite guardar a configuração dos parâmetros habilitados do lançamento global de abonos. Ao acessar novamente este módulo, basta selecionar o perfil criado para o sistema trazer os parâmetros salvos.  
   
**Gravar parâmetros em um novo perfil**  
Podemos salvar os parâmetros do lançamento global de abonos. Este Combo Box possui um perfil que serve como base para o lançamento.  
Para gravar um novo perfil do lançamento, ou seja, para salvar os parâmetros do lançamento global de abonos, o usuário deverá:  
Primeiramente definir na tela os parâmetros que considerar necessário para o lançamento.  
Dar um clique no Combo Box e digitar um nome que lhe seja mais conveniente para o novo perfil.  
Apertar o ícone que se encontra ao lado do Combo Box.  
Depois de ter executado estes passos o usuário terá acabado de gravar um novo perfil.   
E assim deve ser feito para as demais variedades de perfis que quiser que fiquem armazenadas para não ter trabalho no futuro de marcar ou de desmarcar opções do lançamento e seleção.  
**Salvar perfil ao concluir** Este parâmetro é utilizado para incluir um novo perfil de parâmetros. Informe um nome de um novo perfil, marque o parâmetro "salvar perfil ao concluir" e ao clicar no botão "OK" para efetuar o lançamento o sistema gravará o novo perfil de parâmetros.  
**Excluir perfil selecionado**  
Este ícone deve ser utilizado para excluir um perfil do lançamento cadastrado.  
   
   
**Parâmetros do lançamento  
  
Considera atrasos calculados**O Lançamento global de abonos e abonos futuros foi unificado. Esse parâmetro determina se o lançamento é de abono ou abono futuro.  
Com este parâmetro marcado, o sistema salva as informações do abono comum, abonos que irão considerar os atrasos que foram calculados.  
Com este parâmetro desmarcado, o sistema salva as informações da tabela de abono futuro, abonos que irão considerar os atrasos que serão calculados futuramente.  
  
**Considera faltas calculadas**Possui o mesmo comportamento do parâmetro **Considera atrasos calculados**, porém considerando as faltas.  
   
**Considera ocorrências do usuário**  
Este parâmetro considera os tipos de ocorrência cadastrada pelo usuário que possuem o parâmetro abonável marcado. Essas ocorrências personalizadas estão disponíveis na guia Configurações| Tipos de ocorrência são associadas um evento com o CC 0043.  
   
**Tipo de Lançamento**  
Este parâmetro determina o comportamento do lançamento, se haverá acréscimo de abonos no intervalo determinado, se haverá substituição dos abonos pelo novo abono lançado ou se os abonos serão excluídos.  
   
**Considerar abono para o cálculo**  
Este parâmetro determina se o abono lançado será considerado no cálculo. Por padrão este parâmetro fica marcado. Com este parâmetro desmarcado o abono será lançado, porém não será calculado.  
   
**Abonar antes da compensação**  
Este parâmetro determina se o abono será feito antes ou após a compensação. Por padrão, este parâmetro vem desmarcado. Caso o usuário deseje abonar antes que a compensação seja feita, este parâmetro deve ser marcado.  
**Exemplo:**  
Para o funcionário que tem o horário do tipo flexível, no seu cadastro de horário o funcionário deveria ter as seguintes batidas:  
08:00E 12:00S 14:00E 18:00S  
Mas o funcionário executou as seguintes batidas:  
10:30E 12:00S 14:00E 19:00S  
Como o funcionário tem o horário do tipo flexível o sistema irá abonar antes de fazer a compensação, será lançado 02:30 de abono, pois neste dia o funcionário teve 02:30 de atraso e 01:00 hora extra, ao abonar sobrar apenas 01:00 de extra.  
**Observação:**  
Caso não marque o parâmetro "Abonar antes da compensação", ao fazer o lançamento de abono, o sistema irá lançar 01:30 de abono e não calculará para o funcionário 01:00 hora extra (pois esta hora extra foi compensada antes do lançamento do abono).  
   
**Abonar até o fim da jornada**  
Este parâmetro determina se o abono será lançado para toda a jornada ou será considerado o intervalo configurado pelo usuário. Por padrão este parâmetro fica desmarcado.

**Intervalo do Lançamento**  
Este parâmetro determina o intervalo do Lançamento. Caso o contexto do usuário tenha como propriedade considerar número de horas, o intervalo será definido junto com o número de horas a abonar para aquele intervalo. Caso seja por intervalo, o intervalo será definido junto com o intervalo de horas a abonar para aquele intervalo do período.  
**RM Portal:** ao utilizar o lançamento de abonos por intervalo é recomendado que o parâmetro de iniciais esteja marcado para que o sistema calcule corretamente os intervalos abonados.

**Atenção:**   
Para realizar o lançamento de abonos por intervalo de horas, marque o parâmetro "Considera abonos por intervalo" disponível na guia Configurações/ Parametrizador, processo Iniciais, etapa Cálculo. Com o parâmetro desmarcado, deverá ser informado o número de horas a abonar. Esse parâmetro não pode ser marcado caso realize o lançamento de abonos através da realização de um treinamento (Cadastro de turmas) ou do registro de um atestado (integração com TOTVS Gestão de Pessoas e TOTVS Segurança  
E Saúde Ocupacional). Essas integrações farão o lançamento do abono automaticamente. Para integrar um tipo de abono exclusivo ao TOTVS Folha de pagamento, ainda no parametrizador, processo Iniciais, determine qual abono será utilizado para atestados.  
Para o lançamento de abonos por intervalo no **RM Portal** é necessário queo parâmetro esteja marcado para que o sistema calcule corretamente os intervalos abonados.

**Núm. Horas**  
Esse parâmetro é habilitado somente se o abono for por número de horas  
Lançar por dia: A quantidade de horas parametrizada é replicada para cada dia do período de lançamento.  
Exemplo: 01/10 a 10/10 – 08:00   
Nesse irá lançar 08:00 para todos os dias entre 01/10 e 10/10  
Lançar por período  
Exemplo: 01/10 a 10/10 – 08:00   
Nesse caso irá lançar as 08:00 considerando todo o período, se tiver 04:00 de atraso nos dias 01/10 e 02/10, será lançado somente para esses dois dias, os demais permanecerão como faltas e/ou atrasos.         
   
**Início/Fim:**  
Informe as datas de início e fim do período que será considerado no lançamento.  
**Atenção:**  
Utilize este botão para acionar o calendário e selecionar o período de lançamento.  
**Horas**  
Informe qual o número de horas diário será considerado no lançamento de abonos. Este número será comparado com a quantidade de horas de atraso e/ou faltas de cada dia. O sistema irá lançar o abono para todo o período de atrasos/faltas no dia até se atingir o número de horas informado.   
**Hora de Início**  
Informe a hora de início do intervalo de horas de abono que será lançado.  
**Hora de Término**  
Informe a hora de término do intervalo de horas de abono que será lançado.  
   
**Responsável**  
Informe neste campo a pessoa que será responsável pelo lançamento do abono para o funcionário.  
   
**Abono único**  
Este parâmetro determina o abono a ser lançado.  
Clique na barra de rolagem e selecione o tipo de abono que será lançado para o(s) funcionário(s).
