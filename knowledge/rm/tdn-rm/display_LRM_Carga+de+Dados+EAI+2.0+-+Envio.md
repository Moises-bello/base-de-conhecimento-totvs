---
content_hash: 203216d8cd566fe94319743c95416a01418fe7e835b92d93827434f9af07063f
fetched_at: '2026-06-29T00:10:38.627039+00:00'
page_id: '544210843'
product: rm
source: tdn-rm
title: Carga de Dados EAI 2.0 - Envio
type: documentation
url: https://tdn.totvs.com/display/LRM/Carga+de+Dados+EAI+2.0+-+Envio
version: 13
---

O Processo de **Carga de Dados** é destinado à sincronização de informações cadastrais entre 02(dois) ou mais sistemas TOTVS integrados, garantindo a confiabilidade e integridade desses dados.

---

## **Processo de Carga de Dados - Sincronização de Entidades:**

Este processo está disponível para a integração com o EAI 2.0, a partir da versão 12.1.28 do RM, no módulo **Integração | EAI 2.0 | Ferramentas | Carga de Dados** e pode ser acessado pelo usuário que possui permissão de acesso ao menu, via tag de segurança, em seu Perfil de usuário e ... (Listar as permissões).

A tela de visualização do processo é composta por 06 (seis) componentes principais:

---

### **01. APLICATIVO**

Neste componente, deve-se selecionar qual a aplicação será utilizada para a sincronização das informações com o RM.

Serão listados todos os aplicativos presentes, que integrem com esse sistema (Protheus, Datasul, ...).

### **02. LISTA DE PACOTES DE INTEGRAÇÃO**

Após a seleção do Aplicativo, o componente "02. Lista de Pacotes de Integração" disponibilizará cada um dos Pacotes Instalados que estejam migrados para o EAI 2.0.

### **03. LISTA DE ADAPTER'S**

Selecionado o pacote de integração na etapa anterior, serão listados todos os Adapter's do tipo "Cadastro", que estejam mapeados para este pacote.

Apenas 01 (um) adapter poderá ser selecionado por vez, ou seja, a carga será realizada apenas para uma única entidade por execução.

### **04. FILTROS DE ITENS DA ENTIDADE**

Com a entidade selecionada, é possível incluir filtros personalizados, utilizando os componentes de filtro presentes em todos os módulos da MDI, para especificar um conjunto de informações conforme as necessidades do usuário.

O filtro não é obrigatório para execução do processo. Recomenda-se utilizar o filtro para limitar o número de registros ou que atenda à uma regra especifica, como por exemplo, fazer carga apenas de registros ativos.

### **05. FILTRO COLIGADA**

Nesta opção serão aplicados o filtro de coligada conforme a opção selecionada.

* **Coligada do contexto selecionado:** padrão vem marcado. Esta opção adiciona ao filtro da carga de dados o código da coligada em que o usuário está logado.
* **Coligadas configuradas na integração:** irá aplicar no filtro da carga de dados todas as coligadas que fazem parte do De/Para de integração do aplicativo selecionado.

Informação

O recurso de Filtro Coligada está disponível a partir da versão 12.1.2205.

### **06. OPÇÃO DE REENVIO**

Com esta opção selecionada, serão reenviados todos os itens da entidade selecionada, não apenas os não integrados. Caso o insumo que esteja sendo enviado, com esta opção selecionada, já possua um registro de sincronização, o mesmo será sobrescrito.

Lembrando que os dados que serão sobrescritos no destino são os registros que foram selecionados pelos filtros de tabela mais filtro de coligada.

---

## **Log de Execução**

Após a execução do processo, será apresentado um log contendo todas as informações do contexto de execução. Este log pode apresentar 02 (dois) status de execução:

* A execução do processo foi concluída com sucesso:

Neste contexto, todos os registros selecionados foram enviados e sincronizados com êxito.

* A execução do processo foi concluída com ressalvas:

Neste contexto, alguma inconformidade impossibilitou que o processo fosse realizado com êxito. O(s) motivo(s) serão detalhados na visão da tela Log.

* A execução do processo foi encerrada com falha:

Por fim, caso nenhum dos registros tenha sido sincronizado com sucesso, ou, algum outro fator impossibilite que o processo seja executado, será lançada uma exceção cujo conteúdo indique Erro/Falha na conclusão do processo.
