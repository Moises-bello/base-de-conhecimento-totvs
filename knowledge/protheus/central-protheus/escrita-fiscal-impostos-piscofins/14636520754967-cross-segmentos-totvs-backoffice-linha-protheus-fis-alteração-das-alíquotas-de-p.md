---
article_id: 14636520754967
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 095ac871f27defb36bd3ca12978a8dc0fe7a9f844dd080197f22af7af5fee9c6
fetched_at: '2026-06-28T22:39:36.859848+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alteração das alíquotas
  de PIS e COFINS Apuração para Fornecedores optantes pelo Simples Nacional '
type: support-article
updated_at: '2023-05-16T19:58:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14636520754967-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Altera%C3%A7%C3%A3o-das-al%C3%ADquotas-de-PIS-e-COFINS-Apura%C3%A7%C3%A3o-para-Fornecedores-optantes-pelo-Simples-Nacional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Como ajustar a alíquota de PIS/COFINS Apuração para Fornecedores optantes pelo Simples Nacional?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Para ajustar a alíquota do PIS para 1,2375% e COFINS para 5,7%, será necessário primeiramente alterar o tamanho dos campos abaixo:

Acesse o Configurador > Base de Dados > Dicionário> Base de dados  
   
No cadastro de Produtos: SB1 (B1\_PPIS, B1\_PCOFINS)  
   
Grupo de tributação (Caso utilize exceção fiscal) SF7 (F7\_ALIQPIS, F7\_ALIQCOF)  
   
Notas de entrada SD1 (D1\_ALQIMP5(PIS), D1\_ALQIMP6(COFINS))  
   
Notas de saída SD2 (D2\_ALQIMP5(PIS), D2\_ALQIMP6(COFINS))  
   
Livro Fiscal Item SFT (FT\_ALIQPIS, FT\_ALIQCOF)  
   
Exemplo para alteração dos campos:  
Tamanho 7  
Decimal 4

Para que o valor da alíquota não seja arredondado no pedido de venda/Doc. Entrada, altere o parâmetro MV\_DECALIQ para .T. Sobre o parâmetro.  
  

Caso o Produto utilizado for também para outros casos onde deve seguir a alíquota padrão do PIS/COFINS Apuração, será necessário criar uma Exceção Fiscal, pode realizar duas validações para ser aplicada, com o Produto e Fornecedor, para isso é necessário utilizar a seguinte configuração:  
   
**1- Cadastro das Exceções Fiscais.**  
   
Grupo de Trib. (F7\_GRTRIB) = O código preenchido nesse campo deverá ser informado no cadastro do produto através do campo Grp. Trib. (B1\_GRTRIB).

Obs.: para a inclusão de novos códigos acessar a tabela 21 do configurador.  
   
Estado (F7\_EST) = estado do Fornecedor  
Tipo (F7\_TIPOCLI) = Todos  
Aliq. Pis (F7\_ALIQPIS) = 1,2375  
Aliq. Cof. (F7\_ALIQCOF) = 5,70  
   
GRP. Cli/For (F7\_GRPCLI) = Esse campo não é de preenchimento obrigatório para validar a exceção fiscal, porém caso ele seja preenchido o mesmo conteúdo deverá ser informado no cadastro do fornecedor através do campo Grp. Tribut (A2\_GRPTRIB). UF Busca (F7\_UFBUSCA) = Origem  
   
**2 - Cadastro do Produto.**  
   
Amarrar a Exceção Fiscal ao cadastro do produto através do campo Grupo Trib. (B1\_GRTRIB).  
Nesse campo deverá ser informado o grupo de tributação cadastrado no campo GRUPO (F7\_GRTRIB) da exceção fiscal.  
   
**3 – Cadastro do Fornecedor**  
   
Quando é cadastrado algum código no campo Grp. Cli/For (F7\_GRPCLI), esse mesmo código deverá ser vinculado no campo Grp. Tribut (A2\_GRPTRIB).

Lembrado que os campos F7\_GRPCLI e A2\_GRPTRIB devem estar com o mesmo conteúdo (ambos em branco ou ambos preenchidos com o mesmo código).  
   
**4 - Verifique no configurador se o tamanho campos abaixo estão corretos:**  
Obs.: Se o tamanho de algum deles estiver diferente, a exceção fiscal não será aplicada corretamente.  
   
F7\_GRTRIB = CARACTER, 6  
F7\_GRPCLI = CARACTER, 3  
A1\_GRPTRIB = CARACTER, 3  
A2\_GRPTRIB = CARACTER, 3  
B1\_GRTRIB = CARACTER, 6

Saiba mais:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alteração das casas decimais PIS e COFINS apuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043180793-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Altera%C3%A7%C3%A3o-das-casas-decimais-PIS-e-COFINS-apura%C3%A7%C3%A3o?source=search)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - LIVROS FISCAIS - Exceção Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048767194-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-LIVROS-FISCAIS-Exce%C3%A7%C3%A3o-Fiscal-?source=search)
