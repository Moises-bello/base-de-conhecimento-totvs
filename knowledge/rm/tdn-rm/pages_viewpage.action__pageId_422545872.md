---
content_hash: 665863acefd84a878953e21b9a77a4d7bca85421a46af1a533a1f0595b547beb
fetched_at: '2026-06-29T00:09:21.374532+00:00'
page_id: '422545872'
product: rm
source: tdn-rm
title: DECLAN (RJ)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545872
version: 6
---

É o documento que se destina à apuração do valor adicionado nas operações relativas à circulação de mercadorias e nas prestações de serviços alcançados pela incidência do ICMS, realizadas no Estado, visando a compor o cálculo dos Índices de Participação dos Municípios - IPM na Arrecadação do ICMS.

**Nome Arquivo:** Informe o nome do arquivo Texto a ser gerado pelo sistema  
 O arquivo sugerido será de acordo com o seguinte formato: Declan+Data/Hora da geração-formato: AAAAMMDDHHMMSS+.dcl, exemplo:Declan20020719143540.dcl.

**Filial:** Informe a Filial a qual se deseja gerar o arquivo

**Ano Referência:**Informe o ano de referência para geração do arquivo   
    
 **Outra Informações DECLAN RJ**  
    
 **Quadro A** – Identificação da Declaração  
 Gerado no arquivo, receberá informações relacionadas à filial declarante. Tais informações como Nome, Inscrição Estadual, Telefones, Representante e Contador, disponíveis no Cadastro de Filiais.

**Quadro B** – Resumo geral das operações e prestações  
 Será gerado somente se o contribuinte apresentou movimentação no Ano Referência, ou seja, a questão "Apresentou Movimento de Operações com Mercadorias ou Prestação de Serviços com Incidência do ICMS" deverá estar marcada. Este quadro é um espelho do Resumo Geral das Operações da empresa declarante. Os valores preenchidos nas Entradas e Saídas Internas, Interestaduais ou Internacionais, serão calculados com base no Valor Contábil total para todas as operações no Ano Referência. Se valores como IPI ou ST estiverem compondo o Valor Contábil, não serão deduzidos. As operações relacionadas com o Quadro D, também serão somadas neste registro porém, serão informados como ajustes no Quadro D.

**Quadro C** - Resumo específico de operações com mercadorias  
 O contribuinte deverá ter marcado a primeira questão referente às Operações e Prestações e as duas referentes às Atividades Exercidas. Estas opções encontram-se na pasta Questionário da tela da rotina.  
 Conforme orientações da Secretaria do Estado do Rio de Janeiro, o Quadro C será gerado com base na totalização das mercadorias por operações Internas, Interestaduais ou Internacionais das Entradas e Saídas referente a serviços de Transporte, Telecomunicações e Energia Elétrica. Neste caso, apenas os itens das notas serão utilizados na geração do quadro, além disso, somente os itens associados a Produtos cujo Tipo seja "P", Produto.

**Quadro D** – Ajuste do valor adicionado  
 Será gerado somente se a primeira questão no grupo Operações e Prestações estiver marcada, bem como a primeira questão do grupo Atividades Exercidas, na pasta Questionário da tela da rotina. Caso contrário, será gerado com valor zero. Para que este quadro seja corretamente gerado o usuário deverá preencher o campo CLASSIFICAÇÃO CFOP no cadastro de naturezas de operação, com o respectivo código da tabela de ajuste de valores adicionados que está disponível no site da SEF-RJ.  
***Orientações referentes à geração do quadro D***  
 Operações relativas ao ativo imobilizado na entrada: Para a geração desta informação serão selecionados os seguintes CFOP´s: 1.406 e 2.406; 1.551, 2.551 e 3.551; 1.552 e 2.552; 1.553, 2.553 e 3.553; 1.554 e 2.554; 1.555 e 2.555.

Operações relativas ao uso ou consumo na entrada: Para a geração desta informação serão selecionados os seguintes CFOP´s: 1.407 e 2.407; 1.556, 2.556 e 3.556; 1.557 e 2.557. Incluem-se também neste item as operações de gastos com energia elétrica e comunicação desde que informados no Quadro "B" e relativamente a operações sem crédito de ICMS.

IPI nas entradas de matéria prima: Este valor será calculado da seguinte forma: Será calculada a relação entre o IPI nas saídas que não integram a base de cálculo do ICMS e o total do IPI das saídas. Em seguida, será aplicado este percentual encontrado sobre o valor do IPI das entradas de matérias-primas. Para identificar estas entradas, são considerados os CFOP's: 1.101 e 2.101; 1.102 e 2.102; 1.201 e 2.201; 1.202 e 2.202.

Operações/Prestações que não são FG do ICMS ou não utilizadas no VA de mercadorias nas entradas: Este valor será calculado da seguinte forma:

1
incomplete
Valor nas entradas da diferença entre o valor contábil (VC) e o da base de cálculo (BC) referente às operações escrituradas sob os Códigos Fiscais de Operações e Prestações (CFOP's) abaixo (Outra entrada de mercadoria ou prestação de serviço não especificada):1.949, 2.949 e 3.949. Lançamento: Valor Contábil total - Base Reduzida de ICMS, se a Base Reduzida de ICMS não for maior que 0 (zero), então deverá ser somado o campo Outros de ICMS.

2
incomplete
Valor contábil das operações escrituradas sob os Códigos Fiscais de Operações e Prestações (CFOP) abaixo (Compra/Transferência para utilização na prestação de serviço):1.126, 2.126 e 3.126; 1.154 e 2.154;

3
incomplete
Valor contábil das operações escrituradas sob os Códigos Fiscais de Operações e Prestações (CFOP) abaixo (Retorno de remessa para venda fora do estabelecimento): 1.414 e 2.414; 1.415 e 2.415; 1.904 e 2.904;

4
incomplete
Valor contábil das outras operações escrituradas sob os Códigos Fiscais de Operações e Prestações (CFOP) abaixo que não constituem fato gerador do ICMS: 1.505 a 1.506 e 2.505 a 2.506; 1.601; 1.602; 1.604; 1.605; 1.663 a 1.664 e 2.663 a 2.664; 1.901 a 1.903 e 2.901 a 2.903; 1.905 a 1.909 e 2.905 a 2.909; 1.912 a 1.925 e 2.912 a 2.925; 1.926; 1.933 e 2.933; 3.930.

ICMS Retido por Substituição Tributária: Este ajuste diz respeito tão-somente ao imposto que está indicado, na nota fiscal de entrada no momento da aquisição de mercadoria, como imposto retido. Incluem também neste item, pelo valor lançado, as operações nos CFOP's ( 1.603 e 2.603 ).

Operações relativas ao ativo imobilizado nas saídas: Incluem-se neste item operações com CFOP's: 5.412 e 6.412; 5.551, 6.551 e 7.551; 5.552 e 6.552; 5.553, 6.553 e 7.553; 5.554 a 5.555 e 6.554 a 6.555.

Operações relativas ao uso e consumo nas saídas: Incluem-se neste item operações com CFOP's: 5.413 e 6.413; 5.556, 6.556 e 7.556; 5.557 e 6.557.

IPI que não integra a base de cálculo de ICMS: Inclui-se neste item valor da parcela do IPI que não integra a base de cálculo do ICMS nas saídas das indústrias e estabelecimentos equiparados (incluindo-se os estabelecimentos importadores) bem como o valor da parcela do IPI das devoluções das entradas de matérias-primas acima mencionadas.

IPI que integra a base de cálculo do ICMS: O valor que se constituir em informação de ajuste relativo à parcela do IPI que integra a base de cálculo do ICMS nas saídas de mercadorias será considerado como parcela redutora do valor adicionado total de cada declaração.

Operações/prestações que não são FG do ICMS ou não utilizadas no VA de mercadorias saídas. Este valor será calculado da seguinte forma:

5
complete
Valor nas saídas da diferença entre o valor contábil (VC) e o da base de cálculo (BC) referente às operações escrituradas sob os Códigos Fiscais de Operações e Prestações (CFOP) abaixo (Outra saída de mercadoria ou prestação de serviço não especificada):5.949, 6.949 e 7.949;

6
incomplete
Valor contábil das operações escrituradas sob os Códigos Fiscais de Operações e Prestações (CFOP) abaixo (Devolução compra para utilização na prestação de serviço): 5.210, 6.210 e 7.210;

7
incomplete
Valor contábil das operações escrituradas sob os Códigos Fiscais de Operações e Prestações (CFOP) abaixo (Remessa para venda fora do estabelecimento): 5.414 e 6.414; 5.415 e 6.415; 5.657 e 6.657; 5.904 e 6.904;

8
incomplete
Valor contábil das outras operações escrituradas sob os Códigos Fiscais de Operações e Prestações (CFOP) abaixo que não constituem fato gerador do ICMS: 5.504 a 5.505 e 6.504 a 6.505; 5.601; 5.602; 5.605; 5.606; 5.663 a 5.666 e 6.663 a 6.666; 5.901 a 5.903 e 6.901 a 6.903; 5.905 a 5.909 e 6.905 a 6.909; 5.912 a 5.925 e 6.912 a 6.925; 5.926; 5.929 e 6.929; 5.933 e 6.933; 7.930.

ICMS Retido por Substituição Tributária: Trata-se do Valor Substituição Tributária nas operações de saída em que a empresa declarante é o substituto. Neste caso, soma-se o Valor Substituição Tributária para todas as operações de saída.

Estoque inicial e final: Serão gerados os valores digitados aba de identificação da tela de geração da rotina.

Outros Ajustes – Importações destinadas à industrialização ou comercialização: Serão selecionados os lançamentos quer foram incluídos como os seguintes CFOP´s: 3.101, 3.102 e 3.127.

**Quadro E** – Distribuição do valor adicionado por municípios  
 O contribuinte deverá ter marcado a primeira questão referente às Operações e Prestações e a segunda referente às Atividades Exercidas, na Pasta Questionário. O Quadro E está relacionado com a Distribuição de Valor Adicionado por Municípios. Trata-se de operações de prestação de Serviços, ou seja, saídas. Somente serão selecionados lançamentos de saída para o estado do Rio de janeiro. Para que este quadro seja corretamente gerado o campo o usuário deverá preencher o campo CLASSIFICAÇÃO CFOP com o respectivo código da tabela de Distribuição de Valores Adicionados que está disponível no site da SEF-RJ.

**Quadros F e G** - Receita Bruta – Estabelecimento  
 Receita Bruta do Estabelecimento: trata-se das informações referente à filial para a qual está sendo gerada a DECLAN. A coluna Receita Bruta Total deverá ser preenchida mês a mês e representa não só a receita referente às vendas mas toda receita do estabelecimento. Estes campos serão exibidos na tela da DECLAN.   
 O campo Valor da Receita Bruta do Estabelecimento de Substituição Tributária será preenchido com o somatório do Valor Contábil de todas as operações de saída, internas ou interestaduais com Substituição Tributária.  
 O Quadro F sempre será gerado para a Filial selecionada na tela da DECLAN-RJ. Os valores serão gerados zerados no arquivo da DECLAN-RJ se não forem preenchidos na tela ou se o campo Não Houve Receita no Ano Referência estiver marcado.

**Quadro H** – Valor Adicionado apurado (CRITÉRIOS RES. Nº 2670/1996)  
 Este quadro não será gerado pelo RM Líber, pois este valor será calculado pelo sistema da SEF no momento do envio das informações via internet.

**Classificação de Municípios:**Informe a Classificação de Municípios que será utilizada na geração da rotina. A Classificação de Município é cadastrada em Cadastros | Tabelas Auxiliares | Classificação de Município. Vem preenchido com o valor default informado em Opções | Parâmetros | Gerais/Tabelas.

**Declaração retificadora:**Informe se a declaração a ser gerada será retificadora ou não.

**Única no Estado ou Principal:**Informe se a Empresa/Filial é única no estado ou se é a Empresa/Filial principal ou Centralizadora

**Única em Território Nacional:**Informe se a Empresa/Filial é única no país

**Versão:**Informe o número atual da versão do layout da DECLAN RJ pré-estabelecido pela SEFCON.

**Estoque Inicial:**Informe o valor do Estoque Inicial para geração da declaração.

**Estoque Final:**Informe o valor do Estoque Final para geração da declaração.

**Baixa Contribuinte:**Informe se trata de informações sobre a baixa do Contribuinte ou não.

**Encerramento das Atividades:**Se o campo anterior for confirmado, Informe a data de encerramento das atividades.

**Destino:** Informe o drive destino para geração do arquivo.  
***Atenção*:**Para correta geração do arquivo e conforme exigência da Secretaria da Fazenda do Estado RJ, será de extrema importância que todos os campos do Cadastro de Empresas sejam corretamente informados.   
  Para geração da DECLAN-RJ, serão considerados somente os Lançamentos Fiscais de Entrada/Saída com o Status diferente de Cancelado. Além disto, a Natureza Fiscal associada ao Lançamento, deverá ter no Cadastro de Natureza, o campo Fiscal=SIM.

Serão selecionados os Lançamentos Fiscais cuja Data do Lançamento esteja dentro do Ano Referência, definido na rotina.
