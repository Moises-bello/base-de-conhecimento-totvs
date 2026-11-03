---
content_hash: 196b760d84ed8992fff03198fed779f432cc6b511d6091280905ed4fa9b4d59b
fetched_at: '2026-06-29T00:11:55.967140+00:00'
page_id: '864989807'
product: rm
source: tdn-rm
title: Parâmetros Equipamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864989807
version: 3
---

* O parâmetro “Integrado com SIGA-MNT” define se a integração está ativa no sistema;
* O parâmetro “Valida Filial do equipamento” é utilizado para validar se o equipamento está relacionado à filial do projeto no cadastro de bens, durante a vinculação dos equipamentos aos insumos do projeto;
* O parâmetro “Enviar e-mail de log de erros” define se haverá o envio de e-mail com um texto padrão para o usuário ou um grupo de usuários do sistema (este grupo deve ser criado pelo próprio cliente, conforme modelo de envio de e-mail para um grupo assim como é feito no Outlook), e que receberá informações do log de erros das importações/exportações realizadas pelos coletores móveis, através dos webservices disponibilizados no projeto Mobilidade. O endereço para envio do e-mail de log de erros poderá ser parametrizado por projeto ou um endereço geral;
* O log de erros de sincronização de cadastros será enviado para o endereço parametrizado nos parâmetros gerais. O log de erro dos processos (Avanço Físico, Mão de obra, Equipamentos e Ciclo de Transporte) será enviado para o e-mail parametrizado para o projeto. Caso não esteja parametrizado nenhum endereço para o projeto, será enviado para o e-mail informado nos parâmetros gerais;
* O parâmetro “Configuração de WebService para Calendário e Turnos do Manutenção de Ativos” é utilizado para o recebimento de calendários do Manutenção de Ativos. Maiores detalhes em [ER\_PCREQ-9418\_Integracao\_de\_Calendarios\_e\_Turnos\_com\_NG\_para\_o\_Mobilidade](https://tdn.totvs.com/display/LRM/ER_PCREQ-9418_Integracao_de_Calendarios_e_Turnos_com_NG_para_o_Mobilidade).

* O parâmetro “Tarefa para rateio de horas improdutivas” é utilizado nos processos de rateio e revaloração de apontamentos de equipamentos e mão de obra. Caso esteja informado, as horas improdutivas apontadas serão apropriadas de acordo com a tarefa e motivo de improdutividade informados.

* O parâmetro “Custos Indiretos – Equipamentos” define a composição de custos indiretos de equipamentos;

* O parâmetro “Tratamento para sincronismo de equipamentos associados” define como será o envio de equipamentos para o coletor, somente os associados ao usuário, este como operador, ou todos os equipamentos de todos os projetos associados ao coletor.

**Sincronismo de Bens – SIGAMNT**

* O parâmetro “Integrado com o SIGA-MNT” deve estar HABILITADO;

* + A manutenção de ativos, controlada pelo PROTHEUS, requer que seja sincronizado o cadastro de bens para o RM;
  + A comunicação/integração é realizada utilizando o EAI do RM (TOTVSMessage) através de troca de mensagens no padrão de mensagem única. O EAI do RM disponibiliza WebService e métodos para envio, recebimento, processamento das mensagens inclusive pontos de customizações;
  + Este cadastro no RM, uma vez integrado, significa que a origem de seus registros serão os registros do PROTHEUS então os mesmos não poderão ser manipulados no RM. É necessário rever as permissões de acesso, pois os cadastros que são feitos no BackOffice PROTHEUS devem ficar desabilitados no BackOffice RM;
  + A máscara utilizada para o código do patrimônio no cadastro de patrimônio deve ser com dois níveis. Sendo um para identificar a família do PROTHEUS que corresponde a um Título no patrimônio do RM, e outro nível para identificar o item dentro da família/título. Exemplo: ###. ####;
  + São tratados nesta integração além da manutenção do cadastro do bem, a transferência de filial e de centro de custos. Não é permitido a exclusão de um bem, quando houver esta necessidade, deverá ser inativado;
  + Para o campo “Capacidade de produção” e “Unidade da Capacidade da Produção” foi criada uma tabela de especialização da tabela de patrimônio no TOP. Esta tabela terá a manutenção exclusiva pelo processo de integração.

    - Código: 1005;
    - Descrição: TOTVS Construção Obras e Projetos x Manutenção de Ativos;
    - Mensagem/Versão: EQUIPMENT / 1.002.
