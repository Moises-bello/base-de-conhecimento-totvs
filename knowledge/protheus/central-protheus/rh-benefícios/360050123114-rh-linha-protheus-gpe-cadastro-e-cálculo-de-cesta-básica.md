---
article_id: 360050123114
category: RH - Benefícios
content_hash: ffaab7ceb91e11f28f9a615be724a6e1e0dfb28cd5b4d8afaabfd5039cc34d46
fetched_at: '2026-06-28T22:44:03.514169+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro e Cálculo de Cesta Básica
type: support-article
updated_at: '2025-07-02T13:21:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050123114-RH-Linha-Protheus-GPE-Cadastro-e-C%C3%A1lculo-de-Cesta-B%C3%A1sica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32696463398295) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como cadastrar e calcular a Cesta Básica?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

Para cadastro e cálculo da Cesta Básica, realize os seguintes passos:

**1.** Cadastro do Roteiro BEN  
Acesse: **Atualizações/ Definições de Cálculo/ Períodos** e inclua o roteiro **BEN - Outros Benefícios** com Per. Ativo: Sim. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696463399063)  
  
**2.** Cadastro das Verbas  
Acesse: **Atualizações/ Definições de Cálculo/ Verbas**, e crie três verbas, sendo uma de Provento para o pagamento da Cesta Básica (caso o pagamento seja efetuado em folha), uma de Desconto, para que seja descontado o valor parte funcionário e outra de Base Provento que conterá o valor parte Empresa.   
**Todas as verbas não devem ter Identificador de Cálculo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696446706199)**

**3.** Inclusão do benefício na S011 Acesse: **Atualizações/ Definições de Cálculo/ Manutenção de Tabelas**, localize a tabela **S011**, clique em **Outras Ações** e posteriormente em **Alterar.**Insira uma linha, informe o código e descrição ao benefício como Cesta Básica.![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696446709015)  
  
  
**4.** Cadastro do benefício de Cesta Básica na rotina de Definições de Benefícios  
Acesse: **Atualizações/ Benefícios/ Outros Benefícios/ Definição de Benefícios,** selecione o tipo de Benefício **Cesta Básica** e clique em **Manutenção** para cadastrar o benefício.  
  
Preenchimento dos Campos:**Código:** Utilize este campo para definir um código de identificação do benefício.  
**Descrição:** Use este item para atribuir uma descrição ao benefício.  
**Salário Até ou Quantidade de Salário Mínimo:** Neste campo, informe o valor de salário limite para o recebimento do benefício, escolhendo entre salário até ou quantidade de salário mínimo.  
**Tipo Referência:** Escolha entre três tipos de cálculo para o benefício: valor fixo, percentual salário base ou percentual salário mínimo.  
**Referência:**Use este item para informar o valor do benefício no campo referência, obedecendo ao tipo de referência escolhido.  
**% Pagamento Funcionário:** Preencha este campo, caso o benefício seja concedido via Folha de Pagamento.  
**Tipo de Desconto:**Preencha este campo, caso o benefício seja concedido via Folha de Pagamento.  
**Desconto do Funcionário:** Defina o percentual de desconto do funcionário neste campo.  
**Valor Mínimo e Máximo:**Caso queira informar valor mínimo e máximo para o desconto do funcionário, utilize este campo.  
  
Abaixo, um **exemplo** de **possível** preenchimento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696446710935)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696446712215)

**5.** Inclusão do benefício para o funcionárioAcesse **Atualizações/ Benefícios/ Outros Benefícios/ Manutenção** para amarrar a Cesta Básica ao funcionário. Posicione na matrícula desejada, clique em **Manutenção** e preencha os principais campos

**Tipo Benefício:** Preencha este campo com o tipo de benefício de Cesta Básica  
**Código Benefício:**Insira o código do benefício que o funcionário terá direito  
Após preencher o campo Código Benefício, o sistema preenche automaticamente os campos referente as verbas (que foram cadastradas na rotina de Definição de Benefícios)

Em seguida preencha o restante dos campos:  
**DT. Ini. Pag:** Informe a data para inicio do cálculo  
**Dt. Fim. Pag:** Informe a data de encerramento (campo não obrigatório)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696463408151)

**6.** Cálculo do benefício  
Acesse **Atualizações/ Benefícios/ Outros Benefícios/Cálculo,** informe os parâmetros de cálculo e clique em Calcular  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696446717847)  
No final do processo um LOG será gerado com as informações do cálculo processado.  
  
  
**7.** Relatório para conferencia ou visualização do cálculo individualmente  
  
Para imprimir o relatório, acesse: **Atualizações/Benefícios/Outros Benefícios/Relatório Cálculo**, clique em **Outras Ações/Parâmetros** e informe: **Processo, Período do cálculo e Tipo do Benefício** que deseja imprimir. Os demais parâmetros podem ser configurados conforme necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696446720535)![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696463413911)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696446726167)

Caso queira consultar o cálculo individualmente, acesse **Atualizações/ Benefícios/ Outros Benefícios/ Manutenção**, selecione o funcionário desejado e clique **Outras Ações/ Visualização do Cálculo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696446726935)**

**8.** Integração do roteiro BEN à folha de pagamento  
Após todo este processo de cálculo e conferência, o Roteiro BEN deve ser integrado ao Roteiro FOL, para que os valores sejam efetivamente pagos, para isso, acesse **Atualizações/ Benefícios/ Outros Benefícios/ Integração com Folha** e integre o Roteiro BEN a folha de pagamento.   
  
Após este procedimento, o sistema levará para a tabela RGB em **Atualizações/ Lançamentos/ Por Funcionário**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696463420183)

**Saiba Mais**[RH - Linha Protheus - GPE - Como fazer o cadastro de Outros Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058024473-RH-Linha-Protheus-GPE-Como-fazer-o-cadastro-de-Outros-Benef%C3%ADcios?source=search)  
[RH - Linha Protheus - GPE - Relatório de Outros Benefícios em planilha (GPER065)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053377014-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Outros-Benef%C3%ADcios-em-planilha-GPER065-?source=search)  
[RH - Linha Protheus - GPE - Arquivo de benefícios para o Roteiro BEN - Outros Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13176215796119-RH-Linha-Protheus-GPE-Arquivo-de-benef%C3%ADcios-para-o-Roteiro-BEN-Outros-Benef%C3%ADcios?source=search)  
[RH - Linha Protheus - GPE - Como parametrizar e calcular Vale Combustível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004469422-RH-Linha-Protheus-GPE-Como-parametrizar-e-calcular-Vale-Combust%C3%ADvel-?source=search)
