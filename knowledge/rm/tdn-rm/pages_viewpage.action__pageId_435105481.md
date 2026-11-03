---
content_hash: a85f115917c3f16c6c20bc3dcb9b4df1021c9cdbffb2ec7850f143cc77898ad4
fetched_at: '2026-06-29T00:09:50.296816+00:00'
page_id: '435105481'
product: rm
source: tdn-rm
title: Relatórios - Listagem de Documentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105481
version: 11
---

# Procedimentos para Utilização

---

Visando uma apresentação mais abrangente dos cadastros de documentos, atualizamos o objeto gerencial TCGIRELALG0070 - Listagem de Documentos a Vencer.' para TCGIRELALG0070 - Listagem de Documentos', que tem como objetivo mostrar de forma organizada, todos os documentos cadastrados na base, e não somente os vencidos, de acordo com os parâmetros do filtro executado na geração do relatório.

Para utilizar este relatório é necessário importar o Objeto Gerencial 'TCGIRELALG0070 - Listagem de Documentos' através de Gestão | RM Reports | Importar Estrutura de Relatório.

O relatório estará disponível na pasta de Objetos Gerenciais da instalação do RM.

Após a importação deste relatório, basta então acessar Gestão | RM Reports | TOTVS Incorporação, e  selecionar o relatório TINRELALG0070 - Listagem de Documentos, ir em processos e clicar em "Gerar Relatório".

Será exibida então a tela de filtros disponíveis para geração do relatório com as seguintes tabelas:

* **Cadastro de Documentação**: Permite que seja criado um filtro com os dados do cadastro de documentos, como início de vigência, fim de vigência, descrição, coligada, etc;
* **Clientes / Fornecedores**: Permite que sejam filtrados dados da tabela de clientes / fornecedores;

Importante

Os dados desta tabela dizem respeito ao campo "Órgão Responsável" que é exibido no cadastro dos documentos e também será exibido no relatório.

* **Classificação do Documento**:Dados da classificação do documento, como código ou descrição.

Por padrão na primeira execução deste relatório, o sistema irá apresentar um filtro dinâmico para a tabela de Cadastro de Documentação, permitindo definir um período entre a Data Inicial e Final de Vigência. Como exemplificado acima, este filtro poderá ser alterado a critério do usuário.

*Filtro padrão para a geração do relatório de listagem de documentos*

Após geração do relatório, estarão presentes as seguintes informações dos documentos::

* **Documentação**: Consiste nos campos de descrição da documentação, bem como seu código cadastrado, orgão responsável e observações caso existam;
* **Classificação:** Consiste na classificação do documento apresentado;
* **Período:** Consiste no período do documento apresentado;
* **Associação:** O tipo de entidade que a documentação está associada e a descrição da entidade;
* **Vigência**: Inicio e término da vigência. O término da vigência dos documentos determina sua ordem de apresentação no relatório. Sempre do menor para o maior.
