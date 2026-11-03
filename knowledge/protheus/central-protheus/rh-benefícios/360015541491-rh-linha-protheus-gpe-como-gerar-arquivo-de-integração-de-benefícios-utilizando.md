---
article_id: 360015541491
category: RH - Benefícios
content_hash: 1400285444e1ec14fadf2788008d9a6e57773f28826be177a6fe2699c7187429
fetched_at: '2026-06-28T22:44:03.820448+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar arquivo de integração de benefícios
  utilizando a rotina BENEFARQ
type: support-article
updated_at: '2025-12-03T11:45:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015541491-RH-Linha-Protheus-GPE-Como-gerar-arquivo-de-integra%C3%A7%C3%A3o-de-benef%C3%ADcios-utilizando-a-rotina-BENEFARQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28159917889431) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**  
Como gerar **arquivo de integração de benefícios** utilizando a rotina **BENEFARQ**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**  
Para gerar arquivo de integração de benefícios utilizando a rotina BENEFARQ, realize os seguintes passos:

**1.** Verifique algumas informações necessárias para a geração do arquivo:  
  
**1.1** Acessar o **Cadastro do Funcionário** através do menu **Atualizações> Funcionários> Funcionários** e verifique o preenchimento obrigatório dos campos **RA\_MAE** (Nome da Mãe), **RA\_CIC** (CPF), **RA\_RG** (RG), **RA\_LOCBNF** (Local do Benefício), **RA\_ENDEREC** (Endereço), **RA\_COMPLEM** (Complemento de Endereço), **RA\_MUNICIP** (Município), **RA\_ESTADO** (Estado), **RA\_CEP** (CEP);  
  
**1.2** Verifique se o arquivo **VB.INI**está na pasta *System* do Protheus; Caso não tenha o arquivo, entre em contato com o suporte técnico para obtê-lo;  
  
**2**. Acesse rotina de **Manutenção de Tabelas** através do menu **Atualizações> Definições de Cálculo> Manutenção de Tabelas**;  
  
**3.** Verifique se na tabela **S018 (Fornecedores de Benefícios)** os campos **Arquivo de Entrada INI** e **Arquivo de Saída TXT** estão preenchidos para o fornecedor. Nesse exemplo será utilizado o fornecedor 002 - VB Serviços;

![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_15-35-5.png?version=1&modificationDate=1526409306000&api=v2)  
  
**4.** Verifique se na tabela **S011 (Tipos de Benefícios)** o **tipo de benefício** está vinculado ao fornecedor. Nesse exemplo usaremos o tipo de benefício 01 - Vale Transporte que está relacionado ao fornecedor 002 - VB Serviços;  
![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_15-38-27.png?version=1&modificationDate=1526409508000&api=v2)  
  
**5.** Acesse **Cadastro de Meios de Transporte**através do menu **Atualizações> Benefícios> Vt /Vr /Va> Meios de Transporte** e informe o tipo de benefício.  Neste exemplo 01 - Vale transporte;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32476156942871)  
  
**Observação:** Para o sistema levar o código do benefício no arquivo txt do benefarq, deve ser preenchido o campo **Cod. Bnf. For.**

**6.** Acesse rotina de **Atualização de Benefícios**através do menu  **Atualizações> Benefícios> Vt /Vr /Va > Atualização**e vincule o benefício com o funcionário;

![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_15-44-51.png?version=1&modificationDate=1526409892000&api=v2)

**7.** Realize calculo do benefício através do roteiro VTR;  
  
**8.** Acesse novamente a rotina de **Atualização de Benefícios**através do menu  **Atualizações> Benefícios> Vt /Vr /Va> Atualização**e verifique se o campo Pedido de Compra estará **em aberto**;

![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_15-50-15.png?version=1&modificationDate=1526410215000&api=v2)

**9.** Acesse a rotina **Arquivo Integração**através do menu **Atualizações > Benefícios > Arquivo Integração**em **Perguntas** e informe o **Fornecedor** e **Tipo** **de Benefício** de acordo com as informações nas Tabelas **S018** (Fornecedores de Benefícios) e **S011** (Tipos de Benefícios);

![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_15-53-16.png?version=1&modificationDate=1526410397000&api=v2)

**10.** Após o preenchimento das perguntas, clique em **Informações** e em **Executar**;

![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_15-58-36.png?version=1&modificationDate=1526410717000&api=v2)

Uma mensagem informando o fim do processamento será exibida

![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_15-59-38.png?version=1&modificationDate=1526410778000&api=v2)

O sistema apresenta um log com as informações que foram gravadas no arquivo de saída vb.txt

![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_16-1-10.png?version=1&modificationDate=1526410870000&api=v2)

**11.** Verifique na rotina de **Atualização** de benefícios que o campo Pedido de Compra está Concluído.

![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_16-4-41.png?version=1&modificationDate=1526411082000&api=v2)

**Importante:** Caso ocorra alguma inconsistência durante a geração do arquivo verifique o *log* de processamento para mais detalhes:

![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_16-7-11.png?version=1&modificationDate=1526411231000&api=v2)

É possível informar o número do pedido, possibilitando que mais de um pedido possa ser realizado dentro do mesmo período.![](http://tdn.totvs.com/download/attachments/361446876/image2018-5-15_15-56-40.png?version=1&modificationDate=1526410600000&api=v2)

O sistema não gera o arquivo de benefícios para o **roteiro BEN - Outros Benefícios**

**Saiba Mais**  
[RH - Linha Protheus - GPE - Arquivo de Benefícios - BENEFARQ para customizações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412579856151-RH-Linha-Protheus-GPE-Arquivo-de-Benef%C3%ADcios-BENEFARQ-para-customiza%C3%A7%C3%B5es?source=search)  
[RH - Linha Protheus - GPE - Padronização e conversão de Rdmakes para fonte padrão a partir da versão 12.1.33](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9814106865431-RH-Linha-Protheus-GPE-Padroniza%C3%A7%C3%A3o-e-convers%C3%A3o-de-Rdmakes-para-fonte-padr%C3%A3o-a-partir-da-vers%C3%A3o-12-1-33?source=search)
