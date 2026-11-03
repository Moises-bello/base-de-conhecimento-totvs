---
content_hash: 8eb24775834a52d1065c5b848d92a9147f63d9c4167d4a7042e6909fe11f3083
fetched_at: '2026-06-29T00:05:54.369696+00:00'
page_id: '107938428'
product: rm
source: tdn-rm
title: Perguntas & Respostas - TOTVS Restore
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=107938428
version: 2
---

**Perguntas & Respostas:**

**1. Funciona em todas as versões? 11.40, 11.50.11.80.12.1**  
Sim, o TOTVS Restore independe da versão dos aplicativos da TOTVS RM, ele funciona simplesmente como um instalador e desinstalador dos aplicativos de forma remota através da  
rede.  
**2. Ele atualiza patch e atualização específica?**  
Sim, é possível utilizar todos os instaladores dos aplicativos TOTVS RM existentes atualmente,.MSIs e .EXEs.

**3. Ele pode ser executado em grupo de trabalho?**  
Sim, basta ter um usuário administrador em todas as máquinas daquele grupo de trabalho.

**4. O caminho dos executáveis que serão instalados tem que ser uma pasta compartilhada na rede?**  
Não, os executáveis podem estar tanto na rede ou quanto localmente na máquina. É importante salientar que caso o executável estiver na rede, não utilizar atalhos de mapeamento de rede,  
utilizar o caminho absoluto do arquivo.

**5. O Firewall habilitado pode ocasionar problemas na instalação remota?**  
Sim, o TOTVS Restore faz uma leitura do registro da maquina remota e utiliza WMI(Windows Management Instrumentation) para a instalação remota, tais tarefas podem ser bloqueada pelo  
firewall.

**6. As máquinas inacessíveis serão atualizadas quando forem ligadas?**  
Não, é possível atualizar somente as máquinas que estão acessíveis no momento da atualização.

**7. É possível criar relatório ou agrupar as máquinas por versão instalada?**  
Não, o TOTVS Restore não possui a funcionalidade de criação de nenhum tipo de relatório. O agrupamento das máquinas por versão pode ser feito criando-se vários tipos de ambientes diferentes.

**8. Eu tenho limites de maquinas e de produtos para instalação?**  
Não, o aconselhável é que seja restringida uma quantidade de máquinas de acordo com os recursos de hardware para que não haja sobrecarga na rede, processamento e memória na  
máquina que dispara a atualização para que não haja travamento. Pode ser inserido o numero de produtos para a atualização que desejar.

**9. Durante a atualização executada pelo TOTVS Restore os usuários poderão utilizar outrossoftwares da máquina?**  
Sim, só não poderão usar os softwares da TOTVS RM.

**10. O aplicativo faz uma varredura do meu domínio informando o nome dos computadores? Ou eu tenho que informar manualmente o nome dos micros que serão atualizados?**  
Sim, é possível listar todos os computadores do domínio e adicionar os escolhidos na lista deatualização. Caso deseje poderá informar os nomes das máquinas manualmente também.

**11. Para evitar erros no sistema operacional o correto é seguir a sequência de desinstalação Aplicativo >> Biblioteca? E para a instalação o contrário Biblioteca >> Aplicativo?**  
Sim, as regras seguem as mesmas dos instaladores, ao remover já serão selecionados automaticamente os aplicativos primeiro para depois remover a biblioteca. Na instalação deve ser  
instalado primeiro a biblioteca para depois os aplicativos, esta ordem o usuário deverá informa-la.

**12. A instalação acontece de forma silenciosa no micro do usuário, ou seja, ele pode continuar trabalhando com outros aplicativos enquanto o RM está sendo atualizado?**  
Sim, ele instala de forma silenciosa e o usuário pode utilizar o micro na hora de atualização.

**13. O aplicativo necessita de alguma configuração específica do sistema operacional?**  
Exemplo, desabilitar Firewal do Windows? Todas as premissas para utilização do TOTVS Restore podem ser encontradas no manual, que pode ser baixado na central de downloads do cliente ou pode ser encontrada junto ao caminho de instalação do aplicativo.

**14. Faz a verificação de máquina logada no sistema?**  
Não, essa verificação ainda não é feita.

**15. No momento da instalação ele diz que esta sendo realizado uma cópia, realmente é copiado o instalador para a máquina local? salvo em qual diretório?**  
Sim, ele faz uma cópia para uma pasta temporária (C:\InstallTotvsTempFolder ) para a máquina que está sendo atualizada, ao final da instalação esta pasta temporária é apagada.

**16. Esse aplicativo precisa de Biblioteca instalado? Ou é só instalar ele em qualquer máquina e rodar?**  
Não precisa de biblioteca, somente de .Net Framework 4.0.

**17. Se o usuário estiver usando o software no momento, é exibida alguma mensagem, o programa aguarda fechar o mesmo ou simplesmente começa a desinstalação?**  
Não é recomendado fazer a atualização com o sistema aberto, pois pode ocorrer erro na atualização. O usuário não será informado de nenhuma mensagem.

**18. Existe a possibilidade de schedule ou job de instalação?**  
No momento não existe essa funcionalidade no TOTVS Restore.

**19. O log avisa qual foram feitas?**  
Sim, o log mostra todas as informações da atualização para cada máquina.

**20. Se uma maquina estava disponível, e ate rodar, ela ficou off-line, não tem como gerar algo que facilite para que seja pedido apara rodar penas para estas novamente?**  
No momento não existe essa funcionalidade no TOTVS Restore.

**21. Quando iniciar a instalação aparecerá uma mensagem para o usuário ou esse processo deve ser feito no momento em que não estiver sendo usado?**  
Não aparecerá nenhuma mensagem para o usuário, no momento da atualização o usuário não poderá estar utilizando os softwares TOTVS RM.

**22. Eu posso ter o TOTVS Restore na minha maquina local e selecionar para atualizar todos os servidores?**  
Sim, o TOTVS Restore pode ser utilizado em qualquer máquina para atualizar qualquer máquina desde que estas estejam em um domínio ou grupo de trabalho.

**23. É possível definir limite de instalações simultâneas de forma que as outras ficam aguardando a finalização das atuais?**  
Não é possível, é o usuário quem define a quantidade de atualizações.

**24. O que preciso baixar para fazer a instalação?**  
É necessário ter o TOTVS Restore instalado e ter os instaladores dos aplicativos TOTVS RM.

**25. O BDE está incluso nessa ferramenta?**  
Não, o BDE não é um aplicativo da TOTVS, ele é necessário pelo uso dos sistemas Delphi da TOTVS RM, mas uma vez instalado, não é necessário sua atualização.

**26. Quais versões de sistema operacional o sistema atende?**  
A partir do Windows XP e superiores.

**27. Como deverá ser vendido esse produto? Necessita de alguma licença específica?**  
Não será cobrado pela utilização do TOTVS Restore, todos os clientes TOTVS poderão baixá-lo gratuitamente na central de downloads.

**28. Existe a tela que seleciono os programas para desinstalação e para instalação os programas que selecionar serão instalados em todas as estações selecionadas?**  
Sim, serão instalados em todas as estações selecionadas.

**29. Gostaria de saber em que esta ferramenta nos ajuda utilizando um servidor de aplicação (3 camadas). Como é o procedimento?**  
Ela ajuda para a instalação dos clients.

**30. As versões especificas 'somente exe' e 'dll' tem como atualizar?**  
O TOTVS Restore não atualiza dlls, ele utiliza somente os instaladores .exe e .msi.
