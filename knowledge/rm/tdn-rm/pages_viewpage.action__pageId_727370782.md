---
content_hash: 76920ea2ec0f4e3527c0f0b68eff6d5ffb96d4f7582a9c67db06c63b97d86737
fetched_at: '2026-06-29T00:11:27.567194+00:00'
page_id: '727370782'
product: rm
source: tdn-rm
title: 8- Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=727370782
version: 25
---

Nesta tela, o professor poderá visualizar e gerar relatórios já cadastrados para suas turmas e disciplinas. O acesso a essa tela será feito por meio do **Diário de Classe**: ao selecionar a turma/disciplina e clicar no item de menu **Relatórios**, o professor poderá realizar a geração de relatórios referentes à turma ou disciplina selecionada.

Permissão de acesso

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Relatórios | Emitir relatórios.**

Filtros

Será possível realizar os seguintes filtros na tela. No primeiro acesso, alguns filtros poderão ser carregados automaticamente, de acordo com regras pré-definidas.

**Descrição:** Neste campo, o professor poderá informar um termo de descrição para que o sistema retorne apenas os relatórios que correspondam ao texto informado.

Relatórios disponíveis

O sistema disponibilizará ao professor a lista de relatórios conforme as configurações definidas no parâmetro **Configurações | Parâmetros | RM Portal - Gerais | Portal - Relatório 1/2**, no campo **Relatórios disponibilizados para professores** (Tipo: **TURMA**).

Configurações dos relatórios

Para que seja possível visualizar e imprimir o relatório corretamente por meio do portal, é necessário configurar os relatórios de acordo com as orientações abaixo:

Padrão de relatório

O sistema suporta apenas relatórios desenvolvidos no **RM Reports**. Para mais informações, consulte a documentação do

Relatório tipo "TURMAS"

Para que seja possível gerar o relatório por meio do portal, é necessário configurá-lo com o tipo **“RELATÓRIOS DE TURMAS”**.

Filtros do relatório por professor

Caso deseje filtrar os dados por professor, é necessário incluir o parâmetro **$CODUSUARIO** na consulta SQL, que corresponde ao código do usuário logado. Para mais informações, acesse a documentação **[Variáveis dinâmicas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003987132-Framework-Linha-RM-Frame-Vari%C3%A1veis-din%C3%A2micas-)**

Tabela Master

Cada relatório deve possuir a tabela **MASTER** no **DETALHE1** do relatório, contendo os campos obrigatórios para a correta emissão. Os filtros são enviados automaticamente pelo portal para os relatórios.

**Tabela MASTER:** STURMADISC (Turma/Disciplina)

**Campos-chave da tabela:** CODCOLIGADA, IDTURMADISC  
*(Os filtros desses campos são enviados automaticamente pelo portal.)*

Para a emissão do relatório por meio do **Portal**, não é permitido selecionar a tabela **MASTER** utilizando uma fonte de dados do tipo **Consulta SQL**.

Emissão dos relatórios

Para realizar o download do relatório, o professor possui duas opções:

**1ª opção:**  
Na página principal, basta clicar sobre o relatório desejado; em seguida, o download será iniciado automaticamente.

**2ª opção:**  
Na página principal, o professor deve clicar no botão **“Gerar”** para que o download do relatório selecionado seja realizado.
