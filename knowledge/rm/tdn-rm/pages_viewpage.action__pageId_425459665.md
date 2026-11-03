---
content_hash: 0f9adc3d56aeb5b377df7bcd4be606aa9851ee3dcdba3a04ee4a1547f767172c
fetched_at: '2026-06-29T00:09:37.996121+00:00'
page_id: '425459665'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento x Logix (BackOffice) – Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459665
version: 5
---

**Integração Folha | Logix – Funcionário**

---

A Integração Folha x Logix de Cadastro de Funcionário tem o objetivo de enviar os dados de funcionários visando integrar estas informações para utilização dos dados com o backoffice Logix.  
Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

· O módulo de Integração, deve estar configurado a integração Folha de Pagamento RM x BackOffice Logix:

* Clique no menu ferramentas | Configurar | Faça a configuração do banco de dados | Avance o processo e clique na a integração Folha de Pagamento RM x BackOffice Logix

·          Feito o processo acima, acesse o menu Integração | Gestão | Fórmula Visual | Fórmula Visual | Processos | Importação de Fórmula Visual e importa o pacote (FOPWKF0004 - Employee.TotvsWF).

* O pacote deverá ser disponibilizado no instalador, dentro da pasta "Objetos gerenciais/Fórmulas Visuais"

·          O sistema exibe tela de processo para importação da fórmula visual, selecione a categoria | marque a opção "Importar Gatilhos" e execute o processo. Para verificar se os gatilhos foram importados corretamente, selecione a fórmula visual (Employee\_2\_003) | clique em editar | na aba Gatilhos procure pelos gatilhos "FOPFUNCDATA; FOPFUNCAODATA; FOPRESCISAODATA; FOPSECAODATABR".

· Acesse o menu Integração | Mensagem única | Integrações | Selecione a integração TOTVS Folha pagamento RM x Backoffice Logix | clique em Anexos | Mapeamento de Entidades e verifique se a entidade com código 1020 (Employee\_2\_003) está mapeada.  
  
O processo de integração de funcionário da folha de pagamento será gerado por meio gatilhos por fórmula visual e gatilhos internos que serão disparados. Este envio será através de uma aplicação WebService que permitirá enviar dados em formato XML.  
   
Desta forma, a integração atenderá os seguintes objetivos.  
   
**Gatilhos por fórmula visual:**

* Inclusão de Funcionário: a inclusão de funcionário é gerada no TOTVS Folha de Pagamento e enviado para o sistema LOGIX.
* Alteração de Funcionário: a alteração de funcionário é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Rescisão: a rescisão de funcionário é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Alteração de filial no cadastro de seção: a alteração de filial no cargo de seção é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Alteração de cargo no cadastro de função: a alteração de cargo no cadastro de função é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.

**Gatilhos Internos:**

* Exclusão de Funcionário: a exclusão de funcionário é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Lançamento de Férias: o lançamento de férias é gerado no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Finalização de Férias: a finalização de férias é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Rescisão Coletiva: a rescisão coletiva é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Cancelar Rescisão: o cancelamento de rescisão é gerado no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Alteração Global de Campos Cadastrais: a alteração global de campos cadastrais é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.
* Transferência para mesma empresa: a transferência para mesma empresa é gerada no TOTVS Folha de Pagamento e enviada para o sistema LOGIX.

---

**Informações Complementares**  
  
Informações sobre Web Services
