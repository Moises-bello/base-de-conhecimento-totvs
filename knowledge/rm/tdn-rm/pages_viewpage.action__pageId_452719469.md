---
content_hash: 7b42962ed678cf0c47a4883f72683102629d8b01f471ce31ab5faa10bd01abd7
fetched_at: '2026-06-29T00:10:07.907179+00:00'
page_id: '452719469'
product: rm
source: tdn-rm
title: Comparativo SEFIP x Folha Analítica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719469
version: 3
---

falseATENÇÃO:

A partir da release **12.1.2606**, esta rotina foi descontinuada, pois sua funcionalidade passou a ser atendida pelo **eSocial**.

Neste módulo será possível analisar o arquivo de fechamento do SEFIP(\*.SFP) gerado pelo validador SEFIP.EXE e arquivo FOLHAANALITICA\_NET.txt gerado através da geração da Folha Analítica comparando linha a linha dos arquivos os valores informados de base de FGTS e INSS. Com essa funcionalidade, o usuário poderá identificar com maior facilidade possíveis diferenças no cálculo da folha de pagamento versus os valores a serem informados para a Caixa Econômica Federal.  
   
O arquivo FOLHAANALITICA\_NET.txt deverá ser gerado em Relatórios | Folha Analítica | Comparativo SEFIP x Folha Analítica, marcando o parâmetro "Gera arquivo para comparativo SEFIP x Folha Analítica".  
   
Deverá ser gerado o arquivo SEFIP.RE em Relatórios | SEFIP | SEFIP e validar no aplicativo SEFIP.EXE da Caixa Econômica Federal.  
   
Após validar o arquivo, deverá ser realizado o fechamento do SEFIP para que seja gerado o arquivo \*.SFP no diretório onde tiver instalado o programa da Caixa Econômica Federal.  
   
O usuário deverá informar em Arquivo de fechamento do SEFIP (\*.SFP) o arquivo gerado no fechamento realizado no programa SEFIP.EXE da Caixa Econômica Federal.  
   
O usuário deverá informar em Arquivo FOLHAANALITICA\_NET.txt em o arquivo gerado no módulo de Folha Analítica do Programa de Folha de Pagamento (RM Labore). O usuário poderá visualizar o arquivo antes de executar o processo de comparação.  
   
Observação 1  
Ao ser processado o módulo será gerado um arquivo com Razão social da empresa, CNPJ da empresa, CNPJ da empresa, Competência (mês e ano da folha), Código do recolhimento SEFIP, Tipo de arquivo (Folha ou 13º salário), dados do funcionário (PIS e NOME), Remuneração sem 13º(corresponde a base de FGTS), Remuneração  13º(corresponde a base de FGTS13), Base INSS folha(Corresponde a base de INSS), Base INSS 13º(corresponde a base de INSS13) e Valor desc. INSS(Corresponde o INSS descontado).  
   
Observação 2  
As diferenças entre as colunas SEFIP x Folha Analítica, serão destacadas em vermelho.  
   
Observação 3  
No cabeçalho dos dados do funcionário será apresentada uma descrição de qual arquivo se refere os valores.  
   
Observação 4  
É possível que o relatório retorne somente os funcionários com diferença. Para isto basta marcar o parâmetro 'Imprimir Apenas Diferenças' no processo de Comparativo SEFIP x Folha Analítica. Não marcando este parâmetro o processo irá gerar o relatório para todos os funcionários informados nos dois arquivos, independentemente de haver diferenças.
