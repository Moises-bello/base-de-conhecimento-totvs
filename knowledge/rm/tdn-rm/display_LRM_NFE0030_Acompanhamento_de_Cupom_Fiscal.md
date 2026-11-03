---
content_hash: 1b459274613d569ab83c3041388b1c4e700067c43b08ebbc1fe4e1818803ca8c
fetched_at: '2026-06-29T00:08:12.577990+00:00'
page_id: '243644204'
product: rm
source: tdn-rm
title: NFE0030_Acompanhamento_de_Cupom_Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0030_Acompanhamento_de_Cupom_Fiscal
version: 8
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | 11.82.42 ou 12.1.8 ou posteriores. |
| **Ocorrência:** | NF-e - Acompanhamento de Cupom Fiscal |
| **Passo a passo:** | **Introdução:**  Este passo a passo tem como finalidade auxiliar na parametrização do sistema para o processo de acompanhamento de cupom fiscal.  **1º Passo - Cadastrar o Cupom Fiscal**  No executável do RM Nucleus acessar o **Menu | Cadastro | Tabelas de Tributação | Cupom Fiscal**  Obs: Somente a partir da versão 12 é possível acessar este cadastro através da nova MDI no menu abaixo:    Clicar no Botão Novo  e será aberto a janela a seguir:    Sendo necessário o preenchimento dos campos:            Obs: Lembrando que é necessário cadastrar o cupom apenas onde não há integração com parceiros para inclusão de cupom de forma automática.  **2º Passo - Parametrizar Movimento Emissor de Cupom Fiscal**  Acessar > Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento.  Parametrizar o Tipo de Movimento de Envio de NF-e/NFS-e , na etapa Fis - Dados  Marcar a Flag - Emite Cupom Fiscal    **3º Passo - Criar o Movimento de Cupom Fiscal**  Na aba Integrações | Cupom Fiscal    Preencher as informações dos Dados do Cupom Fiscal.  Na aba Itens | Preencher a quantidade e o valor que foram cadastrados para Cupom Fiscal.      **4**º Passo - Associar ao Cupom Fiscal o movimento****  No executável do RM Nucleus acessar o******Menu | Cadastro | Tabelas de Tributação | Cupom Fiscal******    Clicar no Botão  (**Associar Movimento)**    Selecionar o movimento que foi criado:    Cupom Associado ao Movimento:      ******5º Passo - Parametrizar o movimento de Envio de NF-e******  Verificar se o movimento está parametrizado conforme documentação abaixo:  [NFE0009\_Parametrizar\_movimento\_de\_saida\_para\_a\_emissao\_de\_NF-e](http://tdn.totvs.com/display/LRM/NFE0009_Parametrizar_movimento_de_saida_para_a_emissao_de_NF-e)  NFE0010\_Parametrizar\_movimento\_de\_entrada\_para\_a\_emissao\_de\_NF-e  Após Acessar > **Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento.**  Etapa | Mov - Outros Dados - No Campo Motivo de Referência colocar | 3 - NF Acompanhamento de Cupom Fiscal      ******6º Passo - Criação do movimento para e****nvio da Nota Fiscal Eletrônica**  Acessar o menu Processos | Assistente de Cópia por Referência    Selecionar o Movimento de Cupom Fiscal:    Executar:    Preencher os dados do movimento de destino:    Após efetuar o envio da NF-e:    Será criado as tag's no XML sobre o Cupom Fiscal referenciado responsável pela correta autorização da NF-e:    NF-e Autorizada: |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
