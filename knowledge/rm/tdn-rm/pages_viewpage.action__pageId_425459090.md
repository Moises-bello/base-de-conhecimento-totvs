---
content_hash: 33750c2269ec4c64afbddb1715acb2bcca5fcfbe1ba9065ab91f09786f5ada3d
fetched_at: '2026-06-29T00:09:33.939369+00:00'
page_id: '425459090'
product: rm
source: tdn-rm
title: Integração com ECM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459090
version: 2
---

**Integração com ECM**  
 

---

A integração possibilita a utilização do fluxo de etapas do ECM para os atendimentos abertos através do TOTVS Aprovações e Atendimento. Este recurso permite maior interação visando cada vez mais eficiência e qualidade nos processos.   **Desenvolvimento/Procedimentos**  
Parametrizações Necessárias:  
Para o bom funcionamento da integração, as configurações abaixo devem ser validadas com antecedência junto ao responsável pela implantação:

* Inicialização do banco de dados;
* Alteração da tag ServiceAlias no arquivo Web.Config;
* Inicialização do serviço específico para ECM no Windows.  
  1.     Acessar o ECM.  
  2.     Acessar Painel de Controle | Serviços:

* Adicionar o serviço: Este serviço irá registrar o WebService do TOTVS Aprovações e Atendimento no ECM.

          - Preencher os campos: Código, Descrição, URL.

* Salvar e Atualizar.

3.     Acessar Workflow | Configuração de Processos:

* Adicionar Processo Workflow.

          - Preencher informações cadastrais.  
          - Incluir fluxo de etapas do atendimento através da aba "Workflow Graphical Designer".  
          - Incluir o evento na aba Avançado, como por exemplo, afterReleaseVersion.  
          - Clicar em "Nova Versão" e posteriormente Liberar versão.  
4.     Acessar TOTVS Aprovações e Atendimento.

* Workflow | Tipos.

          - Editar o registro criado em relação ao ECM;  
          - Alterar Tipo de Integração;  
          - Informar usuário, senha e coligada;  
          - Informar o caminho do WebService do ECM.  
5.     Executar processo de sincronização de usuários.

* Workflow | Tipos | Processos | Sincroniza os usuários do Corpore com o usuário do ECM.

6.     Workflow | Grupos.

* Vincular o tipo de atendimento criado para o ECM a um grupo.

**Descrição do Processo**

* Após efetuar todos os procedimentos acima, o atendimento pode ser criado.
* Informar no atendimento o grupo e o tipo corretamente.
* Preencher as informações necessárias.
* Ao avançar etapa da ocorrência será respeitado o fluxo de atendimento do ECM.

**Informações Adicionais**  
Para os tipos de atendimento integrados, o TOTVS Aprovações e Atendimento busca todas as informações referentes ao fluxo no ECM, logo qualquer modificação necessária deve ser realizada diretamente no ECM.  
Obs.:  
 O anexo de Fluxo de Etapas do Tipo de Atendimento do TOTVS Aprovações e Atendimento não apresenta informações quando o mesmo estiver integrado.  
**Atendimentos via Web**  
O grupo e tipo de atendimentos integrados com o ECM poderão ser utilizados também para as ocorrências na web e seguirão o fluxo de etapas de acordo com o ECM.

|  |  |
| --- | --- |
|  | Recursos Adicionais |

---

[Blog - Integração do ECM](http://totvsconnect.blogspot.com/2010/11/como-fazer-integracao-crmrm-agilis-x) [Vídeo - Integração do ECM](http://rmnet.rm.com.br/demorm/RMAgilis/IntegracaoRMAgilisECM/Integracao%20RMAgilis%20ECM.htm)
