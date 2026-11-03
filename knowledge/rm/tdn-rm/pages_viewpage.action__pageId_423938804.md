---
content_hash: 3b4df1acd061a704b39ac3bfe61ce31466fb82d52e27ce2a5d94037e406fb92a
fetched_at: '2026-06-29T00:09:29.089415+00:00'
page_id: '423938804'
product: rm
source: tdn-rm
title: Razão Auxiliar Parametrizável para SPED Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938804
version: 4
---

**ATENÇÃO:** **Com o objetivo de simplificar a parametrização e geração do relatório "Razão Auxiliar" para o SPED contábil, realizamos uma evolução no módulo para que não seja mais necessário utilizar o RM Gerador.**   
**A partir de agora a parametrização do relatório pode ser feita diretamente no cadastro da escrituração contábil clicando na aba "Layout do Relatório Razão Auxiliar".**  
**Para utilizar o novo recurso acesse o cadastro de escrituração contábil do SPED Contábil e realize a parametrização.**  
**Para mais informações** Clique aqui.  
   
O Razão Auxiliar é um relatório no qual as informações podem variar de cliente para cliente, sendo assim, não há um padrão fixo. Baseado nesta realidade foi avaliada a possibilidade de criar um processo onde o usuário irá complementar a parametrização do layout do Razão Auxiliar conforme o padrão dos registros I500, I510, I550, I555 a partir de um relatório definido no RM Gerador.  
**RAZÃO AUXILIAR NO RM GERADOR**   
O relatório criado no RM Gerador deverá ser do tipo Arquivo Bancário e composto por dois grupos: Cabeçalho do Detalhe e Linha Detalhe.

**CABEÇALHO DO DETALHE**

* Deverá conter os campos do tipo texto contendo a descrição dos campos que serão impresso na linha detalhe.
* Na propriedade do grupo "Cabeçalho do Detalhe" na aba "Campos", deverá ser configurada a ordem de impressão conforme a ordem de impressão das colunas da linha detalhe, ou seja, a ordem deve ser a mesma.
* A opção "Não Imprimir" deverá esta marcada.

**LINHA DETALHE**

* Deverá ser composta dos campos necessário para geração do relatório do Razão Auxiliar.
* A ordem dos campos que serão impressos no relatório deverá ser definida conforme a ordem dos campos definidos no grupo cabeçalho do detalhe.
* Os campos tais como PARAMETRO#1, SQL#1 e outros que não serão impressos no relatório e que serão utilizados apenas para o processamento de informações deverão estar com a propriedade visível desmarcada e também deverá ser configurada nas propriedades do grupo "Linha Detalhe" na aba campo a quantidade máxima de caracteres = 0.
* Os campos adicionados na Linha Detalhe do relatório que forem provenientes de tabelas do RM (Campos da Base) e do tipo numérico deverão ser totalizadores no relatório do Razão Auxiliar.
* O número máximo de caracteres devem ser configurados através das propriedades Máx. Caracteres na aba Campos

**GERAÇÃO DO ARQUIVO**  
O arquivo .txt poderá ser visualizado ou gerado em um diretório específico.

**PARAMETRIZAÇÃO DO RELATÓRIO DO RAZÃO AUXILIAR**   
Menu Rotinas Legais > SPED Contábil > Parametrização do Relatório do Razão Auxiliar

**DEFINIÇÃO DO RELATÓRIO RAZÃO AUXILIAR**   
Nesta etapa do processo será necessário informar o relatório criado no RM Gerador, o grupo que representa os títulos das colunas e o grupo que representa as linhas do Relatório Razão Auxiliar.

**PROCESSO DE PARAMETRIZAÇÃO DO LAYOUT DO RAZÃO AUXILIAR**   
Este processo será composto por três etapas nas quais o usuário poderá complementar e validar a parametrização do layout do Razão Auxiliar conforme o padrão dos registros I510, I555, 1500 e 1550 a partir do relatório Razão Auxiliar criado no RM Gerador.

**1º ETAPA – PARAMETRIZAÇÃO DO REGISTRO I510**  
Os campos devem ser apresentados neste registro na mesma ordem em que devem figurar da visualização/impressão. Nesta etapa o Nome do Campo, Tipo e a Quantidade de casas decimais podem ser alterados e as informações originais dos campos conforme o relatório cadastrado no gerador podem ser restauradas acionando o botão Restaurar.

**2º ETAPA – PARAMETRIZAÇÃO DO REGISTRO I555**  
Este registro deve conter os mesmos campos do registro I510. Entretanto, devem estar marcados apenas os que servirão de chave para o cálculo dos totais e os campos que forem totalizadores.

**3º ETAPA – PARAMETRIZAÇÃO DOS REGISTROS I550 E I500**  
Nesta etapa deverá ser validada a impressão/visualização do relatório Razão Auxiliar conforme a regra do registro I500 (considerar que o livro será impresso/visualizado em papel A4, com orientação paisagem, margens de 1,5 cm e com fonte Courier).  
Nesta etapa será possível também efetuar a visualização ou impressão do relatório, possibilitando ao usuário ajustar o tamanho da fonte ou das colunas (em quantidade de caracteres) que irão compor o relatório, baseado na regra definida no registro I510 (quando o conteúdo dos campos (inclusive cabeçalho das colunas) for de tamanho superior ao tamanho da coluna correspondente no relatório, o excedente será impresso nas linhas subseqüentes).

**CONCLUSÃO DA PARAMETRIZAÇÃO**   
Após a parametrização do Layout do Razão Auxiliar para o SPED Contábil basta clicar em Executar para que as configurações escolhidas sejam aceitas.

**CONSIDERAÇÕES DO PROCESSO**

* Os parâmetros definidos neste processo serão armazenados no banco de dados, sendo possível apenas um layout por coligada.
* Sempre que houver alguma modificação no relatório através do RM Gerador, a parametrização do layout do Razão Auxiliar para SPED deverá ser revista, pois a mesma será baseada no layout criado no RM Gerador.
