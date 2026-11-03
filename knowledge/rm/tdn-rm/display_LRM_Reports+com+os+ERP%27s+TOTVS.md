---
content_hash: 32900f9d27379216dc2ab2a05b82072854ee7a4e7eec0881f3fcbd77f853165b
fetched_at: '2026-06-29T00:08:39.193176+00:00'
page_id: '286013551'
product: rm
source: tdn-rm
title: Reports com os ERP's TOTVS
type: documentation
url: https://tdn.totvs.com/display/LRM/Reports+com+os+ERP%27s+TOTVS
version: 10
---

# Índice:

---

.\*ndice:

# Objetivo:

---

     O objetivo desta página é orientar nos processos de configuração do RM Reports para uso em outros ERP's da Totvs.

# Introdução:

---

     Essa ferramenta de origem na linha RM pode ser utilizada por outras linhas da Totvs. Pelo Reports é possível criar uma variedade de relatórios diferentes, partindo do simples ao complexo. Comece pensando sobre a fonte de registro de seu relatório, podendo ser uma consulta SQL, Campos da Base ou Fonte de Dados. Não importa se seu relatório é uma simples lista de registros ou um resumo agrupado de vendas por região, primeiro determine quais campos contêm os dados que deseja ver em seu relatório e em quais tabelas ou consultas será necessário. Depois de feita estas escolhas ficará mais fácil criar seu relatório.

# Configurando Reports em ERP's:

---

falseDesenvolvimento/ProcedimentoBase Exemplo

     Para que o Totvs Reports possa se comunicar com a base de destino é preciso restaurar uma base exemplo. Esta base será a origem da conexão com a base onde se deseja extrair as informações para elaboração/criação dos relatórios. Para download deste arquivo acesse o portal do cliente em: <https://www.totvs.com/>. Concluído login no portal do cliente clique em “Downloads e Atualizações” .

     Preencha no campo busca o conteúdo: “BASEDEDADOS”. Selecione o produto “RM”, Versão “12.1” e o ambiente “Corpore RM”. Clique em “Buscar”. Serão listados os arquivos disponíveis para download. Escolha, de preferência, a versão mais recente disponível. No momento atual; BASEDEDADOSSQL\_12.1.17.MSI e BASEDEDADOSORACLE\_12.1.17.MSI.

false

• Após restaurar a Base é necessário executar o script "Acerta Usuário" na base. Para fazer este procedimento, siga as orientações: [SQL Server - Acerta Usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=61933633)

Instalação da Biblioteca RM

     Para acessarmos a plataforma do Totvs Reports e iniciarmos a elaboração dos relatórios é necessário instalarmos a RM Biblioteca. Para download do instalador acesse o portal do cliente em: <https://www.totvs.com/>. Concluído login no portal do cliente clique em “Downloads e Atualizações” .

     Preencha no campo busca o conteúdo: “BIBLIOTECA”. Selecione o produto “RM”, Versão “12.1” e o ambiente “Corpore RM”. Clique em “Buscar”. Serão listados os instaladores disponíveis para download. Escolha, de preferência, a versão mais recente disponível. No momento atual é; BIBLIOTECARM\_12.1.17.MSI.

Utilizando o RM como BI

     Concluído as etapas de restauração da base exemplo e instalação da RM Biblioteca configuramos o [RM como BI.](http://tdn.totvs.com/x/04Z8B)

Utilize o usuário mestre para logar no RM e realizar as configurações.

Usuário: mestre

Senha: totvs

Conexões em Bases Externas

     A [Conexão em Bases Externas](http://tdn.totvs.com/x/KgGSAw) possibilitará que o usuário crie consultas SQL que se comunicarão com outras bases de dados. Possibilitando até mesmo uma leitura de registros em uma [planilha de Excel](http://tdn.totvs.com/x/QQSLCQ).

Utilizando o Reports - FAQ

     Concluída as configurações o Totvs Reports estará pronto para uso. Acesse nosso [FAQ](http://tdn.totvs.com/x/fQ58Dg) para tirar dúvidas e descobrir as funcionalidades disponíveis nesta ferramenta.

Reports Web Service

     Também é possível a geração do relatório através do WebService, para isso é necessário seguir as documentações de [Como Expor o WebService do RM através do Host](http://tdn.totvs.com/x/HoFXBQ) e [Web Service Reports](http://tdn.totvs.com/x/nN6FDg).

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.15 ou Superiores

false

**Processo:** Reports em ERP's

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
