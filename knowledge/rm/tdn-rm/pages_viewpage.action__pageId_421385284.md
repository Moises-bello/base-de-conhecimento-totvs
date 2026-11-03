---
content_hash: e0d300d4e731caf0d69390236c96e562112dd2173003a7569dc52780fdb1f01a
fetched_at: '2026-06-29T00:09:14.861475+00:00'
page_id: '421385284'
product: rm
source: tdn-rm
title: Edição de Projetos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385284
version: 15
---

---

**Identificação:**

---

Na criação de um projeto, deverão ser fornecidos os seus dados de identificação.

**Cód. Projeto:**

Informe o código do projeto.

**CNPJ / Inscrição Estadual:**

Informe o CNPJ e a Inscrição Estadual do projeto caso exista.

**CIB:**

Cadastro Imobiliário Brasileiro (CIB) como identificador único de imóveis, conforme a Instrução Normativa RFB nº 2.275/2025, e que garante o compartilhamento obrigatório de informações com o Sistema Nacional de Gestão de Informações Territoriais (Sinter).

O campo **CIB** é utilizado no envio da **NFS-e** quando o movimento possui um projeto informado, pois a rotina de envio busca essa informação na **tabela de projetos**. Para mais informações, acesse o link:

**Descrição:**

Informe o nome do projeto.

**Código Nacional de Obras (CNO) e Indicativo de Prestação de Serviços em Obra de Construção Civil:**

Essas informações são necessárias para a geração dos Registros R-2010 e R-2020 da EFD Reinf que contém dados sobre a retenção da contribuição previdenciária sobre serviços prestados/contratados mediante cessão de mão de obra, empreitada e subempreitada.

O Cadastro Nacional de Obras (CNO) refere-se ao registro perante a Receita Federal do Brasil das informações específicas de obras de construção civil, seja para pessoa física ou para pessoa jurídica. O CNO foi criado para substituir o cadastro especifico do INSS, que emite as matrículas CEI de obras de construção civil.

O campo "Indicativo de Prestação de Serviços em Obra de Construção Civil" possui as opções:

* Não se aplica;
* Não é Obra de Construção Civil ou não está sujeita a Matrícula de Obra;
* Obra de Construção Civil - Empreitada Total;
* Obra de Construção Civil - Empreitada Parcial.

**Tipo de Projeto:**

Informe o tipo de projeto podendo  ser "próprio" ou "terceiros". Caso o campo "Indicativo de Prestação de Serviço" seja preenchido com qualquer opção diferente de "Não se Aplica", o campo tipo de projeto não aparece na tela.

Quando o projeto estiver integrado com o BackOffice Protheus o campo tipo de projeto é enviado para o BackOffice juntamente com os demais campos referente ao REINF.

Se o campo "Indicativo de Prestação de Serviço" estiver preenchido como "Não se Aplica" o CNO  não deve ser enviado. [Cadastro Nacional de Obras](https://tdn.totvs.com/display/public/PROT/DT+Cadastro+Nacional+de+Obras)

Os detalhes de como os campos REINF são enviados para o BackOffice é detalhado no TDN :  [Informações do Projeto para EFD - REINF](http://tdn.totvs.com/pages/viewpage.action?pageId=336403938)

**Responsável:**

Informe o responsável pelo projeto.

**Classificação:**

Informe o tipo do projeto, por exemplo, se é uma obra de infraestrutura ou de empreendimento.

**Cód. Filial:**

Informe o código ou a descrição da filial do projeto. Este campo torna-se obrigatório caso o campo Indicativo de Prestação de Serviços em Obras de Construção Civil estiver preenchido com 'Não é obra de Construção Civil ou não está sujeita a matrícula de Obra'.

**Código do Departamento:**

Informe o código ou a descrição do departamento do projeto.

**Código do Centro de Custo:**

Informe o código ou a descrição do centro de custo do projeto.

**Cód. Cliente:**

Informe o código ou nome do cliente/fornecedor do projeto.

**Chapa Responsável:**

Informe o funcionário responsável pelo projeto. O cadastramento dos funcionários é efetuado através do RM Labore. Os funcionários com os status D - Demitido, I - Após. Invalidez, X - C/Dem.no mês e Z - Admissão prox. Mês não estarão disponíveis para seleção e nem ficam visíveis no cadastro do projeto caso estejam vinculados. O preenchimento desse campo é obrigatório, quando o sistema está integrado com o RM Oficina. Ao alterar o funcionário responsável pelo projeto, o sistema irá gerar um registro no anexo "Histórico do projeto", caso o usuário tenha permissão de acesso à tag de segurança "Inserir histórico de projetos".

**Código ART:**

É o Código da Anotação de Responsabilidade Técnica e é utilizado na geração de Notas Fiscais eletrônicas junto ao Conselho Regional de Engenharia, Arquitetura e Agronomia. O TOTVS Gestão Fiscal e o TOTVS Gestão de Estoque, Compras e Faturamento quando integrados através deste campo com o TOTVS Obras e Projetos, permitem que o usuário associe Notas Fiscais aos projetos cadastrados.

**Comentário:**

Informe qualquer comentário livre sobre o projeto, caso necessário.

A seleção nos campos (código e descrição) de filial, departamento e centro de custo só ficam ativas ao digitar parte do texto no campo, o símbolo "%" e pressionar a tecla TAB.

---

**Endereço:**

---

Informe o endereço do projeto.

---

**Campos Livres:**

---

Informe o conteúdo dos campos opcionais do projeto. Estes campos são habilitados em "Opções | Parâmetros | RM Solum | Gerais | Campos Livres e para desativá-los da janela de edição, basta deixar sua descrição em branco.

Os campos livres de valor seguem a configuração de casas decimais de 'Monetários' definidas nos parâmetros do projeto.

---

**Campos Complementares:**

---

Serão visualizados os campos complementares cadastrados em "Cadastros | Campos Complementares". Nessa janela os dados devem ser informados e caso tenha sido definida uma validação do campo complementar com base numa tabela dinâmica, o mesmo será validado nesse momento.

---

**Anexos**

---

**Histórico de Valores do Cálculo do Projeto:**

Exibe os registros dos logs de cada execução do cálculo do Projeto, que gerou alteração do valor deste ou de suas tarefas. Para saber mais a respeito, clique no link e será direcionado para a documentação do .

**Histórico do Projeto:**

Através desta visão é possível inserir/visualizar os status do projeto, assim como os funcionários responsáveis pelo mesmo. Inicialmente, ao inserir um novo Projeto, a posição do mesmo será sempre "A executar". Para alterar a posição do projeto, basta inserir uma nova posição através deste anexo.

Na inserção e alteração de um histórico, será validado se funcionário está ativo na folha de pagamento.

* **Processos que alteram o status automaticamente:**
  + Ao alterar o funcionário responsável, será incluído um novo registro na pasta Histórico do Projeto, com o funcionário alterado, a posição atual do projeto e a data da mudança. O log de status do projeto será inserido através da alteração realizada na chapa do funcionário responsável.
  + Ao gerar a revisão de um projeto, será gerado um registro para o projeto origem com a posição "Revisado". Todo o histórico posição será copiado para o projeto de revisão e será gerado outro registro com a posição "A executar", no qual o funcionário deverá ser o funcionário cadastrado no projeto caso exista, a data da mudança será a data do servidor de banco de dados (data e hora) e o usuário será o usuário corrente.
  + Ao Aplicar uma Alteração de Escopo de Aprovação o sistema gera um registro para o projeto origem com a posição "Concluído".
  + Ao Aplicar uma Alteração de Escopo de Rejeição o sistema gera um registro para o projeto origem com a posição "Cancelado".
  + Ao Equalizar um Projeto de Licitação e executar o Processo Gerenciar Projeto em Negociação o sistema gera um registro para o projeto origem com a posição "Em Negociação".

Para identificarmos na visão de Projetos em que Status se encontram os mesmos, foram criadas as opções de cores:

1. **Em andamento:** São exibidos na cor verde.
2. **Paralisado:** São exibidos na cor vermelha.
3. **Concluído:** São exibidos na cor azul escuro.
4. **A executar:** São exibidos na cor preta.
5. **Em Negociação:** São exibidos na cor azul clara.
6. **Revisado:** São exibidos na cor salmão.
7. **Cancelado:**São Exibidos na cor cinza.

**Integração Totvs Obras e Projetos com BackOffice Protheus:** Quando o projeto estiver integrado com o BackOffice Protheus e estiver com os campos REINF preenchidos serão enviados ao BackOffice conforme documentação:  
Informações do Projeto no RM : [Informações do Projeto para EFD - REINF](http://tdn.totvs.com/pages/viewpage.action?pageId=336403938)  
Informações gerais REINF - RM: [EFD - REINF](http://tdn.totvs.com/display/LRM/EFD-REINF)  
Informações gerais REINF - Protheus: [Manual de utilização REINF](http://tdn.totvs.com/display/TAF/EFD-Reinf)

**Clientes para Faturamento**

* Permite associar um ou mais clientes ao projeto para fins de faturamento
* Ao clicar no botão “+”, será possível incluir novos clientes
* A seleção será feita a partir da tabela CliFor, com as seguintes regras:

+ Exibe apenas registros que sejam:

- Clientes ou Clientes e Fornecedores (Ambos)

+ Não exibe registros que sejam apenas fornecedores

Para mais detalhes como utilizar acesse também :
