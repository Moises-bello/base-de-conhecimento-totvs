---
article_id: 360022836972
category: RH – DIRF
content_hash: 50ce5c86bb5af52a2cdfe34fc80dee2811bbf5e3f4e5f7bd7e0604c2437a725d
fetched_at: '2026-06-28T22:44:06.929364+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a conferência do plano de saúde,
  coparticipação e reembolso para a DIRF
type: support-article
updated_at: '2025-08-13T19:36:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022836972-RH-Linha-Protheus-GPE-Como-realizar-a-confer%C3%AAncia-do-plano-de-sa%C3%BAde-coparticipa%C3%A7%C3%A3o-e-reembolso-para-a-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17458619184535)**Tempo aproximado para leitura: **00:01:30 min****Ocorrência** Sistema não está levando para a DIRF plano de saúde, coparticipação e reembolso e a incidência está correta "R".  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Causa**Inconsistências nas tabelas de histórico de plano de saúde e coparticipação/reembolso, ou  no cadastro de fornecedor de plano de saúde ou no cadastros dos planos de saúde.  
  
**Solução**Para conferência do plano de saúde na DIRF, devem ser considerados os valores da opção **Informações complementares**, ela fica na rotina **Manutenção Arquivo**, na visualização do funcionário, clicando em **>Outras Ações >Informações complementares**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12246986273815)  
  
Para levar para a DIRF os valores de plano de saúde, deverão estar no “Histórico Plano de Saúde” (tabela RHS) e no “Histórico de Coparticipação" (tabela RHP), os dados do plano de saúde, os valores e os dados dos fornecedores consistentes, então valide as informações abaixo:

**1.** Verifique se os registros estão corretos no Relatório de Acumulados do Plano de Saúde (GPER014) em Atualizações> Benefícios> Plano de Saúde> Relatório de Cálculo de Plano de Saúde. Caso não possua esta rotina, [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420942003351)

Este relatório traz informações dos registros do histórico do plano de saúde, no momento do fechamento do roteiro PLA. Se os registros apresentados estiverem incorretos, também apresentará dados inconsistentes de plano de saúde na DIRF.

Compare os valores entre ficha financeira e relatório acumulado plano saúde, ou execute a rotina de Diagnóstico de base para verificar se há diferenças entre o valor do acumulado plano de saúde e desconto de plano de saúde em folha. (Para execução do diagnóstico de base, [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420653856279).

Caso os registros estejam com algum dado incorreto, será necessário avaliar os dados;  
 **2.** Valide se o **Fornecedor do Plano de Saúde** esta correto na rotina Manutenção tabelas, pelo caminho **>Atualizações >Definições de cálculos >Manutenção tabelas**, nas **Tabelas S016 e S017**, é necessário o cadastro completo com **CNPJ válido**, **Nome e registro ANS**;  
  
**3.** Valide na rotina **Manutenção tabelas**, pelo caminho **>Atualizações >Definições de cálculos >Manutenção tabelas**, se nas tabelas **S008, S009, S013, S014, S028, S029, S030** ou **S031** existe o registro do plano de saúde que consta no relatório de acumulado plano de saúde;

**4.** Valide na rotina Plano de Saúde Ativo, pelo caminho **>Atualizações >Benefícios >Plano de saúde >Plano de saúde ativo** se o fornecedor do plano de saúde é um fornecedor cadastrado na **Tabela S016 e S017,** da rotina Manutenção de Tabelas e se os planos cadastrados são planos válidos de acordo com o cadastro realizado nas tabelas **S008, S009, S013, S014, S028, S029, S030** ou **S031** da rotina Manutenção Tabelas;  
  
**5.** Valide no relatório de Acumulado Plano de Saúde se o fornecedor de plano de saúde do histórico consta nas **Tabelas S016 e S017** e se planos são planos válidos de acordo com o cadastro realizado nas tabelas **S008, S009, S013, S014, S028, S029, S030 ou S031** da rotina **Manutenção Tabelas.**

**6.** Realize a geração da DIRF em Miscelânea> DIRF> Gerar Arquivo;  
  
**7.** Realize a conferência entre os valores de plano de saúde que estão dentro da manutenção do arquivo (Miscelânea> DIRF> Manutenção do Arquivo>Visualizar/Alterar >Botão “Outras Ações”> Informações Complementares) e o relatório de acumulados do plano de saúde descrito no item 1.  
 **Caminho rotina Manutenção Tabela:** >Atualizações >Definições de Cálculo >Manutenção Arquivo.

**Observação:** As tabelas que armazenam as alterações do plano de saúde são: **RHK, RHL e RHM  
  
Acesse o vídeo abaixo de como conferir o plano de saúde na DIRF**

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como incluir a rotina Acumulados de Plano de Saúde no menu do Sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420942003351)  
[Valores de Assistência médica não estão aparecendo no arquivo magnético da DIRF. Registros OPSE - TPSE.](https://tdn.totvs.com/pages/releaseview.action?pageId=271667510)  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
