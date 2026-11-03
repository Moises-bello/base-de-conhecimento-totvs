---
article_id: 360052253294
category: Manutenção de Ativos (SIGAMNT)
content_hash: d3033530a8fb59f44652c3f42dfa012bd9a3ff5082e25d708df473d8bac78916
fetched_at: '2026-06-28T22:42:33.055165+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Configuração Planta Gráfica
type: support-article
updated_at: '2021-11-04T13:48:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052253294-Manufatura-Linha-Protheus-MNT-Configura%C3%A7%C3%A3o-Planta-Gr%C3%A1fica
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:05:20 min**  
**Dúvida**Como é realizada a configuração da **Planta Gráfica** no **Manutenção de Ativos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**Para realizar a configuração da **Planta Gráfica** são necessárias as seguintes configurações:  
  
1. Acesse o módulo **Manutenção de Ativos - SIGAMNT** e selecione as opções **Atualizações\Planta Gráfica\Cadastro de Imagens - MNTA906**.  
2. Clique em **Incluir** para adicionar uma **biblioteca de imagens**, no campo **Tipo Imagem - TU1\_TIPIMG**, informar a opção **2 - Diretório**, após posicionar no campo **Imagem - TU1\_IMAGEM** e pressione **Enter**, será apresentada a tela **Pesquisa de Imagens.**3. Para adicionar imagens selecione a opção **Inserir**, localize a imagem no diretório do Sistema, após clique em **Salvar.**4. Será apresentada a mensagem **Deseja Selecionar as Imagens a serem inseridas**, clique em **Sim**.  
5. No quadro da esquerda serão apresentadas todas as imagens da pasta selecionada no **passo 3**, marque as imagens que deseja importar e **Confirme**, informe os dados conforme orientação do *help* de campo e **Confirme**.  
6. Insira todas as imagens necessárias para a edição da **Planta Gráfica**.  
7. Selecione as opções **Atualizações\Planta Gráfica\Edição - MNTA905**.  
8. A tela é dividida em três quadros e um **Menu principal**.  
9. No **Menu Principal**, em **Visualização\Eventos**, configurar os **Eventos**para a composição do círculo de eventos existem **5 posições** possíveis, as quais devem ser relacionadas a um respectivo evento e cor distinta - conforme desejado, assim identificado na rotina **Painel de Gestão - MNTA907**. Neste exemplo, configurar na posição **Primeira**, o evento **OS Corretiva Pendente**.    
10. No quadro da **esquerda Inferior**, temos a **Árvore Lógica**, nela podemos definir a estrutura da **Árvore Lógica** com suas respectivas localizações, inserção das imagens das plantas baixas e bens a serem controlados, bem como a inserção de ilustrações que servem apenas como recurso para uma melhor apresentação do *layout*.  
11. Selecione o primeiro **nível da estrutura**, através do **botão da direita**, selecione a opção **Incluir/Localização**, inclua as localizações necessárias. No campo **Planta Graf. - TAF\_PLANTA**, informe **Sim** para aquelas localizações nas quais necessitará de uma visão mais aprofundada, informe os dados conforme orientação do *help* de campo e **Confirme**.  
12. No quadro da **esquerda Superior**, temos as **Bibliotecas Gráficas**, são imagens nativas acrescentadas das imagens cadastradas no **passo 2**.  
13. Ao selecionar uma imagem no quadro da **esquerda Superior - Bibliotecas Gráficas** e clicar no **quadro da Direita - Palco de Edição**, será apresentada a tela para configurar as propriedades da imagem, informe: **Tipo Imagem = Ilustração**. A imagem selecionada será a visão inicial, ou seja, a primeira imagem a ser exibida na rotina **Painel de Gestão - MNTA907**.  
14. Repita o processo para as demais localizações, atribuindo uma imagem a cada localização na qual foi atribuída a propriedade de **Planta Gráfica - TAF\_PLANTA** igual a **Sim**.  
15. Neste exemplo, nossa **Árvore Lógica** será constituída do nível principal, em segundo nível, temos duas localizações, onde a cada localização, teremos novas localizações.  
16. Para que uma imagem adicionada ao painel tenha a propriedade de navegar para outro nível da **Árvore Lógica**, esta imagem deve ser do **Tipo Imagem** igual a **Planta Gráfica**.  
17. Após a inclusão da primeira imagem **passo 13**, podem ser adicionadas novas imagens. Estas imagens poderão permitir a navegação para outras localizações, desde que a propriedade do campo **Tipo Imagem** seja **Planta Gráfica**.  
18. Ao selecionar uma imagem no quadro da **esquerda Superior - Bibliotecas Gráficas** e clicar no **quadro da Direita - Palco de Edição**, será apresentada a tela para configurar as propriedades da imagem, informe:

* **Tipo Imagem = Planta Gráfica**.
* **Planta Gráfica** = Informe a localização na qual deseja que seja direcionado ao clicar na rotina de **Painel de Gestão - MNTA907**.

19. Selecione outra localização na **Árvore Lógica**, esta localização deve estar como o campo **Planta Gráf.** **- TAF\_PLANTA** igual a **Sim**.

20. Selecione uma imagem do quadro da **esquerda Superior - Biblioteca Gráfica**, em seguida clique no **quadro da Direita - Palco de Edição**, será apresentada a tela de propriedades da imagem, informe:

* **Tipo Imagem = Bem.**
* **Bem = Informar um bem - ST9**, passível de manutenção.

21. Informe os dados conforme orientação do *help* de campo e **Confirme**.

22. Selecione as opções **Atualizações\Planta Gráfica\Painel de Gestão - MNTA907**.

23. Será apresentada em primeira instância, a imagem relacionada ao primeiro nível da estrutura. Conforme cadastrado no **passo 9**, será apresentado um alerta, caso exista uma **OS Corretiva Pendente** para a **localização** ou **Bem** disposto na **Árvore Lógica**.

24. Selecione uma localização, através do **botão da direita**, clique na opção **Ordem de Serviço/ OS. Corretiva.**

25. Clique em **Incluir**, no campo **Situação** informe **Pendente**, informe os demais dados conforme orientação do *help* de campo e **Confirme**.

26. Após incluir a **OS**, clique em **Cancelar**, em seguida em **Sair**, para voltar em **Painel de Gestão - MNTA907**.

27. Será apresentado a partir no nível inicial, o alerta conforme configurado - **Passo 9**.
