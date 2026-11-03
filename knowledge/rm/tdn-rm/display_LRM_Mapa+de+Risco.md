---
content_hash: 925ed5aeb1e39a0ed8bffd248edad9e28aa1263c419c125b38af14b42dc3146f
fetched_at: '2026-06-29T00:10:18.961208+00:00'
page_id: '4812924'
product: rm
source: tdn-rm
title: Mapa de Risco
type: documentation
url: https://tdn.totvs.com/display/LRM/Mapa+de+Risco
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Segurança e Saúde Ocupacional                      **Versão:**11.8X |
| **Processo** | **:** | PPRA |
| **Subprocesso** | **:** | Mapa de Risco |
| **Data da publicação** | **:** | 09/08/2013 |

#### **1 – Introdução**

Criado através da Portaria n° 05 em 17/08/92 tratando da obrigatoriedade, por parte de todas as empresas, da "representação gráfica dos riscos existentes nos diversos locais de trabalho", além de fazer parte da NR-09, o Mapa de Risco tem como objetivos:

* Reunir as informações necessárias para estabelecer o diagnóstico da situação de segurança e saúde no trabalho na empresa;
* Possibilitar, durante a sua elaboração, a troca e divulgação de informações entre os trabalhadores, bem como estimular sua participação nas atividades de prevenção.

#### **2 – Cadastro do Níveis de Risco**

##### **2.1 – Acesso ao módulo**

Delphi: Acesse “Cadastros | Níveis de Mapa de Risco”

Nova MDI: Acesse “PPRA | Níveis Mapa Risco”

##### **2.2 – Cadastro das informações**

Preencha as informações necessárias para o cadastro dos Níveis. Os dados do campo “Grau” são originados da tabela dinâmica “NIVELRISCO” que é de uso interno.

Após salvar os níveis de risco, deve-se criar o mapa de risco.

#### **3 – Criação do Mapa de Risco**

##### **3.1 – Acesso ao módulo**

Delphi: Acesse o menu “Segurança e Saúde Ocupacional | Mapa de Risco”

Nova MDI: Acesse o menu “PPRA | Mapa de Risco”

**3.2 – Níveis da Seção**

O próximo passo para a criação do Mapa de Risco é a associação dos riscos às seções. Para tal, acesse “Anexos | Níveis das Seções” e informe os dados necessários para o cadastro.

#### **4  – Geração do Mapa de Risco**

##### **4.1 – Acesso ao módulo**

Após associação dos riscos às seções, deve-se gerar o mapa clicando em “Processos | Gerar Mapa de Risco”.

O sistema iniciará um assistente onde serão apresentadas as opções “Associando os riscos à planta da seção” e “Gerando o Gráfico do Mapa de Risco”.

##### **4.2 – Associando os Riscos à Planta da Seção**

Neste tipo de geração o usuário irá selecionar o tamanho dos ícones do nível do Risco, a imagem da planta da seção e associar os riscos à planta da seção.

Na tela “Tamanho dos ícones dos Níveis do Risco”, associe um tamanho para cada item de risco (alto, médio e baixo). Aconselha-se manter um tamanho maior para os níveis mais altos.

Na tela “Selecione a planta da seção”, clique no botão “Abrir”(1°) e selecione a imagem correspondente a planta da seção cujo Mapa de Risco será gerado(2°).

Obs.: Através do ícone de webcam é possível capturar imagens e salvá-las através do ícone de Salvar.

Conforme associações de riscos à seção, na tela “Associe os Riscos à planta da Seção” será apresentado o risco associado com seu respectivo grau (1°). Para selecionar o risco e inserí-lo na planta, basta dar um duplo clique sobre ele. Clique no ícone que representa o risco e posicione-o sobre o local desejado na planta(2°). Poderá adicionar Legenda ao mapa, para isso, clique no botão correspondente. Para excluir a legenda ou riscos, basta clicar com botão direito do mouse sobre os mesmos.

Após avançar, os nomes dos riscos não serão apresentados. Apenas os círculos e a legenda são mantidos no mapa.

Avance e finalize o assistente. O Mapa ficará disponível para impressão através do relatório “RELMAPARISC -Visualizar Planta da Seção.rrmx” no RM Reports.

##### **4.2.1 – Gerando Relatório no Reports**

Acesse o menu “Gestão | RM Reports” e clique em “Processos | Importar Estrutura de Relatório”.

Selecione o relatório “RELMAPARISC – Visualizar Planta da Seção” disponível no book de relatórios TOTVS (presente na pasta “RMVitae\Relatório” presente normalmente no caminho ‘C:\totvs\CorporeRM’).

O relatório será apresentado dentro da estrutura “TOTVS Gestão de Pessoas > ‘Nome da Coligada Corrente’”.

Para gerá-lo selecione o relatório e clique em “Processos | Gerar Relatório”.

No assistente que será aberto, escolha o tipo de geração desejado e execute o processo.

**4.3 – Gerando o Gráfico de Mapa de Risco**

No assistente de geração do mapa de risco, selecione o tipo de geração “Gerar o Gráfico do Mapa de Risco”.

Na tela “Geração do Gráfico do Mapa de Risco” deverá ser informado a Filial, Departamento, Seção e Nível desejado para a geração do gráfico. O sistema utilizará estes dados como um filtro, apresentando somente os riscos associados à seção/nível selecionados.

Na tela seguinte, o gráfico poderá ser visualizado conforme opções selecionadas. Clique em ‘Salvar’ para que o gráfico seja salvo como imagem.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[R@RH](https://totvs.byyou.com/?space=rrh)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 4 – (Recursos Humanos)

*Publicador: Joyce Nereu*

*Código: SSO-00004*
