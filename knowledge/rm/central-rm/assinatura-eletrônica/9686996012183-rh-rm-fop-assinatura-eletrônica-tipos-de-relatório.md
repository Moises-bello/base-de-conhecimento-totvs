---
article_id: 9686996012183
category: Assinatura Eletrônica
content_hash: 7f764a518ca4a71a88e31e9db4190888518fc8bbb259dfd22996f9bd8d191f38
fetched_at: '2026-06-28T22:46:44.081088+00:00'
product: rm
section_id: 4403549405207
source: central-rm
title: 'RH - RM - FOP - Assinatura Eletrônica: Tipos de relatório'
type: support-article
updated_at: '2025-02-03T16:09:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9686996012183-RH-RM-FOP-Assinatura-Eletr%C3%B4nica-Tipos-de-relat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29713091547927) Tempo aproximado para leitura: **00:08:34 min****Dúvida**Como configurar os relatórios utilizados na integração com o TOTVS Assinatura Eletrônica?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Na aba **Identificação** será definido se o relatório precisará ser aprovado, assinado pelo remetente, se o documento terá algum tipo de prazo, se utilizará a estrutura de chefes/supervisores, se validará a data do aviso de férias e define como será o nome do documento integrado.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9687169076375)

**Criação de documento para assinatura:**

**Remetente assina**

Marque essa opção caso deseje que o usuário responsável pela execução do processo (usuário do sistema) seja um dos assinantes do documento. Com isso ele passará a figurar na lista de destinatários do documento para assinatura. Será considerado para isso o e-mail do usuário do cadastro de Usuários (GUSUARIO).

**Criar usuário no TOTVS Assinatura eletrônica caso não exista (usuário do destinatário)**

Ao marcar essa opção, durante o processo de integração do documento será verificado se o destinatário existe no sistema TOTVS Assinatura Eletrônica. Caso ele não exista será então realizado um cadastro inicial para o usuário, considerando seu nome, CPF e e-mail do cadastro de pessoa. O usuário então receberá um e-mail informando da criação do usuário, ativação da conta e criação da sua senha.

**Requer aprovação (integra somente após validação do relatório)**Essa opção permite a geração do relatório para posterior conferência e envio para integração. Assim o relatório será gerado e um registro será gravado na tela de monitoramento, com o status **Pendente de aprovação**. O usuário deverá acessar a tela de monitoramento para visualizar o relatório e realizar sua aprovação, momento em que ocorrera o seu envio para o portal TOTVS Assinatura Eletrônica.

**Configuração de prazos:**

**Utiliza prazo para validação/assinatura do documento e cancela se não assinado no prazo.**Ao marcar essa opção o usuário poderá definir o prazo (dias) em que o documento ficará disponível para aprovação/assinatura.   
Caso o documento não esteja assinado até a data limite informada, o usuário poderá excluir este através do processo **Exclusão de Documentos Integrados** existente no módulo **Monitor de Documentos Enviados para Assinatura**.

**Importante:**  
Este processo somente permite a exclusão do documento que não teve a assinatura realizada.  
O documento que teve a assinatura realizada após o prazo, terá seu status alterado para "Fora do prazo de assinatura".

**Opções de envio do aviso/recibo de férias:**Essas opções estão disponíveis apenas para os relatórios dos tipos Aviso de Férias e Recibo de Férias.

**Enviar no dia do aviso/pagamento de férias (se dia não útil antecipar para o dia útil)**Ao marcar essa opção o sistema somente integrará os avisos de férias com data de aviso na data da execução do processo (data do sistema) ou a data de pagamento no dia da execução do processo.

**Aviso de férias**Caso ao executar o processo a data do aviso for a data do sistema, enviará o aviso pois o dia do aviso é igual a data de execução.

Caso o aviso do funcionário esteja cadastrado em um feriado, então essa comunicação será antecipada para o dia útil anterior à data cadastrada.

A mesma regra será usada para o recibo de férias, porém considerando a data de pagamento das férias.

**Enviar com X dias de antecedência**Essa opção permite o envio do documento a X dias do seu início (data do aviso ou data de pagamento).

**Não validar essa regra**Não serão validadas as datas de aviso e pagamento de férias, sendo considerado os funcionários retornados pela seleção durante a execução do processo.

**Utilizar tabela de chefes/supervisores**

Configurações para definir se os chefes ou supervisores serão definidos como destinatários, e qual a relação deles no documento (assinador, testemunha ou validador).

**Regras para geração do nome do arquivo**

Regras para geração do nome do arquivo PDF, que poderá conter dentre as opções disponíveis a inclusão do nome ou chapa do funcionário.

**Relatórios**Na aba **Relatórios**, poderá incluir os relatórios já foram importados e estão disponíveis para o uso no RM Reports, porém nem todos os relatórios disponíveis funcionam via integração. Em casos assim, existe a possibilidade de gerar estes relatórios no RM Reports e integrar **manualmente** estes relatórios na plataforma web do TAE.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9675133321239)

Esses relatórios deverão possuir a tabela de funcionários (PFUNC) como uma das fontes de dados ou receber parâmetros como: **CHAPA, CODCOLIGADA, CODSECAO, DTPAGTOFERIAS, DTFENCFERIAS, DTAVISOFERIAS**.

**Importante:**  Ao realizar uma modificação no relatório que altere os parâmetros do relatório, como por exemplo **Visível em todas as coligadas**, será necessário informá-lo novamente na Aba de Relatórios do Tipo de relatório, antes de realizar o Processo de Integração de relatórios.

**Destinatários Específicos**Na aba **Destinatários Específicos,** é possível configurar os assinadores, testemunhas e validadores padrão para o tipo de relatório cadastrado, as pessoas que estiverem neste campo também receberão em seus e-mails o documento, como por exemplo uma pessoa que seja o responsável pelo Departamento Pessoal que deva assinar o relatório, mesmo não pertencendo a estrutura de chefia ou não seja o remetente do relatório.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9675182117911)

**Saiba mais**

[RH - RM - FOP - Assinatura Eletrônica: Permissão de Acesso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012213541-RH-RM-FOP-Assinatura-Eletr%C3%B4nica-Configura%C3%A7%C3%A3o-de-Acesso)

[RH - RM - FOP - Assinatura Eletrônica: Configuração de Acesso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9472851455767-RH-RM-FOP-Assinatura-Eletr%C3%B4nica-Configura%C3%A7%C3%A3o-de-Acesso)

[Definições e Parametrizações](https://tdn.totvs.com/pages/releaseview.action?pageId=607590749)
