---
content_hash: 0d927f2ff3aa6869c11c0e21023bedcfb761074911efacb0aebb10f64e26879f
fetched_at: '2026-06-29T00:05:57.076117+00:00'
page_id: '161351687'
product: rm
source: tdn-rm
title: RMCTB000012_Razão Auxiliar Parametrizável para SPED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=161351687
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Gestão Contábil – **Versão:** 11.52 |
| **Processo** | : | Razão Auxiliar Parametrizável para SPED |
| **Subprocesso** | : | SPED Contábil |
| **Data da publicação** | : | 12/09/2014 |

**Introdução**

O Razão Auxiliar é um relatório no qual as informações podem variar de cliente para cliente, sendo assim, não há um padrão fixo. Baseado nesta realidade foi avaliado a possibilidade de criar um processo onde o usuário irá complementar a parametrização do layout do Razão Auxiliar conforme o padrão dos registros I500, I510, I550, I555 a partir de um relatório definido no RM Gerador.

**Visão Geral do Processo**

**Razão Auxiliar no RM Gerador**

O relatório criado no RM Gerador deverá ser do tipo Arquivo Bancário e composto por dois grupos: Cabeçalho do Detalhe e Linha Detalhe.

**Cabeçalho do Detalhe**

**·** Deverá conter os campos do tipo texto contendo a descrição dos campos que serão impresso na linha detalhe.  
 **·** Na propriedade do grupo "Cabeçalho do Detalhe" na aba "Campos", deverá ser configurado a ordem de impressão conforme a ordem de impressão das colunas da linha detalhe, ou seja, a ordem deve ser a mesma.  
 **·** A opção "Não Imprimir" deverá esta marcada.

**Linha Detalhe**

**·** Deverá ser composta dos campos necessário para geração do relatório do Razão Auxiliar.  
 **·** A ordem dos campos que serão impressos no relatório deverá ser definida conforme a ordem dos campos definidos no grupo cabeçalho do detalhe.  
 **·** Os campos tais como PARAMETRO#1, SQL#1 e outros que não serão impressos no relatório e que serão utilizados apenas para o processamento de informações deverão estar com a propriedade visível desmarcada e também deverá ser configurada nas propriedades do grupo "Linha Detalhe" na aba campo a quantidade máxima de caracteres = 0.  
 **·** Os campos adicionados na Linha Detalhe do relatório que forem provenientes de tabelas do RM (Campos da Base) e do tipo numérico deverão ser totalizadores no relatório do Razão Auxiliar.  
 **·** O número máximo de caracteres deve ser configurado através das propriedades Máx. Caracteres na aba Campos.

**Definição dos Grupos do Relatório**

Visão do relatório montado:

**Geração do arquivo**

O arquivo .txt poderá ser visualizado ou gerado em um diretório específico.

**Parametrização do relatório do Razão Auxiliar**

Menu Rotinas Legais > SPED Contábil > Parametrização do Relatório do Razão Auxiliar

**Definição do relatório Razão Auxiliar**

Nesta etapa do processo será necessário informar o relatório criado no RM Gerador, o grupo que representa os títulos das colunas e o grupo que representa as linhas do Relatório Razão Auxiliar.   
 Exemplo:

**Processo de parametrização do layout do Razão Auxiliar**

Este processo será composto por três etapas nas quais o usuário poderá complementar e validar a parametrização do layout do Razão Auxiliar conforme o padrão dos registros I510, I555, 1500 e 1550 a partir do relatório Razão Auxiliar criado no RM Gerador.

**1º Etapa – Parametrização do Registro I510**

Os campos devem ser apresentados neste registro na mesma ordem em que devem figurar da visualização/impressão. Nesta etapa o Nome do Campo, Tipo e a Quantidade de casas decimais podem ser alterados e as informações originais dos campos conforme o relatório cadastrado no gerador podem ser restauradas acionando o botão Restaurar.

**2º Etapa – Parametrização do Registro I555**

Este registro deve conter os mesmos campos do registro I510. Entretanto, devem estar marcados apenas os que servirão de chave para o cálculo dos totais e os campos que forem totalizadores.

**3º Etapa – Parametrização dos Registros I550 E I500**

Nesta etapa deverá ser validada a impressão/visualização do relatório Razão Auxiliar conforme a regra do registro I500 (considerar que o livro será impresso/visualizado em papel A4, com orientação paisagem, margens de 1,5 cm e com fonte Courier).   
 Nesta etapa será possível também efetuar a visualização ou impressão do relatório, possibilitando ao usuário ajustar o tamanho da fonte ou das colunas (em quantidade de caracteres) que irão compor o relatório, baseado na regra definida no registro I510 (quando o conteúdo dos campos (inclusive cabeçalho das colunas) for de tamanho superior ao tamanho da coluna correspondente no relatório, o excedente será impresso nas linhas subsequentes).

**Conclusão da Parametrização**

Após a parametrização do Layout do Razão Auxiliar para o SPED Contábil basta clicar em Executar para que as configurações escolhidas sejam aceitas.

Aguarde a finalização do processo.

**Considerações do processo**

**·** Os parâmetros definidos neste processo serão armazenados no banco de dados, sendo possível apenas um layout por coligada.  
 **·** Sempre que houver alguma modificação no relatório através do RM Gerador, a parametrização do layout do Razão Auxiliar para SPED deverá ser revista, pois a mesma será baseada no layout criado no RM Gerador.

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE** [**R@Controladoria**](http://fluig.totvs.com/portal/p/10097/subject/rcontbil)

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 2 – (Controladoria e Finanças), 5 – (Planejamento e Controle Orçamentário), 2 – (RM Saldus).
