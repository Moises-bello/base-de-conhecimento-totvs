---
content_hash: a11a3bc8fe107324982a9d1d4739e89bc492b560f998efb727913d954eb1bf17
fetched_at: '2026-06-29T00:05:55.031527+00:00'
page_id: '120783929'
product: rm
source: tdn-rm
title: Relatório PCMSO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=120783929
version: 5
---

**Produto:** TOTVS Segurança e Medicina do Trabalho                 **Versão:** 11.4X e superiores  
**Processo do Sistema:** Geração do Relatório PCMSO

##### Considerações Iniciais

O conteúdo do PCMSO deverá atender na íntegra o que preconiza a Norma Regulamentadora nº 07 – NR - 07, aprovada pela Portaria nº 3214, de 08 de junho de 1978, do Ministério do Trabalho e Emprego – MTE, e as demais portarias e legislações.

<http://www.mte.gov.br/legislacao/normas_regulamentadoras/nr_07_at.pdf>  
<http://www3.dataprev.gov.br/sislex/paginas/42/1977/6514.htm>  
<http://www3.dataprev.gov.br/sislex/paginas/42/1990/8112.htm>

A Norma Regulamentadora - NR-7, estabelece a obrigatoriedade da elaboração e implantação, por parte dos empregadores e instituições que admitam empregados, do Programa de Controle Médico de Saúde Ocupacional - PCMSO, com o objetivo de promoção e preservação da saúde do conjunto de seus trabalhadores.

O PCMSO deverá ter caráter de prevenção, rastreamento e diagnóstico precoce dos agravos à saúde relacionados ao trabalho, inclusive de natureza sub clínica, além da constatação da existência de casos de doenças profissionais ou danos irreversíveis à saúde dos trabalhadores.

Para a correta elaboração do PCMSO é de suma importância que:  
• Sejam cadastrados os exames aos quais os funcionários da empresa deverão ser submetidos.  
• Sejam cadastrados Perfis de Exames, e para estes perfis associar os exames aos quais os funcionários serão submetidos.  
• Sejam cadastrados os funcionários responsáveis pela monitoração biológica.

**Atenção!**  
Para correta geração do Relatório de PCMSO disponibilizado pelo sistema os riscos deverão ser avaliados por lotação.

##### Como Parametrizar o Sistema para Geração do Relatório de PPRA

Como padrão, o sistema disponibilizará um modelo de PPRA baseado em local de trabalho lembrando que cada empresa deve adaptar este modelo a sua própria realidade. Estes arquivos se encontram no caminho: C:\totvs\CorporeRM\RMVitae\Relatórios, importar os seguintes relatórios, observando o banco de dados (Oracle / SQL):

• PCMSO\_01 – Capa.  
• PCMSO\_02 – Identificação da Empresa.  
• PCMSO\_03 – SESMT.  
• PCMSO\_04 – Exames.

No book de relatórios do sistema será disponibilizado os itens que compõem o relatório modelo, e para correta geração do mesmo, estes deverão ser importados para o sistema através do menu: *Gestão | RM Reports | Processos | Importar Estrutura de Relatório*.

##### Criando o relatório

Para criar o relatório de PPRA será necessário primeiramente definir o tipo de relatório a ser desenvolvido, para isso o usuário deverá acessar: *Relatórios | Tipos de Relatórios,* e incluir um relatório do tipo: *“Saúde”*.

Após a importação dos relatórios, o usuário deverá gerar o modelo de PCMSO. Para geração do modelo de PCMSO, com o relatório selecionado clicar em: *PROCESSOS | GERAR MODELO DE PCMSO*.

Caso o cliente deseje alterar o modelo de PPRA disponibilizado pelo sistema, no anexo: “Itens do Relatório” será possível incluir itens do tipo texto, onde ao clicar no botão: “Editar Texto”, será exibido um editor de texto para o usuário digitar suas informações.

No mesmo anexo, o usuário poderá incluir um relatório a partir do Gerador.NET, neste caso, basta selecioná-lo no LOOKUP de relatórios e selecionar o relatório desejado.

Após a geração do modelo de PCMSO, o deverá ser incluído um relatório de segurança. O usuário deverá acessar: *Relatórios | Relatórios de Segurança* e incluir o relatório criado no passo acima.

Na aba: “Identificação”, deverão ser preenchidos os campos:  
• Código do Relatório  
• Data Início  
• Data Fim  
• Descrição  
• Código Tipo Relatório  
• Código Local de Trabalho

##### Caso deseje, o usuário também poderá preencher os campos: Código Filial, Código Seção, Código Função e Código Posto.

##### Gerando o relatório

Ao selecionar o tipo de relatório a ser gerado serão habilitadas a abas:

**Parametrização:** Onde serão carregados todos os parâmetros esperados pelos relatórios que compõem o tipo. Caso estes já estejam preenchidos na edição do cadastro, aba “Identificação”, eles serão automaticamente sugeridos nesta tela.

           Ex: Se o relatório espera o parâmetro CODSECAO e este campo estiver preenchido na edição, o parâmetro irá recebê-lo como valor. De qualquer forma cabe ao usuário validar esta parametrização ajustando-                  a sempre que necessário. É obrigatório o preenchimento de todos os parâmetros para a geração do relatório.

**Gerar/Visualizar:** Trará informações de quando o relatório foi gerado pela última vez e quem o gerou. Ao clicar no botão "Gerar Relatório" o mesmo será gerado conforme o tipo e parametrização selecionada e todos os subrelatórios de origem no Gerador.NET serão gerados como imagem e por conseqüência não poderão ser alterados.

Ao clicar em "Visualizar" o usuário poderá ver o resultado final de seu relatório, as alterações a partir deste ponto não serão gravadas no banco de dados.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[R@RH](https://totvs.byyou.com/?space=rrh)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 4 – (Recursos Humanos)
