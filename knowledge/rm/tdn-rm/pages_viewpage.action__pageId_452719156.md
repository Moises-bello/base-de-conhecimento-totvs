---
content_hash: d48dcbe9174cc2be5dd3587ca8defedf07ddf473b706cc2c7eb3d415e084f77b
fetched_at: '2026-06-29T00:10:03.790748+00:00'
page_id: '452719156'
product: rm
source: tdn-rm
title: Funções - RHU
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719156
version: 3
---

**Funções**

---

O cadastro de Funções tem como objetivo guardar as informações referente às funções existentes na empresa, permitido realizar diversos procedimentos no RM Vitae, como por exemplo Seleção, Requisições, dentre outros. Através deste cadastro é possível incluir, editar e excluir Funções.

**Atenção** Devido a particularidade de tratamento de Órgãos Federais, este cadastro também poderá ser visualizado com a nomenclatura "Cargo", caso o parâmetro "Utilizar notação de Órgão Federal" esteja setado para este fim.

**Pontos da Função (Controle de Benefício)** Será visualizado esse campo quando parametrizado no sistema para trabalhar com controle de pontuação por função. Nesse campo você poderá informar o total de pontos atribuídos a todos os funcionários que estão vinculados a essa função. Somente valores inteiros, igual ou maior que zero, serão permitidos para o lançamento dos pontos.

**Atenção** A Função inativa não será levada em consideração na somatória dos pontos do funcionário.

**Observações** - É possível visualizar o Radar de Competências por dentro do cadastro da Função. - O campo "Exibir no Organograma" tem como finalidade a exibição ou não da função no Organograma, através do menu Gerência de RH| Cargos e Salários| Organograma. Se uma dada função for desmarcada, as funções hierarquicamente inferiores também não estarão disponíveis no organograma. - O campo "Atividade de Transporte" somente deverá ser marcado quando a função em questão estiver relacionada a atividades de transporte. Este campo está relacionado à impressão da Guia de INSS com contribuição SEST/SENAT. - No campo "Pontos da Função (Controle de Benefícios)" poderá ser informado o total de pontos atribuídos a todos os funcionários que estão vinculados a essa função. Este campo somente será visualizado quando o sistema estiver parametrizado para trabalhar com controle de pontuação por função. Somente valores inteiros, igual ou maior que zero, serão permitidos para o lançamento dos pontos. Sendo que na função inativa não será levada em consideração na somatória dos pontos do funcionário. - Controle de Lotação Você poderá visualizar aqui a lotação atual da função, com relação a Vagas e Verbas definidas para a mesma. A disponibilização dos campos aqui apresentados para preenchimento estará ligada diretamente aos Parâmetros de Controle de Lotação. Quando os campos relacionados aos "LIMITES" apresentarem a mensagem "Sem Controle" é possível identificar que não existe um controle de lotação por aquele tipo (Vaga e/ou Verba) A primeira linha de campos aqui apresentados estará ligada as informações do controle de Vagas e a segunda ao controle de Verbas Para melhor entender os dados aqui listados, segue as informações abaixo:

**Controle de Lotação - Controle de Vagas**

Limite:  Permite definir/visualizar o número máximo de funcionários que poderão estar alocados na função. Este campo se encontrará desabilitado para preenchimento, quando existir outro tipo de controle de lotação definido nos parâmetros, que não seja por Função. Quando o Controle de Lotação for por Função, este campo será validado nas efetivações e transferências de funcionários.   Alocadas:  Permite visualizar o número de funcionários que se encontram atualmente alocados na Função em questão.   Disponíveis:  Permite visualizar o número de Vagas disponíveis, quando existir controle de lotação por Função. Este campo é calculado baseando-se no Limite Funcionários deduzido do número de Funcionários Alocados.   Excedentes:  Permite visualizar o número de funcionários excedentes alocados na Função em questão. Este campo é calculado baseando-se no número de Funcionários Alocados deduzido do número Limite permitido para Alocação de Funcionários.

Pendentes:   
  Permite visualizar o total de vagas pendentes na função, levando em consideração as requisições de Aumento de Quadro e de Substituição que estejam com os status: Pendente, Em Andamento, Aprovado e Suspenso.  
 Potencial:   
  Permite visualizar o total da soma dos campos Limite e Pendentes.

**Controle de Lotação - Controle de Verbas**

% Limite:  Permite definir/visualizar o percentual aplicado a Verba Geral definida nos parâmetros, para calcular o campo acima descrito com o valor "Limite Disponível" para efetivação e/ou transferências de funcionários alocados na Função. Este campo se encontrará desabilitado para preenchimento, quando existir outro tipo de controle de lotação definido nos parâmetros, que não seja por Função, ou quando o tipo de verba a ser controlado for definido como "Por Valor", validando assim o valor informado no campo "Limite de Verbas". Quando o Controle de Lotação for por Função, este campo será validado nas efetivações e transferências de funcionários. Limite:  Permite definir/visualizar o valor máximo da soma dos salários diretos que podem ser pagos mensalmente aos funcionários alocados na Função. Este campo se encontrará desabilitado para preenchimento, quando existir outro tipo de controle de lotação definido nos parâmetros, que não seja por Função, ou quando o tipo de verba a ser controlado for definido como "Por Percentual", validando assim o valor da Verba Geral. Quando o Controle de Lotação for por Função, este campo será validado nas efetivações e transferências de funcionários.   Alocada:  Permite visualizar a soma de todos os salários diretos pagos aos funcionários que se encontram atualmente alocados na Função em questão.   Disponível:  Permite visualizar o valor ainda disponível para contratação ou aumentos salariais dos funcionários alocados na Função , quando existir controle de lotação por Função. Este campo é calculado baseando-se no Limite de Verba deduzido do valor dos salários dos Funcionários já alocados. Quando o tipo de verba a ser controlado for definido como "Por Percentual", este campo será baseado no "% Limite" que será habilitado para preenchimento (desta forma o campo Limite Verba não estará disponível, sendo então um campo calculado), validando assim o valor do % aplicado a Verba Geral deduzido da soma de salários diretos pagos aos funcionários alocados nesta Função.   Excedente:  Permite visualizar o valor excedente pago aos funcionários alocados na Função em questão. Este campo é calculado baseando-se na soma dos salários diretos pagos aos Funcionários alocados, deduzido do número Limite de Verba permitido para efetivação e/ou transferências de Funcionários.  
    
 Pendentes:   
  Permite visualizar o total de verbas pendentes na função, levando em consideração as requisições de Aumento de Quadro e de Substituição que estejam com os status: Pendente, Em Andamento, Aprovado e Suspenso.  
 Potencial:   
  Permite visualizar o total da soma dos campos Limite e Pendentes.  
 % Potencial de Verbas:  
  Permite visualizar o % limite de verba + % do potencial de verba (este percentual é calculado dinamicamente sendo 100\*Verba Pendente / Verba geral).

Através do cadastro é possível controlar:

**Pasta Descrição - Função** Esta pasta destina-se ao cadastramento da descrição da Função em questão.

**Pasta Outras Informações - Função** Esta pasta destina-se ao cadastramento da "Descrição para o PPP" e "Objetivo da Função".

**Atenção** - O campo "Descrição para o PPP" aparecerá no relatório do PPP (campo 14) se a profissiografia for por função.

**Pasta Funções Subordinadas - Função** Esta pasta destina-se ao cadastramento da subordinação vinculada a Função em questão, tendo como objetivo possibilitar a montagem do Organograma e Plano de Carreira da empresa. - Chefia: função de chefia a qual a função em questão se encontra subordinada. - Próxima Função: próxima função a qual ocupantes da função em questão poderão a vir exercer na empresa.

**Pasta Mapa de Competência da Função** Esta pasta grava os mapas de competência associados para a função. Através deste cadastro é possível inserir ou excluir mapas de competências para uma função.

**Pasta Campos Complementares - Função** Caso existam campos complementares criados para a função, estes serão exibidos nesta pasta. Para verificar a existência dos campos complementares acesse: Cadastros | Campos complementares | Funções.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Características Pessoais Quadro de Lotação Históricos da Função Histórico de Tarefas na Função  
 Histórico de limite de vagas da Função  
 Histórico de limite de vagas - Quadro de Lotação Benefícios Vinculados a Função Histórico de Vinculação de Benefícios a Função Perfis de Exame  
 Histórico de Vinculação de Tabela Salarial a Função  
 Campos Complementares

|  |  |
| --- | --- |
|  | Como Fazer |

---

Administração de Tarefas Copiar Características da Função Assistente de Vinculação de Benefícios Copiar Função entre Coligadas
