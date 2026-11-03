---
content_hash: f57f744bcc4e1364906bec43ec3d9c7f09b7c51d601b4d050da132ea3ed29db4
fetched_at: '2026-06-29T00:09:21.797021+00:00'
page_id: '422545912'
product: rm
source: tdn-rm
title: Livro Eletrônico (Ato Cotepe)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545912
version: 5
---

**Definição do Processo**  
 O objetivo deste documento é de orientação ao processo de geração da rotina Estadual Livro Eletrônico (Ato Cotepe) Brasília.  
    
 **Regras Gerais**  
 A geração da rotina é realizada pelo RM Liber, menu Rotinas Legais – Estaduais – Livro eletrônico (Ato Cotepe).   
 Será exibido uma tela onde o usuário informará os dados referentes à filial, período, registros, etc. O sistema consistirá a filial município de Brasília e lançamentos fiscais escriturados nessa filial.   
 Será consistido código do modelo do documento, CFOP/CFPS utilizados, natureza fiscal e ou não fiscal no caso de lançamento de serviços, itens tributados pelo ICMS/ISS, valores apurados no período de apuração, etc.

**Identificação do Filtro - **Geração da Rotina****   
 **Campo Arquivo Texto**:\* Informe o nome do arquivo Texto a ser gerado pelo sistema. Como default é preenchido com o nome *LIVRO.TXT*.

**Filial:**\* Informe a Filial a qual se deseja gerar o arquivo.

**Período:**\* Informe a periodicidade do arquivo a ser gerado.

**Versão do Layout:**\* Informe a Versão do Layout. Por default vem preenchido com o valor 001.

**Código SRP:**\* Código da versão do leiaute requerido pela Secretaria da Receita Previdenciária, estabelecido conforme ato normativo próprio.

**Finalidade:**\* Selecione o Código da finalidade do arquivo.

**Escrituração Centralizada:**\* Indicador de centralização de escrituração. As opções são: Não, Centralizador e  Centralizado.

**Salvar Preferências do Usuário:**\* Marcando este check box ao ser fechada a tela de geração da rotina a informação dos seguintes campos serão salvas : Filial, Finalidade, Escrituração Centralizada, Rotina Fiscal, Classificação de País, Inventário,Tipo Custo, Classificação de Município, Registros.  
    
 **Aba Informações Complementares - **Geração da Rotina****  
 Os campos dessa aba "Pgtos sem Retenção ISS, Valor Consumo de Água, Valor Folha Pagamento, Valor Aluguel, Valor Consumo Energia Elétrica e Valor Outras Despesas, Valores retidos por prest. Serv. Aut." devem ser informados para a correta geração do Registro B600 – Informações Complementares.  
    
 **Aba Outros Dados - **Geração da Rotina****  
 Campo Rotina Fiscal: Informe a Rotina a qual se deseja gerar o arquivo. O campo Rotina Fiscal é pre cadastrado no menu cadastro – tabelas auxiliares – configuração de campos – rotina fiscal.

Classificação de País: Informe qual Classificação de País será utilizada pela rotina. Esse campo é pre cadastrado no menu cadastro – Países – anexos – codificação de país

Destino: Informe o drive destino onde será gerado o arquivo.

Classificação de Municípios: Informe a Classificação de Municípios que será utilizada na geração da rotina. A Classificação de Município é cadastrada em Cadastros | Tabelas Auxiliares | Classificação de Município. Vem preenchido com o valor default informado em Opções | Parâmetros | Gerais/Tabelas.

Inventário: Marque essa opção caso deseje gerar as informações de inventário, registro H. O sistema consistirá a data do inventário informada, o tipo de custo e internamente será consistido os dados de inventário controlados no TOTVS Gestão de Estoque, Compra e Faturamento.  
 ***Observação*:**Se marcada a opção Inventário, deve-se informar o Tipo Custo. Serão gerados os registros **H001**, **H020**, **H025** e **H990** e os respectivos registros 0200 com informações dos produtos.   
 Este recurso somente estará disponível para os clientes que possuem o TOTVS Gestão de Estoque, Compra e Faturamento.. 

**Tipo de Custo:** Informe qual o Tipo de Custo se 1-Ultimo Custo Unitário ou 2- Custo Médio   
 ***Observação*:**O sistema mostrará a situação do Estoque de cada produto até a data informada no campo Data final do período.   
 O sistema estará gerando o registro de inventário somente para os produtos que possuem o campo Produto Inventariado habilitado. Este campo pertence ao Cadastros/Produtos – anexos dados fiscais.   
 Para gerar o registro de inventário o sistema utiliza os seguintes campos:

Quantidade: este campo será carregado com o saldo total do produto na data de inventário considerando todos os locais de estoque da filial declarante.

Valor Unitário: este campo será carregado de 2 maneiras distintas:

1. Ultimo Custo Unitário: será carregado o último custo unitário considerando o local onde ocorreu a última movimentação antes da data de inventário.
2. Custo Médio / Produto: será realizado um cálculo da média ponderada considerando o custo médio de todos os locais de estoque. Esta forma de cálculo poderá gerar diferenças de centavos que somente serão corrigidas quando o controle de custos for reestruturado.

O Valor Unitário informado acima é apenas um valor utilizado para o cálculo do Valor do Produto, utilizado na geração da Rotina.  Na rotina deve ser informada Quantidade \* Valor Unitário (que deve ser calculado com base no último custo unitário ou custo médio).  
   
**Aba Registros do Filtro - Geração da Rotina**  
Na aba Registros, o usuário irá selecionar os registros a serem gerados.

Legislação

De acordo com a [Portaria nº 267, de 15 de Dezembro de 2014](http://www.fazenda.df.gov.br/aplicacoes/legislacao/legislacao/TelaSaidaDocumento.cfm?txtNumero=267&txtAno=2014&txtTipo=7&txtParte=.), III – Lançamento do ICMS devido apurado pela sistemática da Lei nº 5.005/2012, da seguinte forma: 

* Criar um registro 0450, do qual conste, no campo 2, a expressão "ICMSDEV5005" e, no campo 3, a expressão "ICMS devido de acordo com a sistemática de apuração da Lei nº 5.005/2012, valores a serem considerados no cálculo:

BCo =R$XXXXX,XX;  
BC das Entradas =R$XXXXXXXX,XX;   
VCv =R$ XXXXXXXX,XX;   
VTB=R$XXXXXXX,XX;  
VI=R$XXXXXXX,XX;  
VINT=XXXXXXX,XX,

**Onde**:

BCo corresponde à base de cálculo das entradas referentes às operações no regime;

VCv corresponde ao valor contábil das vendas efetuadas no regime acrescido do valor contábil das mercadorias adquiridas para industrialização e comercialização quando consumidas ou integradas ao ativo permanente;   
e os demais valores são os constantes na fórmula do inciso V do art. 3º da Lei nº 5.005/2012.

* Criar um registro E340, do qual conste, no campo 2, o código de ajuste "199"; no campo 3, o valor do ICMS apurado de acordo com a sistemática da Lei nº 5.005/2012; e, no campo 8, o código "ICMSDEV5005".

* Implementação dos sub tipos ESTCRED5005, ESTDEBI5005 e ICMSDEV5005 nos lançamentos Outros Débitos e Créditos. Estes Subtipos estarão disponíveis na filial do estado "DF" ou para Lançamentos com o Cod ETD igual a "DF". - No Encerramento do Período ICMS os novos SubTipos serão considerados. - Ato Cotepe: Geração dos Registro 0450 e E340 com os codigos do subtipo do lançamentos de outros débitos e créditos
