---
content_hash: 023caaca03b870985575f0bf6a9061b6919d0556f853dca337efae5cb6944ed6
fetched_at: '2026-06-29T00:09:26.619034+00:00'
page_id: '423938339'
product: rm
source: tdn-rm
title: Conceitos Patrimoniais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938339
version: 23
---

Para realizar a importação de dados por arquivo texto no TOTVS Gestão Patrimonial, será utilizada a ferramenta "RM Conector", que facilita a execução destas operações de forma dinâmica, utilizando a própria regra dos cadastros.  
Esta ferramenta pode ser acessada através do Menu Utilitários| Rm Conector | Importação. A partir deste menu, você seleciona e/ou edita o Conceito referente ao cadastro que deseja importar no Módulo do patrimônio, pois é por meio dele que você informa o caminho onde esta o arquivo que deseja importar.

Na Aba "Conexões de Origem" deve ser informado o caminho onde esta o arquivo "txt", e após salvar o cadastro do Conceito, ir em processo > Processar Conceito. O processo de importação por texto contempla a importação dos seguintes cadastros:

* Patrimônio
* Títulos
* Rateio Gerencial do Patrimônio
* Localização
* Responsável
* Histórico Transferência de Controle

**Observações:**

1. Caso seja a primeira vez a utilizar o processo de importação, é necessário que se inclua um novo conceito e defina para qual cadastro o mesmo será utilizado, através da importação do conceito.
2. Os conceitos estão disponíveis através do menu Gestão > TOTVS Compartilhamento.
3. No Layout de importação, existe a coluna "Obrigatório". Ela consiste na obrigatoriedade ou não do preenchimento do campo. Quando informado com "X", o mesmo tem preenchimento obrigatório, quando vazio,  o preenchimento é opcional.

 Atualmente possuímos os seguintes conceitos disponíveis:

Lista de conceitos

CONPAT0001 - Exportação Histórico de Controle (Funcionário)  
CONPAT0002 - Exportação Histórico de Controle (Localização)  
CONPAT0003 - Exportação Histórico de Controle (Responsável)  
CONPAT0004 - Exportação do Patrimônio  
CONPAT0012 - Exportação Histórico Controle  (Responsável)  
CONPAT0013 - Exportação Histórico Controle (Departamento)  
CONPAT0014 - Exportação Histórico Controle (Filial)  
CONPAT0015 - Exportação Histórico Controle (Funcionário)  
CONPAT0016 - Exportação Histórico Controle (Localização)  
CONPAT0017 - Exportação Histórico Controle Simples (Centro de Custo)  
CONPAT0018 - Exportação Histórico de Controle (Centro de Custo)  
CONPAT0019 - Exportação Histórico de Controle (Departamento)  
CONPAT0020 - Exportação Histórico de Controle (Filial)  
CONPAT0021 - Exportação Localização  
CONPAT0022 - Exportação patrimônio  
CONPAT0023 - Exportação Responsável  
CONPAT0024 - Importação do Histórico de Controle (Centro de Custo)  
CONPAT0025 - Importação do Histórico de Controle (Departamento)  
CONPAT0026 - Importação do Histórico de Controle (Filial)  
CONPAT0027 - Importação do Histórico de Controle (Funcionário)  
CONPAT0028 - Importação do Histórico de Controle (Localização)  
CONPAT0029 - Importação do Histórico de Controle (Responsável)

Dicas!

1) Existem casos em que o conceito não é executado ou importa os valores incorretamente dependendo do conteúdo (letras com acentuação, Ç ou Ã por exemplo) porque o arquivo txt está com uma codificação diferente do conceito. Os conceitos possuem codificação UTF-8, portanto caso o arquivo não tenha essa configuração será necessário altera-lo. Para isso basta editar o conceito e alterar a seguinte configuração:

Tela

2) O conceito por padrão interrompe a importação em casos de avisos. Caso necessário desativar essa configuração para permitir que o conceito termine a execução sem exibir esses avisos, desmarque a opção "Parar execução caso houver algum aviso".  
Edite o conceito e desmarque os 3 pontos:

Tela
