---
content_hash: cbdbf8401e7a6b906876f6c319fac8174dc07644ac9f9bd8dd06586cc21019ea
fetched_at: '2026-06-29T00:05:54.085077+00:00'
page_id: '107382544'
product: rm
source: tdn-rm
title: Relatório PPRA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=107382544
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Segurança e Saúde Ocupacional                      **Versão:**11.4X |
| **Processo** | **:** | Relatório Segurança |
| **Subprocesso** | **:** | Relatório PPRA |
| **Data da publicação** | **:** | 11/12/2013 |

**Considerações Iniciais**

O conteúdo do PPRA deverá atender na íntegra o que preconiza a NR-9 do Ministério do Trabalho e Emprego e as diversas legislações do Ministério da Previdência em especial o Decreto n. 3.048/1999 e a Instrução Normativa n. 99/2003.

[www.mte.gov.br/legislacao/normas.../nr\_09\_at.pdf](http://www.mte.gov.br/legislacao/normas.../nr_09_at.pdf)

<http://www010.dataprev.gov.br/sislex/paginas/23/1999/3048.htm>

<http://www010.dataprev.gov.br/sislex/paginas/38/INSS-DC/2003/99.htm>

O Programa de Prevenção de Riscos Ambientais – PPRA, exigível desde 1995 é um programa gerencial elaborado pela empresa, que deve abranger todos os seus trabalhadores.

A elaboração, implantação, acompanhamento e avaliação do PPRA poderão ser feitas pelo Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho - SESMT ou por pessoa ou equipe de pessoas que, a critério do empregador, sejam capazes de desenvolver o disposto na NR-09. O PPRA deverá ter assinatura de profissional legalmente habilitado, com registro no respectivo conselho de classe.

Para a correta elaboração do PPRA é de suma importância que:

* Sejam reconhecidos e avaliados os riscos aos quais os funcionários estarão expostos na empresa.
* Sejam cadastrados EPI’s /EPC’s e estes vinculados aos riscos.
* Sejam cadastrados os funcionários responsáveis pelos registros ambientais.

**Importante:**

Para correta geração do Relatório de PPRA disponibilizado pelo sistema os riscos deverão ser avaliados por lotação.

**Como Parametrizar o Sistema para Geração do Relatório de PPRA**

Como padrão, o sistema disponibilizará um modelo de PPRA baseado em local de trabalho lembrando que cada empresa deve adaptar este modelo a sua própria realidade. Estes arquivos se encontram no caminho: C:\totvs\CorporeRM\RMVitae\Relatórios, importar os seguintes relatórios, observando o banco de dados (Oracle / SQL):

* ·          PPRA\_01 – Capa.
* ·          PPRA\_02 – Identificação da Empresa.
* ·          PPRA\_03 – Atividades-Características.
* ·          PPRA\_04 – SESMT.
* ·          PPRA\_05 – Riscos.

No book de relatórios do sistema será disponibilizado os itens que compõem o relatório modelo, e para correta geração do mesmo, estes deverão ser importados para o sistema através do menu: Gestão | RM Reports | Processos | Importar Estrutura de Relatório.

**Criando o relatório**

Para criar o relatório de PPRA será necessário primeiramente definir o tipo de relatório a ser desenvolvido, para isso o usuário deverá acessar:

Relatórios | Tipos de Relatórios, e incluir um relatório do tipo: “Segurança”.

Após a importação dos relatórios, o usuário deverá gerar o modelo de PPRA. Para geração do modelo de PPRA, com o relatório selecionado clicar em: PROCESSOS | GERAR MODELO DE PPRA.

Caso o cliente deseje alterar o modelo de PPRA disponibilizado pelo sistema, no anexo: “Itens do Relatório” será possível incluir itens do tipo texto, onde ao clicar no botão: “Editar Texto”, será exibido um editor de texto para o usuário digitar suas informações.

No mesmo anexo, o usuário poderá incluir um relatório a partir do Gerador.NET, neste caso, basta selecioná-lo no LOOKUP de relatórios e selecionar o relatório desejado.

Após a geração do modelo de PPRA, o deverá ser incluído um relatório de segurança. O usuário deverá acessar: Relatórios | Relatórios de Segurança e incluir o relatório criado no passo acima.

Na aba: “Identificação”, deverão ser preenchidos os campos:

* Código do Relatório
* Data Início
* Data Fim
* Descrição
* Código Tipo Relatório
* Código Local de Trabalho

Caso deseje, o usuário também poderá preencher os campos: Código Filial, Código Seção, Código Função e Código Posto.

**Gerando o relatório**

Ao selecionar o tipo de relatório a ser gerado serão habilitadas a abas:

**Parametrização:** Onde serão carregados todos os parâmetros esperados pelos relatórios que compõem o tipo. Caso estes já estejam preenchidos na edição do cadastro, aba “Identificação”, eles serão automaticamente sugeridos nesta tela.

Ex: Se o relatório espera o parâmetro CODSECAO e este campo estiver preenchido na edição, o parâmetro irá recebê-lo como valor. De qualquer forma cabe ao usuário validar esta parametrização ajustando-a sempre que necessário. É obrigatório o preenchimento de todos os parâmetros para a geração do relatório.

**Gerar/Visualizar:** Trará informações de quando o relatório foi gerado pela última vez e quem o gerou. Ao clicar no botão "Gerar Relatório" o mesmo será gerado conforme o tipo e parametrização selecionada e todos os sub-relatórios de origem no Gerador.NET serão gerados como imagem e por conseqüência não poderão ser alterados. 

Ao clicar em "Visualizar" o usuário poderá ver o resultado final de seu relatório, as alterações a partir deste ponto não serão gravadas no banco de dados.
