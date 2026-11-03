---
content_hash: 9eeeb6bb7b6771eca179e79741b76fdbbf4b2acb1b5ae26f3cbc597775d6f74d
fetched_at: '2026-06-29T00:06:06.958874+00:00'
page_id: '201733719'
product: rm
source: tdn-rm
title: Caminho de Relacionamento Entre Diferentes Tabelas
type: documentation
url: https://tdn.totvs.com/display/LRM/Caminho+de+Relacionamento+Entre+Diferentes+Tabelas
version: 17
---

Nas versões inferiores a **12.1.5**, o caminho de relacionamento trabalhava de maneira menos dinâmica e menos intuitiva, através de um carregamento de dados preso à ordem de inserção dos controles na estrutura do relatório.

Com a **Reestruturação do Reports,** a partir da versão **12.1.5**, o caminho de relacionamento entre diferentes tabelas, passou a trabalhar de maneira mais dinâmica e mais configurável, já que o usuário pode escolher uma combinação de tabelas e como relacioná-las umas com as outras.

Diferentemente das versões anteriores à **12.1.5**, o novo Reports possui uma nova estrutura interna, onde uma consulta sql é gerada a partir das tabelas adicionadas ao relatório, bem como o relacionamento entre elas, por isso, o caminho de relacionamento é tão importante, já que impacta diretamente no resultado do relatório gerado.

## **Exemplo Prático**

*Construção de um boleto usando o **"Caminho de Relacionamento entre Diferentes tabelas"***

***Imagem 1 - Construção do boleto***

Um relatório pode conter diversas fontes de dados, entre elas, tabelas do banco de dados e consultas sql.

******Imagem 2 - Fontes de dados do relatório******

Um relatório pode ter também uma **tabela mestra (Ligada ao detalhe mais externo)**, cujo caminho de relacionamento com outras tabelas se inicia. ******Imagem 3 - Tabela Mestra (Ligada ao detalhe mais externo)******

Ao utilizar um componente **[TIPO: TEXTO]**, vinculado à um campo de uma tabela de dados **[CONTA.NUMAGENCIA],** o sistema cria automaticamente vários caminhos de relacionamento entre a tabela mestra, a tabela vinculada ao componente adicionado e também com outras tabelas anteriormente adicionadas à estrutura do relatório.

***Imagem 4 - Campo de texto NUMAGENCIA1 adicionado à estrutura do relatório. Nesse momento é criado vários caminhos de relacionamento entre as tabelas adicionadas à estrutura do relatório.***

O usuário poderá escolher entre os diversos caminhos de relacionamento entre as tabelas. Essa configuração deve ser feita corretamente para que o relatório seja íntegro em sua geração.

***Imagem 5 - Caminho de Relacionamento entre as tabelas adicionadas na estrutura do relatório.***

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

 

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
