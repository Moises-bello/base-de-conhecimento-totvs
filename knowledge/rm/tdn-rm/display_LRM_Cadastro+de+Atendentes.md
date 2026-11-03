---
content_hash: f5573bf13ffcd7c45ed40a0d41afdf4db7be934639d322689a2bd6291860c289
fetched_at: '2026-06-29T00:09:37.237252+00:00'
page_id: '425459579'
product: rm
source: tdn-rm
title: Cadastro de Atendentes
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Atendentes
version: 5
---

**Atendentes**

---

Nesta opção cadastram-se os atendentes que poderão ser envolvido na resolução de uma determinada ocorrência.   
   
**Atenção**

Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros | Segurança | Perfis | Pasta Acesso a Menus.  
Através do cadastro é possível controlar:

**Identificação**  
 Nesta Janela deverá ser efetuado o cadastramento de cada atendente que poderá ser envolvido na resolução de uma determinada ocorrência. São disponibilizados os seguintes campos para preenchimento:

Código do Atendente   
Este campo será preenchido automaticamente, quando o cadastro do atendente for incluído.

Ativo  
Deverá ser definido se o atendente permanecerá ativo ou não, se está opção estiver desmarcada este atendente não está disponível para resolução de ocorrências ou em outros processos que dependem deste cadastro de atendentes.

É funcionário  
Deverá ser marcada esta opção caso o atendente seja um funcionário já cadastrado na base de dados.

Pessoa   
Selecione a pessoa que será atendente no TOTVS Aprovações e Atendimento. A pessoa deve ser previamente cadastrada no aplicativo RM Vitae.

**Observação**

Caso não tenha nenhuma pessoa cadastrada, será possível efetuar o cadastro clicando-se no ícone ao lado desse campo, abrindo a janela de edição de Pessoas do RM Vitae.

Usuário   
Um usuário existente no menu Cadastros | Segurança | Usuários tem que ser vinculado ao atendente, isso é feito para que o atendente possa efetuar o login no aplicativo.

Hierarquia   
Informe a Hierarquia a qual pertence o atendente, ou seja, a quem ele é subordinado. O Chefe hierárquico do atendente receberá informações sobre os alarmes de seus subordinados e poderá fazer alterações nos atendimentos dos mesmos.  
A hierarquia é cadastrada através do menu Cadastros | Hierarquia.

Localidade   
Este campo será preenchido de acordo com a região em que se encontra o atendente.

Tipo de atendente  
Deverá ser definido o tipo de atendente ao qual o atendente deve ser vinculado.

Grupo de alarme  
Deverá ser definido o grupo de alarme ao qual o atendente deve ser vinculado.

Número mínimo de avaliações  
Este campo será preenchido para que um determinado atendente chefe possa ter um número mínimo de avaliações nos atendimentos mais discutidos.

Nível de Acesso   
Defina neste campo, o nível de acesso que o atendente selecionado deverá possuir para a visualização das ocorrências. O atendente só visualizará os atendimentos com nível de acesso menor ou igual ao seu, ou atendimentos com nível de acesso superior, desde que este atendimento esteja sob a responsabilidade do atendente.

Exemplo  
Caso o atendente possua um nível 10 e uma ocorrência possua o nível 15, o atendente não visualizará a ocorrência em nenhum local até mesmo na Pesquisa de Atendimentos. O atendente só conseguirá visualizar a ocorrência quando o mesmo estiver com a ocorrência sob a sua responsabilidade.   
Nem mesmo os atendentes que são chefes ou o responsável pelo contato com o cliente conseguem visualizar a ocorrência se a mesma possuir um nível de acesso maior que a do atendente definida no cadastro de atendentes.

Assinatura do atendente  
Assinatura do atendente, contendo nome completo, cargo, nome da empresa, telefone/ramal e endereço eletrônico.

Indica em quais módulos aparece  
Selecione para quais módulos do TOTVS Aprovações e Atendimento (Atendimento, Vendas e Marketing) o atendente poderá ser utilizado.

Gerar apontamento automático para este atendente  
Selecionando esta opção, o sistema gera apontamento automático no momento de edição dos atendimentos. O sistema busca como hora de início e término o momento de início de edição e de fim de edição do atendimento em questão e grava esse apontamento. Nos parâmetros gerais do TOTVS Aprovações e Atendimento deve ser informada a atividade referente ao apontamento automático, esta marcação garante que o apontamento só será salvo se o mesmo for gerado de maneira correta do início ao término da edição do atendimento.

Gerar estatística para este atendente  
Selecionado esta opção ao executar o serviço "Carregar estatística para suporte" será verificados os atendentes que possuem esta opção selecionada para geração desta estatística.

Autoriza repasse para qualquer atendente  
Selecionando esta opção o atendente terá permissão para repasse de atendimentos para todos os atendentes e grupos de atendentes cadastrados.

Filtrar pela mesma hierarquia/seção do atendente  
Selecionando esta opção serão exibidos no campo 'Atendente substituto' apenas os atendentes que se encontram na mesma hierarquia/seção do atendente em questão.

Atendente Substituto   
Permite a definição do atendente substituto no atendimento, caso o atendente em questão esteja inativo no momento do repasse dos atendimentos.

Ramal  
Preencher o número do ramal telefônico do atendente.

Ramal de siga-me   
Este campo deverá ser preenchido caso seja determinado o serviço 'Sigame' de uma determinada operadora telefônica, onde o atendente direciona seu ramal de atendimento para outro específico.

Nome do computador  
Preencher com o nome do usuário da máquina ou estação de trabalho do atendente.

Celular  
Este campo deverá ser preenchido para que seja possível a aprovação do atendimento via whatsapp, através da integração com a WorkNow. Esta funcionalidade está disponível a partir do Release 12.1.2506.

**Observação**  
O TOTVS Aprovações e Atendimento permite informar um atendente substituto mesmo que ele não esteja ativo no sistema.

---

**Informações Complementares**

Especialidade  Autorização de repasse 

Vincular Usuário ao Atendente

**Como Fazer**

Adicionar Autorização de repasse

Retirar autorização de repasse para o atendente

Copiar autorização de repasse
