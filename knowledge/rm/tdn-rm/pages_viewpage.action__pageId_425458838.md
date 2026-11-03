---
content_hash: 3d06641bcde1a04966259117442dd1c550bcd9036c5a196bf015be8beb9e96e2
fetched_at: '2026-06-29T00:09:32.393359+00:00'
page_id: '425458838'
product: rm
source: tdn-rm
title: Integração Educacional - Abertura de Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458838
version: 2
---

**Integração Educacional - Abertura de Atendimentos**   
O Módulo de Cliente On Line é um recurso que permite o acompanhamento e o gerenciamento das requisições de forma rápida e prática. Todos os tipos de clientes: Cliente, Pessoa, Aluno, Professor e Prospect  ( referente as respectivas tabelas FCFO, PPESSOA, SALUNO, SPROFESSOR, HPROSPECT) podem acessar o módulo de cliente on line desde que possuam um usuário pré-cadastrado e a permissão liberada no perfil.  
   
A integração do TOTVS Aprovações e Atendimento x Educacional proporciona maior interação para a abertura de atendimentos. Para os usuários logados como Aluno (canto superior direito da página: Ambiente -> Entrar como (Aluno) ), a abertura das solicitações ocorrerá de forma diferenciada visando a otimização do processo e a completude das informações.   
   
Ao clicar em Novo (abrir novo atendimento), a página é redirecionada para as regras de validação do Educacional com informações relativas ao curso, período letivo, habilitação e RA, além disso apresenta o grupo de atendimentos e o tipo de atendimentos para escolha, eles podem variar de acordo com o assunto que a solicitação se refere.   
   
A partir desse momento, o sistema é redirecionado para a edição do atendimento no Módulo do Cliente On Line, onde os campos necessários devem ser preenchidos e o atendimento deve ser salvo. O avanço de etapa é realizado automaticamente e atendimento é inserido na primeira etapa do fluxo.   
   
Caso o tipo de atendimento escolhido pelo aluno possua um modelo associado e o parâmetro  "Substituir todos os valores  atuais  pelos do modelo do tipo de atendimento" esteja marcado (disponível em: Educacional / Atividades Acadêmicas / Configurações / Edição do Tipo de Atendimento), na edição do atendimento os campos correspondentes entre o atendimento (winforms) e o atendimento (web) serão substituídos automaticamente. A princípio a esta substituição está disponível somente para os campos do atendimento, não abrange os parâmetros vinculados ao tipo de atendimento.  
Através  da aba Dados Adicionais são listados informações do contexto educacional, por exemplo, matrícula, período letivo, RA entre outros, informações sobre o tipo de atendimento (Descrição, Detalhamento, Procedimentos e Aceite) e o Serviço que somente será apresentado caso esteja devidamente configurado no Educacional, do contrário uma mensagem de alerta será apresentada: "Serviço não disponível".  
Os parâmetros permitem associação de setença SQL para que seja montado um lookup com as informações da setença. Para manter compatibilidade com o educacional caso o usuário esteja logado como aluno e a sentença associada possuam como parâmetro os seguintes campos do educacional (IDPERLET, IDHABILITACAOFILIAL, RA), o sistema deverá buscar esses valores no contexto do educacional.  
Ex:  
SELECT RA,CODATENDIMENTO FROM SATENDIMENTO (NOLOCK)    
WHERE CODCOLIGADA = :CODCOLIGADA   
AND IDPERLET= :IDPERLET   
AND IDHABILITACAOFILIAL = :IDHABILITACAOFILIAL   
AND RA = :RA  
   
Neste caso a sentença possui como parâmetros os campos do Educacional, dessa forma o lookup será montando tendo como valores para esse campo, os valores que estão preenchidos no contexto do Educacional. Para os novos atendimentos, os valores virão do contexto do Educacional e no caso de atendimentos já existentes, esses valores virão da SATENDIMENTO , tendo como o filtro o atendimento corrente. Todo esse processo será transparente para o Aluno ficando a montagem da sentença a cargo dos administradores do sistema.  
Na visão de atendimentos do Módulo de Cliente On Line está disponível os filtros pré-definidos para facilitar a visualização dos registros:  
**Todos:**   Retorna todos os atendimentos do cliente logado.   
   
**Sob minha responsabilidade:** Retorna os registros que estão aguardando alguma ação do cliente. (Atenção.: a solicitação pode não estar em inserida no fluxo de atendimento ou retornou para análise/ações).  
   
**Aguardando retorno:**   Retorna os registros que não estão sob a responsabilidade do cliente. Os mesmos são apresentados somente leitura, com exceção do campo Discussão que sempre está disponível para inserções. Apenas o processo para incluir arquivos anexos estará disponível, os demais processos e ações estarão bloqueados até que o atendimento volte a responsabilidade do cliente.  
   
**Concluídos:**   Retorna todos os atendimentos que estiverem com a situação de concluído. Eles também não podem sofrer alterações e estarão sob modo somente leitura.  
   
**Cancelados:**   Retorna todos os atendimentos que estiverem com a situação de cancelado. Eles não podem sofrer alterações e estarão sob o somente leitura.  
   
O atendimento será analisado e encaminhado com a possível solução ou com questionamentos na aba de discussão para posterior continuidade. As informações registradas na discussão pelo atendente podem ou não ser visualizadas pelo aluno. No momento da inserção do texto na discussão (atendimentos winforms) somente as informações marcadas como publicáveis (Edição do Atendimento/ Aba Discussão / Flag "Publicável discussão no cliente online") serão disponibilizadas para o aluno acompanhar, mas qualquer informação da discussão adicionada direto pelo Módulo de Cliente On Line já é marcada por padrão como publicável.  
Para facilitar a explicação ou exemplificação do que foi solicitado, os arquivos anexos podem ser utilizados. A *priori* somente a inclusão estará disponível. Este recurso tende a aumentar a compreensão do problema que será detalhado no entendimento pelo atendente responsável pela solução do atendimento. O entendimento pode ser aprovado ou reprovado pelo cliente. Cada etapa que o atendimento percorrer será gravado no histórico de etapas, onde é possível visualizar informações sobre a etapa atual e as etapas anteriores pelo qual o atendimento já passou.  
Uma solicitação (atendimento) realizada incorretamente pode ser cancelada e posteriormente excluída do sistema. Esta situação pode ocorrer devido a um engano ou duplicidade de atendimentos. Vale ressalatar que somente administradores do sistema possuem tal permissão e somente atendimentos sobre a responsabilidade do cliente podem ser cancelados.  
**Observação.:**  
Para garantir a segurança do sistema, é possível bloquear os tipos de atendimentos, através do anexo "Bloquear Tipo de Atendimento" no perfil do usuário, para que seja visualizado apenas os tipos que realmente forem necessários para o dia-a-dia no trabalho, impedindo assim o uso incorreto das informações.  
Deve ser parametrizado nas configurações gerais do sistema, no módulo de Cliente On Line o atendente o responsável para pleno funcionamento da funcionalidade.
