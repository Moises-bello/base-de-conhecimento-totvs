---
article_id: 360021563052
category: RH – DIRF
content_hash: 59560b847ee93a9647a55a59cc918c91d492ccab4bbebd40feb5a44e1604776a
fetched_at: '2026-06-28T22:44:07.193473+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Quando os planos de saúde são informados manualmente
  para o funcionário o que fazer para DIRF
type: support-article
updated_at: '2025-08-15T12:49:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021563052-RH-Linha-Protheus-GPE-Quando-os-planos-de-sa%C3%BAde-s%C3%A3o-informados-manualmente-para-o-funcion%C3%A1rio-o-que-fazer-para-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20880947125655)** Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Quando os planos de saúde são informados manualmente na folha para o funcionário o que fazer para DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Quando não é utilizado o processo padrão de cálculo, integração e fechamento do plano de saúde (>Benefícios > Planos Ativos) e os valores de planos de saúde, co-participação e reembolso são lançados de forma manual na folha é possível levar as informações para DIRF, porém, somente no registro INF.

Registros como **TPSE** e **OTPSE** serão gravados no arquivo somente se for utilizado a forma padrão de cálculo do plano de saúde. Caso contrário, será necessário realizar lançamento manual no validador ou em Informações Complementares, ou alimentar as tabelas **RHP-Histórico de Co-partic./Reembols**o e **RHS-Histórico de cálculo de plano de Saúde**, sendo que para essa ultima opção, é necessário existir os cadastros dos fornecedores de plano de Saúde nas tabelas **S016** e **S017** e os cadastros de plano de saúde nas tabelas **S008, S009, S013, S014, S028, S029, S030** ou **S031** que constam na rotina Manutenção de Tabelas.

As verbas de plano de saúde devem estar com **incidência R para DIRF,** desta forma elas irão para manutenção do arquivo (Tabelas SR4 e SRL) porém vão ficar sem informação de **fornecedor do plano** (CNPJ e RAZÃO SOCIAL), isso deverá ser lançado manualmente na manutenção do arquivo na parte de **Informações Complementares**, pois se trata de informações obrigatórias no layout da DIRF.  
  
Para lançar, entre na rotina **Manutenção de Arquivo** pelo caminho **>Miscelânea >Dirf >Manutenção de Arquivo**, selecione o funcionário a fazer a manutenção, clique **>Outras Ações >Alterar**, na manutenção clique em **>Outras Ações >Informações Complementares**  
  
Também é preciso preencher o campo Espec.Outros com as seguintes informações.

**Posição 1 tamanho 1:**  
**T** = Titular  
**C**=Conjuge/Companheiro;**F**=Filho;**E**=Enteado;**P**=Pai/Mae;**O**=Agregado/Outros                          
  
**Posição 2 tamanho 3**  
**MED** = Ass. Medica  
**ODO** = Ass. Odontologica  
  
**Posição 5 tamanho 2**  
Codigo do dependente (RB\_COD)  
  
![](http://tdn.totvs.com/download/attachments/223181985/image2018-1-18_18-9-6.png?version=1&modificationDate=1516306146000&api=v2)

**Posição 7**  
Caso seja reembolso escrever **REEMBOLSO**

**Exemplo:**  
Para um Titular com assistência médica → TMED  
Para um Titular com assistência odontológica → TODO  
  
Para um Dependente(filho) com assistência médica → FMED01  
Para um Dependente(filho) com assistência odontológica →FODO01  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13266950284183)  
  
**IMPORTANTE:** Com a melhoria da tela de Informações complementares em MVC, não é possível mais alterar o campo CPF COMPLEM ao editar o registro, então para informar o CNPJ correto do fornecedor de plano de saúde, pode ser usada a opção Alt. Inform,Compl ou pode ser deletada a linha e incluída uma nova linha com os registros, as duas orientações constam na documentação [DT DIRF Alteração do campo 'CPF Complem.'](https://tdn.totvs.com/pages/releaseview.action?pageId=745142025).  
  
Também é possível customizar a DIRF para carregar os dados de plano de saúde corretamente para informações complementares com o ponto de entrada **GPE550ICD**, para mais informações do ponto de entrada, acesse a documentação [GPE550ICD - Informações Complementares DIRF](https://tdn.totvs.com/pages/releaseview.action?pageId=6079234)  
  
  
**Saiba mais**  
<http://tdn.totvs.com/pages/viewpage.action?pageId=223181985>  
[RH - Linha Protheus - GPE - Como realizar a conferência do plano de saúde, coparticipação e reembolso para a DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022836972)

[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
