---
content_hash: 59acd8ae098322e872aa64ca8170d5d3f2b8d86a0fbf2b687e077c572f0fce75
fetched_at: '2026-06-29T00:09:37.476435+00:00'
page_id: '425459617'
product: rm
source: tdn-rm
title: Arquivos Anexos do Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Arquivos+Anexos+do+Atendimento
version: 35
---

Você pode anexar arquivos importantes ao seu atendimento, como documentos, imagens, planilhas e etc... Esses arquivos ficam armazenados na Base de Dados ou no Repositório de Arquivos (FileRepo) de acordo com o **[parâmetro](https://tdn.totvs.com/pages/viewpage.action?pageId=425458436&draft=true)** selecionado e podem ser acessados sempre que precisar.  
  
Em Atendimentos > Anexos> Arquivos anexos do atendimento, você pode adicionar, visualizar, baixar, excluir e gerenciar todos os documentos relacionados a um atendimento, independentemente de onde eles foram originalmente armazenados.

Para anexar um arquivo Clique no botão "+" e preencha os campo abaixo:

* **Detalhes do arquivo:** inserir o nome do arquivo que será anexado.
* **Nome do arquivo:** Selecione o arquivo do seu computador clicando em (...).
* **Carregar documento:**Botão para carregar o arquivo já incluído anteriormente, onde o arquivo será aberto em uma nova aba ou janela, permitindo que você visualize seu conteúdo.
* **Atendente que incluiu:** Mostra o nome do atendente que adicionou o arquivo.
* **Atendente que alterou:** Mostra o nome do atendente que realizou a última alteração no arquivo.
* **Data alteração:** Indica a data da última alteração no arquivo.
* **Status:** Mostra o status atual do arquivo (Ex: Adicionado, Excluído, Modificado).

Após essas informações preenchidas o  sistema irá armazenar o arquivo de acordo com as configurações definidas (**[Base de dados ou FileRepo](https://tdn.totvs.com/pages/viewpage.action?pageId=425458436)**).

Além de anexar arquivos clicando no botão "+", você pode arrastar e soltar os arquivos  anexando os  diretamente nas abas de acompanhamento (Solicitação, Discussão e Solução).

###### **Observação:** No Windows 11, a funcionalidade de arrastar e soltar pode não funcionar corretamente se o Host e RM estiverem sendo executados com privilégios de administrador. Nesse caso, execute-os com privilégios normais para utilizar essa funcionalidade.

Para excluir um arquivo, selecione-o e clique no ícone "X" em vermelho. Em seguida, confirme a exclusão.

Lembre-se de que o método de exclusão pode variar :

* **Arquivos da Base de Dados:** Serão marcados como excluídos e permanecerão visíveis no sistema, com o status excluído.

* **Arquivos do (FileRepo):** Serão removidos permanentemente e não estarão mais visíveis.

A opção "Editar arquivo" permite que você faça alterações no arquivo anexado e na descrição.

* **Inclusão no Arquivo (FileRepo) :** Na inclusão de arquivos do pelo FileRepo não será exibido o código do arquivo na visão.

* **Inclusão no Arquivo na base de dados** **:**Na inclusão de arquivos pela base de dados é exibido o código do arquivo.

**OBS:** Quando estiver utilizando arquivos do FileRepo, o tamanho dos arquivos não será exibido na visualização do anexo, já que não há restrição de tamanho.

**Importante:**Independentemente de onde um arquivo foi armazenado nos (Base de Dados ou Repositório de arquivos (FileRepo), a forma como você interage é sempre a mesma. Você verá todos os arquivos em um único local e poderá realizar as mesmas ações em todos eles.

Quando estiver habilitado o parâmetro FileRepo a visualização de alguns campos serão diferentes.(Por exemplo: Cod Arquivo, Atendente, Atendente atual não será visualizados na visão e edição dos anexos)

Lembre-se também que, ao alterar o parâmetro de "Base de dados" para "Repositório de arquivos (FileRepo)" ou vice-versa, para visualizar as mudanças de comportamento, é necessário fechar o anexo e habilitar a configuração de seleção de colunas, conforme mostrado nas imagens abaixo:

| **1.Utilizando Base de Dados.** |
| --- |

---

| 2.Utilizando FileRepo |
| --- |

---

Salvar Arquivos Anexos do Atendimento
