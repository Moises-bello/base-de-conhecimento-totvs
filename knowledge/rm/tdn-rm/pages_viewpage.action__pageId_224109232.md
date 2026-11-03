---
content_hash: f7e05dc2cc62958c3f4de6341ce16824a6fd4e8659547982398045ea88048c4e
fetched_at: '2026-06-29T00:06:23.986177+00:00'
page_id: '224109232'
product: rm
source: tdn-rm
title: DT_Controle_de_Baixa_e_Revisão_Gestão_de_Glosas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224109232
version: 133
---

# Controle de Baixa e Revisão na Gestão de Glosas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento e Tesouraria | Controle de Glosa  Recurso de Glosa  Controle de Recebimento | |
| **Cadastros Iniciais:** | São necessárias várias contas faturadas e com movimento de fatura gerado. |
| **Requisito (ISSUE):** | PCREQ-8993 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZATENDIMENTO, SZATENDIMENTOREC, SZCONTROLEGLOSA, SZCONTROLEGLOSAITEM, SZCONTROLRECEB, SZRESUMOGLOSA |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.9 |
| **Versão Expedida:** | 12.1.9 |

## Descrição

Esta implementação consiste em tratar o recebimento a maior nas contas médicas e contabilizar separadamente o que é glosa e o que é recebimento a maior. Ao finalizar o controle de glosa de uma conta, o sistema soma os valores pagos a maior e os valores glosados.

No **Controle de Recebimento**, ao realizar o recebimento por conta, o sistema já preenche o campo de recebimento a maior e o valor de perda (obtido pelo recurso de glosa), além o valor recebido. O valor recebido já engloba os dois campos novos e ao integrar com o **RM Fluxus**, o sistema preenche os valores opcionais correspondentes.

Outra implementação consiste em marcar os itens que não possuem informação de pagamento. Com isso, ao finalizar o **Controle de Glosa** da conta e finalizar o recurso de glosa, o sistema cria uma nova conta com os itens sem informação de pagamento. No controle de glosa foi incluído o filtro de Contas Normais, de recurso e contas sem informação de pagamento.

Além disso será possível informar uma glosa irrecuperável que já existe na versão atual, porém se informa o valor irrecuperável. Com isso, a diferença poderá ser recursada posteriormente e o valor da perda já é informado no momento da glosa. Existe também a opção de se dar um desconto no valor do item. O desconto pode ser em percentual ou um valor absoluto. Quando existir desconto não pode existir glosa e vice-versa.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.9 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.9.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).
2. Faça o login, com seu E-mail e Senha.
3. Na barra de menu superior, clique em DOWNLOAD.
4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   1. Linha: RM
   2. Versão: RM 12.1.9
   3. Tipo: Patch

Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Opções/Parâmetros/Parâmetros Gerais**, e selecione a página **Integrações/RM Fluxus**.
2. O valor opcional da Perda acumulada foi substituída pelo campo complementar "SAGLOSAACUM". O script do RM Atualizador já faz a troca do parâmetro e dos valores antigos. Com isso é necessário acessar os parâmetros do sistema de Gestão Financeira para parametrizar corretamento o Valor opcional do recebimento a maior. Note que o campo é o mesmo que utilizávamos para a perda acumulada. Bastar alterar a descrição para "**Recebimento a maior**" e a Ação para "**Acrescentar**". Com esta parametrização, ao realizar a baixa e possuir valor recebido a mais, o sistema preencherá o valor opcional e o Fluxus fará a baixa corretamente.
3. Para permitir informar um valor de desconto no Controle de glosa, deve-se marcar o parâmetro abaixo.
4. Com o sistema devidamente parametrizado, deve-se selecionar uma remessa no menu **Faturamento/Geração de Movimento de Fatura**, e gerar o movimento para que o mesmo gere o título a receber. Com o título gerado é possível realizar as integração dos valores de perda e recebimento a maior.
5. Acesse o menu **Faturamento/Controle e Glosas**. Informe o período desejado, a unidade de faturamento, a unidade de atendimento, o convênio e clique no botão de pesquisar.
6. Selecione a remessa desejada e abra uma conta para realizar o controle de glosa  
   1. 1. Realize glosas, dê descontos, informe pagamentos a maior e marque itens como "Sem informação de pagamento"
7. Itens sem informação de pagamento.
8. Com as glosas realizadas, temos o resumo da conta da seguinte maneira:  
   Diárias: Recebimento a maior = 159,23 +  20,77 = 180,00  
   Taxas: Desconto de 20% = 612,15 - 122,43 = 489,72  
   Materiais: Glosa = 182,27 - (97,64 - 60,00) - 6,04 (Sem informação de pagamento) = 138,59  
   Medicamentos: Sem informação de pagamento = 55,89 - (5,84 + 5,44) = 44,61
9. Ao concluir o controle de glosa da conta, o sistema exibirá o resumo abaixo:
10. Na grid também são exibidos os totais de glosa, pagamento a maior e o total recebido.
11. Agora acesso o menu **Faturamento/Recurso de Glosas**. Selecione a conta que quer recursar, de um duplo clique para fazer o recurso.
12. Apenas o item que sofreu glosa poderá ser recursado. Note que apenas o valor "recursável" é que poderá aparecer. O valor irrecuperável será debitado. No nosso exemplo, 17,64 (2 x 8,82) é irrecuperável, restando assim 20,00 (2 x 10,00) para recurso.
13. No exemplo acima foi recursado 10,00.
14. Acesse o menu **Tesouraria/Controle de Recebimentos**, selecione a página **Fatura**, informe a competência ao qual pertence, selecione o convênio e a unidade de faturamento.
15. Selecione a remessa desejada.
16. Selecione a página Contas e localize o atendimento que quer realizar a baixa. (recebimento por conta).
17. Dê um duplo clique na conta desejada. Os campos: Valor, Receb. a Maior, Perda e o Desconto são preenchidos automaticamente pelo sistema. Eles são obtidos do controle de glosa e recurso de glosa. O valor recebido já engloba os outros dois valores, o que quer dizer que do total de 852,92 recebidos, 20,77 foi de pagamento a maior e 27,64 foi de perda. Clique no botão "Gravar" e será solicitado alguns dados para complementar o envio ao sistema financeiro.
18. Ao integrar com o **RM Fluxus**, a baixa no valor informado é realizada com os respectivos valores de desconto, perda e pagamento a maior.
19. Após realizar o recebimento da conta, iremos verificar a conta gerada com os itens sem informação de pagamento, que era no valor de 17,32. Acesse o **Controle de Glosas**, selecione a fatura, clique em Abrir e na tela abaixo, selecione o filtro conforme a imagem. Neste ponto o processo é igual à realização do controle de glosas. Nesta conta somente os itens marcados como sem informação de pagamento serão exibidos.

divs
