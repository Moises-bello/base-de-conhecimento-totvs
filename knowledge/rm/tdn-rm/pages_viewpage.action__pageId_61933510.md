---
content_hash: 9124b2eb8f035b556c65a2dad9495ebad524f6b0cb337367100f71734e9ea18d
fetched_at: '2026-06-29T00:11:02.639572+00:00'
page_id: '61933510'
product: rm
source: tdn-rm
title: Identificador de Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61933510
version: 19
---

# Índice:

---

# Objetivo:

---

       O objetivo deste documento é auxiliar na utilização de Identificador de Relatórios.

# Introdução:

---

O Identificador de Relatórios ele representa um geração única de Relatório

# Como utilizar:

---

Primeiramente você deverá incluir no relatório o "Identificador do Relatório". Para isso, após selecionar o relatório que irá ser tratado clique na barra de "Ferramentas", selecione a opção "Variável" e a arraste para o corpo do relatório onde será impresso o código de registro do relatório.

     - Uma vez com a variável arrastada para a estrutura do relatório você irá selecionar a variável e teclar F4. Na "Grade de Propriedades" em "Dados" defina "CódigoRelatorio" em "Variável".

      - Depois de feita a escolha do tipo variável e salvar, o sistema irá mostrar um código mascarado no relatório.

     -  Após realizar as devidas alterações execute o relatório para que o código seja processado. Para gerar o relatório, volte a tela de listagens de relatórios, selecione o relatório modificado e clique no menu em "Processos → Gerar Relatório".

***Observação:***  
***O relatório só gera o Código Identificador ao ser executado com a opção "Apenas Geração - O relatório gerado ficará disponível na visão de processos, para uma posterior consulta". Nos demais processos não irão funcionar.***

     - Uma vez gerado o relatório o código será apresentado no mesmo:

       - Para realizar a validação do relatório acesse o RM Portal e clique na opção "Certificador de Relatórios".

     - Na tela seguinte você deverá digitar o código que foi apresentado após a geração do relatório no RM. Após digitar o código clique no botão "Buscar".

     - O sistema irá listar o relatório que foi gerado com o código e disponibilizará a visualização do mesmo, caso desejado.

     - Caso deseja visualizar, o sistema irá gerar o relatório demonstrando o código do identificador.

# Passagem de GUID por parâmetro:

---

       Trata-se de um novo recurso para passar o ID do relatório diretamente via querystring.

Essa opção estará disponível na versão 12.1.24.122 ou superiores.

# Como utilizar:

---

    Para acessar o relatório diretamente basta passar o GUID do relatório no parâmetro UIDREL via querystring.

    Modelo para formação do link:

***[Endereço do Portal]/Source/RptGeradorRelatoriosNet/RM.Rpt.Reports/Anonymous/RptFindReportByGuid.aspx?uidrel=[Id do Relatório]***

    Ao criar esse link é possível acessar o relatório diretamente como mostra no exemplo abaixo.

# Exemplo:

---

     Link utilizado:

**http://localhost/CorporeAtual/Source/Rpt-GeradorRelatoriosNet/RM.Rpt.Reports/Anonymous/RptFindReportByGuid.aspx?uidrel=784451e1-081c-4b39-9f97-090ca1e09336**

     Ao acessar esse endereço ele já abre diretamente na página de relatórios do qual eu utilizei o ID como mostra na imagem abaixo:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Identificador de Relatórios

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
