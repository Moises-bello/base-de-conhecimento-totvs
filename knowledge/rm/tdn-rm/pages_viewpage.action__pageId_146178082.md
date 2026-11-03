---
content_hash: 4c4a5624d408c00e5cd541004fcb40a1dc80ceff8958230fb3092cbef54f1b24
fetched_at: '2026-06-29T00:05:55.706475+00:00'
page_id: '146178082'
product: rm
source: tdn-rm
title: Utilizando tradutor de relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146178082
version: 45
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Reports                        **Versão:**11.80 |
| **Processo** | **:** | Importação/Exportação |
| **Subprocesso** | **:** | Tradução de relatórios |
| **Data da publicação** | **:** | 11/06/2014 |

# **TRADUTOR DE RELATÓRIO**

    O tradutor de relatório tem a função de traduzir objetos do tipo texto contidos nos relatórios, para Inglês ou Espanhol. Com esta funcionalidade, usuários que utilizam o sistema em inglês ou espanhol, poderão receber relatórios traduzidos de maneira eficaz.

---

**Trabalhando com a funcionalidade de tradutor de relatório**

   **1°)**  Acesse a guia/menus  "**Gestão |** Ferramentas de Análise | **RM Reports".**

    **2°)** Depois de carregada a visão, selecione o relatório a ser traduzido.

     

    **3°)** Depois de selecionado o relatório, é necessário exportá-lo. Através do arquivo exportado é possível realizar o procedimento de tradução. Para realizar a exportação do relatório, clique em **Processos**, em seguida, **Exportar dados para tradução do relatório.**

**4°)** Atribua um nome ao arquivo e selecione onde ele será gerado, após preenchido clique em **Executar.**

**5°)**Concluído o processo, devemos localizar o arquivo **.XLS** no diretório onde foi gerado.

**6°)** Abra o arquivo **.XLS**. O excel fará uma verificação no arquivo e mostrará a mensagem abaixo. Clique em **sim** na mensagem para o arquivo ser aberto, para podermos dar início ao processo de tradução.

**7°)** Concluída a abertura do arquivo .**XLS.** Na parte esquerda temos os campos em português, na direita os campos que deverão ser preenchidos no idioma desejado, no exemplo utilizamos o inglês.

| **Observação:** Somente objetos do tipo Texto serão traduzidos. |
| --- |

    **8°)** Após completar a tradução na coluna da direita salve e feche o arquivo para que as alterações sejam concluídas.

    

    **9°)** Após ter salvo o arquivo, importe-o através do sistema. Para isso é necessário marcar o relatório que será feito a tradução, pois será gerado um relatório filho do relatório selecionado com os componentes do tipo texto traduzidos.

    

    **10°)** Para importar o arquivo **.XLS**, clique em **Processos**, em seguida, **Importar tradução do relatório.**

    

    **11°)** Será apresentada uma tela com opções de importação. Em **Idioma**marque o idioma em que foi feito o preenchimento no arquivo **.XLS,**na coluna **Translate(Passo 7)** e logo abaixo informar qual o caminho está alocado o arquivo **.XLS**. Em seguida clique em **Executar.**

    **12°)** Observe que foi gerado um relatório filho e sua nomenclatura possui uma concatenação de acordo com a linguagem que foi selecionada no passo 11.

    

    **13°)** Após o relatório traduzido, basta gerá-lo e verificar as traduções. Marque-o e clique em **Processos, logo após, Gerar Relatório.**

    **14°)** Confira se todas as informações mostradas estão de acordo, logo após, clique em **Executar.**

    

    **15°)** Após executar o processo de gerar o relatório traduzido será mostrado na tela, os campos traduzidos conforme preenchido no passo 7.

    

---

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
