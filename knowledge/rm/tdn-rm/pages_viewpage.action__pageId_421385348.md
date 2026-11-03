---
content_hash: 16adf9fba75551cfbe70de7ebee6ae6173bf1a928c110333aa5c9110fe554e03
fetched_at: '2026-06-29T00:09:15.325177+00:00'
page_id: '421385348'
product: rm
source: tdn-rm
title: Configuração de Mobilidade Sincronismo 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385348
version: 4
---

---

Para que o coletor móvel possa se comunicar com o TOTVS Obras e Projetos, são necessárias algumas configurações e também o cadastramento, no TOP, das informações que serão enviadas para o coletor.  
    
 O aplicativo TOP Mobile pode ser utilizado a partir da versão 5.0 do Android.   
 O tráfego de informações acontece via serviços REST que são acionados a partir do coletor móvel e para que os mesmos estejam disponíveis, é necessário realizar a instalação do TOTVS RM Portal para que o WebService FrameHTML seja criado no IIS e o sincronismo ocorra com sucesso.  
 É realizado em todo o sincronismo a validação da versão do aplicativo em relação à versão do sistema pois os mesmos devem ser compatíveis.  
    
 Para que as informações sejam sincronizadas, algumas particularidades são necessárias:

* Usuários: - Usuários devem estar associados ao coletor;
* Permissões devem estar definidas para o usuário associado: - Avanço Físico: Permite utilização de Avanço Físico no coletor; - Equipamentos: Permite utilização de Equipamentos no coletor; - Mão de Obra: Permite utilização de Mão de Obra no coletor; - Ciclo de Transporte: Permite utilização de Ciclo de Transporte no coletor.
* Projetos: - Projetos devem estar associados ao coletor; - Data Início e Data Fim do projeto (considera o cronograma).
* Parâmetros devem estar definidos para o sincronismo com o coletor: - Permissão para sincronizar imagens para o coletor; - Permissão para registrar fotos e associá-las ao apontamento do avanço físico.
* Folha Tarefa deve estar associada ao coletor: - Folhas Tarefa que possuem tarefas associadas; - Apontamento via Coletor; - Status: Associada ao Coletor ou Gerada; - Folhas que ainda não foram enviadas para o coletor; - Folhas de Projetos que não estão Paralisados, Cancelados, Revisados ou Concluídos e que não são revisões Horizontal; - Folhas que estão referenciadas para o coletor ou que possuem equipes onde o usuário do coletor é responsável.
* Equipes de Mobilidade devem estar associadas ao coletor: - Equipes nas quais o usuário do responsável da equipe, pessoa, está associado ao coletor.
* Ciclos de Transporte devem estar associados ao coletor: - Todos os Ciclos de Transporte dos projetos que estão associados ao coletor.
* Motivos de Improdutividade devem estar cadastrados na coligada: - Todos os motivos de improdutividade da coligada.
* Imagens: - Se a permissão para sincronizar imagens para o coletor estiver habilitada, as imagens de Coligada e Usuários de coletor que estão associados à uma pessoa são enviadas.

O sincronismo deve ser executado para que os dados sejam sincronizados entre o TOP Mobile e o TOTVS Obras e Projetos, sendo que este processo poderá ocorrer de forma manual ou automática.

* **Sincronismo Manual**

O usuário irá selecionar o processo de sincronismo manual, preencher o WebService que será utilizado no sincronismo, informar o usuário de acesso e a respectiva senha.

* **Sincronismo Automático**

O sincronismo automático é realizado por meio da leitura do QR Code gerado pelo sistema. O QR Code é gerado no cadastro dos usuários de coletores móveis e também pode ser enviado via e-mail.   
 Para mais detalhes da geração do QR Code, veja:    
 Ao selecionar o tipo de sincronismo automático, a câmera será habilitada para a leitura do QR Code. A câmera deve ser direcionada ao QR Code gerado e logo que a leitura é feita o sincronismo se inicia automaticamente.

* **Versão demonstrativa**

A versão demonstrativa é uma versão que já vem limitada com um banco de dados cadastrado e pode ser gerada ao selecionar o tipo de sincronismo manual. Selecionando o tipo de sincronismo manual a opção "Versão Demonstrativa" é exibida no final da página. A única condição para a opção não ser estiver exibida é o campo WebService estar preenchido, deve-se apagar o preenchimento do WebService para executar a versão demonstrativa.  
 A versão possui um banco de dados limitado que já vem cadastrado e possui cadastro para todas as funcionalidades do TOP Mobile mas não realiza sincronismo por se tratar de uma versão demonstrativa.
